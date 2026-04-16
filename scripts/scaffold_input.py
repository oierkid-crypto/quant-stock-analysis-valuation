#!/usr/bin/env python3
import argparse
import datetime as dt
import json
from pathlib import Path

from quote_snapshot import a_or_hk_snapshot

PLACEHOLDER_FIELDS = {
    "one_line_thesis": "请填写一句话投资主张",
    "executive_summary": "请填写执行摘要",
    "why_now_1": "请填写 why now 1",
    "why_now_2": "请填写 why now 2",
    "why_now_3": "请填写 why now 3",
    "market_is_pricing": "请填写市场当前在交易什么",
    "variant_view": "请填写你的差异化观点",
    "business_framing": "请填写业务框架",
    "profit_structure_summary": "请填写利润结构总结",
    "new_narrative_summary": "请填写新叙事总结",
    "in_numbers_1": "请填写已进入报表的叙事1",
    "in_numbers_2": "请填写已进入报表的叙事2",
    "becoming_material_1": "请填写正在成为重要增量1",
    "becoming_material_2": "请填写正在成为重要增量2",
    "optionality_1": "请填写主要属于期权1",
    "optionality_2": "请填写主要属于期权2",
    "narrative_conclusion": "请填写叙事结论",
    "segment_design_logic": "请填写为什么这样分部",
    "valuation_router": "segment_sotp_pe / segment_sotp_ps / hybrid_sotp_pe_ps / simple_core_pe",
    "base_period": "请填写估值基期",
    "valuation_method_summary": "请填写估值方法摘要",
    "equity_value": "请填写总股权价值",
    "shares_outstanding": "请填写总股本",
    "quarterly_watch_1": "请填写季度跟踪点1",
    "quarterly_watch_2": "请填写季度跟踪点2",
    "quarterly_watch_3": "请填写季度跟踪点3",
    "quarterly_why": "请填写这些指标为什么重要",
    "bull_case": "请填写 bull 情景假设",
    "bull_tp": "请填写 bull 目标价",
    "bull_upside": "请填写 bull 空间",
    "base_case": "请填写 base 情景假设",
    "bear_case": "请填写 bear 情景假设",
    "bear_tp": "请填写 bear 目标价",
    "bear_upside": "请填写 bear 空间",
    "risk_1": "请填写风险1",
    "risk_2": "请填写风险2",
    "risk_3": "请填写风险3",
    "risk_4": "请填写风险4",
    "fragility_geo": "请填写地域集中风险判断",
    "fragility_customer": "请填写客户/渠道集中风险判断",
    "fragility_legal": "请填写诉讼/IP 风险判断",
    "fragility_regulatory": "请填写监管/政策风险判断",
    "fragility_discount": "请填写是否需要估值折价",
    "final_stance": "请填写最终观点",
    "reference_1": "请填写参考资料1",
    "reference_2": "请填写参考资料2",
    "reference_3": "请填写参考资料3",
    "reference_4": "请填写参考资料4",
    "reference_5": "请填写参考资料5",
}


def main():
    ap = argparse.ArgumentParser(description='Create a starter JSON for the report template using a live quote snapshot.')
    ap.add_argument('--ticker', required=True, help='e.g. 300124.SZ or 06656.HK')
    ap.add_argument('--output', required=True, help='Path to scaffold JSON')
    ap.add_argument('--target-price', default='', help='Optional pre-filled target price')
    ap.add_argument('--upside', default='', help='Optional pre-filled upside/downside')
    ap.add_argument('--rating', default='TBD', help='Optional rating placeholder')
    args = ap.parse_args()

    snap = a_or_hk_snapshot(args.ticker)
    price = snap.get('price')
    data = {
        'company_name': snap.get('name') or args.ticker,
        'ticker': args.ticker,
        'one_line_thesis': PLACEHOLDER_FIELDS['one_line_thesis'],
        'market': 'Hong Kong' if snap.get('market') == 'HK' else ('A-share' if snap.get('market') == 'A' else snap.get('market', 'Unknown')),
        'current_price': f"{price} {snap.get('currency', '')}" if price is not None else 'TBD',
        'target_price': args.target_price or 'TBD',
        'upside': args.upside or 'TBD',
        'rating': args.rating,
        'date': dt.date.today().isoformat(),
    }
    data.update(PLACEHOLDER_FIELDS)

    # pre-fill segments with placeholders
    for i in range(1, 5):
        data[f'segment_{i}'] = f'请填写分部{i}名称'
        data[f'segment_{i}_rev'] = 'TBD'
        data[f'segment_{i}_quality'] = 'TBD'
        data[f'segment_{i}_role'] = 'TBD'
        data[f'segment_{i}_base'] = 'TBD'
        data[f'segment_{i}_growth'] = 'TBD'
        data[f'segment_{i}_method'] = 'TBD'
        data[f'segment_{i}_multiple'] = 'TBD'
        data[f'segment_{i}_value'] = 'TBD'
        data[f'segment_{i}_multiple_why'] = 'TBD'

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(str(out))


if __name__ == '__main__':
    main()
