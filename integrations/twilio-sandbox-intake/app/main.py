from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import JSONResponse, PlainTextResponse

load_dotenv()

APP_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.getenv("DATA_DIR", APP_DIR / "data")).resolve()
DATA_DIR.mkdir(parents=True, exist_ok=True)
FLOW_PATH = APP_DIR / "config" / "homework_flow.json"
FLOW = json.loads(FLOW_PATH.read_text())
AUTO_FORWARD_TO_PAPERCLIP = os.getenv("AUTO_FORWARD_TO_PAPERCLIP", "true").lower() == "true"
PAPERCLIP_INBOUND_WEBHOOK_URL = os.getenv("PAPERCLIP_INBOUND_WEBHOOK_URL", "").strip()
PAPERCLIP_WEBHOOK_SECRET = os.getenv("PAPERCLIP_WEBHOOK_SECRET", "").strip()
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "").strip()
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "").strip()
AGENCY_NAME = os.getenv("AGENCY_NAME", "ZimSME AI Solutions")

PACKAGE_MAP = {
    "1": "Starter Site",
    "starter": "Starter Site",
    "starter site": "Starter Site",
    "basic": "Starter Site",
    "2": "Business Site",
    "business": "Business Site",
    "business site": "Business Site",
    "medium": "Business Site",
    "3": "Premium Site",
    "premium": "Premium Site",
    "premium site": "Premium Site",
    "corporate": "Premium Site",
    "4": "AI Quick Win",
    "ai": "AI Quick Win",
    "ai quick win": "AI Quick Win",
    "5": "Launch Audit",
    "launch": "Launch Audit",
    "launch audit": "Launch Audit",
    "6": "App Discovery",
    "app": "App Discovery",
    "app discovery": "App Discovery",
}

ASSET_EXTENSIONS = {
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "application/pdf": ".pdf",
}

app = FastAPI(title="Twilio Sandbox Intake Service")


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "client"


def sender_key(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]


def state_path(sender: str) -> Path:
    return DATA_DIR / "sessions" / f"{sender_key(sender)}.json"


def now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def load_state(sender: str) -> Dict[str, Any]:
    path = state_path(sender)
    if path.exists():
        return json.loads(path.read_text())
    session_id = datetime.utcnow().strftime("%Y%m%d-%H%M%S") + "-" + sender_key(sender)
    base = DATA_DIR / "jobs" / session_id
    (base / "messages").mkdir(parents=True, exist_ok=True)
    (base / "assets").mkdir(parents=True, exist_ok=True)
    state = {
        "sender": sender,
        "session_id": session_id,
        "job_dir": str(base),
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "current_step_index": -1,
        "answers": {},
        "media": [],
        "status": "new",
    }
    save_state(sender, state)
    return state


def save_state(sender: str, state: Dict[str, Any]) -> None:
    state["updated_at"] = now_iso()
    path = state_path(sender)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2))
    write_summary_files(state)


def get_step(state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    idx = state.get("current_step_index", -1)
    steps = FLOW["steps"]
    if idx < 0 or idx >= len(steps):
        return None
    return steps[idx]


def set_step(state: Dict[str, Any], idx: int) -> None:
    state["current_step_index"] = idx


def advance_step(state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    idx = state.get("current_step_index", -1) + 1
    if idx >= len(FLOW["steps"]):
        state["status"] = "completed"
        return None
    state["current_step_index"] = idx
    return FLOW["steps"][idx]


def twiml(message: str) -> str:
    safe = (
        message.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return f'<?xml version="1.0" encoding="UTF-8"?><Response><Message>{safe}</Message></Response>'


def write_message_log(state: Dict[str, Any], payload: Dict[str, Any]) -> None:
    path = Path(state["job_dir"]) / "messages" / f"{datetime.utcnow().strftime('%Y%m%d-%H%M%S-%f')}.json"
    path.write_text(json.dumps(payload, indent=2))


def detect_logo_slot(state: Dict[str, Any], filename: str, content_type: str) -> str:
    if not any(m.get("kind") == "logo" for m in state.get("media", [])):
        return "logo"
    return "gallery"


async def maybe_download_media(url: str, dest: Path) -> bool:
    if not url:
        return False
    headers = {}
    auth = None
    if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
        auth = (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            resp = await client.get(url, auth=auth, headers=headers)
            resp.raise_for_status()
            dest.write_bytes(resp.content)
            return True
    except Exception:
        return False


async def store_media(state: Dict[str, Any], num_media: int, form: Dict[str, str]) -> None:
    for idx in range(num_media):
        url = form.get(f"MediaUrl{idx}", "")
        content_type = form.get(f"MediaContentType{idx}", "")
        ext = ASSET_EXTENSIONS.get(content_type, ".bin")
        kind = detect_logo_slot(state, f"media-{idx}{ext}", content_type)
        filename = f"{kind}-{len(state.get('media', [])) + 1}{ext}"
        asset_dir = Path(state["job_dir"]) / "assets"
        dest = asset_dir / filename
        downloaded = await maybe_download_media(url, dest)
        entry = {
            "kind": kind,
            "url": url,
            "content_type": content_type,
            "filename": filename,
            "stored": downloaded,
            "stored_path": str(dest) if downloaded else None,
        }
        state.setdefault("media", []).append(entry)


def parse_package(raw: str) -> Optional[str]:
    key = raw.strip().lower()
    return PACKAGE_MAP.get(key)


def build_completion_message(state: Dict[str, Any]) -> str:
    answers = state.get("answers", {})
    media = state.get("media", [])
    package = answers.get("package", "Unknown package")
    name = answers.get("business_name", "your business")
    image_count = len([m for m in media if m.get("kind") == "gallery"])
    has_logo = any(m.get("kind") == "logo" for m in media)
    summary = (
        f"Thank you! We have your intake for {name}.\n\n"
        f"Package: {package}\n"
        f"Images received: {image_count}\n"
        f"Logo received: {'Yes' if has_logo else 'No'}\n\n"
        f"Your info has been saved and the project brief is ready for internal review."
    )
    return summary


def write_summary_files(state: Dict[str, Any]) -> None:
    job_dir = Path(state["job_dir"])
    job_dir.mkdir(parents=True, exist_ok=True)
    answers = state.get("answers", {})
    media = state.get("media", [])
    (job_dir / "answers.json").write_text(json.dumps(answers, indent=2))
    summary_lines = [
        f"# Client Intake Summary\n",
        f"- Session ID: {state.get('session_id')}\n",
        f"- Sender: {state.get('sender')}\n",
        f"- Status: {state.get('status')}\n",
        "\n## Answers\n",
    ]
    for key, value in answers.items():
        summary_lines.append(f"- **{key}**: {value}\n")
    summary_lines.append("\n## Media\n")
    for item in media:
        summary_lines.append(f"- {item.get('kind')}: {item.get('filename')} (stored={item.get('stored')})\n")
    (job_dir / "summary.md").write_text("".join(summary_lines))

    brief_lines = [
        f"# Build Brief\n\n",
        f"## Client\n",
        f"- Business Name: {answers.get('business_name', '')}\n",
        f"- Package: {answers.get('package', '')}\n",
        f"- Goal / CTA: {answers.get('target_customer', '')}\n",
        f"- Contact Details: {answers.get('contact_details', '')}\n",
        f"- Social Links: {answers.get('social_links', '')}\n",
        f"- Brand Story: {answers.get('brand_story', '')}\n",
        f"- Services: {answers.get('services', '')}\n",
        f"- Special Requests: {answers.get('special_requests', '')}\n",
        f"- Testimonials: {answers.get('testimonials', '')}\n",
        f"- Media Count: {len(media)}\n",
        "\n## Notes\n",
        "- Review the saved media folder for logo and gallery assets.\n",
        "- Run a QA check before client handoff.\n",
    ]
    (job_dir / "build-brief.md").write_text("".join(brief_lines))


async def forward_to_paperclip(state: Dict[str, Any]) -> None:
    if not PAPERCLIP_INBOUND_WEBHOOK_URL or not AUTO_FORWARD_TO_PAPERCLIP:
        return
    payload = {
        "source": "twilio-whatsapp-intake",
        "session_id": state.get("session_id"),
        "sender": state.get("sender"),
        "status": state.get("status"),
        "answers": state.get("answers", {}),
        "media": state.get("media", []),
        "job_dir": state.get("job_dir"),
    }
    headers = {"Content-Type": "application/json"}
    if PAPERCLIP_WEBHOOK_SECRET:
        headers["X-Paperclip-Webhook-Secret"] = PAPERCLIP_WEBHOOK_SECRET
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            await client.post(PAPERCLIP_INBOUND_WEBHOOK_URL, json=payload, headers=headers)
    except Exception:
        return


@app.get("/healthz")
async def healthz() -> Dict[str, str]:
    return {"status": "ok"}


@app.get("/debug/jobs")
async def debug_jobs() -> Dict[str, Any]:
    jobs_root = DATA_DIR / "jobs"
    jobs_root.mkdir(parents=True, exist_ok=True)
    jobs = sorted([p.name for p in jobs_root.iterdir() if p.is_dir()])
    return {"jobs": jobs[-20:]}


@app.post("/twilio/whatsapp")
async def twilio_whatsapp(request: Request, Body: str = Form(default=""), From: str = Form(default=""), ProfileName: str = Form(default=""), NumMedia: str = Form(default="0"), MessageSid: str = Form(default="")) -> Response:
    form = await request.form()
    form_dict = {k: str(v) for k, v in form.items()}
    sender = From or "unknown"
    state = load_state(sender)

    write_message_log(state, {
        "received_at": now_iso(),
        "message_sid": MessageSid,
        "from": sender,
        "profile_name": ProfileName,
        "body": Body,
        "num_media": NumMedia,
        "form": form_dict,
    })

    num_media = int(NumMedia or "0")
    if num_media > 0:
        await store_media(state, num_media, form_dict)

    body = (Body or "").strip()

    if state.get("status") == "completed":
        msg = "This intake is already complete. Reply RESET if you want to start a fresh one."
        if body.upper() == "RESET":
            st = load_state(sender)
            st["status"] = "new"
            st["answers"] = {}
            st["media"] = []
            st["current_step_index"] = -1
            save_state(sender, st)
            return Response(content=twiml(FLOW["greeting"]), media_type="application/xml")
        return Response(content=twiml(msg), media_type="application/xml")

    if state.get("current_step_index", -1) == -1:
        step = advance_step(state)
        if body:
            pkg = parse_package(body)
            if pkg and step and step.get("mode") == "package":
                state["answers"][step["key"]] = pkg
                next_step = advance_step(state)
                save_state(sender, state)
                return Response(content=twiml(f"Package selected: {pkg}.\n\n{next_step['prompt']}"), media_type="application/xml")
        save_state(sender, state)
        return Response(content=twiml(FLOW["greeting"] + "\n\n" + step["prompt"]), media_type="application/xml")

    step = get_step(state)
    if step is None:
        step = advance_step(state)
        save_state(sender, state)
        return Response(content=twiml(FLOW["greeting"]), media_type="application/xml")

    mode = step["mode"]
    key = step["key"]

    if mode == "package":
        pkg = parse_package(body)
        if not pkg:
            save_state(sender, state)
            return Response(content=twiml("Please choose one of the listed options, for example: Starter Site, Business Site, Premium Site, AI Quick Win, Launch Audit, or App Discovery."), media_type="application/xml")
        state["answers"][key] = pkg
        next_step = advance_step(state)
        save_state(sender, state)
        return Response(content=twiml(f"Package selected: {pkg}.\n\n{next_step['prompt']}"), media_type="application/xml")

    if mode == "assets":
        if body and body.upper() != "DONE":
            existing = state["answers"].get(key, "")
            state["answers"][key] = (existing + "\n" + body).strip() if existing else body
        if body.upper() == "DONE":
            next_step = advance_step(state)
            save_state(sender, state)
            if next_step is None:
                state["status"] = "completed"
                save_state(sender, state)
                await forward_to_paperclip(state)
                return Response(content=twiml(build_completion_message(state)), media_type="application/xml")
            return Response(content=twiml(f"Thanks, I saved your assets.\n\n{next_step['prompt']}"), media_type="application/xml")
        save_state(sender, state)
        current_assets = len(state.get("media", []))
        return Response(content=twiml(f"Saved. I currently have {current_assets} file(s) for this project. Send more files if needed, then reply DONE when finished."), media_type="application/xml")

    if body:
        state["answers"][key] = body
    elif num_media > 0:
        state["answers"][key] = state["answers"].get(key, "[media received]")
    else:
        save_state(sender, state)
        return Response(content=twiml(step["prompt"]), media_type="application/xml")

    next_step = advance_step(state)
    if next_step is None:
        state["status"] = "completed"
        save_state(sender, state)
        await forward_to_paperclip(state)
        return Response(content=twiml(build_completion_message(state)), media_type="application/xml")

    save_state(sender, state)
    return Response(content=twiml(next_step["prompt"]), media_type="application/xml")
