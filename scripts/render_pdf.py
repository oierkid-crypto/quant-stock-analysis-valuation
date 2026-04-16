#!/usr/bin/env python3
import argparse
import math
import textwrap
from pathlib import Path

PAGE_W = 595
PAGE_H = 842
LEFT = 52
TOP = 60
BOTTOM = 50
BODY = 11
SMALL = 9
H1 = 22
H2 = 16
H3 = 13
LEADING = 16
MONO_CHAR_W = 6.1
TEXT_WIDTH = PAGE_W - LEFT * 2
MAX_CHARS = int(TEXT_WIDTH / 6.2)


def esc(s: str) -> str:
    return s.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')


def classify(line: str):
    raw = line.rstrip('\n')
    if raw.startswith('# '):
        return ('h1', raw[2:].strip())
    if raw.startswith('## '):
        return ('h2', raw[3:].strip())
    if raw.startswith('### '):
        return ('h3', raw[4:].strip())
    if raw.startswith('|'):
        return ('table', raw)
    if raw.startswith('- '):
        return ('bullet', raw[2:].strip())
    if not raw.strip():
        return ('blank', '')
    return ('body', raw)


def wrap(kind, text):
    if kind == 'table':
        return [text[:MAX_CHARS]]
    width = MAX_CHARS
    if kind == 'bullet':
        width = MAX_CHARS - 4
    if kind == 'h1':
        width = 38
    elif kind == 'h2':
        width = 52
    elif kind == 'h3':
        width = 62
    return textwrap.wrap(text, width=width, break_long_words=False, replace_whitespace=False) or ['']


def layout(markdown: str):
    pages = []
    page = []
    y = PAGE_H - TOP

    def new_page():
        nonlocal page, y
        if page:
            pages.append(page)
        page = []
        y = PAGE_H - TOP

    for raw in markdown.splitlines():
        kind, text = classify(raw)
        if kind == 'blank':
            y -= LEADING // 2
            continue
        lines = wrap(kind, text)
        size = {'h1': H1, 'h2': H2, 'h3': H3, 'body': BODY, 'bullet': BODY, 'table': SMALL}[kind]
        needed = len(lines) * (size + 4) + 4
        if y - needed < BOTTOM:
            new_page()
        for i, line in enumerate(lines):
            x = LEFT
            shown = line
            font = 'F1'
            if kind == 'table':
                font = 'F2'
                shown = line
            if kind == 'bullet':
                if i == 0:
                    shown = '• ' + line
                else:
                    shown = '  ' + line
            page.append((font, size, x, y, shown))
            y -= (size + 4)
        y -= 4
    if page:
        pages.append(page)
    return pages


def pdf_bytes(pages):
    objects = []

    def add(obj: bytes):
        objects.append(obj)
        return len(objects)

    font1 = add(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>')
    font2 = add(b'<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>')

    page_ids = []
    content_ids = []
    pages_root_placeholder = len(objects) + 1
    add(b'PAGES_PLACEHOLDER')

    for page in pages:
        content = ['BT']
        for font, size, x, y, text in page:
            content.append(f'/{font} {size} Tf')
            content.append(f'1 0 0 1 {x} {y} Tm')
            content.append(f'({esc(text)}) Tj')
        content.append('ET')
        stream = '\n'.join(content).encode('latin-1', 'replace')
        cid = add(b'<< /Length ' + str(len(stream)).encode() + b' >>\nstream\n' + stream + b'\nendstream')
        content_ids.append(cid)
        pid = add(b'<< /Type /Page /Parent ' + f'{pages_root_placeholder} 0 R'.encode() +
                  b' /MediaBox [0 0 595 842] /Resources << /Font << /F1 ' + f'{font1} 0 R'.encode() +
                  b' /F2 ' + f'{font2} 0 R'.encode() + b' >> >> /Contents ' + f'{cid} 0 R'.encode() + b' >>')
        page_ids.append(pid)

    kids = ' '.join(f'{pid} 0 R' for pid in page_ids).encode()
    objects[pages_root_placeholder - 1] = b'<< /Type /Pages /Kids [ ' + kids + b' ] /Count ' + str(len(page_ids)).encode() + b' >>'
    catalog = add(b'<< /Type /Catalog /Pages ' + f'{pages_root_placeholder} 0 R'.encode() + b' >>')

    out = [b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n']
    offsets = [0]
    pos = len(out[0])
    for i, obj in enumerate(objects, start=1):
        offsets.append(pos)
        chunk = f'{i} 0 obj\n'.encode() + obj + b'\nendobj\n'
        out.append(chunk)
        pos += len(chunk)
    xref = pos
    out.append(f'xref\n0 {len(objects)+1}\n'.encode())
    out.append(b'0000000000 65535 f \n')
    for off in offsets[1:]:
        out.append(f'{off:010d} 00000 n \n'.encode())
    out.append(b'trailer\n')
    out.append(b'<< /Size ' + str(len(objects)+1).encode() + b' /Root ' + f'{catalog} 0 R'.encode() + b' >>\n')
    out.append(b'startxref\n' + str(xref).encode() + b'\n%%EOF\n')
    return b''.join(out)


def main():
    ap = argparse.ArgumentParser(description='Render markdown to a simple readable PDF without external dependencies.')
    ap.add_argument('--input', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    md = Path(args.input).read_text(encoding='utf-8')
    pages = layout(md)
    data = pdf_bytes(pages)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    print(str(out))


if __name__ == '__main__':
    main()
