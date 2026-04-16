#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path


def run(cmd):
    print('+', ' '.join(cmd))
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser(description='Convenience runner for the institutional equity research pipeline.')
    sub = ap.add_subparsers(dest='command', required=True)

    s = sub.add_parser('scaffold', help='Create starter JSON from a ticker')
    s.add_argument('--ticker', required=True)
    s.add_argument('--output', required=True)

    b = sub.add_parser('build', help='Build the final research document from structured input JSON')
    b.add_argument('--input', required=True)
    b.add_argument('--template', default='templates/output-template.md')
    b.add_argument('--md-output', required=True)
    b.add_argument('--pdf-output', required=True)

    q = sub.add_parser('quote', help='Fetch a live quote snapshot')
    q.add_argument('--ticker', required=True)
    q.add_argument('--output', default='')

    args = ap.parse_args()
    root = Path(__file__).resolve().parent.parent

    if args.command == 'scaffold':
        run([sys.executable, str(root / 'scripts' / 'scaffold_input.py'), '--ticker', args.ticker, '--output', args.output])
    elif args.command == 'build':
        run([sys.executable, str(root / 'scripts' / 'build_report.py'), '--input', args.input, '--template', args.template, '--output', args.md_output])
        run([sys.executable, str(root / 'scripts' / 'render_pdf.py'), '--input', args.md_output, '--output', args.pdf_output])
    elif args.command == 'quote':
        cmd = [sys.executable, str(root / 'scripts' / 'quote_snapshot.py'), '--ticker', args.ticker]
        if args.output:
            cmd += ['--output', args.output]
        run(cmd)


if __name__ == '__main__':
    main()
