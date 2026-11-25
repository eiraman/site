# SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
# SPDX-License-Identifier: Apache-2.0
"""Illustrazioni SVG della home v6 di Eiraman (Perché A, Perché B, Come, Cosa).

Tutte disegnate a mano con lo stesso tratto e i token colore del sito
(classi .ln .fw .hm .ai .dn .pp e testi .lb .lm .la, definite in site-extra.css sotto .ill).
"""
import html

esc = html.escape


def person(x, y, cls="hm", s=1.0):
    """Figura umana stilizzata: testa in (x, y), altezza circa 32*s."""
    r = 7 * s
    return (f'<circle class="{cls}" cx="{x}" cy="{y}" r="{r:.1f}"/>'
            f'<path class="{cls}" d="M{x-11*s:.1f} {y+25*s:.1f}c0-8.5 4.9-13.5 {11*s:.1f}-13.5s{11*s:.1f} 5 {11*s:.1f} 13.5z"/>')


def svg(vb, aria, inner, cls=""):
    return (f'<svg class="ill-svg {cls}" viewBox="{vb}" role="img" aria-label="{esc(aria)}" '
            f'xmlns="http://www.w3.org/2000/svg">{inner}</svg>')


def ill_a(lb, aria):
    """Un unico edificio uguale per tutti; costi e tempi; esigenze specifiche fuori."""
    p = []
    p.append('<path class="ln" d="M16 268H504"/>')
    # costi e tempi (in alto a sinistra)
    p.append('<g class="cost">'
             '<ellipse class="fw" cx="52" cy="104" rx="20" ry="6.5"/><path class="fw" d="M32 104v10c0 3.6 9 6.5 20 6.5s20-2.9 20-6.5v-10"/>'
             '<path class="fw" d="M32 114v10c0 3.6 9 6.5 20 6.5s20-2.9 20-6.5v-10"/>'
             '<path class="ln" d="M96 88h26M96 136h26"/><path class="fw" d="M100 90h18l-9 21z"/><path class="fw" d="M100 134h18l-9-21z"/>'
             f'<text class="lm" x="77" y="164" text-anchor="middle">{esc(lb["cost"])}</text></g>')
    # edificio unico
    p.append('<rect class="fw" x="160" y="62" width="186" height="206" rx="4"/><path class="ln strong" d="M160 96H346"/>')
    p.append(f'<text class="lb" x="253" y="85" text-anchor="middle">{esc(lb["top"])}</text>')
    for r in range(4):
        for c in range(4):
            p.append(f'<rect class="pp" x="{176 + c*42}" y="{110 + r*30}" width="26" height="17" rx="2"/>')
    p.append('<rect class="pp" x="236" y="230" width="34" height="38" rx="2"/>')
    # persone in fila verso l'ingresso
    for i, x in enumerate((36, 70, 104, 138)):
        p.append(person(x, 226, "hm" if i % 2 == 0 else "hm2"))
    # esigenze specifiche: forme diverse, tratteggiate, fuori
    p.append('<g class="needs">'
             '<path class="dn dash" d="M404 92l24 42h-48z"/>'
             '<path class="dn dash" d="M470 128l7 14 15 2-11 10 3 15-14-7-14 7 3-15-11-10 15-2z"/>'
             '<path class="dn dash" d="M410 176l17-10 17 10v20l-17 10-17-10z"/>'
             f'<text class="lm" x="446" y="232" text-anchor="middle">{esc(lb["need1"])}</text>'
             f'<text class="lm" x="446" y="252" text-anchor="middle">{esc(lb["need2"])}</text></g>')
    return svg("0 0 520 290", aria, "".join(p), "ab")


def ill_b(lb, aria):
    """Bivio tra due sponde: AI chiusa ai soli tecnici, AI libera senza governo, manca il ponte."""
    p = []
    # sponde e fondovalle
    p.append('<path class="fw" d="M16 176H196V282H16z"/><path class="fw" d="M324 176H504V282H324z"/>')
    p.append('<path class="ln" d="M196 282H324"/>')
    # ponte mancante
    p.append('<path class="dn dash thin" d="M196 176Q260 126 324 176"/>')
    p.append(f'<text class="lm" x="260" y="120" text-anchor="middle">{esc(lb["gap"])}</text>')
    # sinistra: porta chiusa, AI dietro
    p.append('<rect class="ai" x="56" y="84" width="72" height="56" rx="8"/><text class="la" x="92" y="118" text-anchor="middle">AI</text>')
    p.append('<path class="ln strong" d="M40 64H144M40 172H144' + ''.join(f'M{x} 64V172' for x in range(46, 146, 14)) + '"/>')
    p.append('<rect class="dn" x="80" y="146" width="24" height="20" rx="3"/><path class="dn" d="M85 146v-7a7 7 0 0 1 14 0v7"/>')
    p.append(f'<text class="lb" x="92" y="44" text-anchor="middle">{esc(lb["left"])}</text>')
    # destra: AI libera, fili aggrovigliati, allerta
    p.append('<path class="dn wire" d="M360 140c-24 10-10 30 10 24s20-26 40-14-6 30 16 30 30-24 52-12M380 98c-30-6-34 22-10 22s14-28 38-28 10 26 34 18"/>')
    p.append('<rect class="ai" x="384" y="102" width="72" height="56" rx="8"/><text class="la" x="420" y="136" text-anchor="middle">AI</text>')
    p.append('<path class="dn" d="M478 56l18 32h-36z"/><path class="dnk" d="M478 68v9M478 82v1"/>')
    p.append(f'<text class="lb" x="420" y="44" text-anchor="middle">{esc(lb["right"])}</text>')
    # persona di business, in basso
    p.append(person(260, 236, "hm"))
    p.append('<text class="lq" x="284" y="226">?</text>')
    return svg("0 0 520 296", aria, "".join(p), "ab")


def ill_how(lb, aria):
    """Il ponte: cinque modelli di management attraversano e diventano AI Squad."""
    p = []
    ys = (70, 114, 158, 202, 246)
    for name, y in zip(lb["models"], ys):
        p.append(f'<g class="mpill"><rect class="fw" x="14" y="{y}" width="156" height="34" rx="17"/>'
                 f'<text class="lb" x="92" y="{y+22}" text-anchor="middle">{esc(name)}</text></g>')
        p.append(f'<path class="ln flow" d="M170 {y+17}C186 {y+17} 186 200 202 200"/>')
    # ponte
    p.append('<path class="ln strong" d="M202 200H382"/>')
    p.append('<path class="acc draw" d="M202 200Q292 112 382 200"/>')
    for x in (232, 262, 292, 322, 352):
        yy = 200 - (1 - ((x - 292) / 90) ** 2) * 44
        p.append(f'<path class="ln" d="M{x} {yy:.1f}V200"/>')
    p.append('<path class="ln" d="M214 200v40M370 200v40"/>')
    # persona di business che governa
    p.append(person(292, 26, "hm"))
    p.append('<path class="hm-line" d="M292 62V150M310 46C370 46 404 84 406 124"/>')
    p.append(f'<text class="lb" x="318" y="30">{esc(lb["gov"])}</text>')
    # AI Squad
    p.append(f'<text class="lm" x="474" y="120" text-anchor="middle">{esc(lb["teams"])}</text>')
    for y in (130, 184, 238):
        p.append(f'<rect class="ai" x="400" y="{y}" width="148" height="44" rx="10"/>')
        for i, x in enumerate((428, 456, 484, 512)):
            p.append(f'<circle class="ai dot" cx="{x}" cy="{y+22}" r="7"/>')
    p.append('<path class="ln" d="M382 200H400"/>')
    # profili qualificati da chi sviluppa
    p.append('<rect class="pp" x="188" y="262" width="210" height="56" rx="10"/>')
    p.append('<path class="hm" d="M206 276l12-5 12 5v10c0 7-6 11-12 14-6-3-12-7-12-14z"/><path class="hmk" d="M213 286l4 4 7-8"/>')
    p.append(f'<text class="lb" x="240" y="285">{esc(lb["prof1"])}</text><text class="lm" x="240" y="305">{esc(lb["prof2"])}</text>')
    p.append('<path class="ln flow" d="M398 290C420 290 430 282 444 282"/>')
    return svg("0 0 560 330", aria, "".join(p), "d")


def ill_what(lb, aria):
    """La produzione si sposta da una fabbrica lontana a servizi su misura, dentro il perimetro di rischio."""
    p = []
    p.append('<path class="ln" d="M16 256H226"/>')
    # fabbrica lontana, sbiadita
    p.append('<g class="far"><path class="pp" d="M28 256V184l28 16v-16l28 16v-16l28 16V146h18v110z"/>'
             '<path class="ln" d="M52 226h12M76 226h12M100 226h12"/>'
             f'<text class="lm" x="76" y="280" text-anchor="middle">{esc(lb["far"])}</text></g>')
    # spostamento
    p.append('<path class="acc dash draw" d="M140 170C176 120 212 112 250 120"/><path class="acc" d="M242 112l10 8-11 6"/>')
    # perimetro di rischio
    p.append('<rect class="fence" x="262" y="34" width="282" height="236" rx="20"/>')
    p.append(f'<text class="lfence" x="282" y="60">{esc(lb["fence"])}</text>')
    # servizi su misura accanto a ciascuna persona
    for (px, py) in ((300, 104), (420, 104), (360, 194)):
        p.append(person(px, py, "hm"))
        bx, by = px + 22, py - 8
        p.append(f'<rect class="ai svc" x="{bx}" y="{by}" width="50" height="40" rx="8"/>'
                 f'<path class="aik" d="M{bx+15} {by+21}l7 7 13-14"/>')
    return svg("0 0 560 292", aria, "".join(p), "d")


def ill_how_m(lb, aria):
    """Versione verticale per telefono del ponte."""
    p = []
    p.append(person(292, 22, "hm"))
    p.append(f'<text class="lb" x="270" y="30" text-anchor="end">{esc(lb["gov"])}</text>')
    p.append('<path class="hm-line" d="M314 40C334 140 330 380 274 444"/>')
    for i, name in enumerate(lb["models"]):
        y = 70 + i * 42
        p.append(f'<g class="mpill"><rect class="fw" x="60" y="{y}" width="200" height="34" rx="17"/>'
                 f'<text class="lb" x="160" y="{y+22}" text-anchor="middle">{esc(name)}</text></g>')
    p.append('<path class="ln flow" d="M160 278V318"/><path class="ln" d="M153 310l7 9 7-9"/>')
    p.append('<path class="ln strong" d="M60 372H260"/><path class="acc draw" d="M60 372Q160 302 260 372"/>')
    for x in (90, 125, 160, 195, 230):
        yy = 372 - (1 - ((x - 160) / 100) ** 2) * 35
        p.append(f'<path class="ln" d="M{x} {yy:.1f}V372"/>')
    p.append('<path class="ln" d="M160 380V398"/>')
    p.append(f'<text class="lm" x="160" y="416" text-anchor="middle">{esc(lb["teams"])}</text>')
    for y in (426, 474, 522):
        p.append(f'<rect class="ai" x="50" y="{y}" width="220" height="40" rx="10"/>')
        for x in (100, 140, 180, 220):
            p.append(f'<circle class="ai dot" cx="{x}" cy="{y+20}" r="7"/>')
    p.append('<rect class="pp" x="50" y="586" width="220" height="50" rx="10"/>')
    p.append('<path class="hm" d="M66 598l12-5 12 5v10c0 7-6 11-12 14-6-3-12-7-12-14z"/><path class="hmk" d="M73 608l4 4 7-8"/>')
    p.append(f'<text class="lb" x="100" y="607">{esc(lb["prof1"])}</text><text class="lm" x="100" y="626">{esc(lb["prof2"])}</text>')
    p.append('<path class="ln flow" d="M160 586V564"/>')
    return svg("0 0 330 646", aria, "".join(p), "m")


def ill_what_m(lb, aria):
    """Versione verticale per telefono dei servizi vicini."""
    p = []
    p.append('<path class="ln" d="M16 118H140"/>')
    p.append('<g class="far"><path class="pp" d="M24 118V58l24 14V58l24 14V58l24 14V28h16v90z"/>'
             f'<text class="lm" x="16" y="144">{esc(lb["far"])}</text></g>')
    p.append('<path class="acc dash draw" d="M150 70C220 70 250 110 252 172"/><path class="acc" d="M244 164l8 10 8-10"/>')
    p.append('<rect class="fence" x="14" y="186" width="302" height="270" rx="20"/>')
    p.append(f'<text class="lfence" x="34" y="214">{esc(lb["fence"])}</text>')
    for (px, py) in ((60, 262), (190, 262), (125, 362)):
        p.append(person(px, py, "hm"))
        bx, by = px + 22, py - 8
        p.append(f'<rect class="ai svc" x="{bx}" y="{by}" width="50" height="40" rx="8"/>'
                 f'<path class="aik" d="M{bx+15} {by+21}l7 7 13-14"/>')
    return svg("0 0 330 470", aria, "".join(p), "m")
