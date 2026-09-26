#!/usr/bin/env python3
"""Build the Thai site (/th/*) from the English pages + tools/i18n/th/*.json.

    python3 tools/i18n/build_th.py            # build /th pages, inject hreflang into EN pages, update sitemap
    python3 tools/i18n/build_th.py --check    # only report missing translations

English stays the source of truth: edit the EN page, re-run, and any new/changed string shows up
as missing until it is added to tools/i18n/th/<page>.json. Re-running is safe (idempotent).
"""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import htmltext

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
I18N = os.path.join(ROOT, 'tools', 'i18n')
SITE = 'https://jaideeclear.com'

# slug -> EN path. Every page listed here gets a /th/ twin + hreflang pair.
PAGES = {
    'index': '/', 'films': '/films', 'properties': '/properties',
    'window-tinting-villas': '/window-tinting-villas', 'window-tinting-houses': '/window-tinting-houses',
    'window-tinting-condos': '/window-tinting-condos', 'window-tinting-offices': '/window-tinting-offices',
    'window-tinting-hotels': '/window-tinting-hotels', 'window-tinting-bangkok': '/window-tinting-bangkok',
    'window-tinting-phuket': '/window-tinting-phuket', 'window-tinting-chonburi': '/window-tinting-chonburi',
    'schedule': '/schedule', 'about': '/about', 'thank-you': '/thank-you',
    # Phase 2 (2026-09-26): every non-blog page
    'locations': '/locations', 'our-work': '/our-work', 'affiliates': '/affiliates', 'careers': '/careers',
    'window-tinting-restaurants': '/window-tinting-restaurants', 'window-tinting-shophouses': '/window-tinting-shophouses',
    'window-tinting-schools': '/window-tinting-schools', 'window-tinting-padel-courts': '/window-tinting-padel-courts',
}
NOINDEX = {'thank-you'}  # no hreflang / sitemap for non-indexable pages


def th_path(en_path):
    return '/th' if en_path == '/' else '/th' + en_path


def abs_url(path):
    return SITE + path


def has_th(slug):
    return os.path.exists(os.path.join(I18N, 'th', slug + '.json'))


def load_dict(slug):
    d = json.load(open(os.path.join(I18N, 'th', '_common.json'), encoding='utf-8'))
    d.update(json.load(open(os.path.join(I18N, 'th', slug + '.json'), encoding='utf-8')))
    return d


# ---------- link + asset rewriting for pages that live one folder down ----------
_URL_ATTR = re.compile(r'''(\s(?:href|src|poster|action|data-src)\s*=\s*)(["'])(.*?)\2''', re.I | re.S)
_SRCSET = re.compile(r'''(\ssrcset\s*=\s*)(["'])(.*?)\2''', re.I | re.S)


def map_internal(url):
    """EN internal page URL -> TH twin when one exists, else the URL made root-absolute."""
    if url.startswith(('#', 'mailto:', 'tel:', 'data:', 'javascript:', "'", '+')) or not url:
        return url
    rest = ''
    m = re.match(r'^([^?#]*)(.*)$', url, re.S)
    path, rest = m.group(1), m.group(2)
    if path.startswith(SITE):
        path = path[len(SITE):] or '/'
    elif path.startswith(('http:', 'https:', '//')):
        return url
    elif not path.startswith('/'):
        path = '/' + path                       # relative asset/page -> root-absolute
    slug_path = re.sub(r'\.html$', '', path)
    slug_path = '/' if slug_path in ('/index', '') else slug_path
    for slug, en in PAGES.items():
        if slug_path == en and has_th(slug):
            return th_path(en) + rest
    return path + rest


def rewrite_urls(html):
    out = []
    for kind, part in htmltext.segments(html):
        if kind == 'tag' and not part.startswith('</'):
            if part.lower().startswith('<link') and re.search(r'rel=["\'](canonical|alternate|preconnect|stylesheet|icon)', part, re.I) \
                    and 'favicon' not in part:
                out.append(part); continue
            part = _URL_ATTR.sub(lambda m: m.group(1) + m.group(2) + map_internal(m.group(3)) + m.group(2), part)
            part = _SRCSET.sub(lambda m: m.group(1) + m.group(2) + ', '.join(
                map_internal(c.strip().split(' ')[0]) + ('' if ' ' not in c.strip() else ' ' + c.strip().split(' ', 1)[1])
                for c in m.group(3).split(',')) + m.group(2), part)
        out.append(part)
    return ''.join(out)


_TH = '\u0E00-\u0E7F'
_HEADING = re.compile(r'(<h[1-3]\b[^>]*>)(.*?)(</h[1-3]>)', re.S | re.I)
_GAP = re.compile(r'([' + _TH + r'])\s+((?:<(?!/?(?:br|p|div)\b)[^>]+>\s*)+)([' + _TH + r'])|([' + _TH + r'])((?:\s*<(?!/?(?:br|p|div)\b)[^>]+>)+)\s+([' + _TH + r'])')


def tighten_thai_headings(html):
    """Thai has no spaces between words. Fragments joined across <span>/<em> in headings pick up the
    template's whitespace ("ติดฟิล์มกระจก <em>บ้าน</em>"); drop it so the keyword reads as one phrase."""
    def fix(m):
        inner = m.group(2)
        for _ in range(3):
            inner = _GAP.sub(lambda g: (g.group(1) + g.group(2).strip() + g.group(3)) if g.group(1) else (g.group(4) + g.group(5).strip() + g.group(6)), inner)
        return m.group(1) + inner + m.group(3)
    return _HEADING.sub(fix, html)


# ---------- head tags ----------
def hreflang_block(en_path):
    en, th = abs_url(en_path), abs_url(th_path(en_path))
    return ('<!-- hreflang:start -->\n'
            f'<link rel="alternate" hreflang="en" href="{en}">\n'
            f'<link rel="alternate" hreflang="th" href="{th}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{en}">\n'
            '<!-- hreflang:end -->')


_BLOCK = re.compile(r'\n?<!-- hreflang:start -->.*?<!-- hreflang:end -->', re.S)
_SWITCH = re.compile(r'<!-- langswitch:start -->.*?<!-- langswitch:end -->', re.S)
_SWITCH_CSS = re.compile(r'\n?<style id="langswitch-css">.*?</style>', re.S)

SWITCH_CSS = ('<style id="langswitch-css">'
              '.lang-link{display:inline-flex;align-items:center;justify-content:center;min-width:44px;height:38px;padding:0 12px;'
              'border:1.5px solid var(--line,#E9E0D2);border-radius:999px;font-family:var(--head,inherit);font-weight:700;'
              'font-size:.85rem;color:var(--ink,#16120F);text-decoration:none;background:#fff}'
              '.lang-link:hover{border-color:var(--orange,#F5A623)}'
              '.mobmenu .lang-link{margin-top:6px;align-self:flex-start}'
              'html[lang="th"]{--sans:"Inter","Noto Sans Thai",system-ui,sans-serif;--head:"Plus Jakarta Sans","Noto Sans Thai","Inter",sans-serif}'
              'html[lang="th"] body{line-height:1.7}'
              '</style>')


def switch_link(href, label, hreflang):
    return (f'<!-- langswitch:start --><a class="lang-link" href="{href}" hreflang="{hreflang}" lang="{hreflang}" '
            f'aria-label="{"English version" if hreflang == "en" else "ภาษาไทย"}">{label}</a><!-- langswitch:end -->')


def add_switch(html, href, label, hreflang):
    html = _SWITCH.sub('', html)
    link = switch_link(href, label, hreflang)
    # desktop: first item inside .nav-right; mobile: end of .mobmenu
    html = re.sub(r'(<div class="nav-right">)', r'\1' + link.replace('\\', r'\\'), html, count=1)
    html = re.sub(r'(<nav class="mobmenu"[^>]*>.*?)(</nav>)', lambda m: m.group(1) + link + m.group(2), html, count=1, flags=re.S)
    html = _SWITCH_CSS.sub('', html)
    return html.replace('</head>', SWITCH_CSS + '\n</head>', 1)


def strip_generated(html):
    return _SWITCH_CSS.sub('', _SWITCH.sub('', _BLOCK.sub('', html)))


# ---------- EN side ----------
def update_en(slug, en_path):
    fn = os.path.join(ROOT, slug + '.html')
    html = open(fn, encoding='utf-8').read()
    html = strip_generated(html)
    if slug not in NOINDEX:
        html = re.sub(r'(<link rel="canonical"[^>]*>)', lambda m: m.group(1) + '\n' + hreflang_block(en_path), html, count=1)
    html = add_switch(html, th_path(en_path), 'ไทย', 'th')
    open(fn, 'w', encoding='utf-8').write(html)


# ---------- TH side ----------
def ld_hook_for(en_path):
    en_url, th_url = abs_url(en_path).rstrip('/'), abs_url(th_path(en_path))

    def fix(obj):
        if isinstance(obj, dict):
            ident = str(obj.get('@id', ''))
            is_entity = ident.endswith(('#business', '#website', '#organization'))
            new = {}
            for k, v in obj.items():
                if k in ('url', 'item') and isinstance(v, str) and not is_entity:
                    p = v[len(SITE):] if v.startswith(SITE) else None
                    if p is not None:
                        v = abs_url(map_internal(p or '/'))
                new[k] = fix(v)
            if any(t in str(obj.get('@type', '')) for t in ('WebPage', 'FAQPage', 'Service', 'BreadcrumbList', 'Article')):
                new.setdefault('inLanguage', 'th')
            return new
        if isinstance(obj, list):
            return [fix(v) for v in obj]
        return obj
    return fix


def build_th(slug, en_path, strict=False):
    src = open(os.path.join(ROOT, slug + '.html'), encoding='utf-8').read()
    src = strip_generated(src)
    d = load_dict(slug)
    missing = [s for s in htmltext.extract(src) if s not in d]
    if missing:
        print(f'  ! {slug}: {len(missing)} untranslated string(s):')
        for s in missing[:12]:
            print('      -', s[:90])
        if strict:
            return False
    html = htmltext.translate(src, d, script_hook=ld_hook_for(en_path))
    html = rewrite_urls(html)
    html = tighten_thai_headings(html)
    thp = th_path(en_path)
    html = html.replace('<html lang="en"', '<html lang="th"', 1)
    html = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + abs_url(thp) + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + abs_url(thp) + m.group(2), html, count=1)
    if 'og:locale' in html:
        html = re.sub(r'<meta property="og:locale" content="[^"]*">', '<meta property="og:locale" content="th_TH">', html)
    else:
        html = html.replace('</title>', '</title>\n<meta property="og:locale" content="th_TH">\n<meta property="og:locale:alternate" content="en_US">', 1)
    if slug not in NOINDEX:
        html = re.sub(r'(<link rel="canonical"[^>]*>)', lambda m: m.group(1) + '\n' + hreflang_block(en_path), html, count=1)
    # Thai webfont
    html = re.sub(r'(fonts\.googleapis\.com/css2\?[^"]*?)(&display=swap)', r'\1&family=Noto+Sans+Thai:wght@400;500;600;700;800\2', html, count=1)
    html = add_switch(html, en_path, 'EN', 'en')
    # page-specific hooks
    if slug == 'careers':
        # The EN careers page is bilingual (Thai helper lines + EN/TH columns). On /th/ the main text is
        # already Thai, so hide the helper lines and the translated EN column; keep the native Thai column.
        html = html.replace('</head>', '<style id="th-careers">.th{display:none!important}.lang-col.lang-en,.lang-label{display:none!important}'
                            '.lang-grid{grid-template-columns:1fr!important}</style>\n</head>', 1)
    if slug == 'schedule':
        html = html.replace("window.location.href = 'thank-you.html';", "window.location.href = '/th/thank-you';")
        html = html.replace("let lang = 'en';", "let lang = 'th';")
    os.makedirs(os.path.join(ROOT, 'th'), exist_ok=True)
    out = os.path.join(ROOT, 'th', ('index' if slug == 'index' else slug) + '.html')
    open(out, 'w', encoding='utf-8').write(html)
    return True


# ---------- sitemap ----------
def update_sitemap():
    fn = os.path.join(ROOT, 'sitemap.xml')
    xml = open(fn, encoding='utf-8').read()
    xml = re.sub(r'\n  <!-- Thai -->.*?<!-- /Thai -->', '', xml, flags=re.S)
    lastmod = __import__('datetime').date.today().isoformat()
    rows = [f'  <url><loc>{abs_url(th_path(p))}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
            for s, p in PAGES.items() if s not in NOINDEX]
    xml = xml.replace('</urlset>', '\n  <!-- Thai -->\n' + '\n'.join(rows) + '\n  <!-- /Thai -->\n</urlset>')
    open(fn, 'w', encoding='utf-8').write(xml)


def main():
    check = '--check' in sys.argv
    ok = True
    for slug, en_path in PAGES.items():
        if not os.path.exists(os.path.join(I18N, 'th', slug + '.json')):
            print(f'  ! {slug}: no translation file yet'); ok = False; continue
        if check:
            src = strip_generated(open(os.path.join(ROOT, slug + '.html'), encoding='utf-8').read())
            d = load_dict(slug)
            miss = [s for s in htmltext.extract(src) if s not in d]
            print(f'{slug:28} {"OK" if not miss else str(len(miss)) + " missing"}')
            ok &= not miss
            continue
        ok &= build_th(slug, en_path)
    if not check:
        for slug, en_path in PAGES.items():
            if os.path.exists(os.path.join(ROOT, 'th', ('index' if slug == 'index' else slug) + '.html')):
                update_en(slug, en_path)
        update_sitemap()
        print('built', len(PAGES), 'TH pages')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
