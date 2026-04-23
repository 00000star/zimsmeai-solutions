---
name: "homework-collector"
description: "Drives the WhatsApp intake conversation that collects all client information needed to build their website, app, or AI solution. Used by FrontDesk."
---

# Homework Collector

## Purpose

This skill runs the intake conversation on WhatsApp. When a new client comes in, FrontDesk uses this flow to collect every piece of information WebBot or AIExpert needs to build without asking the client twice.

The tone throughout is: **warm, professional, efficient.** Like a smart business assistant — not a form, not a bot.

---

## Trigger Conditions

Use this skill when:
- A new client has confirmed their package and paid 50% deposit
- FrontDesk needs to collect homework before routing the build task

Do NOT use this skill for initial sales conversations — those use the SPIN selling approach in FrontDesk's AGENTS.md.

---

## The Intake Flow

Run these steps in order. Wait for the client's response at each step before proceeding.

---

### MESSAGE 1 — Welcome & Kickoff

Send immediately after deposit is confirmed.

```
Hi [Name]! 🎉 Welcome to ZimSME AI — we're excited to build your [package] website!

I'm going to ask you a few quick questions to make sure we get your site *exactly* right. 
It should take about 10 minutes. Ready?

First things first — what's the full name of your business?
```

**Capture:** `business_name`

---

### MESSAGE 2 — Business Description

```
Great name! 👍

In 2–3 sentences, tell me what your business does. 
Imagine explaining it to someone who's never heard of it before. What do you do, who do you help, and where are you based?
```

**Capture:** `business_description`, `location`

---

### MESSAGE 3 — Services

```
Got it! Now let's talk about your services or products.

Please list everything you offer — even if it's a long list. 
For each one, add a short description and a price if you're comfortable sharing it.

Example:
• Women's haircuts — $5
• Braiding — from $8
• Hair relaxer — $10
```

**Capture:** `services_list` (name, description, price for each)

---

### MESSAGE 4 — Contact Details

```
Perfect. Let's get your contact info set up on the site.

Please share:
1. Your WhatsApp number (this will be the main contact on the site)
2. Your email address (if you have one)
3. Your physical address or area (even just the suburb and city)
4. Your business hours
```

**Capture:** `whatsapp_number`, `email`, `address`, `business_hours`

If client says "same number I'm using" — confirm by repeating the number back.

---

### MESSAGE 5 — Social Media

```
Do you have any social media pages for the business?

If yes, please send me the links or usernames for:
• Facebook
• Instagram
• LinkedIn (if applicable)
• TikTok (if applicable)

If you don't have any yet, no problem — just say "None" and we can set those up separately.
```

**Capture:** `social_links`

---

### MESSAGE 6 — About the Business

```
Now let's make your "About" section shine. ✨

Tell me your business story:
1. When did you start?
2. Why did you start it?
3. What makes you different from others doing the same thing?
4. Any awards, certifications, or achievements?

Don't worry about making it perfect — just speak from the heart. I'll polish it up.
```

**Capture:** `about_story`, `founded_year`, `differentiators`, `achievements`

---

### MESSAGE 7 — Stats & Proof

```
Great story! 🙌

Now, let's add some numbers to build trust on your site. Even rough numbers work.

Do you know approximately:
1. How many clients/customers have you served?
2. How many years have you been in business?
3. Any other number you're proud of? (e.g. "served 50 events", "30+ staff")

If you're just starting out, say "new business" and we'll use trust signals instead.
```

**Capture:** `stats_numbers`, `years_in_business`

---

### MESSAGE 8 — Branding

```
Almost done! Let's sort out your branding.

1. Do you have a logo? If yes, please send it as a PNG or JPG.
   (WhatsApp-compressed is fine — just send the best quality you have)

2. What are your brand colours? 
   You can send a hex code, describe them ("dark green and gold"), 
   or just say "match the logo" and we'll pick from it.

3. Do you have any photos of your business, products, or team? 
   Please send ALL the photos you have — we'll pick the best ones.
   More is better! Send them one by one or in an album.
```

**Capture:** `logo_file`, `brand_colors`, `photos` (list of all sent images)

Wait patiently for all images. If they send many, acknowledge each batch:
```
Got those! Keep them coming 📸
```

---

### MESSAGE 9 — Testimonials

```
One more thing — do you have any happy clients who've given you good feedback?

If yes, please share 1–3 quotes or reviews (even WhatsApp messages from clients work).
Include their first name and what they do if you can.

If you don't have any yet, no worries — I'll write some starter ones based on your services.
```

**Capture:** `testimonials`

---

### MESSAGE 10 — Special Requests

```
Last question, I promise! 😄

Is there anything specific you want on your site that we haven't covered?
Examples:
• A booking calendar
• A specific page layout you've seen and liked
• A particular feature ("I want a price list table")
• Anything at all

If nothing comes to mind, just say "No, I trust you!" and we'll take it from there.
```

**Capture:** `special_requests`

---

### MESSAGE 11 — Confirmation & Handover

After receiving the answer to MESSAGE 10, compile everything and send a summary:

```
Thank you so much [Name]! 🎉 We have everything we need.

Here's a quick summary of what we collected:

✅ Business: [business_name]
✅ Location: [location]
✅ Services: [count] services listed
✅ Photos: [count] images received
✅ Logo: [received / not received]
✅ Brand Colours: [description]
✅ Social Media: [platforms listed or "None"]
✅ Special Requests: [summary or "None"]

Your [package] website build starts NOW. 🚀

Expected delivery: [delivery date based on tier]
We'll send you a staging link on WhatsApp as soon as it's ready for your review.

If anything changes or you have more photos to send, just WhatsApp us anytime.

Thank you for choosing ZimSME AI! 🙏
```

---

## Creating the Build Task

After sending MESSAGE 11, immediately create a new task in the Web Presence Factory project with:

**Title:** "Build [TIER] site — [Business Name]"
**Assignee:** WebBot
**Project:** Web Presence Factory
**Status:** todo

**Task body must include ALL of this:**

```markdown
## Client: [Business Name]
**Package:** [Basic | Medium | Corporate]
**Deposit:** Confirmed ✓
**Delivery Target:** [date]

## Business Info
- **Name:** [business_name]
- **Tagline:** (generate from description)
- **Location:** [location]
- **WhatsApp:** [whatsapp_number]
- **Email:** [email]
- **Address:** [address]
- **Hours:** [business_hours]

## Services
[list each service with description and price]

## About
[about_story from client]

## Stats
- [stat 1]
- [stat 2]  
- [stat 3]

## Branding
- **Primary Colour:** [color from client]
- **Logo:** [received / not received — if received, attach or note filename]
- **Photos received:** [count and description of each]

## Social Media
[links or "None"]

## Testimonials
[quotes or "None — WebBot to generate"]

## Special Requests
[client requests or "None"]

## Image Files
[List every image the client sent, named and described]
- hero-candidate.jpg — [description]
- logo.png — [description]
- gallery-1.jpg — [description]
...

## Skill
Use the `html-site-generator` skill. Template: `templates/[tier]/index.html`
```

---

## Handling Difficult Situations

### Client sends blurry/small images
```
Thanks for sending! A couple of these might be a bit small for the website. 
Do you have a higher resolution version of [specific image]? 
Even a screenshot from Facebook or WhatsApp works if it's clearer.
If not, no problem — we'll work with what we have!
```

### Client has no logo
```
No logo yet? No problem! We'll use your business name in a clean, styled font for now.
If you'd like a logo designed in the future, we offer that as an add-on — just let us know.
```

### Client is slow to respond
Wait 24 hours. Then:
```
Hi [Name]! Just checking in on the homework for your website build. 
No rush — but whenever you're ready, we're here. 😊
Just reply to continue from where we left off.
```

Wait another 48 hours. If no response, escalate to CEO with a "homework pending" note on the task.

### Client requests something out of scope
```
Great idea! That's actually not included in your current [package], 
but we can absolutely add it as an upgrade.
Let me get you a quick price — I'll send it over shortly.
```

Then create a scope-change task for FrontDesk to quote.
