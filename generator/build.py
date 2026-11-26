# SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
# SPDX-License-Identifier: Apache-2.0
"""Genera la release statica Eiraman 0.3 (IT alla radice, EN in /en/).

Public repository layout (see README.md, "Withheld inputs"): the author photo, the historical specification 0.3
and the 0.2 release pages are not in this repository. The brand files in brand/ are trademarks (brand/PROVENANCE.md). When an input is missing the build
renders a visible placeholder instead and records it in manifest.json under "placeholders".
Environment: EIRAMAN_OUT (output folder, required), EIRAMAN_PROFILES (role-profiles checkout, default ../role-profiles),
EIRAMAN_BRAND (folder with the logo PNGs), EIRAMAN_PHOTO (author photo), EIRAMAN_SPEC03 (folder with Eiraman.md and
Eiraman.en.md), EIRAMAN_OLD (0.2 release folder)."""
import os, re, json, hashlib, shutil, math, html, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from icons import sprite, icon
from content import SLUG, ORDER, UI, EMBLEM, HOME, METHOD, COMP, ORIG, SRC, ORIGINS, ABOUT, HOME4, PRACT, FWPAGE, FW_SEE, BEZOS_LINE, HOME6, LEVELS, COSTDASH, HOME7, USO, GUIDE, KIT_URL, kit_zip, KIT_ZIP, CC_URL, CODEX_URL, PY_URL, AVVIO_IT, AVVIO_EN, RP_FAM, RPAGE, REQ_TEMPLATE, PROGETTI, COMMUNITY_LINKS, COMMUNITY_REPOS, COMMUNITY_REPO
import mdlite
import favicon  # brand mark drawn in code; the mark is a trademark (brand/PROVENANCE.md, TRADEMARK.md)
import illus6
SPEC03 = os.environ.get("EIRAMAN_SPEC03") or os.path.join(HERE, "spec03")  # optional; the historical specification lives in the guide repository (history/)
PLACEHOLDERS = []  # withheld inputs replaced by a placeholder in this build
def _missing(what):
    if what not in PLACEHOLDERS: PLACEHOLDERS.append(what)

ROOT = os.path.abspath(os.path.join(HERE, ".."))
# Versions (community/VERSIONING.md). Bump them together with the CHANGELOG.md entry of the release.
SITE_VERSION = "0.6.0"  # 0.4.0 was the 25 November 2026 deployment, published under the label 0.3.0 (CHANGELOG.md)
KIT_VERSION = "0.6.0"   # kit/eiraman-kit.zip; its line continues the 0.3.x copies named in the licence notice
OLD = os.environ.get("EIRAMAN_OLD") or os.path.join(ROOT, "releases", "0.2.0-candidata")
OUT = os.environ.get("EIRAMAN_OUT") or os.path.join(ROOT, "build", sys.argv[1] if len(sys.argv) > 1 else SITE_VERSION)
LOGO = os.environ.get("EIRAMAN_BRAND") or os.path.join(ROOT, "brand")
LOGO_FILES = ("eiraman-su-chiaro.png", "eiraman-su-scuro.png")
# A fork without the brand files (the Marks are not licensed) still builds, with a text wordmark.
HAS_BRAND = all(os.path.isfile(os.path.join(LOGO, n)) for n in LOGO_FILES)
def _og_tags(lang, title, desc, url):
    if HAS_BRAND: return favicon.og_tags(lang, title, desc, url, DOMAIN)
    e = lambda s: html.escape(s, quote=True)
    return (f'<meta property="og:type" content="website">\n<meta property="og:site_name" content="Eiraman">\n'
            f'<meta property="og:title" content="{e(title)}">\n<meta property="og:description" content="{e(desc)}">\n'
            f'<meta property="og:url" content="{e(url)}">\n')
DOMAIN = "https://eiraman.tech/"
FONTS = "https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,500;0,600;1,400&family=Barlow+Condensed:wght@500;600&display=swap"
esc = html.escape

import hashlib as _h
CSS_VER = _h.sha256((open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site.css"), encoding="utf-8").read() + open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site-extra.css"), encoding="utf-8").read()).encode()).hexdigest()[:10]

def href(lang, key, frm_lang=None):
    s = SLUG[key][0 if lang == "it" else 1]
    return f"{s}.html"

def path_of(lang, key):
    return (f"{SLUG[key][0]}.html" if lang == "it" else f"en/{SLUG[key][1]}.html")

def url_of(lang, key):
    p = path_of(lang, key)
    return DOMAIN + (p if not p.endswith("index.html") else p[:-10])

def up(lang):
    return "" if lang == "it" else "../"

# ---------- emblema Perché / Come / Cosa ----------
def emblem(lang, size_cls="emblem"):
    e = EMBLEM[lang]; c = 130
    def pt(a, r):
        a = math.radians(a); return (c + r * math.sin(a), c - r * math.cos(a))
    parts = [f'<svg class="{size_cls}" viewBox="0 0 260 260" role="img" aria-label="{esc(e["label"])}">',
             '<defs>',
             f'<path id="em-outer-{lang}" d="M {c},{c-112} A 112 112 0 1 1 {c-0.01},{c-112}"/>']
    cols = ["var(--em-1)", "var(--em-2)", "var(--em-3)"]
    centers = [0, 120, 240]; r = 76
    for i, a0 in enumerate(centers):
        a1, a2 = a0 - 55, a0 + 55
        p1, p2 = pt(a1, r), pt(a2, r)
        if i == 0:
            d = f"M {p1[0]:.2f},{p1[1]:.2f} A {r} {r} 0 0 1 {p2[0]:.2f},{p2[1]:.2f}"
        else:
            d = f"M {p2[0]:.2f},{p2[1]:.2f} A {r} {r} 0 0 0 {p1[0]:.2f},{p1[1]:.2f}"
        parts.append(f'<path id="em-arc{i}-{lang}" d="{d}"/>')
    parts.append('</defs>')
    parts.append(f'<circle cx="{c}" cy="{c}" r="112" fill="none" stroke="var(--em-ring)" stroke-width="1.5"/>')
    parts.append(f'<text font-family="var(--f-mono)" font-size="9.5" fill="var(--band-muted)"><textPath href="#em-outer-{lang}" startOffset="0" textLength="698" lengthAdjust="spacing">{esc(e["what"])}</textPath></text>')
    for i, a0 in enumerate(centers):
        parts.append(f'<use href="#em-arc{i}-{lang}" fill="none" stroke="{cols[i]}" stroke-width="34" stroke-linecap="butt"/>')
        parts.append(f'<text font-family="var(--f-display)" font-weight="600" font-size="15" fill="var(--em-ink)" dominant-baseline="middle" text-anchor="middle"><textPath href="#em-arc{i}-{lang}" startOffset="50%">{esc(e["how"][i])}</textPath></text>')
    # piccole frecce nei vuoti per il ciclo
    for a in (60, 180, 300):
        x, y = pt(a, r); ang = a + 90
        parts.append(f'<path d="M -4,-5 L 4,0 L -4,5" transform="translate({x:.1f},{y:.1f}) rotate({ang - 90})" fill="none" stroke="var(--band-muted)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')
    parts.append(f'<circle cx="{c}" cy="{c}" r="40" fill="var(--em-why)"/>')
    parts.append(f'<text x="{c}" y="{c+1}" text-anchor="middle" dominant-baseline="middle" font-family="var(--f-display)" font-weight="600" font-size="19" fill="var(--em-why-ink)">{esc(e["why"])}</text>')
    parts.append('</svg>')
    return "".join(parts)

# ---------- impaginazione comune ----------
GLOSS = {
 "it": [(r"porte a una e (?:a )?due vie", "(decisioni che non si possono e che si possono annullare)"),
        (r"porte? a una via", "(decisione che non si può annullare)"),
        (r"porte? a due vie", "(decisione che si può annullare)")],
 "en": [(r"one-way and two-way doors", "(decisions that cannot and can be undone)"),
        (r"one-way doors?", "(a decision that cannot be undone)"),
        (r"two-way doors?", "(a decision that can be undone)")]}
def gloss(lang, body):
    parts = re.split(r'(<[^>]+>)', body); done = set(); skip = 0
    for i, p in enumerate(parts):
        if p.startswith("<"):
            tag = re.match(r'</?\s*([a-zA-Z0-9]+)', p)
            if tag and tag.group(1).lower() in ("script", "style", "svg", "template", "title", "summary", "h1", "h2", "h3", "a", "button"):
                skip += -1 if p.startswith("</") else (0 if p.endswith("/>") else 1)
            continue
        if skip > 0: continue
        for n, (pat, g) in enumerate(GLOSS[lang]):
            if n in done or (n > 0 and 0 in done): continue
            m = re.search(pat, p, re.I)
            if m and not p[m.end():m.end()+3].lstrip().startswith("("):
                w = m.group(0).lower()
                if n > 0 and (w.startswith("porte") or w.endswith("doors")):
                    g = {"(decisione che non si può annullare)": "(decisioni che non si possono annullare)",
                         "(decisione che si può annullare)": "(decisioni che si possono annullare)",
                         "(a decision that cannot be undone)": "(decisions that cannot be undone)",
                         "(a decision that can be undone)": "(decisions that can be undone)"}.get(g, g)
                p = p[:m.end()] + " " + g + p[m.end():]; done.add(n)
                if n == 0: done.update({1, 2})
        parts[i] = p
    return "".join(parts)

def page(lang, key, title, desc, body, extra_head=""):
    body = gloss(lang, body)
    u = UI[lang]; pre = up(lang)
    other = "en" if lang == "it" else "it"
    other_href = (f"en/{SLUG[key][1]}.html" if lang == "it" else f"../{SLUG[key][0]}.html")
    cur = ' aria-current="page"'
    navs = "".join(f'<a href="{lnk(lang, k)}"{cur if (k == key or (k == "metodo" and key in ORDER and key != "livelli")) else ""}>{esc(t)}</a>' for k, t in u["nav"])
    foot = "".join(f'<a href="{path_of(lang, k)[3:] if lang=="en" else path_of(lang,k)}">{esc(t)}</a>' for k, t in u["footnav"])
    lang_sw = (f'<b aria-current="true">IT</b><span aria-hidden="true">|</span><a href="{other_href}" hreflang="en" lang="en">EN</a>' if lang == "it"
               else f'<a href="{other_href}" hreflang="it" lang="it">IT</a><span aria-hidden="true">|</span><b aria-current="true">EN</b>')
    home = path_of(lang, "home")[3:] if lang == "en" else "index.html"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url_of(lang, key)}">
{_og_tags(lang, title, desc, url_of(lang, key))}<link rel="alternate" hreflang="it" href="{url_of('it', key)}">
<link rel="alternate" hreflang="en" href="{url_of('en', key)}">
<link rel="alternate" hreflang="x-default" href="{url_of('it', key)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{pre}assets/site.css?v={CSS_VER}">
{favicon.HEAD_TAGS.format(pre=pre) if HAS_BRAND else ''}{extra_head}</head>
<body>
{sprite()}
<a class="skip" href="#main">{u['skip']}</a>
<header class="site-head"><div class="in">
<a class="brand" href="{home}" aria-label="Eiraman · {u['home']}">{f'<img class="logo-light" src="{pre}brand/eiraman-su-chiaro.png" width="1112" height="172" alt="EIRAMAN"><img class="logo-dark" src="{pre}brand/eiraman-su-scuro.png" width="1112" height="172" alt="EIRAMAN">' if HAS_BRAND else '<b class="brand-placeholder" data-placeholder="brand">EIRAMAN</b>'}</a>
<nav class="nav" aria-label="{u['method']}">{navs}</nav>
<details class="menu"><summary>{icon('layers')}{u['menu']}</summary><nav aria-label="{u['menu']}">{navs}</nav></details>
<span class="lang" aria-label="{u['lang_label']}">{lang_sw}</span>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-foot"><div class="in"><span>{u['foot']} · {u['tog']}</span><nav>{foot}</nav></div></footer>
</body>
</html>
"""

def lnk(lang, key):
    return path_of(lang, key)[3:] if lang == "en" else path_of(lang, key)

# ---------- home ----------
def build_home_v3(lang):
    h = HOME[lang]; u = UI[lang]
    prob = "".join(f'<div class="tile {"deny" if i==2 else "fw"}"><div class="ic">{icon(ic, "lg")}</div><h3>{esc(t)}</h3><p>{esc(p)}</p></div>' for i, (ic, t, p) in enumerate(h["prob"]))
    steps = "".join(f'<div class="step {tone}"><div class="num">{i+1}</div><div class="pic">{icon(ic, "xl")}</div><h3>{esc(t)}</h3><p>{esc(p)}</p></div>' for i, (ic, tone, t, p) in enumerate(h["how"]))
    who1 = "".join(f'<li>{icon(ic)}<span>{esc(t)}</span></li>' for ic, t in h["who1"])
    who2 = "".join(f'<li>{icon(ic)}<span>{esc(t)}</span></li>' for ic, t in h["who2"])
    stairs = "".join(f'<div class="stair"><div class="lv">{lv}</div>{icon(ic, "lg")}<h3>{esc(t)}</h3><p>{esc(p)}</p></div>' for ic, lv, t, p in h["stairs"])
    bridges = "".join(f'<div class="br"><span class="from">{icon(ic)}{esc(a)}</span><span class="ar" aria-hidden="true">→</span><span class="to">{esc(b)}</span></div>' for ic, a, b in h["bridges"])
    oic, ot, op = h["out"]
    stairs += f'<div class="stair out">{icon(oic, "lg")}<h3>{esc(ot)}</h3><p>{esc(op)}</p></div><div class="ground"></div>'
    body = f"""
<section class="band hero"><div class="in">
<div><p class="kicker">{esc(h['kicker'])}</p><h1>{esc(h['h1'])}</h1><p class="sub">{esc(h['sub'])}</p>
<div class="cta"><a class="btn primary" href="#come">{esc(h['cta1'])} {icon('arrow')}</a><a class="btn ghost" href="{lnk(lang,'pilota')}">{esc(h['cta2'])}</a></div></div>
{emblem(lang)}
</div></section>
<section class="sec"><div class="in">
<div class="sec-head"><span class="tag">{esc(h['prob_tag'])}</span><h2>{esc(h['prob_h'])}</h2></div>
<div class="tiles">{prob}</div>
<div class="bridges" aria-label="{esc(h['bridge_tag'])}"><p class="bridge-tag">{icon('bridge')} {esc(h['bridge_tag'])}: <b>{esc(h['bridge_h'])}</b></p>{bridges}</div></div></section>
<section class="sec alt" id="come"><div class="in">
<div class="sec-head"><span class="tag">{esc(h['how_tag'])}</span><h2>{esc(h['how_h'])}</h2></div>
<div class="steps">{steps}</div></div></section>
<section class="sec"><div class="in">
<div class="sec-head"><h2>{esc(h['who_h'])}</h2></div>
<div class="duo"><article class="who human"><header>{icon('manager','lg')}<h3>{esc(h['who_h1'])}</h3></header><ul>{who1}</ul></article>
<article class="who ai"><header>{icon('team','lg')}<h3>{esc(h['who_h2'])}</h3></header><ul>{who2}</ul></article></div>
</div></section>
<section class="sec"><div class="in">
<div class="sec-head"><span class="tag">{esc(h['what_tag'])}</span><h2>{esc(h['what_h'])}</h2><p>{esc(h['stairs_note'])}</p></div>
<div class="stairs">{stairs}</div></div></section>
<section class="invite"><div class="in"><h2>{esc(h['invite'])}</h2><a class="btn primary" href="{lnk(lang,'metodo')}">{esc(h['invite_btn'])} {icon('arrow')}</a></div></section>
"""
    return page(lang, "home", h["title"], h["desc"], body)

# ---------- home v6 (molto grafica: perché A/B, come, cosa) ----------
def build_home_v6(lang):
    h = HOME6[lang]
    path = "".join(f'<li><a href="#{anchor}">{icon(ic, "lg")}<span>{esc(t)}</span></a></li>' for ic, t, anchor in h["path"])
    body = f"""
<section class="band hero h6-hero"><div class="in">
<div><h1>{esc(h['h1'])}</h1><p class="sub">{esc(h['sub'])}</p></div>
<nav class="gc-path" aria-label="{esc(h['path_label'])}"><ol>{path}</ol></nav>
</div></section>
<section class="sec h6-why" id="perche"><div class="in">
<p class="h6-tag">{icon('why')} {esc(h['why_tag'])}</p>
<div class="h6-pair">
<article class="h6-card rv"><figure class="ill">{illus6.ill_a(h['a_lbl'], h['a_aria'])}</figure><h2>{esc(h['a_h'])}</h2><p>{esc(h['a_p'])}</p></article>
<article class="h6-card rv"><figure class="ill">{illus6.ill_b(h['b_lbl'], h['b_aria'])}</figure><h2>{esc(h['b_h'])}</h2><p>{esc(h['b_p'])}</p></article>
</div></div></section>
<section class="sec alt h6-how" id="come"><div class="in">
<p class="h6-tag">{icon('bridge')} {esc(h['how_tag'])}</p>
<h2 class="h6-big">{esc(h['how_h'])}</h2>
<figure class="ill wide rv">{illus6.ill_how(h['how_lbl'], h['how_aria'])}{illus6.ill_how_m(h['how_lbl'], h['how_aria'])}</figure>
<div class="h6-two"><p>{esc(h['how_p1'])}</p><p>{esc(h['how_p2'])}</p></div>
</div></section>
<section class="sec h6-what" id="cosa"><div class="in h6-split">
<div><p class="h6-tag">{icon('building')} {esc(h['what_tag'])}</p><h2 class="h6-big">{esc(h['what_h'])}</h2><p class="h6-lede">{esc(h['what_p'])}</p>
<p><a class="btn primary" href="{lnk(lang,'metodo')}">{esc(h['cta'])} {icon('arrow')}</a></p></div>
<figure class="ill rv">{illus6.ill_what(h['what_lbl'], h['what_aria'])}{illus6.ill_what_m(h['what_lbl'], h['what_aria'])}</figure>
</div></section>
<script>(function(){{var els=document.querySelectorAll('.rv');if(!('IntersectionObserver' in window)){{els.forEach(function(e){{e.classList.add('in')}});return;}}var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}})}},{{threshold:.12}});els.forEach(function(e){{io.observe(e)}});}})();</script>
"""
    head = "<script>document.documentElement.classList.add('js')</script>\n"
    return page(lang, "home", h["title"], h["desc"], body, extra_head=head)


H7_DRAW = [
 # 1 · chi decide legge una pagina
 '<svg viewBox="0 0 200 130" role="img" aria-hidden="true">'
 '<circle class="d-h" cx="62" cy="40" r="16"/>'
 '<path class="d-h" d="M32 112 C32 82 46 66 62 66 C78 66 92 82 92 112 Z"/>'
 '<rect class="d-pg" x="104" y="28" width="62" height="82" rx="4"/>'
 '<line class="d-ln" x1="114" y1="46" x2="156" y2="46"/><line class="d-ln" x1="114" y1="58" x2="156" y2="58"/>'
 '<line class="d-ln" x1="114" y1="70" x2="148" y2="70"/><line class="d-bad" x1="114" y1="40" x2="140" y2="40"/>'
 '<line class="d-ln" x1="114" y1="82" x2="156" y2="82"/><line class="d-ln" x1="114" y1="94" x2="140" y2="94"/>'
 '<path class="d-arm" d="M88 84 L106 74"/></svg>',
 # 2 · gli agenti lavorano, nessuna chiusura senza prova
 '<svg viewBox="0 0 200 130" role="img" aria-hidden="true">'
 '<rect class="d-a" x="22" y="22" width="34" height="34" rx="9"/><rect class="d-a" x="66" y="22" width="34" height="34" rx="9"/>'
 '<rect class="d-a" x="44" y="66" width="34" height="34" rx="9"/>'
 '<circle class="d-eye" cx="33" cy="37" r="2.4"/><circle class="d-eye" cx="45" cy="37" r="2.4"/>'
 '<circle class="d-eye" cx="77" cy="37" r="2.4"/><circle class="d-eye" cx="89" cy="37" r="2.4"/>'
 '<circle class="d-eye" cx="55" cy="81" r="2.4"/><circle class="d-eye" cx="67" cy="81" r="2.4"/>'
 '<rect class="d-pg" x="118" y="30" width="58" height="76" rx="4"/>'
 '<line class="d-ln" x1="128" y1="46" x2="166" y2="46"/><line class="d-ln" x1="128" y1="58" x2="160" y2="58"/>'
 '<circle class="d-ok" cx="160" cy="92" r="17"/><path class="d-tick" d="M151 92 L157 98 L169 85"/>'
 '<path class="d-arrow" d="M104 64 L114 64"/></svg>',
 # 3 · tre livelli: per me, per il team, per i clienti
 '<svg viewBox="0 0 200 130" role="img" aria-hidden="true">'
 '<rect class="d-s1" x="20" y="88" width="52" height="26" rx="3"/>'
 '<rect class="d-s2" x="74" y="62" width="52" height="52" rx="3"/>'
 '<rect class="d-s3" x="128" y="36" width="52" height="78" rx="3"/>'
 '<circle class="d-h" cx="46" cy="70" r="8"/>'
 '<circle class="d-h" cx="92" cy="44" r="7"/><circle class="d-h" cx="108" cy="44" r="7"/>'
 '<circle class="d-h" cx="140" cy="18" r="6"/><circle class="d-h" cx="154" cy="18" r="6"/><circle class="d-h" cx="168" cy="18" r="6"/>'
 '<text class="d-num" x="46" y="106" text-anchor="middle">0</text><text class="d-num" x="100" y="94" text-anchor="middle">1</text>'
 '<text class="d-num" x="154" y="80" text-anchor="middle">2</text></svg>',
]


H7_STEPS = {"it": ["Visione", "Design Thinking AI", "Mandato", "AI Squad", "Prove", "Servizio in produzione"],
            "en": ["Vision", "AI Design Thinking", "Mandate", "AI Squad", "Evidence", "Service in production"]}
H7_FLOW_LABEL = {"it": "Dalla visione al servizio in produzione: più modelli AI esplorano l'idea e un analista la fa convergere, l'idea diventa un mandato, un'AI Squad costruisce, le prove verificano, il servizio entra in produzione.",
                 "en": "From vision to service in production: several AI models explore the idea and an analyst makes it converge, the idea becomes a mandate, an AI Squad builds, evidence verifies, the service goes into production."}

def _flow_icons(cx, cy, k):
    """Disegni delle cinque tappe, centrati in (cx, cy)."""
    if k == 0:   # idea: lampadina
        return (f'<circle class="f-h" cx="{cx}" cy="{cy-6}" r="22"/><rect class="f-h" x="{cx-10}" y="{cy+14}" width="20" height="12" rx="3"/>'
                f'<path class="f-ray" d="M{cx-36} {cy-6} h-10 M{cx+36} {cy-6} h10 M{cx} {cy-40} v-10 M{cx-26} {cy-32} l-7 -7 M{cx+26} {cy-32} l7 -7"/>')
    if k == 1:   # Design Thinking AI: divergenza e convergenza
        return (f'<circle class="f-h" cx="{cx-30}" cy="{cy}" r="6"/>'
                f'<path class="f-dt" d="M{cx-24} {cy} L{cx-2} {cy-22} M{cx-24} {cy} L{cx-2} {cy} M{cx-24} {cy} L{cx-2} {cy+22}"/>'
                f'<circle class="f-a" cx="{cx}" cy="{cy-22}" r="7"/><circle class="f-a" cx="{cx}" cy="{cy}" r="7"/><circle class="f-a" cx="{cx}" cy="{cy+22}" r="7"/>'
                f'<path class="f-dt" d="M{cx+7} {cy-22} L{cx+26} {cy} M{cx+7} {cy} L{cx+26} {cy} M{cx+7} {cy+22} L{cx+26} {cy}"/>'
                f'<circle class="f-ok" cx="{cx+30}" cy="{cy}" r="6"/>')
    if k == 2:   # mandato: foglio con firma
        return (f'<rect class="f-pg" x="{cx-24}" y="{cy-32}" width="48" height="62" rx="4"/>'
                f'<path class="f-ln" d="M{cx-14} {cy-18} h28 M{cx-14} {cy-8} h28 M{cx-14} {cy+2} h20"/>'
                f'<path class="f-sign" d="M{cx-14} {cy+18} c6 -8 10 6 16 -2 s8 4 12 -2"/>')
    if k == 3:   # AI Squad che costruisce blocchi
        return (f'<rect class="f-a" x="{cx-40}" y="{cy-30}" width="24" height="24" rx="7"/><rect class="f-a" x="{cx-12}" y="{cy-30}" width="24" height="24" rx="7"/>'
                f'<rect class="f-a" x="{cx+16}" y="{cy-30}" width="24" height="24" rx="7"/>'
                f'<rect class="f-blk" x="{cx-34}" y="{cy+4}" width="20" height="20" rx="2"/><rect class="f-blk" x="{cx-10}" y="{cy+4}" width="20" height="20" rx="2"/>'
                f'<rect class="f-blk" x="{cx+14}" y="{cy+4}" width="20" height="20" rx="2"/><rect class="f-blk" x="{cx-22}" y="{cy-16}" width="20" height="0" rx="2"/>')
    if k == 4:   # prove: lente con visto
        return (f'<circle class="f-ok" cx="{cx-4}" cy="{cy-4}" r="24"/><path class="f-tick" d="M{cx-15} {cy-4} l8 8 l15 -16"/>'
                f'<path class="f-handle" d="M{cx+14} {cy+14} l16 16"/>')
    # servizio in produzione: finestra applicazione con utenti
    return (f'<rect class="f-win" x="{cx-34}" y="{cy-30}" width="68" height="48" rx="5"/><path class="f-bar" d="M{cx-34} {cy-20} h68"/>'
            f'<circle class="f-dot" cx="{cx-27}" cy="{cy-25}" r="2"/><circle class="f-dot" cx="{cx-20}" cy="{cy-25}" r="2"/>'
            f'<path class="f-ln" d="M{cx-24} {cy-8} h30 M{cx-24} {cy+2} h40"/>'
            f'<circle class="f-h" cx="{cx-16}" cy="{cy+32}" r="6"/><circle class="f-h" cx="{cx}" cy="{cy+32}" r="6"/><circle class="f-h" cx="{cx+16}" cy="{cy+32}" r="6"/>')

def h7_flow(lang):
    steps = H7_STEPS[lang]
    xs = [85, 251, 417, 583, 749, 915]
    parts = ['<svg class="h7-flow h" viewBox="0 0 1000 190" role="img" aria-label="' + esc(H7_FLOW_LABEL[lang]) + '">']
    parts.append('<path class="f-path" d="M85 82 H915"/>')
    for i, x in enumerate(xs):
        parts.append(f'<circle class="f-st" cx="{x}" cy="82" r="50"/>' + _flow_icons(x, 82, i))
        parts.append(f'<text class="f-lbl" x="{x}" y="168" text-anchor="middle">{esc(steps[i])}</text>')
    for x in xs[:-1]:
        parts.append(f'<path class="f-arr" d="M{x+62} 76 l8 6 l-8 6"/>')
    parts.append('</svg>')
    # versione verticale per telefono
    v = ['<svg class="h7-flow v" viewBox="0 0 380 744" role="img" aria-label="' + esc(H7_FLOW_LABEL[lang]) + '">']
    v.append('<path class="f-path" d="M70 62 V682"/>')
    for i in range(6):
        y = 62 + i * 124
        v.append(f'<circle class="f-st" cx="70" cy="{y}" r="48"/>' + _flow_icons(70, y, i))
        v.append(f'<text class="f-lbl" x="140" y="{y+7}">{esc(steps[i])}</text>')
    v.append('</svg>')
    return '<div class="h7-flowbox">' + "".join(parts) + "".join(v) + '</div>'

def build_home_v7(lang):
    h = HOME7[lang]
    blocks = "".join(
        f'<section class="h7-block"><p class="h7-k">{esc(k)}</p><h2>{esc(hh)}</h2>' + (f'<p>{esc(p)}</p>' if p else '') + '</section>'
        for k, hh, p in h["blocks"])
    body = f"""
<section class="h7"><div class="in h7-in">
<h1>{esc(h['h1'])}</h1>
<p class="h7-lead">{esc(h['lead'])}</p>
{h7_flow(lang)}
<div class="h7-blocks">{blocks}</div>
<p class="h7-cta"><a class="btn primary" href="{lnk(lang,'metodo')}">{esc(h['btn'])}</a></p>
</div></section>
"""
    return page(lang, "home", h["title"], h["desc"], body)

def build_home(lang):
    return build_home_v7(lang)

# ---------- panoramica ----------

def build_home_v4(lang):
    h = HOME4[lang]; old = HOME[lang]; u = UI[lang]
    tiles = "".join(
        f'<li class="ft" style="--i:{n}"><span class="ft-ic">{icon(ic,"lg")}</span>'
        f'<span class="ft-from">{esc(a)}</span><span class="ft-to">{esc(b)}</span></li>'
        for n, (ic, a, b) in enumerate(h["tiles"]))
    counters = "".join(f'<div class="ctr"><b>{esc(n)}</b><span>{esc(l)}</span></div>' for n, l in h["counters"])
    quiz = ""
    for q, ans, why in h["quiz"]:
        quiz += (f'<li class="q" data-ans="{ans}"><p class="q-t">{esc(q)}</p>'
                 f'<div class="q-b"><button type="button" class="q-btn ai" data-pick="ai" >{icon("door2")}<span>{esc(h["q_ai"])}</span></button>'
                 f'<button type="button" class="q-btn me" data-pick="me" >{icon("door1")}<span>{esc(h["q_me"])}</span></button></div>'
                 f'<p class="q-r" aria-live="polite"></p>'
                 f'<details class="q-nojs"><summary>{esc(h["q_show"])}</summary><p>{esc(why)}</p></details>'
                 f'<template class="q-why">{esc(why)}</template></li>')
    legend = f'<p class="q-legend">{icon("door2")}{icon("door1")}<span>{esc(BEZOS_LINE[lang])}</span></p>'
    rev = (f'<div class="rev" role="img" aria-label="{esc(h["rev_t"])}"><p class="rev-t">{icon("doc")} {esc(h["rev_t"])}</p>'
           f'<p class="rev-h bad">{esc(h["rev_bad"])}</p><ul>' + "".join(f"<li>{esc(x)}</li>" for x in h["rev_bad_l"]) + '</ul>' +
           ((f'<p class="rev-h">{esc(h["rev_ok"])}</p><ul>' + "".join(f"<li>{esc(x)}</li>" for x in h["rev_ok_l"]) + '</ul>') if h.get("rev_ok_l") else '') +
           f'<p class="rev-h">{esc(h["rev_ask"])}</p><ul>' + "".join(f"<li>{esc(x)}</li>" for x in h["rev_ask_l"]) + '</ul></div>')
    extras = {"": "", "counters": f'<div class="ctrs">{counters}</div>', "quiz": legend + f'<ol class="quiz">{quiz}</ol>', "rev": rev}
    week = ""
    for s in h["stages"]:
        week += (f'<li class="day {s["tone"]}"><span class="d-dot">{icon(s["ic"])}</span><div class="d-body"><p class="d-lab">{esc(s["lab"])}</p>'
                 f'<p class="fw-shift"><span class="fw-old">{esc(s["frm"])}</span><span class="fw-ar" aria-hidden="true">→</span>'
                 f'<a class="fw-new" href="{lnk(lang,s["key"])}">{esc(s["to"])}</a></p>'
                 f'<p class="d-desc">{esc(s["desc"])}</p>{extras[s["extra"]]}'
                 f'<p class="you">{icon("manager")}<b>{esc(h["you"])}</b> {esc(s["you"])}</p></div></li>')
    stairs = "".join(f'<div class="stair"><div class="lv">{lv}</div>{icon(ic, "lg")}<h3>{esc(tt)}</h3><p>{esc(pp)}</p></div>' for ic, lv, tt, pp in old["stairs"])
    oic, ot, op = old["out"]
    stairs += f'<div class="stair out">{icon(oic, "lg")}<h3>{esc(ot)}</h3><p>{esc(op)}</p></div><div class="ground"></div>'
    js = """<script>
(function(){document.documentElement.classList.add('js');
document.querySelectorAll('.quiz .q').forEach(function(q){var r=q.querySelector('.q-r');var why=q.querySelector('.q-why').innerHTML;
q.querySelectorAll('.q-btn').forEach(function(b){b.addEventListener('click',function(){var ok=b.dataset.pick===q.dataset.ans;
q.querySelectorAll('.q-btn').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
q.classList.remove('ok','no');q.classList.add(ok?'ok':'no');r.innerHTML='<b>'+(ok?'""" + esc(h["q_ok"]) + """':'""" + esc(h["q_no"]) + """')+'</b> '+why;});});});})();
</script>"""
    pe = h["pearl"]
    body = f"""
<section class="hero4 pearl-hero"><div class="in">
<div class="h4-text"><p class="kicker">{esc(h['kicker'])}</p><h1>{esc(h['h1'])}</h1><p class="sub">{esc(h['sub'])}</p>
<div class="cta"><a class="btn primary" href="#settimana">{esc(h['cta1'])} {icon('arrow')}</a></div></div>
<figure class="pearl"><p class="pearl-tag">{esc(pe['tag'])}</p>
<blockquote><p>{esc(pe['story'])}</p><p class="pearl-q">{esc(pe['quote'])}</p></blockquote>
<figcaption><p class="pearl-t">{esc(pe['thesis'])}</p>
<a href="https://en.wikisource.org/wiki/The_Pearl_of_Love" rel="noopener" target="_blank">{esc(pe['src'])} {icon('arrow')}</a></figcaption></figure>
</div></section>
<section class="sec alt week4" id="settimana"><div class="in">
<div class="sec-head"><span class="tag">{esc(h['wk_tag'])}</span><h2>{esc(h['wk_h'])}</h2><p class="ex">{icon('alert')} {esc(h['wk_note'])}</p></div>
<ol class="week">{week}</ol>
<p class="time">{icon('calendar','lg')}<span>{esc(h['time'])} <small>({esc(h['time_s'])})</small></span></p>
</div></section>
{js}
"""
    return page(lang, "home", old["title"], old["desc"], body)

# ---------- panoramica ----------
def build_method(lang):
    m = METHOD[lang]; u = UI[lang]
    dots = {"why": "var(--em-why-ink)", "how": "var(--em-2)", "what": "var(--em-3)"}
    cols = "".join(f'<div class="col"><h3><span class="dot" style="background:{dots[k] if k!="why" else "var(--primary)"}"></span>{esc(t)}</h3><p>{esc(p)}</p></div>' for k, t, p in m["cols"])
    cards = ""
    for k in ORDER:
        c = COMP[k]; t = c[lang]; tone = c["tone"]
        cards += f'<a class="card {tone}" href="{lnk(lang,k)}"><span class="ic">{icon(c["icon"], "lg")}</span><span><h3>{esc(t["card"])}</h3><p>{esc(t["line"])}</p><span class="go">{u["explore"]} →</span></span></a>'
    o = ORIG[lang]
    cards += f'<a class="card new" href="{lnk(lang,"originalita")}"><span class="ic">{icon("why", "lg")}</span><span><h3>{esc(o["card"])}</h3><p>{esc(o["line"])}</p><span class="go">{u["explore"]} →</span></span></a>'
    P = PRACT[lang]
    mg = (f'<div class="pr-head" aria-hidden="true"><span></span><span>{esc(P["keep"])}</span><span>{esc(P["change"])}</span><span>{esc(P["you"])}</span></div>' +
          "".join(f'<article class="pr"><div class="pr-name"><span class="ic">{icon(ic,"lg")}</span><div><p class="pr-old">{esc(a)}</p>'
                  f'<h3><a href="{lnk(lang,k)}">{esc(b)}</a></h3></div></div>'
                  f'<p><span class="pr-l">{esc(P["keep"])}</span>{esc(kp)}</p><p><span class="pr-l">{esc(P["change"])}</span>{esc(ch)}</p>'
                  f'<p class="pr-you"><span class="pr-l">{esc(P["you"])}</span>{icon("manager")} {esc(y)}</p></article>'
                  for ic, a, b, kp, ch, y, k in P["rows"]))
    refs = "".join(f'<a class="card" href="{lnk(lang,k)}"><span class="ic">{icon(ic,"lg")}</span><span><h3>{esc(t)}</h3><p>{esc(p)}</p></span></a>' for k, ic, t, p in m["ref"])
    body = f"""
<section class="band"><div class="in">
<nav class="crumbs" aria-label="breadcrumb"><a href="{lnk(lang,'home')}">{u['home']}</a><span>/</span><span>{u['method']}</span></nav>
<h1>{esc(m['h1'])}</h1><p class="why">{esc(m['why'])}</p></div></section>
<section class="sec"><div class="in"><div class="circle3"><div class="emblem-wrap" style="background:var(--band);border-radius:16px;padding:14px">{emblem(lang)}</div>{cols}</div></div></section>
<section class="sec"><div class="in">
<div class="sec-head" id="framework"><span class="tag">{icon('bridge')} {UI[lang]['origin']}</span><h2>{esc(PRACT[lang]['h'])}</h2><p>{esc(PRACT[lang]['p'])}</p></div>
<div class="prs">{mg}</div><p class="tm">{esc(PRACT[lang]['tm'])}</p><p class="fwlink"><a class="btn ghost" href="{lnk(lang,'framework')}">{icon('bridge')} {esc(PRACT[lang]['fwlink'])} {icon('arrow')}</a></p></div></section>
<section class="sec alt"><div class="in">
<div class="sec-head"><h2>{esc(m['explore_h'])}</h2><p>{esc(m['explore_p'])}</p></div>
<div class="cards">{cards}</div></div></section>
<section class="sec"><div class="in">
<div class="sec-head"><h2>{esc(m['ref_h'])}</h2></div><div class="cards ref">{refs}</div>
<p class="note" style="margin-top:20px">{esc(m['note'])}</p>
<p class="teaser"><a href="{lnk(lang,'chi')}">{icon('person')} {esc(ABOUT[lang]['teaser'])} {icon('arrow')}</a></p></div></section>
"""
    return page(lang, "metodo", m["title"], m["desc"], body)

# ---------- estrazione dalla specifica 0.2 ----------
SPEC = {}
def spec_html(lang):
    if lang not in SPEC and not os.path.isfile(os.path.join(SPEC03, "Eiraman.md" if lang == "it" else "Eiraman.en.md")):
        _missing("spec03")
        SPEC[lang] = ('<article class="prose" data-placeholder="spec03"><h1>' + ("Specifica 0.3" if lang == "it" else "Specification 0.3") + '</h1><p>'
                      + ("La specifica storica 0.3 non fa parte di questo repository." if lang == "it" else "The historical specification 0.3 is not part of this repository.")
                      + '</p></article>')
    if lang not in SPEC:
        src = open(os.path.join(SPEC03, "Eiraman.md" if lang == "it" else "Eiraman.en.md"), encoding="utf-8").read()
        body = src.split("\n", 1)[1]
        if lang == "it":
            lm = lambda u: u if u.startswith("http") else {"../en/framework/Eiraman.en.md": "en/framework/Eiraman.en.md", "Fonti.md": "framework/Fonti.md"}.get(u, u)
            T = dict(toc="Indice", h1="Metodo Eiraman · specifica 0.3", dl_spec="framework/Eiraman.md", dl_src="framework/Fonti.md", l1="Specifica in Markdown", l2="Fonti e bibliografia")
        else:
            lm = lambda u: u if u.startswith("http") else {"../../framework/Eiraman.md": "../framework/Eiraman.md", "../../framework/Fonti.md": "../framework/Fonti.md"}.get(u, u)
            T = dict(toc="Contents", h1="The Eiraman Method · specification 0.3", dl_spec="framework/Eiraman.en.md", dl_src="../framework/Fonti.md", l1="Specification in Markdown", l2="Sources and bibliography")
        toc = []
        content = mdlite.md(body, lm, toc)
        side = "".join(f'<li><a href="#{h}">{mdlite.inline(x)}</a></li>' for h, x in toc)
        SPEC[lang] = (f'\n<aside class="toc"><details open><summary>{T["toc"]}</summary><ol class="plain">{side}</ol></details>\n'
                      f'<p class="dl"><a href="{T["dl_spec"]}">{T["l1"]}</a><a href="{T["dl_src"]}">{T["l2"]}</a></p></aside>\n'
                      f'<article class="prose"><h1>{T["h1"]}</h1>{content}</article>')
    return SPEC[lang]

def spec_part(lang, anchor):
    if 'data-placeholder="spec03"' in spec_html(lang):
        return ('<p class="muted" data-placeholder="spec03">' + ("Testo normativo non incluso in questo repository." if lang == "it"
                else "Normative text not included in this repository.") + '</p>')
    a = re.search(r'<article class="prose">(.*)</article>', spec_html(lang), re.S).group(1)
    m = re.search(rf'<(h[23]) id="{re.escape(anchor)}">', a)
    if not m: raise SystemExit(f"ancora mancante {lang} {anchor}")
    lvl = m.group(1); start = m.start()
    stop_pat = r'<h2 ' if lvl == "h2" else r'<h[23] '
    n = re.compile(stop_pat).search(a, m.end())
    chunk = a[start: n.start() if n else len(a)]
    chunk = re.sub(r' id="[^"]*"', '', chunk)
    chunk = chunk.replace("<h3", "<h4").replace("</h3>", "</h4>").replace("<h2", "<h3").replace("</h2>", "</h3>")
    return chunk

# ---------- grafiche delle pagine componente ----------
def g_flow(items, tones=None):
    out = []
    for i, (ic, t) in enumerate(items):
        if i: out.append(f'<span class="fl-ar" aria-hidden="true">{icon("arrow")}</span>')
        out.append(f'<div class="fl {tones[i] if tones else "ai"}"><span class="ic">{icon(ic,"lg")}</span><b>{esc(t)}</b></div>')
    return f'<div class="flow">{"".join(out)}</div>'

def graphic(key, lang):
    t = COMP[key][lang]
    if key == "fasi":
        items = "".join(f'<div class="ph"><span class="ic">{icon(ic,"lg")}</span><b>{esc(n)}</b><span class="you">{icon("manager")}<span><em>{esc(t["you"])}</em> {esc(y)}</span></span></div>' for ic, n, y in t["phases"])
        return f'<div class="phases">{items}</div>'
    if key == "decisioni":
        trio = "".join(f'<div class="tile {tone}"><div class="ic">{icon(ic,"lg")}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for ic, tone, h, p in t["trio"])
        return f'<div class="tiles trio">{trio}</div><p class="silence">{icon("silence","lg")}<span>{esc(t["silence"])}</span></p>'
    if key == "qualita":
        return g_flow(t["flow"], ["fw", "ai", "ai", "ai", "ai"])
    if key == "profili":
        return g_flow(t["flow"], ["fw", "ai", "human", "ai"])
    if key == "ritmo":
        waves = "".join('<i></i>' for _ in range(14))
        return (f'<div class="lanes"><div class="lane po"><span class="lab">{icon("manager")}{esc(t["lane_po"])}</span><div class="track">'
                + "".join(f'<span class="rev">{esc(t["review"])}</span>' for _ in range(3)) +
                f'</div></div><div class="lane ai"><span class="lab">{icon("team")}{esc(t["lane_ai"])}</span><div class="track waves">{waves}</div></div></div>')
    if key == "livelli" and "LEVELS" in globals():
        return levels_graphic(lang)
    if key == "livelli":
        h = HOME[lang]
        stairs = "".join(f'<div class="stair"><div class="lv">{lv}</div>{icon(ic, "lg")}<h3>{esc(tt)}</h3><p>{esc(p)}</p></div>' for ic, lv, tt, p in h["stairs"])
        oic, ot, op = h["out"]
        return f'<div class="stairs">{stairs}<div class="stair out">{icon(oic,"lg")}<h3>{esc(ot)}</h3><p>{esc(op)}</p></div><div class="ground"></div></div>'
    if key == "documenti":
        rows = "".join(f'<div class="pyr-row {tone}" style="--w:{60+i*20}%"><b>{esc(n)}</b><span>{esc(d)}</span></div>' for i, (n, d, tone) in enumerate(t["pyr"]))
        return f'<div class="pyr-wrap"><div class="pyr">{rows}</div><div class="third">{icon("stamp","lg")}<b>{esc(t["third"])}</b></div></div>'
    if key == "squadre":
        rows = "".join(f'<div class="pyr-row {tone}" style="--w:{56+i*22}%"><b>{esc(n)}</b><span>{esc(d)}</span></div>' for i, (n, d, tone) in enumerate(t["pyr"]))
        return f'<div class="pyr-wrap"><div class="pyr">{rows}</div><div class="third">{icon("coin","lg")}<b>{esc(t["pyr_note"])}</b></div></div>' + g_flow(t["flow"], ["fw", "ai", "ai", "ai", "human"])
    if key == "architettura":
        parts = "".join(f'<div class="bp"><span class="n">{i+1}</span><span class="ic">{icon(ic,"xl")}</span><b>{esc(n)}</b><span>{esc(d)}</span></div>' for i, (ic, n, d) in enumerate(t["body"]))
        return f'<div class="bodyparts">{parts}</div>'
    if key == "scoperta":
        return g_flow(t["flow"], ["ai", "human", "ai", "human"])
    if key == "sicurezza":
        ins = "".join(f"<li>{icon('lock')}{esc(x)}</li>" for x in t["inside_items"])
        outs = "".join(f"<li>{icon('outside')}{esc(x)}</li>" for x in t["outside_items"])
        return f'<div class="zones"><div class="zone-in"><h3>{icon("shield","lg")}{esc(t["inside"])}</h3><ul>{ins}</ul></div><div class="zone-out"><h3>{icon("globe","lg")}{esc(t["outside"])}</h3><ul>{outs}</ul></div></div>'
    return ""

def levels_graphic(lang):
    L = LEVELS[lang]
    r0, r1, r2 = L["rings"]
    rings = (f'<figure class="lv-rings"><svg viewBox="0 0 420 300" role="img" aria-label="{esc(L["rings_label"])}">'
             '<rect x="6" y="6" width="408" height="288" rx="18" class="lv-out-bg"/>'
             '<circle cx="210" cy="160" r="128" class="lv-c2"/><circle cx="210" cy="160" r="86" class="lv-c1"/><circle cx="210" cy="160" r="44" class="lv-c0"/>'
             f'<text x="210" y="164" text-anchor="middle" class="lv-t0">0 · {esc(r0)}</text>'
             f'<text x="210" y="98" text-anchor="middle" class="lv-t">1 · {esc(r1)}</text>'
             f'<text x="210" y="52" text-anchor="middle" class="lv-t">2 · {esc(r2)}</text>'
             f'<text x="30" y="34" class="lv-tout">✕ {esc(L["ring_out"])}</text></svg></figure>')
    cards = ""
    for x in L["levels"]:
        ex = "".join(f"<li>{esc(e)}</li>" for e in x["ex"]); need = "".join(f"<li>{icon('check')}<span>{esc(e)}</span></li>" for e in x["need"])
        cards += (f'<article class="lv-card lv{x["n"]}"><header><span class="lv-n">{x["n"]}</span>{icon(x["ic"],"lg")}<h3>{esc(x["h"])}</h3></header>'
                  f'<p class="lv-who"><b>{esc(L["who_lbl"])}:</b> {esc(x["who"])}</p>'
                  f'<p class="lv-lbl">{esc(L["ex_lbl"])}</p><ul class="lv-ex">{ex}</ul>'
                  f'<p class="lv-lbl">{esc(L["need_lbl"])}</p><ul class="lv-need">{need}</ul></article>')
    o = L["out"]
    outs = "".join(f"<li>{icon('outside')}<span>{esc(e)}</span></li>" for e in o["items"])
    out = f'<article class="lv-outcard"><header>{icon("alert","lg")}<h3>{esc(o["h"])}</h3></header><p>{esc(o["p"])}</p><ul>{outs}</ul></article>'
    up = "".join(f'<li><span class="st">{i+1}</span>{icon(ic,"lg")}<b>{esc(h)}</b><span>{esc(p)}</span></li>' for i, (ic, h, p) in enumerate(L["up"]))
    story = "".join(f'<li class="lv{n}"><span class="lv-n">{n}</span><b>{esc(h)}</b><span>{esc(p)}</span></li>' for n, h, p in L["story"])
    return (f'<div class="lv-top">{rings}<div class="lv-cards">{cards}</div></div>{out}'
            f'<h3 class="sub lv-h">{icon("steps","lg")}{esc(L["up_h"])}</h3><ol class="lv-up">{up}</ol>'
            f'<p class="lv-down">{icon("alert")}<span>{esc(L["down"])}</span></p>'
            f'<aside class="lv-story"><h3>{icon("bulb","lg")}{esc(L["ex_h"])}</h3><ol>{story}</ol></aside>')

def build_comp(lang, key):
    c = COMP[key]; t = c[lang]; u = UI[lang]; i = ORDER.index(key)
    tiles = ""
    if t.get("tiles") and key not in ("decisioni",):
        tiles = '<div class="tiles">' + "".join(f'<div class="tile {tone}"><div class="ic">{icon(ic,"lg")}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for ic, tone, h, p in t["tiles"]) + '</div>'
    g = graphic(key, lang)
    if t.get("tests"):
        g_tests = f'<h3 class="sub">{esc(t["tests_h"])}</h3><div class="tiles">' + "".join(f'<div class="tile {tone}"><div class="ic">{icon(ic,"lg")}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for ic, tone, h, p in t["tests"]) + '</div>'
    else:
        g_tests = ""
    see = ""
    links = [f'<a href="{lnk(lang,k)}">{esc(COMP[k][lang]["card"])}</a>' for k in c.get("see", [])]
    if key in FW_SEE:
        links.append(f'<a href="{lnk(lang,"framework")}{"#" + FW_SEE[key] if FW_SEE[key] else ""}">{esc(FWPAGE[lang]["h1"])}</a>')
    if links:
        see = f'<p class="see">{icon("arrow")}<span>{u["see"]}:</span> ' + " · ".join(links) + '</p>'
    story = ""
    if t.get("story"):
        s = t["story"]
        story = (f'<figure class="story"><div class="ic">{icon("bulb","lg")}</div><div><figcaption>{esc(s["h"])}</figcaption>'
                 f'<p>{esc(s["p"])}</p><p class="src"><a href="https://en.wikisource.org/wiki/The_Pearl_of_Love" rel="noopener" target="_blank">{esc(s["src"])}</a></p></div></figure>')
    orig = ORIGINS[key][0 if lang == "it" else 1]
    rules = '<ul class="rules">' + "".join(f'<li><span class="id">{esc(rid)}</span><span>{esc(txt)}</span></li>' for rid, txt in t["rules"]) + '</ul>'
    anchors = c.get("norm_en", c["norm"]) if lang == "en" else c["norm"]
    norm = "".join(spec_part(lang, a) for a in anchors)
    secs = ", ".join("§" + str(n).replace("bis", " bis") for n in c["spec"])
    spec_link = lnk(lang, "specifica") + f"#s{c['spec'][0]}"
    prev_k = ORDER[i-1] if i > 0 else None; next_k = ORDER[i+1] if i < len(ORDER)-1 else None
    pager = '<nav class="pager" aria-label="pager">'
    pager += (f'<a class="prev" href="{lnk(lang,prev_k)}"><span>← {u["prev"]}</span><b>{esc(COMP[prev_k][lang]["card"])}</b></a>' if prev_k else f'<a class="prev" href="{lnk(lang,"metodo")}"><span>← {u["method"]}</span><b>{u["method"]}</b></a>')
    pager += (f'<a class="next" href="{lnk(lang,next_k)}"><span>{u["next"]} →</span><b>{esc(COMP[next_k][lang]["card"])}</b></a>' if next_k else f'<a class="next" href="{lnk(lang,"specifica")}"><span>{u["next"]} →</span><b>{"Specifica 0.3" if lang=="it" else "Specification 0.3"}</b></a>')
    pager += '</nav>'
    body = f"""
<section class="band"><div class="in">
<nav class="crumbs" aria-label="breadcrumb"><a href="{lnk(lang,'home')}">{u['home']}</a><span>/</span><a href="{lnk(lang,'metodo')}">{u['method']}</a><span>/</span><span>{esc(t['card'])}</span></nav>
<span class="part">{u['part'].format(n=i+1, t=len(ORDER))}</span>
<h1>{esc(t['h1'])}</h1>{(f'<p class="claim">{esc(t["claim"])}</p>' if t.get('claim') else '')}<p class="why">{esc(t['why'])}</p>
<p class="origin">{icon('bridge')}<span>{u['origin']}:</span> <b>{esc(orig)}</b></p></div></section>
<section class="sec"><div class="in block">
<h2>{icon('gear','lg')}{u['how']}</h2><p class="lede">{esc(t['how'])}</p>{(f'<p class="muted"><small>{esc(t["status"])}</small></p>' if t.get('status') else '')}
{g}{tiles}{g_tests}{story}{see}
</div></section>
<section class="sec alt"><div class="in block">
<h2>{icon('doc','lg')}{(LEVELS[lang]['details_h'] if key == 'livelli' and 'LEVELS' in globals() else u['what'])}</h2>
{rules}
<details class="norm"><summary>{icon('lens')}{u['norm']} · {secs}</summary><div class="prose">{norm}</div></details>
<p><a class="specref" href="{spec_link}">{icon('arrow')}{u['specref']} {secs}</a></p>
{pager}
</div></section>
"""
    return page(lang, key, f"{t['card']} · Eiraman", t["why"], body)


def build_orig(lang):
    o = ORIG[lang]; u = UI[lang]
    def srcs(keys):
        if not keys: return ""
        items = []
        for k in keys:
            it, en, url = SRC[k]
            items.append(f'<a href="{url}" rel="noopener">{esc(en if (lang == "en" and en) else it)}</a>')
        return f'<p class="src"><span>{esc(o["src_lbl"])}:</span> ' + " · ".join(items) + '</p>'
    bricks = "".join(f'<div class="tile fw"><div class="ic">{icon(ic,"lg")}</div><h3>{esc(h)}</h3><p>{esc(p)}</p>{srcs(ks)}</div>' for ic, h, p, ks in o["bricks"])
    own = "".join(f'<div class="own"><div class="ic">{icon(ic,"xl")}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for ic, h, p in o["own"])
    nots = "".join(f'<li>{icon("check")}<span>{esc(x)}</span></li>' for x in o["not_list"])
    body = f"""
<section class="band"><div class="in">
<nav class="crumbs" aria-label="breadcrumb"><a href="{lnk(lang,'home')}">{u['home']}</a><span>/</span><a href="{lnk(lang,'metodo')}">{u['method']}</a><span>/</span><span>{esc(o['card'])}</span></nav>
<h1>{esc(o['h1'])}</h1><p class="why">{icon('why','lg')} {esc(o['why'])}</p></div></section>
<section class="sec"><div class="in block">
<h2>{icon('layers','lg')}{esc(o['how_h'])}</h2><p class="lede">{esc(o['how_p'])}</p>
<div class="tiles">{bricks}</div></div></section>
<section class="sec alt"><div class="in block">
<h2>{icon('target','lg')}{esc(o['own_h'])}</h2><p class="lede">{esc(o['own_p'])}</p>
<div class="owns">{own}</div></div></section>
<section class="sec"><div class="in block">
<div class="duo"><article class="who"><header>{icon('alert','lg')}<h3>{esc(o['not_h'])}</h3></header><ul>{nots}</ul></article>
<article class="who ai"><header>{icon('stamp','lg')}<h3>{esc(o['proof_h'])}</h3></header><p>{esc(o['proof_p'])}</p><p><a class="btn primary" href="{lnk(lang,'progetti')}">{esc(o['proof_btn'])} {icon('arrow')}</a></p></article></div>
</div></section>
"""
    return page(lang, "originalita", o["title"], o["why"], body)

# ---------- chi sono ----------
PHOTO = os.environ.get("EIRAMAN_PHOTO") or ""  # author photo: excluded from the public repository
def cost_dash(lang):
    d = COSTDASH[lang]
    kp = "".join(f'<div class="cd-k"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a, b in d["kpis"])
    return (f'<figure class="cost-dash" role="img" aria-label="{esc(d["label"])}"><figcaption>{icon("coin","lg")}{esc(d["h"])}</figcaption>'
            f'<div class="cd-bar"><span class="cd-lbl">{esc(d["bar"])}</span><div class="cd-track"><i class="cd-fill" style="width:64%"></i>'
            f'<b class="cd-m m80" style="left:80%"><em>{esc(d["warn"])}</em></b><b class="cd-m m100" style="left:100%"><em>{esc(d["stop"])}</em></b></div>'
            f'<span class="cd-spent">{esc(d["spent"])}</span></div><div class="cd-kpis">{kp}</div></figure>')

def build_framework(lang):
    f = FWPAGE[lang]; u = UI[lang]; L = f["lab"]
    spec = lnk(lang, "specifica")
    idx = "".join(f'<a class="fx-idx" href="#{x["id"]}"><span class="ic">{icon(x["ic"],"lg")}</span><span><small>{esc(x["old"])}</small><b>{esc(x["new"])}</b></span></a>' for x in f["fws"])
    diff = "".join(f'<div class="tile ai"><div class="ic">{icon(ic,"lg")}</div><h3>{esc(h)}</h3><p>{esc(pp)}</p></div>' for ic, h, pp in f["diff"])
    secs = ""
    for n, x in enumerate(f["fws"]):
        chips_b = "".join(f'<li>{esc(c)}</li>' for c in x["before"])
        chips_a = "".join(f'<li>{esc(c)}</li>' for c in x["after"])
        src = (f'<p class="fx-src">{esc(L["src"])}: ' + " · ".join(f'<a href="{esc(url)}" rel="noopener" target="_blank">{esc(lab)}</a>' for lab, url in x["src"]) + '</p>') if x["src"] else ""
        keep = "".join(f'<li>{esc(k)}</li>' for k in x["keep"])
        change = "".join(f'<li>{esc(k)}</li>' for k in x["change"])
        rules = "".join(f'<li><span>{esc(r)}</span><span class="fx-links"><a href="{lnk(lang,k)}">{esc(f["more"])}</a> · <a href="{spec}#{s}">{esc(L["spec"])} §{s[1:].replace("bis"," bis")}</a></span></li>' for r, k, s in x["rules"])
        secs += f"""
<section class="sec fx{' alt' if n % 2 else ''}" id="{x['id']}"><div class="in">
<header class="fx-head"><span class="fx-n">{n+1:02d}</span><span class="ic">{icon(x['ic'],'xl')}</span><div><p class="fx-old">{esc(x['old'])}</p><h2>{esc(x['new'])}</h2>{f'<p class="fx-sub">{esc(x["sub"])}</p>' if x.get("sub") else ""}</div></header>
{f'<p class="fx-bezos">{icon("door2")}{icon("door1")}<span>{esc(x["bezos"])}</span></p>' if x.get("bezos") else ""}
<figure class="fx-schema" aria-label="{esc(L['before'])} → {esc(L['after'])}"><div class="fx-b"><p>{esc(L['before'])}</p><ul>{chips_b}</ul></div>
<div class="fx-ar" aria-hidden="true">{icon('arrow','lg')}</div><div class="fx-a"><p>{esc(L['after'])}</p><ul>{chips_a}</ul></div></figure>
<div class="fx-grid">
<div class="fx-box"><h3>{icon('lens')} {esc(L['orig'])}</h3><p>{esc(x['orig'])}</p>{src}</div>
<div class="fx-box"><h3>{icon('check')} {esc(L['keep'])}</h3><ul>{keep}</ul></div>
<div class="fx-box wide"><h3>{icon('cycle')} {esc(L['change'])}</h3><ul>{change}</ul></div>
</div>
{cost_dash(lang) if x['id'] == 'reporting' and 'COSTDASH' in globals() else ''}
<p class="you">{icon('manager')}<b>{esc(L['you'])}:</b> {esc(x['you'])}</p>
<div class="fx-rules"><h3>{icon('doc')} {esc(L['rules'])}</h3><ul>{rules}</ul></div>
</div></section>"""
    body = f"""
<section class="band"><div class="in">
<nav class="crumbs" aria-label="breadcrumb"><a href="{lnk(lang,'home')}">{u['home']}</a><span>/</span><a href="{lnk(lang,'metodo')}">{u['method']}</a><span>/</span><span>{esc(f['crumb'])}</span></nav>
<p class="kicker">{'Perché' if lang=='it' else 'Why'}</p>
<h1>{esc(f['h1'])}</h1><p class="why">{esc(f['why'])}</p></div></section>
<section class="sec"><div class="in">
<div class="sec-head"><span class="tag">{'Come' if lang=='it' else 'How'}</span><h2>{esc(f['idx_h'])}</h2><p>{esc(f['idx_p'])}</p></div>
<nav class="fx-idxs" aria-label="{esc(f['idx_h'])}">{idx}</nav>
<div class="sec-head" style="margin-top:40px"><h2>{esc(f['diff_h'])}</h2></div>
<div class="tiles">{diff}</div></div></section>
{secs}
<section class="sec"><div class="in"><p class="tm">{esc(f['tm'])}</p>
<div class="cta"><a class="btn primary" href="{lnk(lang,'metodo')}">{esc(HOME4[lang]['invite_btn'])} {icon('arrow')}</a></div></div></section>
"""
    return page(lang, "framework", f["title"], f["desc"], body)

def build_about(lang):
    a = ABOUT[lang]; u = UI[lang]; pre = up(lang); L = COMMUNITY_LINKS
    tiles = lambda rows, cls: "".join(f'<div class="tile {cls}"><div class="ic">{icon(ic,"lg")}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for ic, h, p in rows)
    ext = lambda href, label: f'<a href="{esc(href)}" rel="noopener">{esc(label)} {icon("arrow")}</a>'
    path, edu = tiles(a["path"], "fw"), tiles(a["edu"], "ai")
    repos = "".join(f'<li><a href="{esc(COMMUNITY_REPO + r)}" rel="noopener"><code>eiraman/{esc(r)}</code></a> · {esc(d)}</li>' for r, d in COMMUNITY_REPOS)
    lic = "".join(f"<li>{esc(x)}</li>" for x in a["lic"])
    body = f"""
<section class="band"><div class="in">
<nav class="crumbs" aria-label="breadcrumb"><a href="{lnk(lang,'home')}">{u['home']}</a><span>/</span><span>{esc(a['crumb'])}</span></nav>
<h1>{esc(a['crumb'])}</h1>
<div class="about-hero">{f'<img class="portrait" src="{pre}assets/paolo-ungari.jpg" width="640" height="640" alt="{esc(a["alt"])}">' if os.path.isfile(PHOTO) else '<div class="portrait" data-placeholder="photo" aria-hidden="true"></div>'}
<div><p class="why-h">{icon('person')} {esc(a['author_h'])}</p><h2 class="name">{esc(a['name'])}</h2><p class="role">{esc(a['role'])}</p>
<p class="why-h">{icon('why')} {esc(a['why_h'])}</p><p class="why">{esc(a['why'])}</p>
<p><a class="btn ghost" href="https://www.linkedin.com/in/paolo-ungari-57a1b27/" rel="me noopener" target="_blank">{esc(a['li'])} {icon('arrow')}</a></p></div></div>
</div></section>
<section class="sec"><div class="in block">
<h2>{icon('steps','lg')}{esc(a['path_h'])}</h2>
<div class="tiles">{path}</div></div></section>
<section class="sec alt"><div class="in block">
<h2>{icon('bulb','lg')}{esc(a['edu_h'])}</h2>
<div class="tiles">{edu}</div></div></section>
<section class="sec" id="comunita"><div class="in block">
<h2>{icon('group','lg')}{esc(a['com_h'])}</h2><p>{esc(a['com_p'])}</p>
<h3>{esc(a['gov_h'])}</h3><p>{esc(a['gov_p'])}</p>
<div class="tiles">{tiles(a["gov"], "fw")}</div>
<p class="teaser">{ext(L["gov"], a["gov_link"])}</p></div></section>
<section class="sec alt"><div class="in block">
<h2>{icon('team','lg')}{esc(a['wg_h'])}</h2>
<div class="tiles">{tiles(a["wg"], "ai")}</div>
<p class="teaser">{ext(L["wg"], a["wg_link"])}</p></div></section>
<section class="sec"><div class="in block">
<h2>{icon('pen','lg')}{esc(a['ct_h'])}</h2>
<div class="tiles">{tiles(a["ct"], "fw")}</div>
<p class="teaser">{ext(L["path"], a["path_link"])} · {ext(L["ct"], a["ct_link"])}</p></div></section>
<section class="sec alt"><div class="in block narrow">
<h2>{icon('hand','lg')}{esc(a['coc_h'])}</h2><p>{esc(a['coc_p'])}</p>
<p class="teaser">{ext(L["coc"], a["coc_link"])}</p></div></section>
<section class="sec" id="licenze"><div class="in block narrow">
<h2>{icon('scale','lg')}{esc(a['lic_h'])}</h2><ul>{lic}</ul><p class="muted">{esc(a['lic_note'])}</p>
<p class="teaser">{ext(L["lic"], a["lic_link"])} · {ext(L["tm"], a["tm_link"])}</p>
<h3>{esc(a['repos_h'])} <small class="muted">({esc(a['repos_note'])})</small></h3><ul>{repos}</ul>
<p class="teaser"><a href="{lnk(lang,'metodo')}">{esc(a['back'])} {icon('arrow')}</a></p></div></section>
"""
    return page(lang, "chi", a["title"], a["desc"], body)

# ---------- riferimento tecnico ----------
def build_spec(lang):
    inner = spec_html(lang)
    inner = inner.replace('<summary>Indice</summary>', '<summary>Indice</summary>').replace("metodo.html", "specifica.html")
    title = "Specifica 0.3 · Eiraman" if lang == "it" else "Specification 0.3 · Eiraman"
    desc = "Testo normativo completo del metodo Eiraman 0.3." if lang == "it" else "Full normative text of the Eiraman method 0.3."
    crumbs = (f'<nav class="crumbs" aria-label="breadcrumb"><a href="{lnk(lang,"home")}">{UI[lang]["home"]}</a><span>/</span><a href="{lnk(lang,"metodo")}">{UI[lang]["method"]}</a><span>/</span><span>{"Specifica" if lang=="it" else "Specification"}</span></nav>')
    head = f'<section class="band"><div class="in">{crumbs}<h1>{"Specifica 0.3" if lang=="it" else "Specification 0.3"}</h1><p class="why">{"Il testo normativo completo, per chi vuole ogni dettaglio." if lang=="it" else "The full normative text, for those who want every detail."}</p></div></section>'
    body = head + f'<div class="doc in">{inner}</div>'
    return page(lang, "specifica", title, desc, body)


import re as _rr
_RUOLI = [('\\bIl PO\\b', 'Il Manager umano'), ('\\bil PO\\b', 'il Manager umano'), ('\\bdel PO\\b', 'del Manager umano'), ('\\bal PO\\b', 'al Manager umano'), ('\\bAl PO\\b', 'Al Manager umano'), ('\\bdal PO\\b', 'dal Manager umano'), ('\\bThe PO\\b', 'The Human Manager'), ('\\bthe PO\\b', 'the Human Manager'), ('\\bPO\\b', 'Manager umano'), ('\\bIl Controllore\\b', 'Il Coordinatore AI'), ('\\bil Controllore\\b', 'il Coordinatore AI'), ('\\bdal Controllore\\b', 'dal Coordinatore AI'), ('\\bal Controllore\\b', 'al Coordinatore AI'), ('\\bdel Controllore\\b', 'del Coordinatore AI'), ('\\bControllore\\b', 'Coordinatore AI'), ('\\bThe Controller\\b', 'The AI Coordinator'), ('\\bthe Controller\\b', 'the AI Coordinator'), ('\\bController\\b', 'AI Coordinator'), ('Coordinatore AI AI', 'Coordinatore AI'), ('AI AI Coordinator', 'AI Coordinator')]
def _ruoli(t):
    for a, b in _RUOLI: t = _rr.sub(a, b, t)
    return t

def build_map(lang):
    f = os.path.join(OLD, "diagramma.html" if lang == "it" else "en/diagram.html")
    if not os.path.isfile(f):
        _missing("release-0.2")
        title = "Mappa funzionale · Eiraman" if lang == "it" else "Functional map · Eiraman"
        msg = "La mappa funzionale non è ancora inclusa in questo repository." if lang == "it" else "The functional map is not yet included in this repository."
        return page(lang, "mappa", title, title, f'<section class="sec" data-placeholder="release-0.2"><div class="in"><h1>{esc(title)}</h1><p>{esc(msg)}</p></div></section>')
    t = open(f, encoding="utf-8").read()
    t = _ruoli(t)
    style = re.search(r"<style>(.*?)</style>", t, re.S).group(1)
    style = style[style.index(".wrap{"):]  # rimuove i token della 0.2: valgono quelli del sito
    main = re.search(r'<main id="main">(.*)</main>', t, re.S).group(1)
    main = main.replace('href="metodo.html"', 'href="specifica.html"').replace('href="method.html"', 'href="specification.html"')
    main = main.replace('class="dg page-wide"', 'class="dg page-wide in" style="padding-block:36px"')
    for a, b in (("un utente senza specialisti può sostenere", "un utente di business può sostenere, quando la competenza sta nei profili e non in ogni progetto"),
                 ("Fin dove si può arrivare senza specialisti", "Che cosa puoi costruire, e per chi"),
                 ("a user without specialists can bear", "a business user can bear, when competence lives in the profiles and not in every project"),
                 ("How far you can go without specialists", "What you can build, and for whom")):
        main = main.replace(a, b)
    title = "Mappa funzionale · Eiraman" if lang == "it" else "Functional map · Eiraman"
    desc = "Cinque schemi tecnici del metodo Eiraman." if lang == "it" else "Five technical diagrams of the Eiraman method."
    return page(lang, "mappa", title, desc, main, extra_head=f"<style>{style}</style>\n")

def build_pilot(lang):
    f = os.path.join(OLD, "pilota.html" if lang == "it" else "en/pilot.html")
    t = open(f, encoding="utf-8").read()
    main = re.search(r'<main id="main">(.*)</main>', t, re.S).group(1)
    main = main.replace('class="in narrow prose"', 'class="in narrow prose" style="padding-block:40px"')
    main = main.replace("perché una tabella richiesta era incompleta. È l'esempio citato nella specifica: un documento", "perché non superava i controlli richiesti. È il caso descritto nella specifica: un documento")
    main = main.replace("because a required table was incomplete. It is the example cited in the specification: a rejected", "because it did not pass the required checks. It is the case described in the specification: a rejected")
    title = "I dati · Eiraman" if lang == "it" else "Data · Eiraman"
    desc = "Il pilota del metodo Eiraman: che cosa si misura e come." if lang == "it" else "The Eiraman method pilot: what is measured and how."
    return page(lang, "pilota", title, desc, main)

# ---------- come usarlo ----------
def uso_tree(lang):
    it = lang == "it"
    wps = [("W1", "WP-1", "Design Thinking" if it else "Design Thinking", "done", None, "12 €"),
           ("W1", "WP-2", "Architettura e piano" if it else "Architecture and plan", "done", None, "8 €"),
           ("W2", "WP-3", "Modulo di richiesta" if it else "Request form", "prog", 70, "25 €"),
           ("W2", "WP-4", "Notifiche" if it else "Notifications", "prog", 40, "18 €"),
           ("W2", "WP-5", "Collaudo" if it else "User acceptance", "todo", None, "6 €")]
    H = 330; ys = [45 + i * 60 for i in range(5)]; wy = {"W1": (ys[0] + ys[1]) / 2, "W2": (ys[2] + ys[4]) / 2}
    xr, xw, xp = 90, 290, 600
    g = [f'<svg class="uso-tree" viewBox="0 0 900 {H}" role="img" aria-label="{esc(USO[lang]["tree_label"])}">']
    for w in ("W1", "W2"):
        g.append(f'<path class="br" d="M{xr+80} {H/2:.0f} C{xr+150} {H/2:.0f} {xw-110} {wy[w]:.0f} {xw-55} {wy[w]:.0f}"/>')
    import math
    for (w, i, tt, st, pc, c), y in zip(wps, ys):
        g.append(f'<path class="br" d="M{xw+55} {wy[w]:.0f} C{xw+150} {wy[w]:.0f} {xp-130} {y} {xp-20} {y}"/>')
        g.append(f'<text class="cost" x="{xp-28}" y="{y-7}" text-anchor="end">{"Stima" if it else "Estimate"}: {c}</text>')
    g.append(f'<rect class="nroot" x="{xr-80}" y="{H/2-20:.0f}" width="160" height="40" rx="8"/><text class="tr" x="{xr}" y="{H/2+5:.0f}" text-anchor="middle">{"Progetto" if it else "Project"}</text>')
    for w in ("W1", "W2"):
        g.append(f'<rect class="nwave" x="{xw-55}" y="{wy[w]-17:.0f}" width="110" height="34" rx="17"/><text class="tl" x="{xw}" y="{wy[w]+5:.0f}" text-anchor="middle">Wave {w[1]}</text>')
    for (w, i, tt, st, pc, c), y in zip(wps, ys):
        if st == "done":
            n = f'<circle class="n-done" cx="{xp}" cy="{y}" r="17"/><path class="tick" d="M{xp-7} {y} l5 5 l10 -11"/>'
        elif st == "prog":
            a = 2 * math.pi * pc / 100; x2 = xp + 17 * math.sin(a); y2 = y - 17 * math.cos(a)
            n = (f'<circle class="n-prog" cx="{xp}" cy="{y}" r="17"/><path class="n-arc" d="M{xp} {y-17} A17 17 0 {1 if pc > 50 else 0} 1 {x2:.1f} {y2:.1f}"/>'
                 f'<text class="pct" x="{xp}" y="{y+4}" text-anchor="middle">{pc}%</text>')
        else:
            n = f'<circle class="n-todo" cx="{xp}" cy="{y}" r="17"/>'
        g.append(n + f'<text class="wid" x="{xp+28}" y="{y-3}">{i}</text><text class="wt" x="{xp+28}" y="{y+15}">{esc(tt)}</text>')
    g.append("</svg>")
    return "".join(g)

def _gscreen(s, lang):
    sc = s["screen"]
    if sc == "folder":
        rows = "".join(f'<li style="--i:{i}"><span class="fi">{"▸" if f.endswith("/") else "·"}</span>{esc(f)}</li>' for i, f in enumerate(s["files"]))
        inner = f'<ul class="g-files">{rows}</ul>'
    elif sc == "terminal":
        inner = "".join(f'<div class="g-ln" style="--i:{i}">{esc(l)}</div>' for i, l in enumerate(s["lines"])) + '<span class="g-cur" aria-hidden="true"></span>'
    elif sc == "chat":
        inner = "".join(f'<div class="g-bub {w}" style="--i:{i}">{esc(x)}</div>' for i, (w, x) in enumerate(s["bubbles"]))
    else:
        it = lang == "it"
        inner = (f'<div class="g-v bad" style="--i:0">{"Prima le cattive notizie" if it else "Bad news first"}</div>'
                 f'<div class="g-v do" style="--i:1">Do-03 · {"scade tra 2 giorni" if it else "due in 2 days"}</div>'
                 f'<div class="g-v" style="--i:2"><span class="g-bar"><i></i></span><small>{"Budget: 64% del tetto" if it else "Budget: 64% of the cap"}</small></div>'
                 f'<div class="g-v tree" style="--i:3"><b class="nd ok"></b><b class="nd ok"></b><b class="nd pr"></b><b class="nd td"></b></div>')
    return (f'<figure class="g-win" aria-hidden="true"><figcaption><i></i><i></i><i></i><span>{esc(s["wtitle"])}</span></figcaption>'
            f'<div class="g-body g-{sc}">{inner}</div></figure>')

def _guide(lang):
    g = GUIDE[lang]
    kit = KIT_URL
    if not KIT_SHA: raise RuntimeError("KIT_SHA non calcolato: build_kit() deve precedere le pagine")
    avvio = (AVVIO_IT if lang == "it" else AVVIO_EN).replace("{zip}", kit_zip(kit)).replace("{sha}", KIT_SHA)
    panes = []
    for n, s in enumerate(g["steps"], 1):
        lis = []
        for txt, code in s["items"]:
            extra = c = ""
            if code == "LINKS":
                extra = f' <a href="{CC_URL}" rel="noopener">Claude Code</a> · <a href="{CODEX_URL}" rel="noopener">Codex</a> · <a href="{PY_URL}" rel="noopener">Python</a>'
                code = None
            elif code == "REQ":
                code = REQ_TEMPLATE[lang]
            elif code == "AVVIO":
                code = avvio
                extra = f' <a href="{KIT_ZIP}">{esc(g["dl"])}</a>'
            if code:
                c = f'<div class="g-code"><pre><code>{esc(code)}</code></pre><button type="button" class="g-copy" data-ok="{esc(g["copied"])}">{esc(g["copy"])}</button></div>'
            lis.append(f"<li>{esc(txt)}{extra}{c}</li>")
        need = (f'<p class="g-need"><b>{esc(g["need_h"])}:</b> ' + "; ".join(esc(x) for x in g["need"]) + ".</p>") if n == 1 else ""
        panes.append(f'<section class="gpane" id="guida-{n}" data-g="{n}" aria-labelledby="gt-{n}">'
                     f'<div class="g-text"><h3 id="gt-{n}"><span class="n">{n:02d}</span> {esc(s["t"])}</h3>{need}<ol>{"".join(lis)}</ol></div>'
                     f'{_gscreen(s, lang)}</section>')
    js = """<script>(function(){var w=document.querySelector('.gwrap');if(!w)return;var box=w.querySelector('.guide'),tiles=w.querySelectorAll('.gstep'),
panes=w.querySelectorAll('.gpane'),pin=false,t=null,hov=window.matchMedia&&matchMedia('(hover:hover) and (pointer:fine)').matches;
function open(n){clearTimeout(t);box.classList.add('open');box.removeAttribute('hidden');tiles.forEach(function(x){var on=x.dataset.g==n;x.setAttribute('aria-expanded',on);x.classList.toggle('on',on)});
panes.forEach(function(p){var on=p.dataset.g==n;if(on&&!p.classList.contains('cur')){p.classList.remove('play');void p.offsetWidth;p.classList.add('play')}p.classList.toggle('cur',on)})}
function close(){pin=false;box.classList.remove('open');tiles.forEach(function(x){x.setAttribute('aria-expanded','false');x.classList.remove('on')});panes.forEach(function(p){p.classList.remove('cur','play')})}
tiles.forEach(function(x){if(hov)x.addEventListener('mouseenter',function(){if(!pin)open(x.dataset.g)});
x.addEventListener('click',function(){if(pin&&x.classList.contains('on')){close();return}pin=true;open(x.dataset.g)});
x.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();x.click()}})});
if(hov){w.addEventListener('mouseleave',function(){if(!pin)t=setTimeout(close,500)});w.addEventListener('mouseenter',function(){clearTimeout(t)})}
w.querySelector('.g-close').addEventListener('click',close);document.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
w.querySelectorAll('.g-copy').forEach(function(b){b.addEventListener('click',function(){var c=b.previousElementSibling.innerText,l=b.textContent;
(navigator.clipboard?navigator.clipboard.writeText(c):Promise.reject()).then(function(){b.textContent=b.dataset.ok;setTimeout(function(){b.textContent=l},1500)},function(){})})})})();</script>"""
    return (f'<div class="guide" id="guida" hidden><button type="button" class="g-close" aria-label="{esc(g["close"])}">×</button>{"".join(panes)}</div>', js)

def build_uso(lang):
    a = USO[lang]; u = UI[lang]
    guide_html, guide_js = _guide(lang)
    steps = "".join(f'<div class="tile human gstep" role="button" tabindex="0" aria-expanded="false" aria-controls="guida" data-g="{n+1}"><div class="ic">{icon(ic,"lg")}</div><span class="n">{n+1:02d}</span><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for n, (ic, h, p) in enumerate(a["steps"]))
    what = "".join(f'<div class="tile ai"><div class="ic">{icon(ic,"lg")}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for ic, h, p in a["what"])
    own = "".join(f"<p>{esc(x)}</p>" for x in a["own"])
    body = f"""
<section class="band"><div class="in">
<nav class="crumbs" aria-label="breadcrumb"><a href="{lnk(lang,'home')}">{u['home']}</a><span>/</span><span>{esc(a['crumb'])}</span></nav>
<h1>{esc(a['h1'])}</h1><p class="why">{esc(a['why'])}</p>
</div></section>
<section class="sec"><div class="in block">
<h2>{icon('steps','lg')}{esc(a['how_h'])}</h2>
<p class="g-hint">{esc(GUIDE[lang]['hint'])}</p>
<div class="gwrap"><div class="tiles t5">{steps}</div>{guide_html}</div></div></section>
<section class="sec alt"><div class="in block">
<h2>{icon('eye','lg')}{esc(a['what_h'])}</h2>
<div class="tiles">{what}</div></div></section>
<section class="sec"><div class="in block">
<h2>{icon('layers','lg')}{esc(a['tree_h'])}</h2>
<div class="uso-box">{uso_tree(lang)}</div></div></section>
<section class="sec alt"><div class="in block narrow prose">
<h2>{icon('pen','lg')}{esc(a['own_h'])}</h2>{own}
<p class="muted"><small>{esc(a['state'])}</small></p>
<p class="teaser"><a href="{lnk(lang,'metodo')}">{esc(a['back'])} {icon('arrow')}</a></p></div></section>
"""
    return page(lang, "uso", a["title"], a["desc"], body + guide_js, extra_head="<script>document.documentElement.classList.add('js')</script>\n")

# ---------- Role Profile ----------
RP_DIR = os.path.abspath(os.environ.get("EIRAMAN_PROFILES") or os.path.join(ROOT, "..", "role-profiles"))
def _rp_load():
    fams = {}
    for fid, *_ in RP_FAM:
        d = os.path.join(RP_DIR, fid); items = []
        if os.path.isdir(d):
            for sub in sorted(os.listdir(d)):
                j = os.path.join(d, sub, "profilo.json")
                if os.path.isfile(j):
                    try: items.append(json.load(open(j, encoding="utf-8")))
                    except Exception: pass
        fams[fid] = items
    return fams

def build_rp(lang):
    a = RPAGE[lang]; u = UI[lang]; it = lang == "it"
    fams = _rp_load()
    how = "".join(f'<div class="tile fw"><div class="ic">{icon(ic,"lg")}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for ic, h, p in a["how"])
    total = sum(len(v) for v in fams.values()) + 1
    lead = f'<article class="rp-fam rp-lead"><header><span class="ic">{icon("manager","lg")}</span><div><h3>{esc(a["ctrl"])}</h3><p>{esc(a["ctrl_d"])}</p></div></header></article>'
    tiles, panes, n = [], [], 1
    tiles.append(f'<div class="tile human gstep rp-tile" role="button" tabindex="0" aria-expanded="false" aria-controls="guida" data-g="1">'
                 f'<div class="ic">{icon("manager","lg")}</div><h3>{esc(a["ctrl"])}</h3><span class="n">1 {esc(a["n1"])}</span><p>{esc(a["ctrl_d"])}</p></div>')
    panes.append(f'<section class="gpane rp-pane" id="guida-1" data-g="1" aria-labelledby="gt-1"><h3 id="gt-1">{esc(a["ctrl"])}</h3>'
                 f'<div class="rp-cards"><article class="rp-card"><h4>{esc(a["ctrl"])}</h4><p>{esc(a["ctrl_d"])}</p>'
                 f'<p class="rp-meta">{esc(a["pyr"]["alto"])} · Seniority SD4</p><p>{esc(a["ctrl_x"])}</p></article></div></section>')
    for fid, n_it, n_en, d_it, d_en, ic in RP_FAM:
        items = fams.get(fid) or []
        if not items: continue
        n += 1; fname = n_it if it else n_en; fdesc = d_it if it else d_en
        tiles.append(f'<div class="tile ai gstep rp-tile" role="button" tabindex="0" aria-expanded="false" aria-controls="guida" data-g="{n}">'
                     f'<div class="ic">{icon(ic,"lg")}</div><h3>{esc(fname)}</h3><span class="n">{len(items)} {esc(a["n1"] if len(items) == 1 else a["n"])}</span><p>{esc(fdesc)}</p></div>')
        cards = []
        for p in items:
            nome = p.get("nome_en") if not it and p.get("nome_en") else p.get("nome", "")
            desc = p.get("descrizione_breve_en") if not it and p.get("descrizione_breve_en") else p.get("descrizione_breve", "")
            s = p.get("seniority") or {}
            cat = p.get("catalogo") or []
            ex = "".join(f'<li><span class="sd">{esc(c["seniority"])}</span>{esc(c["task"])}</li>' for c in cat[:3]) if it else ""
            cards.append(f'<article class="rp-card"><h4>{esc(nome)}</h4><p>{esc(desc)}</p>'
                         f'<p class="rp-meta">{esc(a["pyr"].get(p.get("piramide"), p.get("piramide","")))} · Seniority {esc(s.get("minima","?"))}–{esc(s.get("massima","?"))} · {len(cat)} {esc(a["tasks"])}</p>'
                         + (f'<p class="lbl">{esc(a["ex"])}</p><ul class="rp-ex">{ex}</ul>' if ex else "") + '</article>')
        panes.append(f'<section class="gpane rp-pane" id="guida-{n}" data-g="{n}" aria-labelledby="gt-{n}">'
                     f'<h3 id="gt-{n}">{esc(fname)} <small>{len(items)} {esc(a["n1"] if len(items) == 1 else a["n"])}</small></h3><p class="muted">{esc(fdesc)}</p>'
                     f'<div class="rp-cards">{"".join(cards)}</div><p class="muted rp-full">{esc(a["full"])}</p></section>')
    guide_js = _guide(lang)[1]
    blocks_html = (f'<p class="g-hint">{esc(a["rp_hint"])}</p><div class="gwrap"><div class="tiles rp-tiles">{"".join(tiles)}</div>'
                   f'<div class="guide" id="guida" hidden><button type="button" class="g-close" aria-label="{esc(a["close"])}">×</button>{"".join(panes)}</div></div>')
    git = (f'<p><a class="btn ghost" href="{esc(KIT_URL)}" rel="noopener">{esc(a["git_link"])} {icon("arrow")}</a></p>' if KIT_URL else "")
    body = f"""
<section class="band"><div class="in">
<nav class="crumbs" aria-label="breadcrumb"><a href="{lnk(lang,'home')}">{u['home']}</a><span>/</span><span>{esc(a['crumb'])}</span></nav>
<h1>{esc(a['h1'])}</h1><p class="why">{esc(a['why'])}</p>
</div></section>
<section class="sec"><div class="in block">
<h2>{icon('layers','lg')}{esc(a['how_h'])}</h2>
<div class="tiles">{how}</div></div></section>
<section class="sec"><div class="in block narrow">
<h2>{icon('steps','lg')}{esc(a['sd_h'])}</h2><p>{esc(a['sd_p'])}</p>
<div class="tbl-wrap"><table class="sd-tab"><thead><tr>{"".join(f"<th>{esc(c)}</th>" for c in a['sd_cols'])}</tr></thead><tbody>{"".join(f"<tr><td><b>{esc(x)}</b></td><td>{esc(y)}</td><td>{esc(z)}</td></tr>" for x,y,z in a['sd_rows'])}</tbody></table></div>
</div></section>
<section class="sec alt"><div class="in block">
<h2>{icon('team','lg')}{esc(a['list_h'])} <small class="rp-count">{total} · {esc(a['state'])}</small></h2>
{blocks_html}
<p class="muted">{esc(a['own'])} {esc(a['git'])}</p>{git}
</div></section>
"""
    return page(lang, "profili-ruolo", a["title"], a["desc"], body + guide_js, extra_head="<script>document.documentElement.classList.add('js')</script>\n")

# ---------- pacchetto scaricabile del kit ----------
KIT_LICENSE = ("# Licences · Licenze\n\n"
    "Copyright 2026 Paolo Ungari and contributors.\n\n"
    "| Material | Licence | SPDX |\n|---|---|---|\n"
    "| The Eiraman Guide and its text (`framework/`) | Creative Commons Attribution-ShareAlike 4.0 International: https://creativecommons.org/licenses/by-sa/4.0/legalcode | `CC-BY-SA-4.0` |\n"
    "| Role Profiles, AI Coordinator profile texts (`role-profiles/`, `CONTROLLORE.md`, `STATO.md`, `AVVIO.md`) | Creative Commons Attribution 4.0 International: https://creativecommons.org/licenses/by/4.0/legalcode | `CC-BY-4.0` |\n"
    "| Code (`.py` files) | Apache License 2.0: https://www.apache.org/licenses/LICENSE-2.0 | `Apache-2.0` |\n"
    "| Eiraman name and logo | Not licensed: trademark, see https://github.com/eiraman/community/blob/main/TRADEMARK.md | `LicenseRef-Eiraman-Trademark` |\n\n"
    "The licence of each file is stated in its SPDX header where present; otherwise this table applies. "
    "Attribution: \"The Eiraman Guide by Paolo Ungari and contributors\"; see https://github.com/eiraman/community/blob/main/LICENSING.md.\n\n"
    "**Licence transition.** Copies distributed up to version 0.3.x under CC BY-NC-ND 4.0 (texts, specification, Role Profiles) "
    "or MIT (scripts) remain available to their holders under those original licences.\n\n"
    "---\n\n"
    "Testi della Guida: CC BY-SA 4.0. Role Profile e testi del profilo del Coordinatore AI: CC BY 4.0. Codice: Apache 2.0. "
    "Nome e logo Eiraman: marchio, non coperto da queste licenze (TRADEMARK.md). Le copie distribuite fino alla versione 0.3.x "
    "restano disponibili ai loro titolari con le licenze originali (CC BY-NC-ND 4.0 e MIT).\n")
KIT_SHA = None  # impronta SHA-256 dello zip del kit: calcolata in main() prima delle pagine che la citano
KIT_BUNDLED = None  # versions of the artifacts inside the kit, written to manifest.json (community/VERSIONING.md)

def _released_version(changelog):
    """Latest released version in a Keep a Changelog file, or None."""
    if not os.path.isfile(changelog): return None
    m = re.search(r"^## \[(\d+\.\d+\.\d+[^\]]*)\]", open(changelog, encoding="utf-8").read(), re.M)
    return m.group(1) if m else None

def kit_bundled(arcs, rp):
    """Versions of what the kit contains. None: not in the kit; "unknown": in the kit, version not recorded at the source."""
    ctrl = os.path.join(rp, "controllore", "CONTROLLORE.md")
    m = re.search(r"^Versione (\d+\.\d+\.\d+)", open(ctrl, encoding="utf-8").read(), re.M) if "CONTROLLORE.md" in arcs else None
    return {"guide": None,  # the kit does not ship the Eiraman Guide
            "specification": "0.3" if "framework/Eiraman.md" in arcs else None,  # historical Italian specification, withheld input
            "registry": (_released_version(os.path.join(rp, "CHANGELOG.md")) or "unknown") if any(a.startswith("role-profiles/") for a in arcs) else None,
            "ai_coordinator_profile": (m.group(1) if m else "unknown") if "CONTROLLORE.md" in arcs else None,
            "tools": None}  # the validator and the activation tool are not in the kit

def build_kit():
    import zipfile
    rp = RP_DIR
    files = []
    ctrl = os.path.join(rp, "controllore")  # AI Coordinator profile, draft
    for n in ("CONTROLLORE.md", "STATO.md", "AVVIO.md"):
        files.append((os.path.join(ctrl, n), n))
    files.append((os.path.join(ctrl, "tools", "vista_manager.py"), "tools/vista_manager.py"))
    files.append((os.path.join(SPEC03, "Eiraman.md"), "framework/Eiraman.md"))
    files.append((os.path.join(rp, "README.md"), "role-profiles/README.md"))
    withheld = [f for f in files if not os.path.isfile(f[0])]
    if withheld:
        _missing("kit:" + ",".join(a for _, a in withheld))
        files = [f for f in files if f not in withheld]
    for base, dirs, fs in os.walk(rp):
        rel = os.path.relpath(base, rp)
        top = rel.split(os.sep)[0]
        if top in (".", "Controllore", "controllore", "_strumenti") or top.startswith("."): continue
        dirs[:] = sorted(d for d in dirs if not d.startswith(".") and d != "__pycache__")
        for f in sorted(fs):
            if f.startswith(".") or not f.endswith((".md", ".json", ".py")): continue
            files.append((os.path.join(base, f), "role-profiles/" + os.path.join(rel, f).replace(os.sep, "/")))
    global KIT_BUNDLED
    KIT_BUNDLED = kit_bundled({a for _, a in files}, rp)
    files.append((None, "LEGGIMI.md"))
    files.append(("@LIC", "LICENSE.md"))
    out = os.path.join(OUT, "kit", "eiraman-kit.zip"); os.makedirs(os.path.dirname(out), exist_ok=True)
    readme = ("# Kit Eiraman\n\nCopyright 2026 Paolo Ungari e contributori.\n\n"
              "**Licenze.** Testi della Guida: CC BY-SA 4.0. Role Profile e testi del profilo del Coordinatore AI (file .md e .json): CC BY 4.0. "
              "Codice (file .py): Apache 2.0. Nome e logo Eiraman: marchio, regolato da TRADEMARK.md ed escluso dalle licenze CC e Apache. "
              "Dettagli e collegamenti ai testi legali in LICENSE.md. Le copie distribuite fino alla versione 0.3.x restano disponibili "
              "ai loro titolari con le licenze originali (CC BY-NC-ND 4.0 e MIT).\n\n"
              "I Role Profile e il profilo del Coordinatore AI sono **bozze non qualificate**: non vanno usati in produzione prima della qualificazione (specifica §9).\n\n"
              "**Verifica dello zip.** Se hai scaricato il kit come zip, prima di usarlo confronta l'impronta SHA-256 del file con quella pubblicata "
              "nel prompt di avvio su https://eiraman.tech/come-usarlo.html (in inglese: https://eiraman.tech/en/how-to-use.html). Per calcolarla: `shasum -a 256 eiraman-kit.zip` su macOS e Linux, `Get-FileHash eiraman-kit.zip -Algorithm SHA256` in PowerShell su Windows. Se non coincide, non usarlo.\n\n"
              "**Stato.** Nel kit attuale i divieti del mandato sono istruzioni seguite dal Coordinatore AI, non ancora un blocco tecnico dell'ambiente.\n\n"
              "Avvio: apri Claude Code o Codex in questa cartella e scrivi: «Leggi CONTROLLORE.md e framework/Eiraman.md. Da ora sei il Coordinatore AI "
              "Eiraman di questo progetto e io sono il Manager umano. Segui la procedura di avvio del profilo e apri la Vista del Manager.»\n")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for src, arc in sorted(files, key=lambda x: x[1]):
            zi = zipfile.ZipInfo(arc, date_time=(2026, 11, 25, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            data = (readme.encode() if src is None else KIT_LICENSE.encode() if src == "@LIC" else open(src, "rb").read())
            z.writestr(zi, data)
    return len(files), hashlib.sha256(open(out, "rb").read()).hexdigest()

# ---------- I progetti ----------
def redirect_page(lang, key):
    dest = lnk(lang, key)
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="robots" content="noindex">'
            f'<meta http-equiv="refresh" content="0; url={dest}"><link rel="canonical" href="{url_of(lang, key)}"><title>Eiraman</title></head>'
            f'<body><p><a href="{dest}">{"Questa pagina si è spostata" if lang == "it" else "This page has moved"}</a></p></body></html>')

def build_progetti(lang):
    a = PROGETTI[lang]; u = UI[lang]
    tiles, panes = [], []
    for n, pr in enumerate(a["items"], 1):
        tiles.append(f'<div class="tile ai gstep rp-tile" role="button" tabindex="0" aria-expanded="false" aria-controls="guida" data-g="{n}">'
                     f'<div class="ic">{icon(pr["icon"],"lg")}</div><h3>{esc(pr["name"])}</h3><span class="n">{esc(pr["state"])}</span><p>{esc(pr["short"])}</p></div>')
        nums = "".join(f'<div class="pj-num"><b>{esc(v)}</b><span>{esc(k)}</span>{f"<em>{esc(c)}</em>" if c else ""}</div>' for k, v, c in pr["numbers"])
        sec = "".join(f'<div class="pj-sec"><h4>{esc(h)}</h4>' + ("".join(f"<p>{esc(x)}</p>" for x in body) if isinstance(body, list) else f"<p>{esc(body)}</p>") + '</div>'
                      for h, body in pr["sections"])
        bad = "".join(f"<li>{esc(x)}</li>" for x in pr.get("bad", []))
        panes.append(f'<section class="gpane rp-pane" id="guida-{n}" data-g="{n}" aria-labelledby="gt-{n}">'
                     f'<h3 id="gt-{n}">{esc(pr["name"])}</h3><p class="pj-vision"><b>{esc(a["vision"])}</b> {esc(pr["vision"])}</p>'
                     f'<div class="pj-nums">{nums}</div>'
                     + (f'<div class="pj-bad"><h4>{esc(a["bad"])}</h4><ul>{bad}</ul></div>' if bad else "")
                     + f'<div class="pj-secs">{sec}</div><p class="muted rp-full">{esc(pr["source"])}</p></section>')
    guide_js = _guide(lang)[1]
    body = f"""
<section class="band"><div class="in">
<nav class="crumbs" aria-label="breadcrumb"><a href="{lnk(lang,'home')}">{u['home']}</a><span>/</span><span>{esc(a['crumb'])}</span></nav>
<h1>{esc(a['h1'])}</h1><p class="why">{esc(a['why'])}</p>
</div></section>
<section class="sec"><div class="in block">
<h2>{icon('target','lg')}{esc(a['list_h'])}</h2>
<p class="g-hint">{esc(a['hint'])}</p>
<div class="gwrap"><div class="tiles rp-tiles pj-tiles">{"".join(tiles)}</div>
<div class="guide" id="guida" hidden><button type="button" class="g-close" aria-label="{esc(a['close'])}">×</button>{"".join(panes)}</div></div>
</div></section>
<section class="sec alt"><div class="in block narrow prose">
<h2>{icon('lens','lg')}{esc(a['how_h'])}</h2>{"".join(f"<p>{esc(x)}</p>" for x in a['how'])}
</div></section>
"""
    return page(lang, "progetti", a["title"], a["desc"], body + guide_js, extra_head="<script>document.documentElement.classList.add('js')</script>\n")

# ---------- scrittura ----------
def write(rel, text):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    if rel.startswith("en/") and isinstance(text, str):
        text = text.replace("Manager umano", "Human Manager").replace("Coordinatore AI", "AI Coordinator")
    open(p, "w", encoding="utf-8").write(text)

# ---------- file per l'hosting (OVH, Apache) ----------
HTACCESS = """# Eiraman - configurazione Apache per l'hosting condiviso OVH (generato da build.py)
# Nessun elenco dei file nelle cartelle senza index
Options -Indexes

<IfModule mod_rewrite.c>
RewriteEngine On
# Da HTTP a HTTPS (forma raccomandata da OVH per l'hosting condiviso); 302 finché non è verificato online
RewriteCond %{SERVER_PORT} ^80$
RewriteRule ^(.*)$ https://eiraman.tech/$1 [R=302,L]
# Da www a dominio nudo, solo se la richiesta è già in HTTPS: un solo salto, senza loop
RewriteCond %{HTTP_HOST} ^www\.eiraman\.tech$ [NC]
RewriteRule ^(.*)$ https://eiraman.tech/$1 [R=302,L]
</IfModule>

<IfModule mod_headers.c>
# HSTS prudente: un giorno, senza sottodomini né preload
Header always set Strict-Transport-Security "max-age=86400"
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set X-Frame-Options "DENY"
# CSP: script inline ammessi solo per impronta; stili inline (attributi style e <style>); font Google; immagini locali
Header always set Content-Security-Policy "%CSP%"
</IfModule>
"""
CSP = ("default-src 'self'; script-src 'self' %SCRIPTS%; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
       "font-src 'self' https://fonts.gstatic.com; img-src 'self'; connect-src 'self'; object-src 'none'; "
       "base-uri 'self'; form-action 'self'; frame-ancestors 'none'")

def build_host():
    import base64
    pages, scripts = [], set()
    for r, _, fs in os.walk(OUT):
        for f in fs:
            if not f.endswith(".html"): continue
            rel = os.path.relpath(os.path.join(r, f), OUT).replace(os.sep, "/")
            t = open(os.path.join(r, f), encoding="utf-8").read()
            if re.search(r"<script(?!>)", t): raise RuntimeError(f"{rel}: <script> con attributi non previsto dalla CSP")
            for js in re.findall(r"<script>(.*?)</script>", t, re.S):  # impronta di ogni script inline per la CSP
                scripts.add("'sha256-" + base64.b64encode(hashlib.sha256(js.encode("utf-8")).digest()).decode() + "'")
            if 'http-equiv="refresh"' in t or 'content="noindex"' in t: continue  # pagine di solo reindirizzamento
            pages.append(rel)
    pages.sort()
    loc = lambda rel: DOMAIN + ("" if rel == "index.html" else rel[:-len("index.html")] if rel.endswith("/index.html") else rel)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{html.escape(loc(p))}</loc></url>" for p in pages]
    sm.append("</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}sitemap.xml\n")
    open(os.path.join(OUT, ".htaccess"), "w", encoding="utf-8").write(HTACCESS.replace("%CSP%", CSP.replace("%SCRIPTS%", " ".join(sorted(scripts)))))
    print("host: .htaccess, robots.txt, sitemap.xml con", len(pages), "pagine")

def main():
    # Svuota il contenuto senza cancellare la cartella: evita i conflitti con le cartelle sincronizzate
    if os.path.exists(OUT):
        for root, dirs, files in os.walk(OUT, topdown=False):
            for f in files: os.remove(os.path.join(root, f))
            for d in dirs:
                try: os.rmdir(os.path.join(root, d))
                except OSError: pass
    os.makedirs(OUT, exist_ok=True)
    extra_css = open(os.path.join(HERE, "site-extra.css"), encoding="utf-8").read()
    write("assets/site.css", open(os.path.join(HERE, "site.css"), encoding="utf-8").read() + "\n" + extra_css)
    if HAS_BRAND:
        favicon.build(OUT)  # favicon.svg, favicon.ico, apple-touch-icon.png, icon-512.png alla radice
        os.makedirs(os.path.join(OUT, "brand"))
        for n in LOGO_FILES:
            shutil.copy(os.path.join(LOGO, n), os.path.join(OUT, "brand", n))
        favicon.og_image(os.path.join(OUT, "brand", "eiraman-su-chiaro.png"), os.path.join(OUT, favicon.OG_FILE))  # anteprima dei link
    else:
        _missing("brand")
    if os.path.isfile(PHOTO):
        shutil.copy(PHOTO, os.path.join(OUT, "assets", "paolo-ungari.jpg"))
    else:
        _missing("photo")
    for rel, src in (("framework/Eiraman.md", os.path.join(SPEC03, "Eiraman.md")), ("framework/Fonti.md", os.path.join(OLD, "framework/Fonti.md")),
                     ("en/framework/Eiraman.en.md", os.path.join(SPEC03, "Eiraman.en.md"))):
        if not os.path.isfile(src):
            _missing("download:" + rel); continue
        os.makedirs(os.path.dirname(os.path.join(OUT, rel)), exist_ok=True)
        shutil.copy(src, os.path.join(OUT, rel))
    # Il kit si costruisce prima delle pagine: il prompt di avvio ne cita l'impronta (lo zip non contiene pagine HTML)
    global KIT_SHA
    n_kit, KIT_SHA = build_kit()
    print("kit:", n_kit, "file, sha256", KIT_SHA)
    for lang in ("it", "en"):
        write(path_of(lang, "home"), build_home(lang))
        write(path_of(lang, "metodo"), build_method(lang))
        for k in ORDER: write(path_of(lang, k), build_comp(lang, k))
        write(path_of(lang, "specifica"), build_spec(lang))
        write(path_of(lang, "mappa"), build_map(lang))
        write(path_of(lang, "progetti"), build_progetti(lang))
        write(path_of(lang, "pilota"), redirect_page(lang, "progetti"))
        write(path_of(lang, "originalita"), build_orig(lang))
        write(path_of(lang, "chi"), build_about(lang))
        write(path_of(lang, "uso"), build_uso(lang))
        write(path_of(lang, "profili-ruolo"), build_rp(lang))
        write(path_of(lang, "framework"), build_framework(lang))
    build_host()
    files = []
    for r, _, fs in os.walk(OUT):
        for f in fs:
            if f == "manifest.json" or (f.startswith(".") and f != ".htaccess"): continue
            files.append(os.path.relpath(os.path.join(r, f), OUT))
    files.sort()
    man = {"format": 1, "version": SITE_VERSION, "date": "2026-11-26", "languages": ["it", "en"],
           "placeholders": sorted(PLACEHOLDERS),
           "kit": {"path": "kit/eiraman-kit.zip", "version": KIT_VERSION, "bundled": KIT_BUNDLED},
           "sha256": {f: hashlib.sha256(open(os.path.join(OUT, f), "rb").read()).hexdigest() for f in files}}
    json.dump(man, open(os.path.join(OUT, "manifest.json"), "w"), indent=2, ensure_ascii=False)
    print("pagine:", sum(1 for f in files if f.endswith(".html")), "file:", len(files))
    if PLACEHOLDERS: print("placeholders:", ", ".join(sorted(PLACEHOLDERS)))

if __name__ == "__main__":
    main()
