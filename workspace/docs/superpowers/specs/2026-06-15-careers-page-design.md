# Careers Page — Design Spec

**Date:** 2026-06-15
**Client:** JaiDeeClear (jdc)
**Goal:** Add a careers page to jaideeclear.com advertising one open role (Sales Executive), bilingual EN/Thai, applications via Google Form.

## File & routing
- New file: `careers.html` at repo root.
- Serves at `/careers` (relies on existing `vercel.json` `cleanUrls: true`).
- Self-contained page matching site conventions: GTM snippet, `<meta charset>`/viewport, inline `<style>` reusing the about.html design system, JSON-LD, shared sticky nav + mobile drawer, shared footer, WhatsApp CTA.

## Role
- **Sales Executive** — single posting.
- Location: **Bangkok or Phuket**. Type: **Full-time**.
- Compensation shown as **"Competitive base salary + uncapped commission"** (no figures — decided; numbers discussed at interview).
- Language requirement: fully bilingual Thai/English.

## Apply mechanism
- Primary CTA → Google Form `https://forms.gle/pkFJPaHVVKUA1AhWA` (`target="_blank" rel="noopener"`).
- Secondary CTA → WhatsApp `https://wa.me/+66655079694`.

## Bilingual layout — Option A (inline stacked)
Each content block shows **English first, Thai directly beneath** in a slightly muted style. Zero JS. Both languages always visible to readers and to crawlers/AI.

## Page sections
1. **Hero** — eyebrow "We're Hiring · เรากำลังรับสมัคร", bilingual H1, bilingual subhead, "Apply Now" (→ Google Form) + "Ask on WhatsApp".
2. **Quick-facts bar** (stats-bar style) — Role · Location · Type · Compensation.
3. **About the role / About JaiDeeClear** — short bilingual intro.
4. **What You'll Do** — checkmark list (consultation-list style), bilingual.
5. **You're a Fit If** — requirements list, bilingual.
6. **What We Offer** — benefit cards, bilingual.
7. **Apply CTA banner** — "Ready to Apply?", Google Form + WhatsApp.
8. **Footer** — identical to site, with active state handling.

### Content source (provided by client)
- What You'll Do: outreach to property developers & commercial clients; chase/qualify inbound Meta-ad leads; send quotes, follow up, close; book on-site measurements for install team; keep CRM pipeline clean (light admin).
- Fit: 1–3 yrs sales/telesales/B2B outreach; fluent Thai + English (pitch expat villa owners & Thai developers); self-driven; based in Bangkok or Phuket.
- Offer: competitive base + uncapped commission; fast-growing company; clear room to grow.

## SEO / Schema
- `JobPosting` JSON-LD: title, bilingual-safe English description, `employmentType: FULL_TIME`, `hiringOrganization` (JaiDeeClear, registered address 284/12 Kantang Rd, Mueang Trang, Trang 92000, TH, logo, sameAs), `jobLocation` = two entries (Bangkok, Phuket), `datePosted: 2026-06-15`, `validThrough: 2026-09-15`, `directApply: false`, `applicantLocationRequirements`/region TH.
- `BreadcrumbList`: Home › Careers.
- `<link rel="canonical" href="https://jaideeclear.com/careers">`, OG title/description/type/url/image (jdclogo.jpg), unique meta description, title tag.

## Navigation / discoverability
- **Footer link only** (added next to the Blog link) — on the careers page itself for this change. Top-nav site-wide change deferred (single posting doesn't warrant editing all ~15 files). Not adding "Careers" to the top nav unless requested.

## Out of scope
- No changes to other pages' nav/footer (footer link lives on careers.html; site-wide footer rollout deferred).
- No sitemap/llms.txt update in this pass (note as follow-up if desired).
- No language toggle JS.

## Follow-ups (not in this build)
- Optionally add `/careers` to `sitemap.xml` and `llms.txt`.
- Optionally roll the footer "Careers" link + top-nav link across all pages.
- Refresh/remove the posting after `validThrough` (2026-09-15) or once filled.
