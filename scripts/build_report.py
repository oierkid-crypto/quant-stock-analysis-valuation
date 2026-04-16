#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def render_template(template: str, data: dict) -> str:
    def repl(match):
        key = match.group(1).strip()
        val = data.get(key, '')
        if isinstance(val, (dict, list)):
            return json.dumps(val, ensure_ascii=False)
        return str(val)
    return re.sub(r'\{\{\s*([^}]+?)\s*\}\}', repl, template)


def main():
    ap = argparse.ArgumentParser(description='Render markdown report from template + JSON input.')
    ap.add_argument('--input', required=True, help='Path to structured input json')
    ap.add_argument('--template', required=True, help='Path to markdown template')
    ap.add_argument('--output', required=True, help='Path to output markdown')
    args = ap.parse_args()

    data = json.loads(Path(args.input).read_text(encoding='utf-8'))
    template = Path(args.template).read_text(encoding='utf-8')
    rendered = render_template(template, data)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(rendered, encoding='utf-8')
    print(str(out))


if __name__ == '__main__':
    main()
