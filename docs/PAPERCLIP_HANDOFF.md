# Paperclip Handoff Payload

If `PAPERCLIP_INBOUND_WEBHOOK_URL` is configured, the intake service sends a JSON payload like this:

```json
{
  "source": "twilio-whatsapp-intake",
  "session_id": "20260421-000000-abcdef123456",
  "sender": "whatsapp:+263...",
  "status": "completed",
  "answers": {
    "package": "Starter Site"
  },
  "media": [
    {
      "kind": "logo",
      "filename": "logo-1.png",
      "stored": true
    }
  ],
  "job_dir": "/absolute/path/to/job"
}
```

Use this payload to trigger a Paperclip webhook routine or a small bridge that creates tasks in the correct project.
