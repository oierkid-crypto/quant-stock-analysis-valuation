---
name: gs-single-stock-pipeline-v2
description: Institutional single-stock research methodology. Starts with deep research, translates narrative into fundamentals, rebuilds value through SOTP/hybrid valuation, and runs fragility audit before the final rating.
version: 2.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [equity-research, gs-style, valuation, stocks, a-share, hong-kong, us, pipeline-v2]
---

# GS Single-Stock Pipeline V2

## When to load
Load this skill whenever the user asks to analyze a specific stock in a practical investment-research style, especially with prompts like:
- `帮我分析 XXX`
- `分析一下 XXX`
- `看看 XXX 值不值得买`
- `给我做一下 XXX 的估值`
- `Analyze [ticker/company]`
- `Give me a view on [stock]`

This skill is designed for **single-name deep dives** and is **shareable**.

## Core principle
Always follow this order:
1. **Deep research first**
2. **Check whether there is a new narrative**
3. **Map the narrative back to real revenue / profit structure**
4. **Run fragility audit**
5. **Choose the right valuation router**
6. **Show analyst-style derivation and explicit upside/downside**

## V2 workflow

### Step 1: Confirm identity and live market snapshot
Confirm:
- full company identity
- market / ticker
- current live price
- rough market cap
- current PE / PB / PS when available

Use `scripts/quote_snapshot.py` when helpful.

### Step 2: Deep research the business first
Answer:
- what does the company really sell?
- where does revenue come from?
- where does profit come from?
- what does the market think the company is?
- what might the market be underestimating or overestimating?

Minimum outputs:
- core business structure
- revenue buckets / product buckets / segment buckets
- profit-quality differences across segments
- evidence-backed notes on what is mature, what is scaling, and what is still only optionality

### Step 3: Identify whether a new narrative exists
Classify every narrative into one of three maturity levels:
1. **already in the financials**
2. **starting to become material**
3. **still mostly optionality**

Only the first two deserve meaningful valuation weight.

### Step 3.5: Run a mandatory fragility audit before valuation
Check at minimum:
1. **geographic concentration**
2. **customer / channel concentration**
3. **supply-chain dependency**
4. **litigation / IP risk**
5. **regulatory / policy risk**
6. **inventory / delivery / warranty risk**

For each fragility, explicitly decide whether it:
- is not material
- requires disclosure but no valuation change
- requires a valuation discount / lower multiple / scenario penalty

### Step 4: Rebuild the valuation structure around real economics
Do not force one multiple on mixed-quality businesses.
Reconstruct valuation around real revenue/profit structure.

Possible segment patterns:
- mature core business
- second growth curve
- stable cash-flow business
- platform/software/service attach layer
- optionality / emerging business

### Step 5: Choose the right valuation router
Available routers:
- `segment_sotp_pe`
- `segment_sotp_ps`
- `hybrid_sotp_pe_ps`
- `simple_core_pe`

### Step 6: Produce a document-style final output
Generate markdown from `templates/output-template.md` and, when possible, render a readable PDF.

Use:
- `scripts/build_report.py`
- `scripts/render_pdf.py`

## Output requirements
The final note must include:
1. Executive conclusion
2. What the company really is
3. The new narrative
4. GS-style valuation derivation
5. Risks
6. Fragility audit
7. Final stance

## PDF-first publishing standard
Default to a **document-style PDF report** when the user wants a high-readability deliverable.

Preferred workflow:
1. generate markdown using `templates/output-template.md`
2. render PDF with `scripts/render_pdf.py`
3. preserve readable typography, whitespace, hierarchy, and simple tables

## Linked files
- template: `templates/output-template.md`
- scripts:
  - `scripts/quote_snapshot.py`
  - `scripts/build_report.py`
  - `scripts/render_pdf.py`

## Trigger memory
When a user says **“帮我分析 XXXX”**, default to this V2 workflow unless they explicitly ask for a shorter take.
