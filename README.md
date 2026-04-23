# ZimSME AI Solutions — Paperclip Company Package

A ready-to-import Paperclip company for running a Zimbabwe-focused AI-assisted websites, automation, consulting, and MVP app operation.

## What This Package Contains

- 12 agents with clearer departmental responsibilities
- 8 starter projects
- recurring and on-demand starter tasks
- custom company skills
- website delivery templates
- cloud architecture and pricing docs
- a runnable Twilio Sandbox intake service for testing

## Package Layout

```text
zimsmeai-solutions/
├── COMPANY.md
├── .paperclip.yaml
├── README.md
├── SETUP.md
├── agents/
├── projects/
├── tasks/
├── skills/
├── templates/
├── docs/
├── integrations/
└── images/
```

## Import

Use the **package root folder itself** as the import target.

```bash
pnpm paperclipai company import --from ./zimsmeai-solutions --target new --new-company-name "ZimSME AI Solutions"
```

Dry run first if you can.

## Important Notes

- `COMPANY.md`, `AGENTS.md`, `PROJECT.md`, `TASK.md`, and `SKILL.md` are the portable base package files
- `.paperclip.yaml` contains Paperclip-specific runtime settings
- `integrations/twilio-sandbox-intake/` is a starter companion service; it is not imported as an agent package file
- website templates are starter assets, not final client projects
- secrets should be configured in environment variables, never hard-coded into package files

## Suggested Next Steps

1. import the package into Paperclip
2. connect Codex CLI and working directories
3. run the Twilio Sandbox intake service
4. paste its public webhook URL into Twilio Sandbox settings
5. test the full website intake flow
