# Stock Analysis PDF Pipeline

<p align="center">
  <b>A complete single-stock research workflow: narrative → fundamentals → SOTP valuation → fragility audit → analyst-style PDF.</b><br/>
  <b>一套完整的单票研究 workflow：叙事 → 基本面 → SOTP 估值 → 脆弱性检测 → analyst-style PDF。</b>
</p>

<p align="center">
  <a href="#english">🇺🇸 English</a> ·
  <a href="#中文">🇨🇳 中文</a>
</p>

<p align="center">
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green.svg"></a>
  <a href="./requirements.txt"><img alt="Python 3.9+" src="https://img.shields.io/badge/python-3.9%2B-blue.svg"></a>
  <img alt="Stock Analysis" src="https://img.shields.io/badge/stock-analysis-orange.svg">
  <img alt="PDF Reports" src="https://img.shields.io/badge/pdf-reports-red.svg">
</p>

---

<a id="english"></a>
# English

## What this repo is
**Stock Analysis PDF Pipeline** is a shareable single-stock research workflow for prompts like:
- `Analyze [ticker]`
- `Give me a view on [company]`
- `Help me value [stock]`
- `Build a target price framework for [company]`

It is built for people who want something more complete than:
- narrative-only research notes,
- rigid spreadsheet valuation with no market context, or
- generic stock templates that stop before a real investment conclusion.

This repo is designed as a **complete stock valuation workflow**, not just a memo template or a multiple calculator:
- start from **deep research**
- translate the **market narrative** into real revenue/profit structure
- rebuild valuation through **SOTP / hybrid / core-PE routers**
- run a **fragility audit** before accepting the rerating story
- deliver a readable **markdown / PDF analyst note**

## Search relevance
If someone searches GitHub for terms like:
- `stock analysis`
- `stock valuation`
- `equity research pipeline`
- `SOTP valuation`
- `investment memo PDF`
- `single stock analysis`

this repo is intended to be directly relevant.

## Core value proposition
This workflow is built around **completeness**. A usable stock-research pipeline should connect the whole chain:

> **narrative → fundamentals → SOTP valuation → fragility audit → target price / rating / PDF note**

Its four core value pillars are:

1. **Narrative and fundamentals must be linked**  
   A rerating story matters only when it can be traced back to real revenue, profit-pool quality, or segment economics.

2. **Valuation should reflect business structure, not one blunt multiple**  
   Different businesses need different routers: segment SOTP, hybrid PE/PS, or a simpler core-PE approach when SOTP would be fake precision.

3. **Fragility must be part of the model, not a disclaimer at the end**  
   Geographic concentration, channel concentration, litigation/IP risk, regulatory dependence, and delivery/warranty risk should be judged explicitly and translated into discounting when necessary.

4. **The final output should read like an analyst note**  
   The end product is a clear markdown/PDF document with valuation derivation, assumptions, target price, upside/downside, and risks — not an engineering dump.

## Why this framework is complete
Many public stock-analysis repos only cover one part of the job:
- some focus on data collection
- some focus on memo writing
- some provide a valuation template only
- some stop at narrative discussion

This repo is meant to hold the full chain together:
- **Narrative layer** — what new story is the market trading?
- **Fundamental layer** — where do revenue and profit actually come from?
- **Valuation layer** — how should the company be valued segment by segment?
- **Fragility layer** — what could invalidate the rerating?
- **Delivery layer** — how do you turn the work into a readable investment document?

## What’s inside
```text
.
├── SKILL.md
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── examples/
│   └── sample-input.json
├── templates/
│   └── output-template.md
└── scripts/
    ├── quote_snapshot.py
    ├── scaffold_input.py
    ├── build_report.py
    ├── render_pdf.py
    └── run_pipeline.py
```

## Pipeline logic
1. Confirm company identity and live market snapshot  
2. Deep-research the business and segment structure  
3. Identify the new narrative  
4. Classify narrative maturity  
5. Run the fragility audit  
6. Rebuild valuation around real segment economics  
7. Generate a readable markdown/PDF note with target price, upside/downside, and rating  

## Quick start
### 1) Clone
```bash
git clone https://github.com/oierkid-crypto/stock-analysis-pdf-pipeline.git
cd stock-analysis-pdf-pipeline
```

### 2) Fetch a live quote snapshot
```bash
python3 scripts/quote_snapshot.py --ticker 300124.SZ
python3 scripts/quote_snapshot.py --ticker 06656.HK
```

### 3) Create a starter JSON scaffold
```bash
python3 scripts/scaffold_input.py --ticker 300124.SZ --output work/inovance.json
```

### 4) Fill in your research
Use `examples/sample-input.json` as reference, then complete the structured fields after doing your research.

### 5) Build markdown + PDF
```bash
python3 scripts/run_pipeline.py build \
  --input examples/sample-input.json \
  --md-output output/sample.md \
  --pdf-output output/sample.pdf
```

## Script overview
### `quote_snapshot.py`
Fetches a lightweight live snapshot for A-share and Hong Kong stocks.

### `scaffold_input.py`
Creates a starter JSON with prefilled company, ticker, date, and price fields plus placeholders for your research.

### `build_report.py`
Renders a markdown report from a reusable template and structured JSON input.

### `render_pdf.py`
Renders a dependency-light, readable PDF from markdown.

### `run_pipeline.py`
Convenience wrapper for quote / scaffold / build workflows.

## PDF philosophy
This repo defaults to a **document-style PDF**.
The goal is not perfect browser-grade typesetting — the goal is:
- clear section hierarchy
- readable typography
- simple tables
- investment-note style output
- easy sharing

## Current boundary
This is **not** a fully autonomous research agent.
It is a **research pipeline scaffold**:
- methodology
- template
- scripts
- structured workflow

You still need to do the actual research and complete the structured input.

---

<a id="中文"></a>
# 中文

## 这个仓库是干什么的
**Stock Analysis PDF Pipeline** 是一个可分享、可复用的单票研究 workflow，适用于：
- `帮我分析 XXXX`
- `分析一下 XXXX`
- `看看 XXXX 值不值得买`
- `给我做一下 XXXX 的估值`

它适合那些不满足于以下几类做法的人：
- 只讲叙事、不落到报表和估值的研究笔记
- 只会套总 PE、忽略市场重估逻辑的估值模型
- 有模板但无法导出完整投资结论的通用 stock template

这个仓库想做的不是单点工具，而是一套**完整的股票估值 workflow**：
- 从 **deep research** 出发
- 把 **市场叙事** 映射回真实收入/利润结构
- 用 **SOTP / 混合估值 / 核心 PE** 重建估值框架
- 在接受重估逻辑之前，强制做 **fragility audit**
- 最后输出高可读的 **Markdown / PDF analyst note**

## 为什么这个名字有搜索相关性
如果别人会在 GitHub 搜索这些词：
- `stock analysis`
- `stock valuation`
- `equity research pipeline`
- `investment memo pdf`
- `single stock analysis`
- `股票分析`
- `估值模板`
- `单票研究 pipeline`

这个仓库名称和首页说明都能比较直接命中这些需求。

## 核心价值主张
这套 workflow 最重要的不是某一个模板，而是**完整性**。一套真正可用的股票研究流程，应该把这条链路打通：

> **叙事 → 基本面 → SOTP 估值 → 脆弱性检测 → 目标价 / 评级 / PDF 文档**

它的四个核心价值支柱是：

1. **叙事必须和基本面打通**  
   任何重估故事，最终都要能够落回真实的收入来源、利润池质量、分部经济结构。

2. **估值必须反映业务结构，而不是只套一个总 PE**  
   不同业务需要不同 router：有的适合分部 SOTP，有的适合 PE/PS 混合估值，有的只适合核心业务 PE。

3. **脆弱性检测不是最后附带的风险提示，而是模型的一部分**  
   地域集中、渠道依赖、诉讼/IP、监管依赖、交付/质保风险，都应该明确判断是否需要折价，而不是只写成 boilerplate。

4. **最终交付物应该像 analyst note，而不是工程中间件**  
   结论必须落在清晰的 Markdown / PDF 文档里，包含假设、估值推导、目标价、upside/downside 和风险。

## 为什么说这套方案是完整的
很多公开的股票分析 repo 只覆盖其中一段：
- 有的偏数据抓取
- 有的偏 narrative memo
- 有的只给估值模板
- 有的停留在故事讨论

这套 repo 想覆盖的是完整链路：
- **叙事层** —— 市场到底在交易什么新故事？
- **基本面层** —— 收入和利润真正来自哪里？
- **估值层** —— 应该如何按分部或业务质量重建估值？
- **脆弱性层** —— 什么因素会让重估失效？
- **交付层** —— 如何把研究变成可读、可分享的投资文档？

## 仓库内容
```text
.
├── SKILL.md
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── examples/
│   └── sample-input.json
├── templates/
│   └── output-template.md
└── scripts/
    ├── quote_snapshot.py
    ├── scaffold_input.py
    ├── build_report.py
    ├── render_pdf.py
    └── run_pipeline.py
```

## 这套 pipeline 的逻辑
1. 确认公司身份和实时行情快照  
2. 深度研究业务本质和分部结构  
3. 找出新的估值叙事  
4. 判断叙事成熟度  
5. 做脆弱性审计  
6. 按真实分部经济结构重建估值  
7. 输出带目标价、upside/downside、rating 的 Markdown / PDF 文档  

## 快速开始
### 1）拉取仓库
```bash
git clone https://github.com/oierkid-crypto/stock-analysis-pdf-pipeline.git
cd stock-analysis-pdf-pipeline
```

### 2）抓实时行情快照
```bash
python3 scripts/quote_snapshot.py --ticker 300124.SZ
python3 scripts/quote_snapshot.py --ticker 06656.HK
```

### 3）生成研究输入骨架
```bash
python3 scripts/scaffold_input.py --ticker 300124.SZ --output work/inovance.json
```

### 4）补全研究内容
参考 `examples/sample-input.json`，把你的研究结果填到结构化 JSON 里。

### 5）生成 markdown + PDF
```bash
python3 scripts/run_pipeline.py build \
  --input examples/sample-input.json \
  --md-output output/sample.md \
  --pdf-output output/sample.pdf
```

## 脚本说明
### `quote_snapshot.py`
抓 A 股 / 港股的轻量实时行情快照。

### `scaffold_input.py`
生成一个半自动化输入 JSON，预填公司、ticker、日期、价格等信息，并保留研究占位符。

### `build_report.py`
根据结构化 JSON 和模板生成 markdown 报告。

### `render_pdf.py`
把 markdown 渲染成一个轻依赖、可读性较高的 PDF 文档。

### `run_pipeline.py`
为 quote / scaffold / build 提供一体化命令入口。

## PDF 输出理念
这个仓库默认输出的是**文档式 PDF**，而不是工具输出的原始 dump。

目标是：
- 标题层级清楚  
- 文档可读  
- 表格简洁  
- 适合分享  
- 像一份投资 memo，而不是命令行日志  

## 当前边界
这**不是**一个全自动研究代理仓库。  
它更准确地说是一个 **研究 pipeline 脚手架**：
- 方法论  
- 模板  
- 脚本  
- 结构化工作流  

你仍然需要自己完成真实 research，并把结果填进结构化 JSON。

---

## License / 许可证
MIT
