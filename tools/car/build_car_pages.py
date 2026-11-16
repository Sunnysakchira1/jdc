#!/usr/bin/env python3
"""Generate the car sub-pages from car-window-tinting.html (the hub is the template).

    python3 tools/car/build_car_pages.py

Writes car-window-tinting-bangkok.html, car-window-tinting-phuket.html and car-window-film.html.
Edit the copy here, re-run, then run tools/i18n/build_th.py for the Thai twins.
Prices, lifespans and claims must match the hub page (no heat/UV percentages, no "only/first").
"""
import json, os, re, html
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SITE = 'https://jaideeclear.com'
T = open(os.path.join(ROOT, 'car-window-tinting.html'), encoding='utf-8').read()

def sec(name):
    """Return the hub section that starts at <!-- name --> (up to the next comment)."""
    a = T.index('<!-- %s -->' % name)
    b = T.index('<!--', a + 5)
    return T[a:b]

HERO, WHY, PRICING, FILMS, GALLERY, STEPS, FINAL = (sec(n) for n in
    ['hero', 'why', 'pricing', 'films', 'gallery', 'steps', 'final cta'])
ARROW = re.search(r'Get My Car Tinting Quote\s*(<svg.*?</svg>)', HERO, re.S).group(1)

EXTRA_CSS = ('.achips{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;max-width:900px;margin:0 auto}'
             '.achips span{background:#fff;border:1px solid var(--line);border-radius:999px;padding:9px 16px;font-family:var(--head);font-weight:600;font-size:.9rem}'
             '.xlinks3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:900px;margin:0 auto}'
             '.xlinks3 a{display:block;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:20px;text-decoration:none;color:var(--ink)}'
             '.xlinks3 a:hover{border-color:var(--orange)}.xlinks3 b{display:block;font-family:var(--head);margin-bottom:4px}.xlinks3 small{color:var(--muted)}'
             '@media(max-width:800px){.xlinks3{grid-template-columns:1fr}}')

def hero(eyebrow, h1, lede, pill):
    h = HERO
    h = re.sub(r'<div class="eyebrow">.*?</div>', '<div class="eyebrow">%s</div>' % eyebrow, h, count=1, flags=re.S)
    h = re.sub(r'<h1 style="margin-top:14px">.*?</h1>', '<h1 style="margin-top:14px">%s</h1>' % h1, h, count=1, flags=re.S)
    h = re.sub(r'<p class="lede">.*?</p>', '<p class="lede">%s</p>' % lede, h, count=1, flags=re.S)
    h = re.sub(r'<div class="proof-pill">.*?</div>', '<div class="proof-pill">%s</div>' % pill, h, count=1, flags=re.S)
    return h

def intro(eyebrow, h2, prose, points):
    return '''<!-- intro prose (answer first) -->
<section style="padding-bottom:0">
  <div class="wrap">
    <div class="sec-head">
      <div class="eyebrow">%s</div>
      <h2>%s</h2>
    </div>
    <p class="prose">%s</p>
    <ul class="prose-points">%s</ul>
  </div>
</section>

''' % (eyebrow, h2, prose, ''.join('<li>%s</li>' % p for p in points))

def areas(eyebrow, h2, p, chips):
    return '''<!-- areas -->
<section id="areas" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <div class="eyebrow">%s</div>
      <h2>%s</h2>
      <p>%s</p>
    </div>
    <div class="achips">%s</div>
  </div>
</section>

''' % (eyebrow, h2, p, ''.join('<span>%s</span>' % c for c in chips))

def table(eyebrow, h2, p, head, rows, note):
    return '''<!-- compare -->
<section id="compare">
  <div class="wrap">
    <div class="sec-head">
      <div class="eyebrow">%s</div>
      <h2>%s</h2>
      <p>%s</p>
    </div>
    <div class="ptable-wrap">
      <table class="ptable">
        <thead><tr>%s</tr></thead>
        <tbody>
%s
        </tbody>
      </table>
    </div>
    <p class="pnote">%s</p>
  </div>
</section>

''' % (eyebrow, h2, p, ''.join('<th>%s</th>' % x for x in head),
       '\n'.join('          <tr><th>%s</th>%s</tr>' % (r[0], ''.join('<td style="white-space:normal;font-family:var(--sans);font-weight:500">%s</td>' % c for c in r[1:])) for r in rows), note)

def links(eyebrow, h2, items):
    return '''<!-- related -->
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <div class="eyebrow">%s</div>
      <h2>%s</h2>
    </div>
    <div class="xlinks3">%s</div>
  </div>
</section>

''' % (eyebrow, h2, ''.join('<a href="%s"><b>%s</b><small>%s</small></a>' % i for i in items))

def faq(eyebrow, h2, qa):
    out = ['<!-- faq -->\n<section class="stats">\n  <div class="wrap">\n    <div class="sec-head">\n      <div class="eyebrow">%s</div>\n      <h2>%s</h2>\n    </div>\n    <div class="faq-list">' % (eyebrow, h2)]
    for i, (q, a) in enumerate(qa):
        out.append('      <details class="faq"%s><summary>%s<span class="pl">+</span></summary><div class="a">%s</div></details>' % (' open' if i == 0 else '', q, a))
    out.append('    </div>\n  </div>\n</section>\n\n')
    return '\n'.join(out)

def final(eyebrow, h2, p):
    f = FINAL
    f = re.sub(r'(<div class="eyebrow"[^>]*>).*?</div>', r'\g<1>%s</div>' % eyebrow, f, count=1, flags=re.S)
    f = re.sub(r'(<h2 style="margin-top:12px">).*?</h2>', r'\g<1>%s</h2>' % h2, f, count=1, flags=re.S)
    f = re.sub(r'<p>.*?</p>', '<p>%s</p>' % p, f, count=1, flags=re.S)
    return f

def plain(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s))

def page(slug, title, desc, crumb, service_name, service_desc, area, body, qa):
    s = T
    url = SITE + '/' + slug
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % desc, s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % title, s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % desc, s, count=1)
    s = s.replace('<link rel="canonical" href="%s/car-window-tinting">' % SITE, '<link rel="canonical" href="%s">' % url)
    s = s.replace('<meta property="og:url" content="%s/car-window-tinting">' % SITE, '<meta property="og:url" content="%s">' % url)
    s = re.sub(r'<!-- hreflang:start -->.*?<!-- hreflang:end -->', '<!-- hreflang:start -->\n<!-- hreflang:end -->', s, count=1, flags=re.S)
    s = re.sub(r'<!-- langswitch:start -->.*?<!-- langswitch:end -->', '<!-- langswitch:start --><!-- langswitch:end -->', s, flags=re.S)
    # structured data
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    g = json.loads(m.group(1))
    svc, bc, fq = g['@graph']
    svc['name'] = service_name; svc['description'] = service_desc
    svc['areaServed'] = [{'@type': 'Place', 'name': a} for a in area]
    bc['itemListElement'].append({'@type': 'ListItem', 'position': 3, 'name': crumb, 'item': url})
    fq['mainEntity'] = [{'@type': 'Question', 'name': plain(q), 'acceptedAnswer': {'@type': 'Answer', 'text': plain(a)}} for q, a in qa]
    s = s[:m.start(1)] + '\n' + json.dumps(g, ensure_ascii=False, indent=2) + '\n' + s[m.end(1):]
    s = s.replace('@media(max-width:800px){.cfilms{grid-template-columns:1fr}}', '@media(max-width:800px){.cfilms{grid-template-columns:1fr}}\n' + EXTRA_CSS, 1)
    s = s.replace('<span class="cur">Car Window Tinting</span>', '<a href="/car-window-tinting">Car Window Tinting</a>\n    <span class="sep">›</span>\n    <span class="cur">%s</span>' % crumb, 1)
    a = s.index('<!-- hero -->'); b = s.index('<footer')
    s = s[:a] + body + s[b:]
    open(os.path.join(ROOT, slug + '.html'), 'w', encoding='utf-8').write(s)
    print('wrote', slug)

PRICE_Q = ('A small car starts at ฿2,900 with Carbon Classic film and ฿4,800 with Ceramic Nano PRO HD. An SUV or mid-size car is ฿3,500 to ฿11,300. A van or large car is ฿4,500 to ฿12,300. Each price covers the whole car, front windscreen included. Prices exclude 7% VAT. Old tint removal is free.')
NEED_A = 'A parking space where we can open all the doors. A covered or shaded spot, like a carport or condo car park, is best. We bring the film, the tools and the water.'
BOOK_A = 'Send us your car model and your address through the booking form or WhatsApp. We confirm your price and a time, then come to you.'

def city(slug, name, areas_list, places, title, desc):
    qa = [
        ('Is there a car tint shop near me in %s?' % name, 'You do not need one near you. JaiDeeClear is a mobile service. Our team drives to your house, condo car park or office in %s and tints the car there.' % name),
        ('How much does car window tinting cost in %s?' % name, PRICE_Q),
        ('Which areas of %s do you cover?' % name, 'We cover %s. Send us your address and we confirm before you book.' % places),
        ('Can you tint my car in a condo car park?', 'Yes. We need a parking space where we can open all the doors. A covered car park works well. We bring the film, the tools and the water.'),
        ('Do you remove my old tint?', 'Yes. We remove old film for free when we fit new film.'),
        ('How do I book?', BOOK_A),
    ]
    body = (
        hero('Car Tinting · We Come to You · %s' % name,
             'Car Window Tinting <span class="acc">Near You</span> in %s' % name,
             'Looking for a car tint shop near you? Skip the drive. Our team comes to your house, condo or office in %s and tints your car where it is parked.' % name,
             '✦ Mobile car tinting across <b>%s</b>' % name)
        + intro('Car Tinting in %s' % name, 'The car tint shop that <span class="acc">comes to you.</span>',
                'JaiDeeClear is a mobile car tinting service in %s. You do not search for a shop nearby, drive there and wait. We drive to you and fit the film at your home, condo or office. A small car costs from ฿2,900 with Carbon Classic film and from ฿4,800 with Ceramic Nano PRO HD. Old tint removal is free. See the <a href="/car-window-film">three car films</a> or the main <a href="/car-window-tinting">car tinting page</a>.' % name,
                ['No drive across %s to a tint shop' % name, 'One price for the whole car, front windscreen included'])
        + areas('Service Area', 'Where we tint cars in <span class="acc">%s.</span>' % name,
                'We come to these areas and the ones around them. Not on the list? Send us your address.', areas_list)
        + WHY + PRICING + FILMS + GALLERY + STEPS
        + faq('Before You Book', 'Car tinting in %s: your questions <span class="acc">answered.</span>' % name, qa)
        + final('Car Tinting in %s' % name, 'Ready to tint your car without leaving home?', 'Send us your car model and address. We reply with your price and the next free time.'))
    page(slug, title, desc, name, 'Car Window Tinting in %s — JaiDeeClear' % name,
         'Mobile car window tinting in %s, fitted at the customer\'s home, condo or office. Carbon Classic and Ceramic Nano PRO films. Free old tint removal and a written warranty.' % name,
         [name], body, qa)

city('car-window-tinting-bangkok', 'Bangkok',
     ['Sukhumvit', 'Asok', 'Silom', 'Sathorn', 'Ratchada', 'Ladprao', 'Chatuchak', 'Bangna', 'Thonburi'],
     'Sukhumvit, Asok, Silom, Sathorn, Ratchada, Ladprao, Chatuchak, Bangna, Thonburi and the areas around them',
     'Car Window Tinting Bangkok: We Come to You | JaiDeeClear',
     'Mobile car tinting in Bangkok. We tint your car at your home, condo or office. From ฿2,900 per car, windscreen included. Free old tint removal.')
city('car-window-tinting-phuket', 'Phuket',
     ['Patong', 'Kata', 'Karon', 'Kamala', 'Surin', 'Bang Tao', 'Cherng Talay', 'Layan', 'Rawai', 'Chalong', 'Kathu', 'Phuket Town', 'Cape Panwa'],
     'Patong, Kata, Karon, Kamala, Surin, Bang Tao, Cherng Talay, Layan, Rawai, Chalong, Kathu, Phuket Town and Cape Panwa',
     'Car Window Tinting Phuket: We Come to You | JaiDeeClear',
     'Mobile car tinting in Phuket. We tint your car at your villa, condo or office. From ฿2,900 per car, windscreen included. Free old tint removal.')

# ---- car window film guide ----
fqa = [
    ('Which car window film is best?', 'It depends on how long you keep the car. Carbon Classic is the lowest price and lasts 2 to 3 years. Ceramic Nano PRO HD lasts 8 to 10 years and suits most cars. Ceramic Nano PRO MAX HD is our top car film.'),
    ('What is the difference between carbon and ceramic car film?', 'Carbon film has a matte, non-reflective finish. It reduces heat and glare at the lowest price. Ceramic film uses nano-ceramic layers. It rejects more heat, keeps a clear view out and lasts 8 to 10 years.'),
    ('How long does car window film last?', 'Carbon Classic lasts 2 to 3 years. Ceramic Nano PRO HD and PRO MAX HD last 8 to 10 years.'),
    ('Does ceramic car film block phone or GPS signal?', 'No. Our Ceramic Nano films are metal-free, so your phone and GPS work as normal.'),
    ('How much does car window film cost?', PRICE_Q),
    ('How dark can I go?', 'Each film comes in several shades, from light to dark. We bring samples so you can see them on your own glass before we start.'),
    ('Do you fit the film at my home?', 'Yes. Our team drives to your house, condo car park or office in Bangkok or Phuket and fits the film there.'),
]
fbody = (
    hero('Car Window Film · Fitted at Your Home',
         'Car Window Film: <span class="acc">Types, Shades</span> and Prices',
         'Three car films, one clear price each. Compare Carbon Classic, Ceramic Nano PRO HD and Ceramic Nano PRO MAX HD, then have it fitted at your home.',
         '✦ Fitted at homes, condos and offices in <b>Bangkok</b> &amp; <b>Phuket</b>')
    + intro('Car Window Film', 'Three car films. <span class="acc">Here is how they differ.</span>',
            'JaiDeeClear fits three car window films: Carbon Classic, Ceramic Nano PRO HD and Ceramic Nano PRO MAX HD. Carbon Classic is the lowest price and lasts 2 to 3 years. The two Ceramic Nano films last 8 to 10 years. Prices start at ฿2,900 for a whole small car, front windscreen included. We fit every film at your home with our <a href="/car-window-tinting">mobile car tinting service</a>.',
            ['Each price covers the whole car, front windscreen included', 'Old tint removed free before the new film goes on'])
    + table('Compare Car Films', 'Carbon vs ceramic <span class="acc">car film.</span>', 'What each film is, how long it lasts and who it suits.',
            ['Film', 'Type', 'Lifespan', 'Best for', 'Small car'],
            [['Carbon Classic', 'Carbon. Matte, non-reflective finish', '2–3 years', 'An older car or one you will sell soon', '฿2,900'],
             ['Ceramic Nano PRO HD', 'Nano-ceramic. Metal-free', '8–10 years', 'Most cars. Strong heat rejection with a clear view out', '฿4,800'],
             ['Ceramic Nano PRO MAX HD', 'Nano-ceramic. Metal-free', '8–10 years', 'Cars parked in the sun every day. The highest heat rejection we offer', '฿9,300']],
            'Prices are for a whole small car, front windscreen included, excluding 7% VAT.')
    + FILMS + PRICING + GALLERY
    + links('Car Tinting Near You', 'Have it fitted <span class="acc">at your home.</span>',
            [('/car-window-tinting', 'Car tinting at home', 'How the mobile service works'),
             ('/car-window-tinting-bangkok', 'Car tinting in Bangkok', 'Areas we cover in Bangkok'),
             ('/car-window-tinting-phuket', 'Car tinting in Phuket', 'Areas we cover in Phuket')])
    + faq('Car Film Questions', 'Car window film: your questions <span class="acc">answered.</span>', fqa)
    + final('Car Window Film', 'Not sure which car film to pick?', 'Send us your car model and address. We recommend a film and reply with your price.'))
page('car-window-film', 'Car Window Film: Types, Shades &amp; Prices | JaiDeeClear',
     'Compare three car window films: Carbon Classic, Ceramic Nano PRO HD and PRO MAX HD. From ฿2,900 per car, fitted at your home in Bangkok and Phuket.',
     'Car Window Film', 'Car Window Film — JaiDeeClear',
     'Three car window films fitted at the customer\'s home in Bangkok and Phuket: Carbon Classic, Ceramic Nano PRO HD and Ceramic Nano PRO MAX HD. Free old tint removal and a written warranty.',
     ['Bangkok', 'Phuket'], fbody, fqa)
