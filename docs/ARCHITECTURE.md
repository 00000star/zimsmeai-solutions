# Cloud Architecture Blueprint

This package is built around **Paperclip as the internal control plane**, not as the public webhook edge.

## Recommended Runtime Shape

1. **WhatsApp intake service**
   - receives Twilio Sandbox or production WhatsApp webhooks
   - stores text, media, and intake state
   - normalises a clean client brief
   - optionally forwards a structured webhook payload to Paperclip

2. **Paperclip company**
   - owns agents, routines, tasks, approvals, and delivery work
   - receives normalised intake events instead of raw public traffic

3. **Storage layer**
   - local disk for tests
   - object storage for cloud deployments

4. **Delivery output**
   - clean deployable ZIP for Hostinger or similar hosting

## Suggested Deployment

- intake API: FastAPI service
- reverse proxy: Nginx / Caddy / cloud platform ingress
- storage: local for sandbox tests, S3/R2 later
- database: optional SQLite for testing, Postgres later
- Paperclip: separate authenticated deployment or internal service

## Why This Shape

- separates public webhooks from internal agent orchestration
- makes media handling and retries easier
- lets you test without exposing Paperclip directly
- keeps the company package importable while the app code lives alongside it
