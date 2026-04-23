---
name: "html-site-generator"
description: "Generates complete, production-ready static HTML websites from client homework data. Used by WebBot to build Basic, Medium, and Corporate tier sites."
---

# HTML Site Generator

## Overview

This skill transforms client homework (text, images, contact info, services) into a deployable static HTML website. The output is a ZIP file containing `index.html` (and additional pages for Corporate) plus an `images/` folder — ready to upload to Hostinger, WebZim, or any hosting provider.

---

## Step 1: Parse the Homework Task

Before writing a single line of HTML, extract every variable from the task. Create an internal data object:

```
CLIENT DATA:
- business_name: [from homework]
- tagline: [from homework OR generate one]
- location: [city, country — use for badge and SEO]
- whatsapp_number: [digits only, no spaces e.g. 263785378845]
- whatsapp_display: [formatted e.g. +263 785 378 845]
- email: [from homework or leave blank]
- address: [from homework or "Harare, Zimbabwe"]
- hours: [from homework or "Mon–Fri 8am–5pm, Sat 9am–1pm"]
- primary_color: [from brand colors, or derive from logo — see Color section]
- services: [list of services with descriptions]
- about_text: [from homework]
- images: [list of provided images and what they show]
- stats: [years in business, clients served, etc. — infer if not given]
- testimonials: [from homework, or generate 2 plausible ones if none given]
- social_links: [Facebook, Instagram URLs if provided]
- tier: [basic | medium | corporate]
- domain_registrar: [hostinger | webzim | namecheap | porkbun — set based on client location]
```

If any critical field is missing, make the best inference. For example:
- No tagline → write one from the business description
- No stats → use "100+ Clients", "5★ Rated", "Same-Day Service" etc.
- No testimonials → write 2 realistic ones based on the service type
- No brand colors → extract from the logo image description, or pick a professional palette based on industry (see below)

---

## Step 2: Choose the Color Palette

### From logo/brand colors provided:
1. Identify the dominant color — this becomes `--primary`
2. Darken it by ~15% for `--primary-dark` (multiply RGB by 0.85)
3. Lighten it to 10% opacity for `--primary-light` (add "1a" alpha in hex)
4. Choose a complementary `--accent` (adjacent on color wheel or analogous)

### Industry defaults (use when no brand colors given):
| Industry | Primary | Accent |
|----------|---------|--------|
| Healthcare / Clinic | #0ea5e9 (blue) | #06b6d4 (cyan) |
| Food / Restaurant | #f97316 (orange) | #ef4444 (red) |
| Legal / Finance | #1e40af (navy) | #3730a3 (indigo) |
| Beauty / Salon | #db2777 (pink) | #9333ea (purple) |
| Tech / IT | #7c3aed (purple) | #2563eb (blue) |
| Retail / Shop | #16a34a (green) | #059669 (emerald) |
| Construction | #d97706 (amber) | #92400e (brown) |
| Education | #2563eb (blue) | #7c3aed (purple) |
| Agriculture | #15803d (green) | #78350f (brown) |
| Church / NGO | #7c3aed (purple) | #2563eb (blue) |

---

## Step 3: Generate the Site

### For BASIC tier (3 sections, single page):
Use `templates/basic/index.html` as the base.

Fill every `{{PLACEHOLDER}}` with real content:

```
{{BUSINESS_NAME}} → exact business name
{{TAGLINE}} → short tagline (5-8 words)
{{META_DESCRIPTION}} → 150-character SEO description
{{META_KEYWORDS}} → "business type, location, service 1, service 2, EcoCash"
{{PRIMARY_COLOR}} → e.g. #16a34a
{{PRIMARY_DARK}} → e.g. #15803d
{{PRIMARY_LIGHT}} → e.g. #dcfce7
{{ACCENT_COLOR}} → e.g. #059669
{{LOCATION}} → "Harare, Zimbabwe" or client's city
{{HEADLINE_PART_1}} → e.g. "Quality"
{{HEADLINE_HIGHLIGHT}} → highlighted word(s) in primary color, e.g. "Hair Care"
{{HEADLINE_PART_2}} → e.g. " You Can Trust"
{{HERO_DESCRIPTION}} → 2-sentence value proposition
{{WHATSAPP_NUMBER}} → digits only e.g. 263785378845
{{WHATSAPP_DISPLAY}} → formatted e.g. +263 785 378 845
{{WHATSAPP_NUMBER_ENCODED}} → URL-encoded business name
{{STAT_1_NUM}}, {{STAT_1_LBL}} → e.g. "200+", "Happy Clients"
{{STAT_2_NUM}}, {{STAT_2_LBL}} → e.g. "5★", "Google Rating"
{{STAT_3_NUM}}, {{STAT_3_LBL}} → e.g. "8yrs", "In Business"
{{SERVICES_HEADING}} → e.g. "Professional Services Built for You"
{{SERVICES_SUBHEADING}} → 1-sentence summary
{{SERVICES_CARDS}} → generate 3-6 .svc-card divs (see format below)
{{ABOUT_HEADING}} → e.g. "Built on Trust, Driven by Quality"
{{ABOUT_PARA_1}} → first about paragraph (from homework)
{{ABOUT_PARA_2}} → second about paragraph (expand if needed)
{{FEATURE_1}}, {{FEATURE_2}}, {{FEATURE_3}} → key differentiators
{{CONTACT_INTRO}} → 1-sentence invitation
{{CONTACT_BODY}} → 2-sentence contact encouragement  
{{EMAIL}} → from homework or "info@businessname.co.zw"
{{ADDRESS}} → from homework
{{HOURS}} → business hours
{{SERVICE_OPTIONS}} → <option> tags for each service
{{FOOTER_TAGLINE}} → 1-sentence brand statement
{{FOOTER_SERVICE_LINKS}} → <a href="#services"> tags for each service
{{YEAR}} → current year
{{TIDIO_KEY}} → leave as TIDIO_KEY_PLACEHOLDER (client connects their own)
```

### Services card format:
```html
<div class="svc-card">
    <div class="svc-icon">[RELEVANT EMOJI]</div>
    <h3>[SERVICE NAME]</h3>
    <p>[2-3 sentence description, benefit-focused, plain language]</p>
</div>
```

Use contextually appropriate emojis:
- Hair: 💇 | Food: 🍽️ | Law: ⚖️ | Tech: 💻 | Health: 🏥 | Shop: 🛒
- Delivery: 🚚 | Construction: 🏗️ | Education: 📚 | Finance: 💰 | Car: 🚗

### For MEDIUM tier (5 sections, single page):
Use `templates/medium/index.html` as the base. Fill all placeholders PLUS:

```
{{USP_CHIP}} → short unique selling point e.g. "Same-Day Service"
{{SOCIAL_PROOF_NUMBER}} → e.g. "200+"
{{SOCIAL_PROOF_LABEL}} → e.g. "Satisfied Clients"
{{STAT_4_NUM}}, {{STAT_4_LBL}} → 4th stat
{{GALLERY_HEADING}} → e.g. "Our Products & Work"
{{GALLERY_SUBHEADING}} → 1-sentence description
{{GALLERY_ITEMS}} → generate 6 .gal-item divs from client images
{{TESTIMONIALS}} → generate 3 .testi divs (use real ones or write realistic ones)
{{SOCIAL_LINKS}} → social link anchors if client has social media
```

Gallery item format (with image):
```html
<div class="gal-item">
    <img src="images/gallery-1.jpg" alt="[descriptive alt text]">
    <div class="gal-overlay"><span class="gal-text">[Caption]</span></div>
</div>
```

Gallery item format (without image — use for missing slots):
```html
<div class="gal-fallback">🛒<br>Coming Soon</div>
```

Testimonial format:
```html
<div class="testi">
    <div class="stars">★★★★★</div>
    <blockquote>"[Realistic 2-3 sentence review in natural language. If real testimonial provided, use it verbatim. If not, write one that matches the business type and sounds authentic.]"</blockquote>
    <div class="testi-author">
        <div class="testi-avatar">[INITIALS]</div>
        <div>
            <div class="testi-name">[First Name + Last Initial]</div>
            <div class="testi-role">[Business type or area e.g. "Small Business Owner, Harare"]</div>
        </div>
    </div>
</div>
```

### For CORPORATE tier (15 pages):
Corporate is a multi-page site. Generate these files:

| File | Content |
|------|---------|
| `index.html` | Full landing page (use medium template as base, add pricing section) |
| `about.html` | Full about page: story, team, mission, values |
| `services.html` | Detailed services with pricing if applicable |
| `portfolio.html` | Full gallery/case studies grid |
| `blog.html` | Blog listing page (3 starter posts) |
| `blog-post-1.html` | First blog post (SEO-optimised, Zimbabwean context) |
| `blog-post-2.html` | Second blog post |
| `blog-post-3.html` | Third blog post |
| `faq.html` | FAQ page (minimum 10 Q&As from homework + common ones) |
| `team.html` | Team page (add if team photos/names provided) |
| `contact.html` | Full contact page with map embed placeholder |
| `testimonials.html` | Full testimonials page |
| `privacy.html` | Privacy policy (generate standard one with business name) |
| `terms.html` | Terms of service (generate standard one) |
| `404.html` | Custom 404 page |

Navigation for Corporate: Include `<nav>` on every page with links to all main pages.

---

## Step 4: Handle Images

Create an `images/` folder. For each client-provided image:

1. Name it descriptively: `hero.jpg`, `about.jpg`, `logo.png`, `gallery-1.jpg` to `gallery-N.jpg`
2. Reference it in the HTML with `onerror` fallbacks (already in templates)
3. Write a descriptive `alt` attribute for every image (SEO + accessibility)

Image assignment priority:
- Best quality wide photo → `hero.jpg` (used in hero section)
- Team/owner/interior photo → `about.jpg`
- Logo file → `logo.png` (nav + favicon)
- Product/service photos → `gallery-1.jpg`, `gallery-2.jpg`, etc.
- If only 1 photo provided: use it as hero, use fallback emoji everywhere else

---

## Step 5: Blog Posts (Corporate Only)

Write 3 SEO-optimised blog posts for the client's industry. Each post:

- **Title format:** "[Benefit/Question] — [Business Name/Location]"
  - Example: "Why Every Harare Restaurant Needs a Loyalty Programme in 2025"
- **Length:** 600–900 words
- **Structure:** Hook (1 para) → Problem (2 para) → Solution (2 para) → How [Business Name] Helps (1 para) → CTA
- **SEO:** Primary keyword in title, first 100 words, and 2× in body
- **Local:** Use Zimbabwean examples, mention EcoCash, local areas, local competitors as context
- **CTA:** Always ends with "Contact [Business Name] on WhatsApp: +[number]"

---

## Step 6: Quality Checks Before Marking Done

Run through this checklist. Do not hand off until all pass:

### Content
- [ ] No `{{PLACEHOLDER}}` strings remain in any HTML file
- [ ] No Lorem Ipsum text anywhere
- [ ] Business name spelled correctly throughout
- [ ] WhatsApp number correct and tested (format: `https://wa.me/[country_code][number]`)
- [ ] Email address correct
- [ ] All service names from homework are represented

### Technical
- [ ] All HTML files are valid (no unclosed tags)
- [ ] CSS custom properties set correctly (colors render on preview)
- [ ] Mobile viewport meta tag present
- [ ] All `<img>` tags have `alt` attributes
- [ ] All `onerror` fallbacks in place (images degrade gracefully)
- [ ] Contact form submits to WhatsApp correctly
- [ ] Footer attribution "Website by ZimSME AI" present with link
- [ ] `{{YEAR}}` replaced with current year

### SEO
- [ ] `<title>` tag on every page — format: "Business Name | Page Name"
- [ ] Meta description on every page — under 160 characters
- [ ] At least one `<h1>` per page
- [ ] Heading hierarchy correct: H1 → H2 → H3 (no skipping)

---

## Step 7: Output

Create the deliverable as a ZIP file:

```
[business-name-slug].zip
├── index.html
├── about.html          (medium+)
├── services.html       (corporate)
├── portfolio.html      (corporate)
├── blog.html           (corporate)
├── blog-post-1.html    (corporate)
├── blog-post-2.html    (corporate)
├── blog-post-3.html    (corporate)
├── faq.html            (corporate)
├── contact.html        (corporate)
├── testimonials.html   (corporate)
├── privacy.html        (corporate)
├── terms.html          (corporate)
├── 404.html            (corporate)
└── images/
    ├── logo.png
    ├── hero.jpg
    ├── about.jpg
    ├── gallery-1.jpg
    └── ... (all client images, renamed)
```

Post the ZIP link as a task comment. Mark the task `in_review` and assign to CTO.

---

## Domain Registrar Selection

Include a Handover Note with domain recommendation:

| Client Location | Primary Recommendation | URL |
|----------------|----------------------|-----|
| Zimbabwe | WebZim (.co.zw) | webzim.co.zw |
| Zimbabwe (fast) | Hostinger | hostinger.com |
| South Africa | Xneelo | xneelo.co.za |
| Nigeria | QServers | qservers.net |
| UK | Namecheap | namecheap.com |
| USA / International | Porkbun | porkbun.com |
| Any (cheapest) | Cloudflare Registrar | cloudflare.com |

.co.zw domains MUST go through WebZim or Hostinger — no other registrar can register them.

---

## Writing Tone for Generated Copy

All copy generated for client sites must be:
- **Direct:** Lead with the benefit, not the feature
- **Local:** Use language Zimbabwean (or relevant market) business owners use
- **Confident:** No "we try to" or "we hope to" — use "we deliver", "we guarantee"
- **Simple:** No industry jargon. Grade 8 reading level.
- **Action-oriented:** Every section ends with an implicit or explicit CTA

Bad: "Our salon provides a wide range of hairdressing services to clients in Harare."
Good: "Get salon-quality hair care right in Harare — walk in, book on WhatsApp, or call us."
