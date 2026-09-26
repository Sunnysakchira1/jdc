"""Stdlib-only helpers to find and replace visible text in hand-written HTML
without re-serialising the page (markup, inline CSS and JS stay byte-identical)."""
import re, json

# Visible-text segments: anything between tags, outside <script>/<style>/<noscript>/comments
_TOKEN = re.compile(r'(<!--.*?-->|<script\b.*?</script>|<style\b.*?</style>|<noscript\b.*?</noscript>|<[^>]+>)', re.S | re.I)
_ATTR = re.compile(r'''(\s(?:alt|title|placeholder|aria-label|content)\s*=\s*)(["'])(.*?)\2''', re.S | re.I)
# meta tags whose content is human text (others, e.g. viewport/robots, are left alone)
_TEXT_META = re.compile(r'''<meta\s[^>]*(?:name|property)\s*=\s*["'](description|og:title|og:description|twitter:title|twitter:description|og:image:alt)["']''', re.I)
_WORD = re.compile(r'[A-Za-z]{2}')

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

def segments(html):
    """Yield (kind, text) where kind is 'text', 'tag', or 'raw' (script/style/comment)."""
    for part in _TOKEN.split(html):
        if not part:
            continue
        if part.startswith('<'):
            low = part[:9].lower()
            kind = 'raw' if (low.startswith('<!--') or low.startswith('<script') or low.startswith('<style') or low.startswith('<noscript')) else 'tag'
            yield kind, part
        else:
            yield 'text', part

def tag_attr_texts(tag):
    """Human-readable attribute values in one tag."""
    out = []
    is_meta = tag.lower().startswith('<meta')
    for m in _ATTR.finditer(tag):
        name = m.group(1).strip().split('=')[0].strip().lower()
        if name == 'content' and not (is_meta and _TEXT_META.search(tag)):
            continue
        v = m.group(3)
        if _WORD.search(v) and not v.startswith(('http', '/', '#')):
            out.append(v)
    return out

def extract(html):
    """All translatable strings in page order (visible text, attributes, <title>, JSON-LD strings)."""
    found = []
    for kind, part in segments(html):
        if kind == 'text':
            s = norm(part)
            if s and _WORD.search(s):
                found.append(s)
        elif kind == 'tag':
            found += [norm(v) for v in tag_attr_texts(part)]
        elif part[:7].lower() == '<script' and 'ld+json' in part[:80].lower():
            body = part[part.index('>') + 1: part.rindex('<')]
            try:
                found += _json_strings(json.loads(body))
            except ValueError:
                pass
    seen, out = set(), []
    for s in found:
        if s not in seen:
            seen.add(s); out.append(s)
    return out

_SKIP_KEYS = {'@context', '@type', '@id', 'url', 'image', 'logo', 'telephone', 'email', 'sameAs', 'priceRange',
              'postalCode', 'addressCountry', 'latitude', 'longitude', 'item', 'contentUrl', 'thumbnailUrl', 'uploadDate'}

def _json_strings(obj, key=None):
    if isinstance(obj, dict):
        return [s for k, v in obj.items() if k not in _SKIP_KEYS for s in _json_strings(v, k)]
    if isinstance(obj, list):
        return [s for v in obj for s in _json_strings(v, key)]
    if isinstance(obj, str) and _WORD.search(obj) and not obj.startswith('http'):
        return [norm(obj)]
    return []

def _json_translate(obj, t, key=None):
    if isinstance(obj, dict):
        return {k: (v if k in _SKIP_KEYS else _json_translate(v, t, k)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_json_translate(v, t, key) for v in obj]
    if isinstance(obj, str):
        return t.get(norm(obj), obj)
    return obj

def translate(html, t, script_hook=None):
    """Replace every string found in dict t, keeping surrounding whitespace and markup."""
    out = []
    for kind, part in segments(html):
        if kind == 'text':
            s = norm(part)
            if s in t:
                lead = part[:len(part) - len(part.lstrip())]
                tail = part[len(part.rstrip()):]
                part = lead + t[s] + tail
        elif kind == 'tag':
            def rep(m):
                v = norm(m.group(3))
                name = m.group(1).strip().split('=')[0].strip().lower()
                if name == 'content' and not (part.lower().startswith('<meta') and _TEXT_META.search(part)):
                    return m.group(0)
                return m.group(1) + m.group(2) + t.get(v, m.group(3)).replace(m.group(2), '&quot;' if m.group(2) == '"' else '&#39;') + m.group(2) if v in t else m.group(0)
            part = _ATTR.sub(rep, part)
        elif part[:7].lower() == '<script' and 'ld+json' in part[:80].lower():
            head, body, foot = part[:part.index('>') + 1], part[part.index('>') + 1: part.rindex('<')], part[part.rindex('<'):]
            try:
                data = _json_translate(json.loads(body), t)
                if script_hook:
                    data = script_hook(data)
                part = head + '\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n' + foot
            except ValueError:
                pass
        out.append(part)
    return ''.join(out)
