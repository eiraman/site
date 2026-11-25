# SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
# SPDX-License-Identifier: Apache-2.0
"""Minimal pure-Python PNG reader/writer (8-bit RGB/RGBA, non-interlaced)."""
import zlib, struct

def read_png(path):
    data = open(path, 'rb').read()
    assert data[:8] == b'\x89PNG\r\n\x1a\n'
    pos = 8; idat = b''; meta = {}
    while pos < len(data):
        ln = struct.unpack('>I', data[pos:pos+4])[0]; typ = data[pos+4:pos+8]
        body = data[pos+8:pos+8+ln]; pos += 12 + ln
        if typ == b'IHDR':
            w, h, bd, ct, comp, flt, il = struct.unpack('>IIBBBBB', body)
            meta = dict(w=w, h=h, bd=bd, ct=ct, il=il)
        elif typ == b'IDAT': idat += body
        elif typ == b'IEND': break
    assert meta['bd'] == 8 and meta['il'] == 0 and meta['ct'] in (2, 6), meta
    bpp = 4 if meta['ct'] == 6 else 3
    w, h = meta['w'], meta['h']; stride = w * bpp
    raw = zlib.decompress(idat); out = []; prev = bytearray(stride); i = 0
    for _ in range(h):
        f = raw[i]; line = bytearray(raw[i+1:i+1+stride]); i += 1 + stride
        for x in range(stride):
            a = line[x-bpp] if x >= bpp else 0; b = prev[x]; c = prev[x-bpp] if x >= bpp else 0
            if f == 1: line[x] = (line[x] + a) & 255
            elif f == 2: line[x] = (line[x] + b) & 255
            elif f == 3: line[x] = (line[x] + ((a + b) >> 1)) & 255
            elif f == 4:
                p = a + b - c; pa, pb, pc = abs(p-a), abs(p-b), abs(p-c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[x] = (line[x] + pr) & 255
        out.append(line); prev = line
    px = []
    for line in out:
        row = []
        for x in range(w):
            o = x * bpp
            row.append((line[o], line[o+1], line[o+2], line[o+3] if bpp == 4 else 255))
        px.append(row)
    return w, h, px

def write_png(path, w, h, px):
    raw = bytearray()
    for row in px:
        raw.append(0)
        for r, g, b, a in row: raw += bytes((r, g, b, a))
    def chunk(t, b): return struct.pack('>I', len(b)) + t + b + struct.pack('>I', zlib.crc32(t + b) & 0xffffffff)
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0))
    png += chunk(b'IDAT', zlib.compress(bytes(raw), 9)) + chunk(b'IEND', b'')
    open(path, 'wb').write(png)
