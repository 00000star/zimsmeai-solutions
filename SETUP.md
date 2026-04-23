# ZimSME AI — Setup Guide

This package is designed for Paperclip. The company package is importable on its own, while the companion intake service can run beside it.

## 1. Import the Package

Import the root package folder:

```bash
pnpm paperclipai company import --from ./zimsmeai-solutions --target new --new-company-name "ZimSME AI Solutions"
```

## 2. Configure Agent Runtime

This package assumes the `codex_local` adapter for the included agents.

### Minimum requirements

- Codex CLI installed and available as `codex`
- sign in or otherwise make Codex available to the runtime
- a machine that can create and write to the configured absolute working directories under `/tmp/paperclip/zimsmeai-solutions/`

## 3. Create the Working Directories

```bash
mkdir -p /tmp/paperclip/zimsmeai-solutions/{ceo,cto,cmo,frontdesk,projectops,qualitylead,webbot,aiexpert,appmaster,growthhacker,researchlead,launchcoach}
```

## 4. Configure FrontDesk Inputs

Set these in Paperclip for the FrontDesk agent:

- `AGENCY_EMAIL`
- `AGENCY_WHATSAPP`
- `ECOCASH_NUMBER`
- `INNBUCKS_NUMBER` (optional)

## 5. Run the Twilio Sandbox Intake Service

The starter app lives in `integrations/twilio-sandbox-intake/`.

### Quick start

```bash
cd integrations/twilio-sandbox-intake
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8080
```

Expose it publicly with your tunnel or cloud URL and point Twilio Sandbox “When a message comes in” to:

```text
https://YOUR_PUBLIC_URL/twilio/whatsapp
```

## 6. Connect Paperclip Handoff (Optional)

If you want the intake service to forward structured events to Paperclip, set:

- `PAPERCLIP_INBOUND_WEBHOOK_URL`
- `PAPERCLIP_WEBHOOK_SECRET` (optional shared secret)

The service will keep working even if these are blank.

## 7. Test the Company Before Going Live

Run a full dry test:

1. send a WhatsApp enquiry through the Twilio Sandbox
2. confirm FrontDesk-like intake prompts are returned
3. send text answers and image assets
4. confirm a client job folder is created under the intake service data directory
5. confirm a summary brief is generated
6. optionally confirm the normalized payload reaches your Paperclip webhook
7. manually start or route the build inside Paperclip

## 8. Manual Review Items

Even with this package upgraded, still manually verify:

- runtime credentials
- Twilio webhook URL mapping
- media download credentials
- payment numbers
- staging and hosting process
- legal/compliance text for the actual client’s jurisdiction

## 9. Where the Intake Service Stores Data

By default, the companion app stores data under:

```text
integrations/twilio-sandbox-intake/data/
```

Each client gets a timestamped job folder with:
- raw message log
- saved media
- answers JSON
- summary markdown
- build brief markdown
