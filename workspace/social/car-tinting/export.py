#!/usr/bin/env python3
"""Render every .slide in the kit's HTML files to a post-ready PNG.

Usage:  python3 export.py [carousel|posts|ads|all] [en|th|both]
Output: out/<file>-<lang>-<nn>.png at true pixel size (no scaling).
"""
import asyncio, os, re, sys, http.server, socketserver, threading, functools

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = 8912
FILES = {"carousel": "carousel.html", "posts": "posts.html", "ads": "ads.html"}


def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=HERE)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), h)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


async def shoot(page, key, fname, lang, outdir):
    await page.goto(f"http://127.0.0.1:{PORT}/{fname}", wait_until="networkidle")
    await page.evaluate("l => document.getElementById('deck').dataset.t = l", lang)
    # strip the studio chrome and un-scale every slide to true pixels
    await page.evaluate("""() => {
        document.querySelector('.bar')?.remove();
        document.querySelectorAll('.slide').forEach(s => s.style.setProperty('--s','1'));
        document.querySelectorAll('.frame').forEach(f => {
            f.style.width='auto'; f.style.height='auto';
            f.querySelector('.tag')?.remove();
        });
        const d = document.getElementById('deck');
        d.style.padding='0'; d.style.gap='0'; d.style.setProperty('--s','1');
    }""")
    await page.wait_for_timeout(600)
    slides = await page.query_selector_all(".slide")
    made = []
    for i, s in enumerate(slides, 1):
        p = os.path.join(outdir, f"{key}-{lang}-{i:02d}.png")
        await s.screenshot(path=p)
        made.append(p)
    return made


async def main():
    which = (sys.argv[1] if len(sys.argv) > 1 else "all").lower()
    langs = (sys.argv[2] if len(sys.argv) > 2 else "both").lower()
    langs = ["en", "th"] if langs == "both" else [langs]
    keys = list(FILES) if which == "all" else [which]

    outdir = os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    httpd = serve()
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        pg = await br.new_page(viewport={"width": 1400, "height": 1800},
                               device_scale_factor=1)
        for k in keys:
            f = FILES.get(k)
            if not f or not os.path.exists(os.path.join(HERE, f)):
                print(f"skip {k} (no {f})"); continue
            for lang in langs:
                for p in await shoot(pg, k, f, lang, outdir):
                    print(os.path.relpath(p, HERE))
        await br.close()
    httpd.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
