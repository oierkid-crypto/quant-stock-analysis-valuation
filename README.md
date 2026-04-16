# GS-Style Stock Pipeline / GS 风格单票研究 Pipeline

> A shareable **single-stock research pipeline** for prompts like **"帮我分析 XXXX"**.  
> 一个可分享、可复用的 **单票研究 pipeline**，适用于 **“帮我分析 XXXX”** 这类需求。

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](./requirements.txt)

---

## Why this repo exists / 这个仓库为什么存在

Most stock-analysis workflows fail in one of two ways:
1. they become shallow narrative memos with weak valuation discipline;
2. or they become rigid models that ignore how markets actually price new narratives.

This repo is built to solve both problems.

大多数股票分析流程会在两个地方失真：
1. 只会讲故事，估值纪律很弱；
2. 只会套模型，却忽略市场真正如何重估“新叙事”。

这个仓库就是为了解决这两个问题而设计的。

---

## Core selling points / 核心卖点

### English
- **Deep research first** — understand the business before touching valuation.
- **Narrative-aware valuation** — identify what is truly new, and whether it is already in the P&L or still optionality.
- **GS-style analyst output** — produce readable, investment-grade markdown/PDF notes.
- **Fragility audit built-in** — check geographic concentration, channel concentration, legal/IP risk, regulatory risk, and whether they deserve a valuation discount.
- **Shareable and lightweight** — works as a method + template + script toolkit, without requiring a private repo or hidden context.

### 中文
- **先做深度研究** —— 在估值之前，先真正理解公司。  
- **叙事感知型估值** —— 识别什么是新叙事，以及它究竟已经进入报表，还是仍属期权。  
- **GS 风格输出** —— 生成可读性高、接近 sell-side analyst note 的 markdown / PDF 文档。  
- **内置脆弱性审计** —— 强制检查地域集中、渠道集中、诉讼/IP、监管等是否需要估值折价。  
- **轻量且可分享** —— 不依赖私有仓库和隐藏上下文，可以直接分享给别人使用。  

---

## What this repo includes / 仓库包含什么

```text
.
├── SKILL.md                         # Shareable pipeline definition / 可分享 skill 定义
├── README.md                        # Bilingual documentation / 双语说明
├── LICENSE
├── .gitignore
├── requirements.txt
├── examples/
│   └── sample-input.json            # Sample structured input / 示例输入
├── templates/
│   └── output-template.md           # Reusable report template / 可复用输出模板
└── scripts/
    ├── __init__.py
    ├── quote_snapshot.py            # Lightweight A/HK quote snapshot / 轻量行情快照
    ├── scaffold_input.py            # Semi-auto starter JSON scaffold / 半自动输入骨架
    ├── build_report.py              # Render markdown from template / 生成 markdown 报告
    ├── render_pdf.py                # Render a clean PDF / 渲染 PDF
    └── run_pipeline.py              # Convenience runner / 一体化命令入口
```

---

## The pipeline logic / 这套 pipeline 的逻辑

### English
1. Confirm identity and live market snapshot  
2. Deep research the business  
3. Identify the new narrative  
4. Classify narrative maturity (in numbers / becoming material / optionality)  
5. Run fragility audit  
6. Rebuild valuation around real segment economics  
7. Generate a readable final note with target price / upside / rating  

### 中文
1. 确认公司身份与实时行情快照  
2. 深度研究业务本质  
3. 找出新的估值叙事  
4. 判断叙事成熟度（已入表 / 正在变重要 / 仍属期权）  
5. 执行脆弱性审计  
6. 按真实分部经济结构重建估值  
7. 生成带目标价 / upside / rating 的高可读文档  

---

## Fragility Audit / 脆弱性审计

This repo explicitly forces a **fragility audit** before final valuation.

Before you trust a beautiful narrative, ask:
- Is revenue overly concentrated in one region?
- Is the company dependent on a small number of customers or channels?
- Is there litigation / IP risk?
- Are there regulatory / subsidy / tariff risks?
- Does any of this require a multiple haircut?

本仓库特别强调：**在最终估值前，必须做脆弱性审计。**

在你相信一个漂亮叙事之前，必须先问：
- 收入是否过度集中于某一区域？
- 是否依赖少数客户/渠道？
- 是否存在诉讼/IP 风险？
- 是否受监管/补贴/关税高度影响？
- 这些风险是否需要估值折价？

---

## Quick start / 快速开始

### 1) Clone / 拉取仓库
```bash
git clone https://github.com/oierkid-crypto/gs-style-stock-pipeline.git
cd gs-style-stock-pipeline
```

### 2) Fetch a quote snapshot / 抓行情快照
```bash
python3 scripts/quote_snapshot.py --ticker 300124.SZ
python3 scripts/quote_snapshot.py --ticker 06656.HK
```

### 3) Create a starter JSON scaffold / 生成研究输入骨架
```bash
python3 scripts/scaffold_input.py --ticker 300124.SZ --output work/inovance.json
```

Or use the convenience runner / 或使用一体化命令：
```bash
python3 scripts/run_pipeline.py scaffold --ticker 300124.SZ --output work/inovance.json
```

### 4) Fill the JSON after research / 做完研究后填写 JSON
Use `examples/sample-input.json` as reference.  
以 `examples/sample-input.json` 为参考，填入你的研究结果。

### 5) Build markdown report / 生成 markdown 报告
```bash
python3 scripts/build_report.py \
  --input work/inovance.json \
  --template templates/output-template.md \
  --output output/inovance.md
```

Or / 或：
```bash
python3 scripts/run_pipeline.py build \
  --input work/inovance.json \
  --md-output output/inovance.md \
  --pdf-output output/inovance.pdf
```

### 6) Render PDF / 渲染 PDF
```bash
python3 scripts/render_pdf.py \
  --input output/inovance.md \
  --output output/inovance.pdf
```

---

## What the scripts do / 脚本作用说明

### `quote_snapshot.py`
Fetches a lightweight live quote snapshot for A-share and Hong Kong stocks.

为 A 股和港股抓取轻量级实时行情快照。

### `scaffold_input.py`
Creates a starter JSON with prefilled company/ticker/date/price fields and placeholders for the analyst to complete.

生成一个半自动化输入 JSON，预填公司、ticker、日期、价格等字段，并保留研究占位符。

### `build_report.py`
Renders a markdown report from the JSON input and reusable template.

根据结构化 JSON 和模板生成 markdown 报告。

### `render_pdf.py`
Renders a dependency-light, readable PDF report from markdown.

将 markdown 渲染成一个轻依赖、可读性较高的 PDF 报告。

### `run_pipeline.py`
A convenience wrapper for scaffold / quote / build.

对 scaffold / quote / build 提供一体化命令入口。

---

## PDF philosophy / PDF 输出理念

This repo defaults to a **document-style PDF**, not a raw tool dump.

Goals:
- readable like an analyst memo
- clean hierarchy
- clear cover metadata
- simple tables
- good whitespace

本仓库默认输出的是 **文档式 PDF**，而不是工具输出的原始 dump。

目标是：
- 像 analyst memo 一样可读  
- 标题层级清楚  
- 封面信息清晰  
- 表格简洁  
- 留白合理  

---

## Search-friendly keywords / 便于搜索的关键词

If people search GitHub for topics like:
- gs style stock research
- equity research pipeline
- stock valuation template
- single stock analysis
- SOTP valuation
- 股票分析模板
- 单票研究 pipeline
- GS 风格估值

this repo is intended to be relevant.

如果大家在 GitHub 搜索以下方向：
- GS 风格股票研究
- 股票估值 pipeline
- 单票分析模板
- SOTP 估值
- equity research pipeline

这个 repo 的定位就是服务这些需求。

---

## Limitations / 当前边界

### English
This is **not** a fully autonomous “research agent” repo.
It is a **research pipeline scaffold**:
- method
- template
- scripts
- structured workflow

You still need to perform real research and fill the structured input.

### 中文
这**不是**一个全自动“研究代理”仓库。  
它更准确地说是一个 **研究 pipeline 脚手架**：
- 方法论  
- 模板  
- 脚本  
- 结构化流程  

你仍然需要自己完成真实 research，并填入结构化输入。

---

## Recommended use cases / 推荐使用场景

- single-stock deep dive / 单票深度研究
- PM-style memo / PM 风格备忘录
- GS-style valuation note / GS 风格估值说明
- investment committee prep / 投委会准备材料
- shareable stock analysis workflow / 可分享的股票研究工作流

---

## License / 许可证
MIT
