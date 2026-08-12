# Token-Factory / AI-Factory Scenario Workbook
**Release Asset #10 — "Why Are They Spending Trillions on AI?" (Valto Loikkanen, CC BY 4.0)**
**Status: educational / non-advice.** All figures below are either cited facts, attributed statements, transparent derivations from those, or clearly-flagged scenario assumptions. Nothing here is investment, legal, tax, procurement, or policy advice, and no scenario model is a forecast or recommendation — every input is editable and every result is only as good as the inputs you choose.

**Evidence-class legend** (used inline throughout): **[FACT]** = Observed Fact · **[ATTR]** = Attributed Statement · **[CALC]** = Derived Calculation (formula always shown) · **[ASSUMPTION]** = Scenario Assumption (editable, not a market figure) · **[INTERP]** = Interpretation.

**Currency note:** this workbook uses a **global USD baseline**, except Section 1, which reconciles two **EUR-denominated** figures from the author's own published cooperative model — EUR is kept there because that is the currency of the primary sources being reconciled.

---

## 1. FIRST: Reconciling the €42 vs €19.50–23 per-member/month cooperative figures

Two figures exist for a similarly-sized (~50-member, ~10-machine) AI compute cooperative:

- **€42/member/month** — the author's own published figure for a 50-member cooperative, stated in "So, the majority agrees: the time for digital sovereignty has come, now what?" (LinkedIn, published 2026-08-05). This is **[FACT]**: the article states verbatim "50 members: approximately €42 per member/month" (alongside €105 at 20 members and €21 at 100 members), independently confirmed against the live article on 2026-08-12.
- **~€19.50–23/member/month** — a later, more detailed recomputation for a 50-member/10-machine cooperative built explicitly around NVIDIA DGX Spark unit economics (10 units × current $4,699 price ≈ $46,990 capital; 5yr@8% financing ≈ $11,770/yr; electricity ≈ $2,000–4,000/yr; total ≈ $14,000–15,770/yr **before admin/networking**). This is **[CALC]**, carried forward from the background research thread rather than re-derived from scratch here, per this task's brief.

**The published article does not show its own underlying formula** — it states only the three output tiers (20/50/100 members), with no visible per-machine cost, utilization, financing term, or electricity price. That means a full line-by-line audit of the €42 figure is not possible from public material; the reconciliation below is therefore an **[INTERP]**-level exercise in identifying *plausible* differing assumptions, not a proof that any one of them is the actual cause.

Five categories plausibly explain most of the gap:

1. **Hardware/cost assumption.** The €42 figure may assume a costlier or differently-sized machine (or more machines, or a margin buffer per machine) than 10× DGX Spark at $4,699. Any higher per-unit capital figure raises the per-member cost roughly proportionally.
2. **Utilization rate.** The DGX Spark recomputation assumes near-continuous (~70%+) utilization at full throughput. A more conservative utilization assumption in the earlier published figure (e.g., accounting for downtime, contention among 50 members sharing 10 machines, or scheduling overhead) would raise the effective cost per member without changing hardware cost at all.
3. **Financing terms.** Different interest rate, term length, or a cash-purchase (no financing) assumption changes annual capital cost materially — the recomputation's 5yr@8% annuity factor (≈3.99) is one specific, editable choice among many plausible ones.
4. **Electricity price.** The recomputation uses an illustrative electricity price; a higher European retail electricity assumption (commonly €0.25–0.35/kWh vs. the ~$0.20/kWh used in the recomputation) would raise the electricity line, though this alone is a small share of total cost at DGX-Spark power levels.
5. **Overhead/admin inclusion — most likely single largest factor.** The recomputation is explicitly labeled "before admin/networking" — i.e., it excludes cooperative governance/legal setup, shared networking/switch gear, redundancy/spare-capacity margin, support labor, insurance, and software/subscription costs. The published €42 figure may simply be a more complete, real-world all-in number that folds in exactly these excluded categories.

**Reconciliation table (illustrative attribution of the gap, not an audited breakdown):**

| Assumption category | Recomputation (~€19.50–23/member/mo) | Plausible published-figure difference | Evidence class |
|---|---|---|---|
| Hardware/unit cost | 10× DGX Spark @ $4,699 = ~$46,990 capital | Possibly higher per-unit cost or more units assumed | ASSUMPTION (unverifiable which the published figure used) |
| Utilization | Near-continuous, ~70%+ | Possibly lower effective utilization (shared contention, downtime) | ASSUMPTION |
| Financing terms | 5yr @ 8% annuity | Possibly shorter term, higher rate, or cash purchase | ASSUMPTION |
| Electricity price | ~$0.20/kWh illustrative | Possibly higher EU retail rate (~€0.25–0.35/kWh) | ASSUMPTION |
| Admin/overhead/networking | **Explicitly excluded** | Likely included in published figure (governance, networking, support, redundancy, software) | INTERP |

**Formula underlying the recomputation range:** (financed hardware $/yr + electricity $/yr) ÷ 50 members ÷ 12 months = $19.50–23/member/month, using the inputs above; total annual cost of ~$14,000–15,770 ÷ 50 ÷ 12 ≈ $23–26, converging toward the lower end of the quoted €19.50–23 band once currency and rounding are allowed for.

**Bottom line:** the two figures are not necessarily in conflict — they most plausibly describe two different scopes (a narrower "machine + financing + power only" cost vs. a broader "all-in cooperative" cost), not two contradictory measurements of the same thing. This workbook does not privilege one number over the other; both are carried forward, labeled, and the reader should treat the true all-in cost for any real cooperative as falling somewhere in or above this €19.50–42 band depending on which of the five categories above it actually includes.

---

## 2. Methodology note: "how not to model this" — keep owned production and retail pricing separate

**This is a self-correction, preserved deliberately rather than smoothed over.** An earlier pass in this project's own research thread mistakenly priced a self-owned compute facility using retail frontier-lab API prices (OpenAI/Anthropic/Google $/M-token rates) as if those were a cost basis — they are not. Retail API prices are a **finished, marked-up, proprietary-model product price**; they include the lab's own margin, R&D amortization, and business-model choices, and say nothing about what it costs to run open-weight inference on owned or rented hardware.

The corrected framing, used consistently throughout this workbook:

- **Owned-production cost** = electricity + hardware (amortized or financed) + facility/operations, running **open-weight models** (e.g., Qwen, DeepSeek, Kimi) on owned or cooperative hardware. This is the "generate your own power" side.
- **Retail API pricing** = what OpenAI, Anthropic, and Google charge for access to their own proprietary models. This is the "buy from the grid" side — a **comparison benchmark only**, never a substitute for the owned-production cost calculation.

The two numbers can legitimately differ by 1–2 orders of magnitude in either direction depending on utilization, model choice, and what's included in "cost" — that gap is the point of keeping them separate, not an error to reconcile away. Every table below is labeled **OWNED PRODUCTION** or **RETAIL BENCHMARK** so the two are never collapsed into one column.

**Boundary reminder:** none of the figures below constitute a recommendation to build, buy, or avoid any specific compute configuration — they are editable illustrations for understanding cost structure.

---

## 3. Required economic-layer separation (reference only — established in earlier release-asset workbooks, not re-derived here)

| Layer | What it captures | Where it's addressed in this workbook |
|---|---|---|
| Raw energy cost | $/kWh at the meter | Sections 4, 5 |
| Hardware-amortized production cost | capex ÷ expected life, no financing | Section 4 (reference) |
| Financed asset cost | capex + interest, per financing term | Section 4 (financing-term sensitivity) |
| Full operating infrastructure cost | + facility power, cooling, networking | Section 4 (reference) |
| Capacity/utilization cost | above cost ÷ actual (not max) utilization | Section 4 |
| Token production cost | $/M tokens at the owned facility | Section 4 |
| Workload/AI-working-capacity cost | $/M tokens translated into $/agent-hour | Section 6 |
| Outcome and value | NOT mechanically determined by the above | Not modeled numerically — see boundary note, Section 7 |

---

## 4. Owned-production cost tiers (referencing, not re-deriving, earlier workbook figures)

**Boundary note for this section:** these are illustrative scenario builds, not a recommendation to purchase any specific hardware tier, and not a market forecast.

| Tier | Capital (ASSUMPTION/FACT mix) | Financing (5yr@8%) | Electricity | Owned-production cost | Evidence class |
|---|---|---|---|---|---|
| Home factory (1× DGX Spark) | $4,699 **[FACT — current NVIDIA price, cluster A]** | ~$1,177/yr | ~$420/yr (240W, $0.20/kWh ASSUMPTION) | ~$0.6–2/M tokens (25–100% utilization) | CALC (referenced) |
| Cooperative factory (10× DGX Spark, 50 members) | ~$46,990 | ~$11,770/yr | ~$2,000–4,000/yr | ~$0.77–1.20/M tokens at ~70% utilization | CALC (referenced) |
| Industrial factory (GB300 NVL72, 4-rack/288-GPU cluster) | ~$16M **[ASSUMPTION — analyst-estimate based, explicitly not an official NVIDIA price]** | see Section 4.1 sensitivity table | ~568kW max draw, $0.10/kWh ASSUMPTION | ~$0.05–0.12/M tokens depending on financing term and utilization | CALC |

These carry forward the earlier workbook's figures unchanged; see Section 1 for the cooperative-tier discrepancy discussion.

### 4.1 Financing-term sensitivity — industrial tier only (newly derived here, formula shown)

**Formula:** Annual financed capital cost = Capital ÷ AF(n,8%), where AF(n,8%) = (1 − 1.08⁻ⁿ) ÷ 0.08. Annual facility-power cost = 568kW × 90% utilization × 8,760 h/yr × $0.10/kWh **[ASSUMPTION]** ≈ $447,800/yr. Cost per million tokens = (financed capital + facility power) ÷ (max annual tokens × 90% utilization ÷ 1,000,000), where max annual tokens = 2.5M tok/s × 31,536,000 s/yr ≈ 78.84 trillion tok/yr **[the 2.5M tok/s figure is itself an OBSERVED FACT for a 4-rack/288-GPU MLPerf v6.0 aggregate, not a single rack — see source register cluster A]**.

| Financed term | Annuity factor AF(n,8%) | Annual financed capital ($16M) | + Facility power/yr | Total annual cost | Cost per M tokens |
|---|---|---|---|---|---|
| 3 years | 2.577 | $6,206,900 | $447,800 | $6,654,700 | ~$0.094/M tokens |
| 4 years | 3.312 | $4,832,600 | $447,800 | $5,280,400 | ~$0.074/M tokens |
| 5 years | 3.993 | $4,007,300 | $447,800 | $4,455,100 | ~$0.063/M tokens |
| 7 years | 5.206 | $3,073,000 | $447,800 | $3,520,800 | ~$0.050/M tokens |

Cross-check: at 5 years, straight-line depreciation alone ($16M÷5 = $3.2M/yr) implies ~$0.045/M tokens; the financing premium over depreciation is ~$0.0114/M tokens — consistent with the earlier workbook's stated figure. **Longer financing terms mechanically lower the per-token financed-capital cost but increase total interest paid and lock in today's hardware for longer against a fast-depreciating asset class — this table shows the arithmetic trade-off, it does not recommend a term.**

### 4.2 Retail benchmark (comparison point only — never the owned-production cost)

| Model family | Input $/MTok | Output $/MTok | Evidence class |
|---|---|---|---|
| Claude Sonnet 5 (Anthropic) | $2.00 | $10.00 | FACT |
| Claude Opus 5 (Anthropic) | $5.00 | $25.00 | FACT |
| Claude Fable 5 (Anthropic) | $10.00 | $50.00 | FACT |
| GPT-5.6 Terra (OpenAI) | $2.00 | $12.00 | ATTR (via AI-summarized fetch, not raw primary text) |
| GPT-5.6 Sol (OpenAI) | $5.00 | $30.00 | ATTR (same caveat) |
| Gemini 3.1 Pro Preview (Google), ≤200K tokens | $2.00 | $12.00 | FACT (still "Preview," not GA) |

**Reading this table correctly:** owned-production costs above (roughly $0.05–2/M tokens depending on tier and utilization) are 1–2 orders of magnitude below these retail prices. That gap is expected and is exactly the "generate your own power vs. buy from the grid" distinction from Section 2 — it is not evidence that retail labs are irrationally priced, since retail prices bundle proprietary model R&D, safety work, margin, and reliability guarantees that a self-hosted open-weight stack does not include.

---

## 5. Bitcoin-mining gross-energy-monetization comparison

**This is explicitly NOT a profit claim.** It compares only *gross revenue per MWh of electricity consumed* across two energy-monetization mechanisms — Bitcoin mining (a frictionless, protocol-level "plug in and get paid" market) and hypothetical AI-token sales at retail benchmark prices (which have no equivalent frictionless market — OpenRouter and similar routers are only an early, partial analogue). Neither side nets out capex, financing, cooling, staffing, or (for AI) whether anyone would actually buy that many tokens at that price.

**Bitcoin side — formula:** Revenue/MWh = (hashprice $/PH·s⁻¹/day ÷ 1000 to get $/TH·s⁻¹/day) ÷ 24 (→ $/TH·s⁻¹/hr) ÷ (efficiency in J/TH ÷ 1000 → kWh per TH·s⁻¹·hr) × 1000 (kWh→MWh), which simplifies to **Revenue/MWh = 1,333 ÷ efficiency(J/TH)**, anchored to Luxor's reported spot hashprice of **$31.73–32.05/PH/s/day around Aug 10–12, 2026 [FACT, cluster F]**. ASIC efficiency bands (25–38 J/TH for older fleets, sub-14 J/TH for the most efficient current fleets) are **[ASSUMPTION]** — illustrative generational bands, not a specific verified spec sheet checked in this session.

**AI-token side — formula:** at 240W continuous draw and 50 tok/s output **[ASSUMPTION, within DGX Spark's observed power/throughput envelope, cluster A]**, 1 MWh of electricity buys 1,000kWh ÷ 0.24kW = 4,166.7 hours of runtime → 4,166.7 h × 3,600 s/h × 50 tok/s ≈ 750 million output tokens per MWh. Revenue = 750 × price per million tokens.

| Scenario | Basis | Gross revenue per MWh | Evidence class |
|---|---|---|---|
| Bitcoin mining — older fleet (25–38 J/TH) | 1,333 ÷ 25 to 1,333 ÷ 38 | **~$35 – $53** | CALC on FACT anchor + ASSUMPTION efficiency |
| Bitcoin mining — efficient fleet (<14 J/TH) | 1,333 ÷ 14 | **~$95+** (rising further below 14 J/TH) | CALC on FACT anchor + ASSUMPTION efficiency |
| AI tokens sold at $1/M | 750M tokens × $1/M | **$750** | CALC on ASSUMPTION hardware/price inputs |
| AI tokens sold at $5/M | 750M tokens × $5/M | **$3,750** | CALC |
| AI tokens sold at $10/M | 750M tokens × $10/M | **$7,500** | CALC |
| AI tokens sold at $25/M | 750M tokens × $25/M | **$18,750** | CALC |

**Why the AI-token numbers look so much larger:** they assume every token produced is sold at a *retail* frontier-model price (Section 4.2), which is the "buy from the grid" price, not a cost. If the same 750M tokens were valued only at owned-production cost (Section 4, ~$0.6–2/M tokens for a home-tier machine), gross "revenue" would be **$0.45–$1.50 per MWh-equivalent of tokens produced** — below even the least efficient Bitcoin fleet. **The entire comparison is sensitive to which price point you plug in, which is exactly why this is a scenario table with editable inputs, not a profitability claim about either activity, and it must not be read as one.**

---

## 6. Bridging token cost to working-capacity cost (reference, brief)

To connect $/M tokens to $/AI-working-hour (the "workload/AI-working-capacity cost" layer), apply illustrative usage-intensity bands **[ASSUMPTION, informed by OpenAI's self-reported Codex telemetry — ATTR, cluster J, not independently audited]**:

| Usage mode | Tokens/hour (illustrative) | At retail Sonnet 5 pricing (~$6/M blended) | At owned-production cost (~$1/M blended) |
|---|---|---|---|
| Chat/advisor | 10,000–30,000 | $0.06–$0.18/hr | $0.01–$0.03/hr |
| Active copilot | 60,000–120,000 | $0.36–$0.72/hr | $0.06–$0.12/hr |
| Delegated single agent | 200,000–600,000 | $1.20–$3.60/hr | $0.20–$0.60/hr |
| Heavy multi-agent orchestration | 1,000,000–12,000,000+ | $6–$72+/hr | $1–$12+/hr |

**Formula:** $/hour = (tokens/hour ÷ 1,000,000) × $/M-token rate. **Interpretive note [INTERP]:** this shows why heavy orchestration can make AI working-capacity cheap in $/hour terms even at retail prices — but cost per hour of *capacity* says nothing about the *value* of what that capacity produces. A cheap, fast, wrong answer scaled across a multi-agent team is still cheap and wrong at scale.

---

## 7. Standing boundary note (repeated deliberately, not only stated once)

Every table in this workbook is a scenario built on visible, editable assumptions — utilization rates, electricity prices, financing terms, ASIC efficiency bands, and retail price points can all be changed, and doing so will change every downstream number. None of this workbook constitutes investment, legal, tax, procurement, or policy advice, and no figure here should be read as a forecast of what any specific facility, cooperative, or mining/inference operation will actually earn or cost. The final step in the analytical chain — outcome and value — is **not mechanically determined** by any of the cost or revenue figures above; that step depends on human judgment, direction, and context that this workbook does not and cannot model.