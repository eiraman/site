# SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
# SPDX-License-Identifier: Apache-2.0
# The code is Apache-2.0. The mark it draws is the Eiraman logo, a trademark that this licence does not grant
# (Apache-2.0 section 6): see brand/PROVENANCE.md and TRADEMARK.md in the community repository.
"""Favicon Eiraman: la «E» del logo (barre, triangolo blu, stella oro) in SVG e in PNG/ICO.

Geometria ricavata dalla «E» di brand/eiraman-su-chiaro.png (riquadro 132 x 139 px).
Uso: python3 generator/favicon.py <cartella di uscita>
Scrive favicon.svg, favicon.ico (16 e 32 px), apple-touch-icon.png (180 px), icon-512.png.
"""
import os, struct, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pngtool import write_png

W, H = 132, 139
UPPER = [(0, 0), (132, 0), (114, 17), (30, 17), (86, 67), (61, 67), (0, 13)]
LOWER = [(x, H - y) for x, y in UPPER]
TRI = [(1, 28), (41, 69.5), (1, 111)]
STAR_C, STAR_R, STAR_K = (110, 69.5), 19.5, 4.5   # centro, raggio delle punte, ampiezza della curva

# Palette del logo (generator/recolor_logo.py)
LIGHT = {"e": "#1b2a41", "tri": "#2f5f98", "star": "#8a6d3b"}
DARK = {"e": "#e6ebf1", "tri": "#8fb4e6", "star": "#c8b49b"}
TILE = "#f5f7fa"   # fondo chiaro del sito (--bg) per le icone raster

def star_curves():
    """Stella a quattro punte con lati concavi: quattro curve quadratiche (punta, controllo, punta)."""
    cx, cy = STAR_C; r, k = STAR_R, STAR_K
    tips = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    ctrls = [(cx + k, cy - k), (cx + k, cy + k), (cx - k, cy + k), (cx - k, cy - k)]
    return [(tips[i], ctrls[i], tips[(i + 1) % 4]) for i in range(4)]

def svg():
    pts = lambda p: " ".join(f"{x:g},{y:g}" for x, y in p)
    (t0, _, _) = star_curves()[0]
    d = f"M{t0[0]:g} {t0[1]:g}" + "".join(f"Q{c[0]:g} {c[1]:g} {b[0]:g} {b[1]:g}" for _, c, b in star_curves()) + "Z"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -0.5 140 140">'
            f'<style>.e{{fill:{LIGHT["e"]}}}.t{{fill:{LIGHT["tri"]}}}.s{{fill:{LIGHT["star"]}}}'
            f'@media (prefers-color-scheme:dark){{.e{{fill:{DARK["e"]}}}.t{{fill:{DARK["tri"]}}}.s{{fill:{DARK["star"]}}}}}</style>'
            f'<polygon class="e" points="{pts(UPPER)}"/><polygon class="e" points="{pts(LOWER)}"/>'
            f'<polygon class="t" points="{pts(TRI)}"/><path class="s" d="{d}"/></svg>\n')

def _inside(poly, x, y):
    c = False; n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1): c = not c
    return c

def _star_poly(steps=24):
    out = []
    for a, c, b in star_curves():
        for i in range(steps):
            t = i / steps
            out.append(((1-t)**2*a[0] + 2*t*(1-t)*c[0] + t*t*b[0], (1-t)**2*a[1] + 2*t*(1-t)*c[1] + t*t*b[1]))
    return out

def _rgb(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))

def raster(size, pad, tile=True, ss=4):
    """Disegna la «E» in un quadrato di lato size; pad è il margine in frazione del lato."""
    shapes = [(UPPER, LIGHT["e"]), (LOWER, LIGHT["e"]), (TRI, LIGHT["tri"]), (_star_poly(), LIGHT["star"])]
    shapes = [(p, _rgb(c)) for p, c in shapes]
    inner = size * (1 - 2 * pad); scale = inner / max(W, H)
    ox = (size - W * scale) / 2; oy = (size - H * scale) / 2
    bg = _rgb(TILE); rows = []
    for py in range(size):
        row = []
        for px in range(size):
            acc = [0.0, 0.0, 0.0]; cov = 0
            for sy in range(ss):
                for sx in range(ss):
                    x = ((px + (sx + .5) / ss) - ox) / scale; y = ((py + (sy + .5) / ss) - oy) / scale
                    for poly, col in shapes:
                        if _inside(poly, x, y):
                            acc = [acc[i] + col[i] for i in range(3)]; cov += 1; break
            n = ss * ss
            if tile:
                rgb = tuple(round((acc[i] + bg[i] * (n - cov)) / n) for i in range(3)); row.append((*rgb, 255))
            else:
                rgb = tuple(round(acc[i] / cov) for i in range(3)) if cov else (0, 0, 0); row.append((*rgb, round(255 * cov / n)))
        rows.append(row)
    return rows

def _png_bytes(path_tmp, size, rows):
    write_png(path_tmp, size, size, rows); data = open(path_tmp, "rb").read(); os.remove(path_tmp); return data

def build(out):
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "favicon.svg"), "w", encoding="utf-8").write(svg())
    # ICO con PNG incorporati: fondo trasparente, leggibile sulle schede chiare
    tmp = os.path.join(out, ".favicon-tmp.png")
    imgs = [(s, _png_bytes(tmp, s, raster(s, 0.04, tile=False))) for s in (16, 32)]
    head = struct.pack("<HHH", 0, 1, len(imgs)); off = 6 + 16 * len(imgs); dirs = b""; body = b""
    for s, data in imgs:
        dirs += struct.pack("<BBBBHHII", s, s, 0, 0, 1, 32, len(data), off + len(body)); body += data
    open(os.path.join(out, "favicon.ico"), "wb").write(head + dirs + body)
    # Icone a fondo pieno (iOS e Android non accettano la trasparenza)
    write_png(os.path.join(out, "apple-touch-icon.png"), 180, 180, raster(180, 0.16, ss=3))
    write_png(os.path.join(out, "icon-512.png"), 512, 512, raster(512, 0.16, ss=2))

HEAD_TAGS = ('<link rel="icon" href="{pre}favicon.ico" sizes="32x32">\n'
             '<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">\n'
             '<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">\n')

if __name__ == "__main__":
    build(sys.argv[1]); print("favicon scritte in", sys.argv[1])


# ---------- Immagine di anteprima dei link (Open Graph, 1200 x 630) ----------
OG_FILE = "brand/eiraman-anteprima.png"
OG_W, OG_H = 1200, 630

def og_image(logo_png, out_path, logo_w=560):
    """«E» grande al centro e logotipo EIRAMAN sotto, su fondo chiaro: regge anche il ritaglio quadrato centrale."""
    from pngtool import read_png
    sw, sh, src = read_png(logo_png)
    s = sw / logo_w; lw, lh = logo_w, round(sh / s)
    bg = _rgb(TILE); gold = _rgb(LIGHT["star"])
    img = [[(*bg, 255) for _ in range(OG_W)] for _ in range(OG_H)]
    mark = raster(300, 0.0, ss=3)
    mx, my = (OG_W - 300) // 2, 70
    for y in range(300):
        img[my + y][mx:mx + 300] = mark[y]
    x0, y0 = (OG_W - lw) // 2, 470 - lh // 2
    for oy in range(lh):
        ya, yb = oy * s, (oy + 1) * s
        for ox in range(lw):
            xa, xb = ox * s, (ox + 1) * s; acc = [0.0, 0.0, 0.0]; aa = 0.0; wt = 0.0
            for y in range(int(ya), min(sh, int(yb) + 1)):
                fy = min(yb, y + 1) - max(ya, y)
                if fy <= 0: continue
                for x in range(int(xa), min(sw, int(xb) + 1)):
                    fx = min(xb, x + 1) - max(xa, x)
                    if fx <= 0: continue
                    r, g, b, a = src[y][x]; f = fx * fy * a / 255
                    acc[0] += r * f; acc[1] += g * f; acc[2] += b * f; aa += f; wt += fx * fy
            al = aa / wt if wt else 0
            col = tuple(round(acc[i] / aa * al + bg[i] * (1 - al)) if aa else bg[i] for i in range(3))
            img[y0 + oy][x0 + ox] = (*col, 255)
    for y in range(405, 408):
        for x in range(OG_W // 2 - 50, OG_W // 2 + 50): img[y][x] = (*gold, 255)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    write_png(out_path, OG_W, OG_H, img)

def og_tags(lang, title, desc, url, domain="https://eiraman.tech/"):
    import html as _h
    e = lambda t: _h.escape(t, quote=True)
    alt = "Logo EIRAMAN" if lang == "it" else "EIRAMAN logo"
    return (f'<meta property="og:type" content="website">\n'
            f'<meta property="og:site_name" content="Eiraman">\n'
            f'<meta property="og:locale" content="{"it_IT" if lang == "it" else "en_US"}">\n'
            f'<meta property="og:title" content="{e(title)}">\n'
            f'<meta property="og:description" content="{e(desc)}">\n'
            f'<meta property="og:url" content="{e(url)}">\n'
            f'<meta property="og:image" content="{domain}{OG_FILE}">\n'
            f'<meta property="og:image:width" content="{OG_W}">\n'
            f'<meta property="og:image:height" content="{OG_H}">\n'
            f'<meta property="og:image:alt" content="{alt}">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n')
