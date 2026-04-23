# Site Templates

These are the base HTML templates WebBot uses to generate client websites. They contain `{{PLACEHOLDER}}` variables that WebBot fills with real client data using the `html-site-generator` skill.

## Template Tiers

| Folder | Package | Files | Description |
|--------|---------|-------|-------------|
| `basic/` | Basic — $80 | Single-page site + legal pages | Hero + Services + About + Contact |
| `medium/` | Medium — $149 | Single-page site + legal pages | Adds Gallery + Testimonials |
| `corporate/` | Corporate — $299 | 15 pages + shared assets | Full multi-page site |
| `agency-portfolio/` | Internal use | 1 page | Starter site for ZimSME AI itself |

## How WebBot Should Use Them

1. Read `skills/html-site-generator/SKILL.md`
2. Copy the correct template folder
3. Replace every placeholder
4. replace the image placeholders with real client assets
5. review legal pages before delivery
6. run QA and ZIP the final site

## Corporate Notes

The corporate template now includes:
- all 15 expected pages
- shared `styles.css`
- `script.js` for mobile nav
- `nav.html` as a reusable reference partial
- placeholder images so previews do not break
