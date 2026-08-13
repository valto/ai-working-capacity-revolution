# Token-Factory / AI-Factory Scenario Workbook
**Release Asset #10 — "Why Are They Spending Trillions on AI?" (Valto Loikkanen, CC BY 4.0)**
**Status: educational / non-advice.** All figures below are either cited facts, attributed statements, transparent derivations from those, or clearly-flagged scenario assumptions. Nothing here is investment, legal, tax, procurement, or policy advice, and no scenario model is a forecast or recommendation — every input is editable and every result is only as good as the inputs you choose.

**Evidence-class legend** (used inline throughout): **[FACT]** = Observed Fact · **[ATTR]** = Attributed Statement · **[CALC]** = Derived Calculation (formula always shown) · **[ASSUMPTION]** = Scenario Assumption (editable, not a market figure) · **[INTERP]** = Interpretation.

**Currency note:** this workbook uses a **global USD baseline**, except Section 1, which reconciles two **EUR-denominated** figures from the author's own published cooperative model — EUR is kept there because that is the currency of the primary sources being reconciled.

---

## 1. CORRECTED: the €42 vs €19.50–23 per-member/month figures were never comparable — resolved, not merely reconciled

An earlier draft of this workbook treated €42/member/month and €19.50–23/member/month as two competing estimates of the *same* cooperative scenario with an unexplained ~2x gap. On 2026-08-13, the author checked his own original assumptions and clarified the actual situation, which resolves the gap rather than requiring further speculation about it:

1. **€42/member/month was never a hardware-quote-based figure.** It was built on the author's own **illustrative €100,000 excluding-VAT capital assumption** for a shared workstation-class machine — explicitly a scenario assumption, not a verified purchase price for any specific product. The original published article did not disclose this base, which is why the earlier draft of this workbook incorrectly treated €42 as an opaque, unauditable "published fact" to be reverse-engineered. It is not opaque once the €100,000 basis is stated; it is a normal **[ASSUMPTION]**-driven scenario output, fully auditable once the base is given (see the worked recomputation below).
2. **€19.50–23/member/month is a different hardware tier, not a competing estimate of the same one.** That figure was built around 10× NVIDIA **DGX Spark** units at the verified current price of $4,699 each (**[FACT]**) — a much smaller, cheaper, single-GPU-class desktop device, not a workstation-class or rack-scale machine. The two figures were describing different equipment from the start.

**There is therefore no discrepancy to reconcile between two measurements of one thing — there are two different hardware-tier scenarios, each internally consistent, that were mistakenly presented as if they should agree.** The corrected treatment below keeps them explicitly separate.

### 1a. The DGX Station-class scenario, corrected (illustrative €100,000 capital base)

NVIDIA's current DGX Station (GB300-based) is a real, named reference point for the *type* of machine such a cooperative could plausibly share: **748 GB of coherent memory and up to 20 petaFLOPS of FP4 AI compute** (**[FACT]** — nvidia.com/en-us/products/workstations/dgx-station/, checked 2026-08-13), positioned by NVIDIA for running models up to 1 trillion parameters and long-running local AI agents. **NVIDIA does not publish a retail or list price for this system** (**[FACT]** — same source; the page directs buyers to "contact a partner" and a marketplace listing rather than showing a price) — so any purchase price used here is a **quotation-level illustrative assumption**, not an official price, and must not be cited as one.

For illustration only, assume a cooperative acquires a suitable system for **€100,000 excluding VAT** (**[ASSUMPTION]** — explicitly not a DGX Station list price, since none exists), financed over 5 years at 6.5% (**[ASSUMPTION]**):

| Cost line | Formula | Result | Class |
|---|---|---|---|
| Hardware financing | Standard amortizing annuity on €100,000, 5yr, 6.5% APR, converted to a monthly figure | **≈€1,957/month** | **[CALC]** on an **[ASSUMPTION]** capital base |
| Electricity | 1 kW illustrative average continuous draw × 24h × ~30.4 days/month × €0.15/kWh | **≈€108/month** | **[CALC]** on an **[ASSUMPTION]** average-draw figure |
| Cooling/power overhead | 25% allowance on the electricity line | **≈€27/month** | **[ASSUMPTION]** |
| **Total basic compute infrastructure** | Sum of the above three lines | **≈€2,092/month** | **[CALC]** |

**On the 1 kW average-draw assumption:** NVIDIA's own documentation states a **fixed maximum system power budget of 1,600 W (1.6 kW)** for the DGX Station GB300, shared between the GB110 compute module and an optional RTX add-in card (**[FACT]** — docs.nvidia.com/dgx/dgx-station-development-guide/dynamic-power-sloshing.html, checked 2026-08-13). The 1 kW figure used above is therefore an **illustrative average-operating-load assumption, well within the documented 1.6 kW ceiling** — it is not a measured consumption figure for any real deployment, and utilization-dependent draw could plausibly range anywhere up to that 1.6 kW maximum.

**Shared across members (**[CALC]**, same €2,092/month base throughout):**

| Members sharing this one machine | €/member/month |
|---|---|
| 20 | €105 |
| **50** | **€42** |
| 100 | **€21** |

This is the exact arithmetic underlying the author's originally published €42 (50 members) and €21 (100 members) figures — both now shown as **[CALC]** outputs of an explicit, editable €2,092/month base, not as unaudited "published facts." The earlier draft of this workbook was wrong to describe the €42 figure as impossible to audit; it is fully auditable once the €100,000 illustrative capital base (which the original article did not state) is disclosed.

This calculation deliberately excludes people, data storage, software development, applications, support, and model training — it prices only shared hardware financing and power for running open AI models, exactly as originally scoped. One machine would in practice be shared through an inference service rather than dedicating a separate model or machine to every member, with additional machines financed as demand grows.

### 1b. The DGX Spark scenario (unchanged, kept explicitly separate)

The **~€19.50–23/member/month** figure remains valid **as a description of a different, smaller hardware tier**: 10× NVIDIA DGX Spark units at the verified current price of $4,699 each (**[FACT]**) — 10 units × $4,699 ≈ $46,990 capital; 5yr@8% financing ≈ $11,770/yr; electricity ≈ $2,000–4,000/yr; total ≈ $14,000–15,770/yr **before admin/networking**, ÷ 50 members ÷ 12 months. See Section 2 of the Global Baseline Workbook (Release Asset #7) for the full build. This is **[CALC]**, unchanged from the earlier draft.

**Bottom line, corrected:** €42/member/month (50 members, illustrative €100,000 DGX-Station-class machine) and €19.50–23/member/month (50 members, verified $4,699 DGX Spark machines) are not two conflicting estimates of one cooperative. They are two internally consistent, explicitly different hardware-tier scenarios — a single larger shared workstation-class system versus a pool of ten smaller desktop-class devices. **Both are correct for what they describe; neither should be cited as "the" cost of AI-compute cooperation without also stating which hardware tier and member count it assumes.** A cooperative's actual all-in cost depends on which tier of hardware it chooses, its real financing terms and utilization, and — critically — whether people, storage, software, support, and model training are included, none of which either figure above covers.

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
| Industrial factory (GB300 NVL72, 4-rack/288-GPU cluster) | ~$16M **[ASSUMPTION — analyst-estimate based, explicitly not an official NVIDIA price]** | see Section 4.1 sensitivity table | ~568kW max draw, $0.10/kWh ASSUMPTION | ~$0.091–0.312/M tokens, full-layer (capital + financing + opex), CANONICAL figure per the Global Baseline Workbook §5.6 | CALC (referenced) |

These carry forward the earlier workbook's figures unchanged; see Section 1 for the cooperative-tier explanation. **The canonical, full-layer Hyperscale figure used consistently across this paper is the Global Baseline Workbook's §5.6 range ($0.091–0.312/M tokens, mid $0.133/M) — that figure includes capital, financing, electricity, AND opex/overhead. The partial-layer sensitivity table in §4.1 below (capital + financing + electricity only, no opex) is a narrower, deliberately incomplete cross-check on the financing-term lever specifically; its lower headline numbers (as low as $0.050/M) must not be read as an alternative or cheaper "real" Hyperscale cost — they simply omit the opex layer that the canonical figure includes.**

### 4.1 Financing-term sensitivity — industrial tier only, CAPITAL+FINANCING+ELECTRICITY ONLY (opex excluded; not the canonical full-layer figure)

**Scope of this table, stated explicitly:** this sensitivity table isolates only the *financing-term* lever, holding capital, electricity, and utilization fixed while varying loan term. It deliberately **excludes the opex/overhead layer** (facility, cooling beyond raw electricity, staffing, networking, replacement reserve — see the Global Baseline Workbook §5.5, $200,000–$1,000,000/rack/yr) that the canonical Hyperscale figure above includes. **Do not cite the $0.050–0.094/M-tokens figures below as "the" Hyperscale cost — they are a partial-layer illustration of financing-term sensitivity only.**

**Formula:** Annual financed capital cost = Capital ÷ AF(n,8%), where AF(n,8%) = (1 − 1.08⁻ⁿ) ÷ 0.08. Annual facility-power cost = 568kW × 90% utilization × 8,760 h/yr × $0.10/kWh **[ASSUMPTION]** ≈ $447,800/yr. Cost per million tokens = (financed capital + facility power) ÷ (max annual tokens × 90% utilization ÷ 1,000,000), where max annual tokens = 2.5M tok/s × 31,536,000 s/yr ≈ 78.84 trillion tok/yr **[the 2.5M tok/s figure is itself an OBSERVED FACT for a 4-rack/288-GPU MLPerf v6.0 aggregate, not a single rack — see source register cluster A]**.

| Financed term | Annuity factor AF(n,8%) | Annual financed capital ($16M) | + Facility power/yr | Total annual cost (capital+financing+electricity ONLY) | Cost per M tokens (partial layer) |
|---|---|---|---|---|---|
| 3 years | 2.577 | $6,206,900 | $447,800 | $6,654,700 | ~$0.094/M tokens |
| 4 years | 3.312 | $4,832,600 | $447,800 | $5,280,400 | ~$0.074/M tokens |
| 5 years | 3.993 | $4,007,300 | $447,800 | $4,455,100 | ~$0.063/M tokens |
| 7 years | 5.206 | $3,073,000 | $447,800 | $3,520,800 | ~$0.050/M tokens |

Cross-check: at 5 years, straight-line depreciation alone ($16M÷5 = $3.2M/yr) implies ~$0.045/M tokens; the financing premium over depreciation is ~$0.0114/M tokens — consistent with the earlier workbook's stated figure. **Longer financing terms mechanically lower the per-token financed-capital cost but increase total interest paid and lock in today's hardware for longer against a fast-depreciating asset class — this table shows the arithmetic trade-off, it does not recommend a term.** Adding the canonical mid-opex figure ($500,000/yr, per Global Baseline Workbook §5.5) to any row above and recomputing would bring it back into the $0.091–0.312/M range shown in the canonical table — these are not two different measurements of Hyperscale cost, they are the same model shown at two different layers of completeness.

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