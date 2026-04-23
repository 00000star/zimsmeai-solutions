---
name: "Business Health Check Request"
assignee: "launchcoach"
project: "business-consulting"
recurring: false
---

Triggered when a client pays for a Business Health Check ($49 Zim / $99 International) and FrontDesk creates this task.

## What LaunchCoach Must Do

1. Read the client details attached to this task (name, WhatsApp number, business type)
2. Open the `business-health-check` skill: `skills/business-health-check/SKILL.md`
3. Run the 10-question WhatsApp diagnostic via FrontDesk (create a subtask for FrontDesk to relay each question if needed, or send directly if you have WhatsApp access)
4. Once all 10 answers are received, generate the Business Health Report using the skill's report template
5. Use the `pdf` skill to render the report as a PDF
6. Post the PDF file as a task comment
7. Mark this task `in_review` — FrontDesk sends the PDF to the client and handles the upsell conversation

## Task Body (FrontDesk fills in when creating)

- **Client Name:**
- **WhatsApp Number:**
- **Business Name:**
- **Business Type:**
- **Market:** Zimbabwe / International
- **Payment Confirmed:** Yes / No
- **Notes:**
