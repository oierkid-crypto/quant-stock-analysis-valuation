#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import sys


def fetch(url: str) -> str:
    raw = subprocess.check_output(["curl", "-L", "--max-time", "20", url], stderr=subprocess.DEVNULL)
    return raw.decode("gb18030", "ignore")


def a_or_hk_snapshot(ticker: str):
    ticker = ticker.strip().upper()
    if ticker.endswith('.HK'):
        code = ticker.split('.')[0].zfill(5)
        txt = fetch(f'https://qt.gtimg.cn/q=hk{code}')
        m = re.search(r'="(.*)";', txt)
        arr = m.group(1).split('~') if m else []
        return {
            'ticker': ticker,
            'market': 'HK',
            'name': arr[1] if len(arr) > 1 else None,
            'price': float(arr[3]) if len(arr) > 3 and arr[3] else None,
            'prev_close': float(arr[4]) if len(arr) > 4 and arr[4] else None,
            'market_cap_hkd_bn': round(float(arr[45]) / 100, 2) if len(arr) > 45 and arr[45] else None,
            'currency': 'HKD',
        }
    code, market = ticker.split('.')
    prefix = 'sh' if market == 'SH' else 'sz'
    qt = fetch(f'https://qt.gtimg.cn/q={prefix}{code}')
    m = re.search(r'="(.*)";', qt)
    arr = m.group(1).split('~') if m else []
    js = fetch(f'http://finance.sina.com.cn/realstock/company/{prefix}{code}/jsvar.js')
    def extract(key):
        mm = re.search(rf'var {key} = ([^;]+);', js)
        if not mm:
            return None
        val = mm.group(1).strip().strip("'")
        try:
            return float(val)
        except Exception:
            return val
    eps = extract('fourQ_mgsy')
    price = float(arr[3]) if len(arr) > 3 and arr[3] else None
    return {
        'ticker': ticker,
        'market': 'A',
        'name': arr[1] if len(arr) > 1 else None,
        'price': price,
        'prev_close': float(arr[4]) if len(arr) > 4 and arr[4] else None,
        'market_cap_cny_yi': float(arr[45]) if len(arr) > 45 and arr[45] else None,
        'pb': float(arr[46]) if len(arr) > 46 and arr[46] else None,
        'ttm_eps': eps,
        'ttm_pe': round(price / eps, 1) if price and eps and eps > 0 else None,
        'bvps': extract('mgjzc'),
        'profit_yoy': extract('profit_four'),
        'currency': 'CNY',
    }


def main():
    ap = argparse.ArgumentParser(description='Get lightweight live quote snapshot for A/HK stocks.')
    ap.add_argument('--ticker', required=True, help='e.g. 300124.SZ or 06656.HK')
    ap.add_argument('--output', help='Optional output json path')
    args = ap.parse_args()
    data = a_or_hk_snapshot(args.ticker)
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(text)
    print(text)


if __name__ == '__main__':
    main()
