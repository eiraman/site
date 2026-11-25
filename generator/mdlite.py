# SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
# SPDX-License-Identifier: Apache-2.0
"""Sottoinsieme Markdown usato per rendere la specifica in HTML."""
import re, html

# ---------------- markdown (subset) ----------------
def slug(s):
    s = s.lower()
    s = re.sub(r"[àá]", "a", s); s = re.sub(r"[èé]", "e", s); s = re.sub(r"[ìí]", "i", s); s = re.sub(r"[òó]", "o", s); s = re.sub(r"[ùú]", "u", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s

def inline(s, linkmap=None):
    s = html.escape(s, quote=False)
    codes = []
    def keep(m):
        codes.append("<code>" + m.group(1) + "</code>"); return f"\x00{len(codes)-1}\x00"
    s = re.sub(r"`([^`]+)`", keep, s)
    def link(m):
        txt, url = m.group(1), m.group(2)
        if linkmap: url = linkmap(url)
        return f'<a href="{url}">{txt}</a>'
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], s)
    return s

LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")

def md(text, linkmap=None, toc=None, hshift=0):
    lines = text.split("\n")
    return blocks(lines, linkmap, toc, hshift)

def blocks(lines, linkmap, toc, hshift):
    out = []; i = 0; n = len(lines)
    while i < n:
        ln = lines[i]
        if not ln.strip(): i += 1; continue
        m = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if m:
            lvl = len(m.group(1)) + hshift; txt = m.group(2).strip()
            mm = re.match(r"^(\d+)( bis)?\.\s", txt)
            hid = (f"s{mm.group(1)}" + ("bis" if mm.group(2) else "")) if (mm and len(m.group(1)) == 2) else slug(txt)
            if toc is not None and len(m.group(1)) == 2: toc.append((hid, txt))
            out.append(f'<h{lvl} id="{hid}">{inline(txt, linkmap)}</h{lvl}>'); i += 1; continue
        if ln.lstrip().startswith("|"):
            rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(lines[i].strip()); i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            head, body = cells[0], [c for c in cells[2:]]
            t = '<div class="tbl"><table><thead><tr>' + "".join(f"<th>{inline(c, linkmap)}</th>" for c in head) + "</tr></thead><tbody>"
            for r in body: t += "<tr>" + "".join(f"<td>{inline(c, linkmap)}</td>" for c in r) + "</tr>"
            out.append(t + "</tbody></table></div>"); continue
        if ln.startswith(">"):
            q = []
            while i < n and lines[i].startswith(">"):
                q.append(lines[i][1:].lstrip()); i += 1
            out.append("<blockquote>" + blocks(q, linkmap, None, hshift) + "</blockquote>"); continue
        if ln.startswith("```"):
            i += 1; code = []
            while i < n and not lines[i].startswith("```"): code.append(lines[i]); i += 1
            i += 1; out.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>"); continue
        lm = LIST_RE.match(ln)
        if lm and len(lm.group(1)) == 0:
            blk = []
            while i < n:
                cur = lines[i]
                if not cur.strip():
                    # blank: continue list only if next non-blank is indented or a top-level item
                    j = i + 1
                    while j < n and not lines[j].strip(): j += 1
                    if j < n and (lines[j].startswith("  ") or (LIST_RE.match(lines[j]) and not LIST_RE.match(lines[j]).group(1))):
                        if LIST_RE.match(lines[j]) and not lines[j].startswith(" ") and not lines[j].startswith("  "):
                            # next top-level item after blank: keep in same list only if same marker type
                            pass
                        blk.append(""); i += 1; continue
                    break
                if cur.startswith(" ") or (LIST_RE.match(cur) and not LIST_RE.match(cur).group(1)):
                    blk.append(cur); i += 1; continue
                break
            out.append(render_list(blk, linkmap, hshift)); continue
        para = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,6})\s", lines[i]) and not lines[i].lstrip().startswith("|") and not (LIST_RE.match(lines[i]) and not LIST_RE.match(lines[i]).group(1)):
            para.append(lines[i].strip()); i += 1
        out.append("<p>" + inline(" ".join(para), linkmap) + "</p>")
    return "\n".join(out)

def render_list(blk, linkmap, hshift):
    first = LIST_RE.match(blk[0]); ordered = first.group(2)[0].isdigit()
    items = []
    for ln in blk:
        m = LIST_RE.match(ln)
        if m and not m.group(1):
            items.append([m.group(3)])
        else:
            items[-1].append(ln[2:] if ln.startswith("  ") else ln.lstrip())
    tag = "ol" if ordered else "ul"
    start = ""
    if ordered:
        k = int(first.group(2)[:-1])
        if k != 1: start = f' start="{k}"'
    res = f"<{tag}{start}>"
    for it in items:
        # strip trailing blanks
        while it and not it[-1].strip(): it.pop()
        if len(it) == 1:
            res += "<li>" + inline(it[0], linkmap) + "</li>"
        else:
            # first line then rest as blocks
            rest = it[1:]
            # dedent continuation for ordered markers "1. " (3 chars) handled by lstrip of extra space
            rest = [r[1:] if r.startswith(" ") and not r.startswith("  ") else r for r in rest]
            res += "<li><p>" + inline(it[0], linkmap) + "</p>" + blocks(rest, linkmap, None, hshift) + "</li>"
    return res + f"</{tag}>"

