# jaideeclear.com

## Where things go

This repo holds two separate things. Keep them separate.

### 1. The website — repo root

Everything at the repo root is **deployed to jaideeclear.com by Vercel**.
Touching it changes the live site.

```
index.html, *.html      pages
blog/                   blog posts
images/                 images used ON the site
  images/work/            project / portfolio shots
  images/properties/      property-type pages
  images/car-tinting/     car tinting
photos/villas/          install videos + posters
sitemap.xml, robots.txt, llms.txt, vercel.json
favicon.ico, favicon.png
jdclogo.jpg/.png        logos (jdclogo.jpg is the og:image on 27 pages)
insta1-5.jpeg           homepage Instagram strip
catalogue.pdf
```

**Adding a site image:** put it in `images/<category>/` and reference it as
`/images/<category>/file.jpg` — with the leading slash. A bare relative path
breaks on `/blog/` pages.

**Never move these:** `favicon.ico`, `favicon.png`, `robots.txt`, `sitemap.xml`,
`llms.txt` (must be at root), and `jdclogo.jpg` (hardcoded as an absolute URL
in 27 `og:image` tags and the JSON-LD logo).

### 2. Everything else — `workspace/`

Nothing in `workspace/` is deployed. Source material, tools, internal docs.

```
workspace/
  images/          general JaiDee images — see workspace/images/README.md
  remotion/        video project
  video-assets/    source .mov clips, frame grabs
  social/          social carousel + ad generators
  source-assets/   poster PNGs, UV film PDF
  gov/             tender + company registration PDFs (not public)
  screenshots/     page captures
  notes/           working notes
  research/        content research
  docs/            specs
  tools/           generate_city_pages.py, carousel measurement
```

Most of `workspace/` is gitignored — it's large media. See `.gitignore`.

## Quick rule

> Going on the website? → repo root, `images/`
> Everything else? → `workspace/images/`
