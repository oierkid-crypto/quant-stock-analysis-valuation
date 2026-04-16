# Stock Analysis PDF Pipeline

<p align="center">
  <b>Turn single-stock research into clear markdown + PDF investment notes.</b><br/>
  <b>把单票研究流程化，并输出清晰、可分享的 Markdown + PDF 投资文档。</b>
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
- `帮我分析 XXXX`
- `Analyze XXXX`
- `Give me a view on [ticker]`
- `Help me value [company]`

It is built for people who want a better workflow than:
- vague narrative memos with weak valuation discipline, or
- rigid spreadsheets that ignore what the market is actually re-rating.

This repo gives you a practical middle ground:
- deep research first
- narrative-aware valuation
- fragility audit before final rating
- readable markdown and PDF output

## Why people may find this useful
If you search GitHub for terms like:
- `stock analysis`
- `equity research pipeline`
- `stock valuation template`
- `SOTP valuation`
- `investment memo PDF`
- `single stock analysis`

this repo is designed to be directly relevant.

## Core selling points
- **Deep research first** — understand the business before touching valuation.
- **Narrative-aware valuation** — identify what is actually new, and whether it is already in the P&L or still optionality.
- **Fragility audit built in** — explicitly check concentration risk, legal/IP risk, regulatory risk, channel risk, and whether they deserve a valuation discount.
- **GS-style document output** — produce readable markdown and PDF notes instead of raw tool dumps.
- **Lightweight and shareable** — method + template + scripts, without depending on a private repo or hidden context.

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
1. Confirm identity and live market snapshot  
2. Deep research the business  
3. Identify the new narrative  
4. Classify narrative maturity  
5. Run fragility audit  
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
Creates a starter JSON with prefilled company / ticker / date / price fields and placeholders for your research.

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

## Limitations
This is **not** a fully autonomous research agent.
It is a **research pipeline scaffold**:
- method
- template
- scripts
- structured workflow

You still need to do the actual research and complete the structured input.

---

<a id="中文"></a>
# 中文

## 这个仓库是干什么的
**Stock Analysis PDF Pipeline** 是一个可分享、可复用的单票研究工作流，适用于：
- `帮我分析 XXXX`
- `分析一下 XXXX`
- `看看 XXXX 值不值得买`
- `给我做一下 XXXX 的估值`

它适合那些不满足于以下两种做法的人：
- 只会讲故事、估值纪律很弱的研究流程
- 只会套模型、却忽略市场如何重估新叙事的流程

这个仓库提供的是一个更实用的中间方案：
- 先做深度研究
- 再识别新叙事
- 再做叙事感知型估值
- 在最终结论前强制做脆弱性审计
- 最后输出高可读的 Markdown / PDF 投资文档

## 为什么这个名字更利于搜索
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

## 核心卖点
- **先做深度研究** —— 在估值之前，先真正理解公司。  
- **叙事感知型估值** —— 识别什么是新叙事，以及它是否已经进入报表。  
- **内置脆弱性审计** —— 强制检查地域集中、诉讼/IP、渠道依赖、监管风险，并决定是否需要估值折价。  
- **GS 风格文档输出** —— 输出像 analyst memo 一样可读的 markdown / PDF，而不是工程 dump。  
- **轻量可分享** —— 方法论 + 模板 + 脚本，不依赖私有仓库或隐藏上下文。  

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
2. 深度研究业务本质  
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
