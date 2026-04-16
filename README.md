# Quant Stock Analysis Valuation

<p align="center">
  <b>Goldman Sachs-style institutional equity research methodology for single-stock work: narrative → fundamentals → SOTP valuation → fragility audit → analyst note.</b><br/>
  <b>更像机构研究方法论仓库，而不是工具仓库：叙事 → 基本面 → SOTP 估值 → 脆弱性审计 → analyst note。</b>
</p>

<p align="center">
  <a href="#english">🇺🇸 English</a> ·
  <a href="#中文">🇨🇳 中文</a>
</p>

<p align="center">
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green.svg"></a>
  <a href="./requirements.txt"><img alt="Python 3.9+" src="https://img.shields.io/badge/python-3.9%2B-blue.svg"></a>
  <img alt="Institutional Equity Research" src="https://img.shields.io/badge/institutional-equity_research-1f3b5c.svg">
  <img alt="SOTP Valuation" src="https://img.shields.io/badge/SOTP-valuation-6b46c1.svg">
</p>

> **Positioning note**  
> This repository is inspired by institutional sell-side research structure and Goldman Sachs-style deliverable discipline. It is **not** affiliated with, endorsed by, or published by Goldman Sachs.

---

<a id="english"></a>
# English

## What this repository is
**Quant Stock Analysis Valuation** is a bilingual methodology repo for people who want single-stock work to read like **institutional equity research**, not like a loose memo, a retail blog post, or a spreadsheet with a target multiple pasted on top.

It is designed for workflows such as:
- `Analyze [ticker]`
- `Give me an institutional view on [company]`
- `Build a target price framework for [company]`
- `Re-underwrite the narrative for [stock]`

The ambition here is not “yet another stock template.”  
The ambition is to make the research chain coherent from first principle to final conclusion.

## Positioning
This repository should be read as an **institutional research methodology repository**.

The intended keywords are:
- `institutional equity research`
- `equity research methodology`
- `SOTP valuation model`
- `single stock valuation framework`
- `Goldman Sachs style research`
- `narrative to fundamentals`
- `fragility audit`

## Core idea
A serious research process should connect five layers into one chain:

> **market narrative → fundamental structure → SOTP / hybrid valuation → fragility audit → analyst conclusion**

If any one of these layers is missing, the conclusion is weaker than it looks.

## Why this framework exists
A lot of public stock-analysis repos stop too early.

Some stop at:
- data collection,
- memo writing,
- target multiple templates, or
- thematic commentary.

Institutional work requires more.
It requires a process that can explain:
- **what the market thinks the company is**,
- **what the company economically is**,
- **what part of the story is actually new**,
- **how that story should enter valuation**,
- **what fragility could invalidate the rerating**, and
- **what target price / rating conclusion follows from that chain**.

## Methodology pillars
### 1. Narrative must be translated into economics
A rerating story has no analytical value unless it can be mapped back to:
- revenue pools,
- profit-pool quality,
- segment economics,
- business mix, or
- capital allocation logic.

### 2. Valuation should reflect business structure
A company with mixed-quality businesses should not be forced into one blunt multiple.
This framework prefers:
- **segment SOTP** when multiple businesses deserve different treatments,
- **hybrid PE / PS** when one segment is profit mature and another is still scaling,
- **simple core PE** only when additional complexity would be false precision.

### 3. Fragility is part of valuation, not a disclaimer
This methodology treats fragility as a valuation input.
That includes:
- geographic concentration,
- channel concentration,
- litigation / IP exposure,
- policy dependence,
- supply-chain bottlenecks,
- inventory / delivery / warranty risk.

The question is not whether risk exists.  
The question is whether the risk deserves **disclosure only**, a **multiple haircut**, or a **scenario discount**.

### 4. The final output should read like an analyst note
The objective is a readable conclusion with:
- company framing,
- variant view,
- valuation derivation,
- target price,
- upside / downside,
- thesis risks,
- evidence references.

## Goldman Sachs-style discipline, interpreted practically
In this repository, “Goldman Sachs-style” means:
- debate framing before conclusion,
- valuation as a structured bridge rather than a slogan,
- segment logic instead of theme-chasing,
- explicit assumptions,
- explicit downside / variant view,
- institutional presentation discipline.

It does **not** mean imitation of any firm's proprietary model.
It means adopting the standard of clarity and rigor expected from institutional sell-side work.

## SOTP valuation model, in plain English
This framework emphasizes **Sum-of-the-Parts (SOTP)** when a company is really several economic engines under one ticker.

Instead of asking only:
- “What PE should the stock trade on?”

it asks:
- What are the real business segments?
- Which segments are already profit-bearing?
- Which segments are still in revenue scale-up?
- Which segments deserve PE vs PS?
- Which narratives are real and which are still optionality?
- What is the implied equity value when those pieces are valued appropriately?

That is the core difference between a superficial valuation memo and an institutional underwriting framework.

## Repository scope
This repository includes a reusable structure for:
- market snapshot
- business decomposition
- narrative classification
- fragility audit
- valuation routing
- final analyst-style document generation

It is a **methodology + template + lightweight script** repository.
It is not a fully autonomous research engine.

## Quick start
### Clone
```bash
git clone https://github.com/oierkid-crypto/quant-stock-analysis-valuation.git
cd quant-stock-analysis-valuation
```

### Run a quote snapshot
```bash
python3 scripts/quote_snapshot.py --ticker 300124.SZ
python3 scripts/quote_snapshot.py --ticker 06656.HK
```

### Scaffold a research input file
```bash
python3 scripts/scaffold_input.py --ticker 300124.SZ --output work/inovance.json
```

### Build the final research document
Use the `build` command to turn structured input into the final analyst note.

## What is inside
The repository is organized around four layers:
- **methodology** — the research logic and valuation discipline
- **template** — the final analyst-style structure
- **scripts** — lightweight helpers for quote snapshot, scaffolding, report build, and document rendering
- **examples** — a sample structured input for onboarding

## Current boundary
This repository does **not** replace actual research judgment.
You still need to:
- read source materials,
- decide what the real narrative is,
- judge whether it is already in the numbers,
- assign valuation logic thoughtfully.

The point of the repository is to make that work **institutional, repeatable, and readable**.

---

<a id="中文"></a>
# 中文

## 这个仓库是什么
**Quant Stock Analysis Valuation** 是一个双语的**机构研究方法论仓库**。它不是散装 memo，不是零售风格的 stock blog，也不是套一个 target multiple 就结束的估值模板。

它适用于这类工作流：
- `帮我分析 [公司 / ticker]`
- `给我一个机构视角的结论`
- `帮我重做这家公司目标价框架`
- `重新 underwrite 这只股票的叙事`

这个仓库想做的，不是“又一个股票模板”。  
它想做的是：把单票研究从第一性原理到最终结论，真正连成一条完整链路。

## 定位
这个仓库应该被理解成一个**机构研究方法论仓库**，而不是一个展示工具或文档渲染仓库。

它的关键词应该是：
- `institutional equity research`
- `equity research methodology`
- `SOTP valuation model`
- `single stock valuation framework`
- `Goldman Sachs style research`
- `narrative to fundamentals`
- `fragility audit`
- `机构研究方法论`
- `分部估值`
- `单票估值框架`

## 核心思想
一套像样的研究流程，应该把五层逻辑真正打通：

> **市场叙事 → 基本面结构 → SOTP / 混合估值 → 脆弱性审计 → analyst 结论**

这五层里缺任何一层，最后的结论都会看起来比它实际上更强。

## 为什么这套框架存在
很多公开的股票分析 repo，停得太早。

有的停在：
- 数据抓取，
- 研究 memo，
- target multiple 模板，或
- 主题式评论。

但机构研究需要更多。  
它需要一套流程，能够回答：
- **市场以为这家公司是什么**，
- **这家公司在经济意义上到底是什么**，
- **什么部分才是真正的新叙事**，
- **这个叙事应该如何进入估值**，
- **什么脆弱性会让这次重估失败**，
- **沿着这条链路，最后应该落到什么目标价 / 评级**。

## 方法论支柱
### 1. 叙事必须翻译成经济结构
任何重估故事，如果不能映射回：
- 收入池，
- 利润池质量，
- 分部经济结构，
- 业务组合，或
- 资本配置逻辑，

它的分析价值就非常有限。

### 2. 估值必须反映业务结构
一家公司如果本质上由多个质量不同的业务组成，就不应该被粗暴地塞进一个总 PE。

这套框架优先使用：
- **分部 SOTP**：当多个业务应当被区别对待时
- **PE / PS 混合估值**：当一部分业务已成熟盈利，另一部分仍处于放量阶段时
- **核心业务 PE**：只有在继续复杂化会变成假精确时才使用

### 3. 脆弱性不是附录里的风险提示，而是估值的一部分
这套方法把脆弱性直接视为估值输入项。包括：
- 地域集中度，
- 渠道集中度，
- 诉讼 / IP 暴露，
- 政策依赖，
- 供应链瓶颈，
- 库存 / 交付 / 质保风险。

关键不是“有没有风险”。  
关键是这些风险到底只需要**披露**，还是应该对应**multiple haircut** 或 **scenario discount**。

### 4. 最终交付应该像 analyst note
最终目标不是工程中间件，而是一份可读的研究结论，里面应该有：
- 公司定位，
- variant view，
- 估值推导，
- 目标价，
- upside / downside，
- 核心风险，
- 证据引用。

## 如何理解这里说的 Goldman Sachs-style
在这个仓库里，所谓 **Goldman Sachs-style**，指的是一种机构 sell-side 纪律：
- 先定义 debate framing，再给结论
- 估值是结构化推导，不是口号
- 先讲分部逻辑，不追逐主题热词
- 假设必须显式写出来
- downside / variant view 必须清楚
- 呈现方式要有机构研究的节制感

它**不**代表模仿任何机构的 proprietary model。  
它代表的是：用机构卖方研究应有的清晰度和严谨度来组织研究。

## SOTP 估值模型，直白地说是什么
这套框架强调 **SOTP（Sum-of-the-Parts）**，因为很多公司在一个 ticker 下面，其实装着几个不同的经济引擎。

所以问题不只是：
- “这只股票应该给多少 PE？”

而是：
- 真实的业务分部是什么？
- 哪些分部已经是利润池？
- 哪些分部还在收入放量？
- 哪些分部该用 PE，哪些该用 PS？
- 哪些叙事已经成立，哪些还只是 optionality？
- 当这些部分被合理估值后，隐含股权价值到底是多少？

这就是表面估值 memo 和机构式 underwrite 框架的区别。

## 仓库边界
这个仓库提供的是一套可复用结构，用于承载：
- 市场快照
- 业务拆解
- 叙事分类
- 脆弱性审计
- 估值路由
- 最终 analyst-style 文档生成

它本质上是一个 **methodology + template + lightweight script** 仓库。  
它不是一个全自动研究引擎。

## 快速开始
### 拉取仓库
```bash
git clone https://github.com/oierkid-crypto/quant-stock-analysis-valuation.git
cd quant-stock-analysis-valuation
```

### 获取行情快照
```bash
python3 scripts/quote_snapshot.py --ticker 300124.SZ
python3 scripts/quote_snapshot.py --ticker 06656.HK
```

### 生成研究输入骨架
```bash
python3 scripts/scaffold_input.py --ticker 300124.SZ --output work/inovance.json
```

### 生成最终研究文档
使用 `build` 命令把结构化输入转成最终 analyst-style 研究文档。

## 仓库结构
这个仓库实际分成四层：
- **methodology** —— 研究逻辑和估值纪律
- **template** —— 最终 analyst-style 结构
- **scripts** —— 行情抓取、脚手架生成、报告生成、文档渲染等轻量辅助脚本
- **examples** —— onboarding 用的样例输入

## 当前边界
这个仓库并不能替代真实的研究判断。  
你仍然需要：
- 阅读源材料
- 判断真正的新叙事是什么
- 判断它是否已经进入数字
- 谨慎分配估值逻辑

这个仓库的作用，是把这些工作变得更**机构化、可复用、可读**。

---

## License / 许可证
MIT
