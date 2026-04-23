# Twilio Sandbox Intake Service

This is a starter FastAPI service for testing WhatsApp intake with Twilio Sandbox before you build a production-grade intake layer.

## What it does

- receives inbound WhatsApp webhooks from Twilio
- runs a structured homework conversation for website and discovery projects
- accepts text plus multiple images during the branding/assets step
- stores all messages, answers, and media in a client job folder
- generates `answers.json`, `summary.md`, and `build-brief.md`
- optionally forwards a normalized payload to a Paperclip webhook

## Main Endpoints

- `GET /healthz`
- `POST /twilio/whatsapp`
- `GET /debug/jobs`

## Notes

- built for sandbox testing first
- uses sequential question capture rather than advanced AI parsing
- the branding step stays open until the client sends `DONE`
- if Twilio media credentials are present, inbound media is downloaded and stored locally
- if credentials are missing, media URLs are still logged
