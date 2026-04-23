---
name: "business-health-check"
description: "10-question diagnostic that analyses an SME's current situation and returns a prioritised action report. Used by LaunchCoach."
---

# Business Health Check

## Purpose

A $49 (Zimbabwe) / $99 (International) entry product that gives an SME owner a clear, honest picture of what's working, what's hurting them, and what to fix first. It is also the best upsell tool in the agency — every Health Check reveals needs that ZimSME AI can solve.

---

## The 10 Questions

FrontDesk or LaunchCoach collects these via WhatsApp. Ask one at a time. Do not dump all 10 at once.

---

**Q1 — The Business**
```
Tell me about your business in 3 sentences: What do you sell or offer, who are your customers, and how long have you been running?
```
*Captures: business type, target market, stage (new/established)*

---

**Q2 — Revenue**
```
How much does your business make in a typical month? 
You don't need to share the exact number — a range is fine:
A) Under $200/month
B) $200–$500/month
C) $500–$1,500/month
D) $1,500–$5,000/month
E) Over $5,000/month
```
*Captures: revenue stage, which services are relevant*

---

**Q3 — Customers**
```
How do most of your customers find you right now? 
(e.g. word of mouth, Facebook, WhatsApp, walk-ins, referrals, Google, other)
```
*Captures: current marketing channels, gaps*

---

**Q4 — Online Presence**
```
Which of these do you currently have? (Say Yes or No for each)
1. A website
2. A Facebook business page
3. An Instagram page
4. A WhatsApp Business account
5. A Google Business listing
```
*Captures: digital presence gaps*

---

**Q5 — Biggest Challenge**
```
What is the single biggest challenge your business faces RIGHT NOW?
Don't overthink it — what keeps you up at night?
```
*Captures: primary pain point — drives the report's top recommendation*

---

**Q6 — Competition**
```
Do you know who your main competitors are? 
How are you different from them — what do you offer that they don't?
```
*Captures: competitive awareness, differentiation clarity*

---

**Q7 — Pricing**
```
How did you decide on your prices? 
Are you confident your prices are right, or do you ever feel you're charging too little (or too much)?
```
*Captures: pricing confidence, potential to increase revenue*

---

**Q8 — Operations**
```
What takes up most of your time in a typical day?
Is there any task you do repeatedly that you feel could be automated or simplified?
```
*Captures: operational bottlenecks, automation opportunities*

---

**Q9 — Goals**
```
Where do you want your business to be in 12 months?
Be specific — what does success look like to you?
```
*Captures: growth ambition, service alignment*

---

**Q10 — Budget**
```
Last question: What's your budget for improving the business this month?
A) Under $50
B) $50–$150
C) $150–$500
D) $500+
E) I'm not sure yet
```
*Captures: budget tier for recommendations*

---

## Generating the Report

After all 10 answers are received, LaunchCoach generates a **Business Health Report**.

### Report Format:

```markdown
# Business Health Report
**Business:** [name]
**Date:** [date]
**Prepared by:** ZimSME AI Solutions

---

## Overall Health Score: [X/10]

[1-paragraph honest summary of the business's current state]

---

## 🔴 Top 3 Problems (Fix These First)

### Problem 1: [Title]
**What's happening:** [1-2 sentence diagnosis]
**Why it matters:** [impact on revenue or growth]
**Fix:** [specific, actionable recommendation]
**ZimSME AI can help with this:** [Yes/No — if yes, which service]

### Problem 2: [Title]
[same format]

### Problem 3: [Title]
[same format]

---

## 🟡 3 Things to Improve (Next Steps)

### Improvement 1: [Title]
**Current situation:** [what they have]
**What good looks like:** [benchmark]
**Action:** [what to do]

### Improvement 2: [Title]
[same format]

### Improvement 3: [Title]
[same format]

---

## 🟢 3 Things Working Well (Protect These)

[3 genuine strengths identified from the answers — be specific, not generic]

---

## Priority Action Plan

| Priority | Action | Timeline | Cost Estimate |
|----------|--------|----------|---------------|
| 1 | [action] | This week | [cost] |
| 2 | [action] | This month | [cost] |
| 3 | [action] | Next 90 days | [cost] |

---

## How ZimSME AI Can Help

Based on your answers, here's what we'd recommend:

[List only services genuinely relevant to their situation. Do not pitch everything.]

| Service | Why It Fits | Price |
|---------|-------------|-------|
| [service] | [reason specific to their answers] | [price] |

---

*This report was prepared by ZimSME AI Solutions based on the information provided.*
*For a follow-up call or to discuss next steps: wa.me/[AGENCY_WHATSAPP]*
```

---

## Scoring Rubric

Calculate the health score (1–10) based on:

| Area | Max Points | Score if... |
|------|-----------|------------|
| Digital Presence | 2 | 2 = has website + Google listing; 1 = has at least FB/WhatsApp; 0 = none |
| Revenue Stability | 2 | 2 = $500+/month; 1 = $200-$500; 0 = under $200 |
| Customer Acquisition | 2 | 2 = multiple channels; 1 = 1 channel; 0 = word of mouth only |
| Pricing Confidence | 2 | 2 = knows competitors + confident pricing; 1 = unsure; 0 = guessing |
| Operational Clarity | 2 | 2 = knows bottlenecks + has a plan; 1 = sees problems; 0 = no awareness |

---

## Tone of the Report

- **Honest but constructive.** Never sugar-coat problems, but always frame them as solvable.
- **Specific.** Every recommendation must be actionable. "Get a website" is not specific. "Create a 3-page website with your services, WhatsApp button, and EcoCash payment — this typically costs $80 at ZimSME AI" is specific.
- **Local.** Reference Zimbabwean market conditions, EcoCash, local competitors where relevant.
- **Not salesy.** Only mention ZimSME AI services where they genuinely solve a problem identified in the report. If the client doesn't need a mobile app, don't mention it.

---

## Delivery

1. Send the report as a PDF (generate using the pdf skill) — it feels more professional than a WhatsApp message
2. Also send the PDF to them via WhatsApp with this message:

```
Hi [Name]! Your Business Health Report is ready. 📊

Here's what we found: [1-sentence headline from the report]

Full report attached. Take a look and let me know if you have any questions.

The #1 thing I'd recommend starting with is: [Top recommendation]

Want to discuss next steps? Just reply to this message or call/WhatsApp me directly.
```

3. Follow up 3 days later if no response:
```
Hi [Name], just checking if you had a chance to read through your report. 
Happy to walk you through it — takes about 10 minutes. 
When's a good time? 😊
```
