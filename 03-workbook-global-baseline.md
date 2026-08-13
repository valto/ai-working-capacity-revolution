# Release Asset #7 — Global Baseline Workbook
## Energy-to-Tokens Production Cost Curves: Home, Cooperative, Professional, Hyperscale

**Part of:** "Why Are They Spending Trillions on AI?" — Valto Loikkanen, CC BY 4.0
**Model status:** Draft v0.1, editable baseline
**Currency baseline:** Global USD (see localization note below)
**Source cut-off for inputs used here:** 2026-08-13
**Not investment, legal, tax, procurement, or policy advice.** Every scenario below is an editable illustration built on stated assumptions, not a forecast or recommendation.

---

## Evidence-class legend (used throughout every table)

| Tag | Meaning |
|---|---|
| **OBSERVED** | Primary documentation, official spec sheet, or a directly-fetched primary source, checked on/immediately before 2026-08-12. |
| **ATTRIBUTED** | A named person/organization's on-the-record statement. Not independently proven merely because it was said. |
| **DERIVED** | Transparent arithmetic from cited OBSERVED/ATTRIBUTED inputs. Formula always shown. |
| **ASSUMPTION** | A visible, editable scenario parameter — not a market fact. What it controls is stated. |
| **INTERPRETATION** | A labelled explanation of how the above may connect. Never a fact. |

---

## How to adapt this workbook to your own numbers

This workbook is built as a chain of separated economic layers, never collapsed into one number:

```
raw energy cost → hardware-amortized cost → financed asset cost → full operating cost
→ capacity/utilisation cost → token production cost → workload/working-capacity cost
→ outcome and value (NOT mechanically determined by the layers above)
```

To re-run any tier with your own numbers, replace only the labelled **ASSUMPTION** cells — every **OBSERVED** cell is a verified spec/price and should only change if you have a newer primary source:

1. **Capital cost** — swap in your actual purchase price/quote (tax, shipping, import duty excluded unless you add them).
2. **Financing terms** — down-payment %, interest rate, and term (years) are all editable; the formula is a standard amortizing annuity, shown once below so you can reuse it anywhere.
3. **Electricity price ($/kWh)** — replace the low/mid/high scenario with your local industrial, commercial, or residential tariff. This is the single most locally-variable input in the entire model (rates from ~$0.03/kWh to ~$0.40/kWh exist across real global markets).
4. **Utilization (%)** — the share of the year the hardware is actually generating tokens vs. idle. This is usually the single biggest lever on $/million-tokens — always shown as low/mid/high, never a single point estimate.
5. **Throughput (tokens/sec)** — swap in your own benchmark for your own model/quantization/framework. Do not reuse NVIDIA's or any vendor's benchmark number for a different model, precision, or interactivity setting — throughput is workload-specific and can vary 10-50x depending on target latency (see Hyperscale tier notes).
6. **Opex/admin overhead** — add your own facility, staffing, insurance, cooling, and networking costs; the illustrative bands here are placeholders, explicitly marked ASSUMPTION.
7. **Currency** — every figure below is USD. An FX line is shown only where needed to reconcile against a EUR-denominated prior figure; swap in your own rate and date for any other currency.

**Formula used for every "capital + financing per year" row (DERIVED, standard amortizing-loan formula):**

```
down_payment = price × down_payment_%
financed_amount = price − down_payment
annual_loan_payment = financed_amount × rate / (1 − (1 + rate)^(−term_years))
capital_and_financing_per_year = annual_loan_payment + (down_payment / term_years)
```

The second term spreads the down payment evenly across the financing term purely for annualized comparability — you may instead treat the down payment as a one-time year-0 cost if you prefer; both are legitimate and are flagged here as a modelling choice, not a fact.

**Formula used for every "$/million tokens" row (DERIVED):**

```
annual_tokens = throughput_tokens_per_sec × 3600 × 8760 × utilization_%
cost_per_million_tokens = (capital_and_financing_per_year + electricity_cost_per_year + opex_per_year)
                            / (annual_tokens / 1,000,000)
```

**Formula used for every "$/AI-working-hour" row (DERIVED):**

```
cost_per_working_hour = cost_per_million_tokens × (tokens_per_working_hour_for_usage_mode / 1,000,000)
```

where `tokens_per_working_hour_for_usage_mode` comes from the usage-intensity bands defined in Section 6.

---

## 1. Critical methodology rule — do not skip this

**Owned-production cost and retail API price are two different economic layers and must never be blended into one number.**

- The tables below price the *cost of producing tokens on hardware you own or co-own*, running **open-weight models** (e.g., Qwen, DeepSeek, Kimi-class models) — independent of what OpenAI, Anthropic, or Google charge for their own proprietary, closed models.
- Retail API prices (Section 7) are a separate comparison point — the "buy electricity from the grid" analogue to "generate your own solar power." They tell you what it costs to rent someone else's finished token-production capacity; they do not tell you what it costs to build and run your own.
- An earlier pass of this research mistakenly mixed lab retail pricing into an owned-hardware cost curve and had to be self-corrected mid-session. That correction is preserved here deliberately, as a worked "how not to model this" lesson, not smoothed over.

---

## 2. HOME TIER — single NVIDIA DGX Spark

### 2.1 Capital and financing

| Input | Value | Class |
|---|---|---|
| DGX Spark, Founders Edition, current MSRP | $4,699 | **OBSERVED** — NVIDIA Developer Forums official price-change notice, effective week of 2026-02-23 (raised from original $3,999 launch MSRP). URL: forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713 |
| Down payment | 20% ($939.80) | **ASSUMPTION** — controls how much is financed vs. paid up front |
| Financing rate | 8%/yr | **ASSUMPTION** — illustrative consumer/small-business credit rate |
| Financing term | 5 years | **ASSUMPTION** — controls annuity size; shown at 3/4/5/7yr sensitivity below |

| Formula | Result |
|---|---|
| `financed_amount = $4,699 − $939.80 = $3,759.20` | — |
| `annual_loan_payment = $3,759.20 × 0.08 / (1 − 1.08^−5) = $941.52` | — |
| `capital_and_financing_per_year = $941.52 + ($939.80/5) = $941.52 + $187.96` | **$1,129.48/yr** |

Straight-line cash-purchase comparison (no financing): `$4,699 / 5 = $939.80/yr` (**DERIVED**) — shown so you can compare "pay cash" vs. "finance" framing.

**Financing-term sensitivity (DERIVED, same 8% rate, 20% down):**

| Term | Annuity payment/yr | Capital+financing/yr (incl. spread down payment) |
|---|---|---|
| 3 yr | $1,447.79 | $1,635.72 |
| 4 yr | $1,135.02 | $1,322.95 |
| 5 yr | $941.52 | $1,129.48 |
| 7 yr | $702.35 | $890.31 |

### 2.2 Electricity

| Input | Value | Class |
|---|---|---|
| Max continuous power draw | 240W (PSU rating); GB10 SoC TDP 140W | **OBSERVED** — NVIDIA official DGX Spark product page |
| Electricity price scenarios | Low $0.06/kWh · Mid $0.12/kWh · High $0.25/kWh | **ASSUMPTION** — replace with your local residential/commercial tariff |

### 2.3 Throughput (tokens/sec) — benchmark basis

| Scenario | tok/s | Class |
|---|---|---|
| Low (INT4 baseline, vLLM+AutoRound+FlashInfer) | 28.3 | **OBSERVED** — NVIDIA Developer Forums thread by "Albond," Qwen3.5-122B-A10B on single DGX Spark, directly-visible post content |
| Mid (hybrid INT4+FP8 quantization) | 30.8 | **OBSERVED** — same thread, +8.8% over baseline |
| High (+ MTP-1 speculative decoding, "likely the memory bandwidth ceiling" per poster) | 38.4 | **OBSERVED** — same thread, +25% over baseline |
| Headline claim (unconfirmed) | up to 51 | **ATTRIBUTED** — same thread's own summary line references a later post (#71) not independently viewed in this check; treat as unconfirmed |

**Tokens/kWh at 240W (DERIVED):**

| Throughput | Tokens/hour | Tokens/kWh |
|---|---|---|
| 28.3 tok/s | 101,880 | 424,500 |
| 30.8 tok/s | 110,880 | 462,000 |
| 38.4 tok/s | 138,240 | 576,000 |
| 51 tok/s (unconfirmed) | 183,600 | 765,000 |

`tokens_per_kWh = tok/s × 3600 / kW_draw` — e.g. `30.8 × 3600 / 0.240 = 462,000`.

### 2.4 Home tier — full production cost curve ($/million tokens)

Utilization = share of the 8,760 hours/year the machine is actually generating tokens vs. idle. **ASSUMPTION**, shown at low/mid/high.

| Throughput | Utilization | Elec price | Annual tokens (DERIVED) | Electricity cost/yr (DERIVED) | **$/million tokens (DERIVED)** |
|---|---|---|---|---|---|
| 30.8 tok/s | Low 10% | $0.12 | 97.1M | $25 | **$11.89** |
| 30.8 tok/s | Mid 40% | $0.12 | 388.5M | $101 | **$3.17** |
| 30.8 tok/s | High 80% | $0.12 | 777.0M | $202 | **$1.71** |
| 38.4 tok/s | Low 10% | $0.12 | 121.1M | $25 | **$9.53** |
| 38.4 tok/s | Mid 40% | $0.12 | 484.4M | $101 | **$2.54** |
| 38.4 tok/s | High 80% | $0.12 | 968.8M | $202 | **$1.37** |
| 30.8 tok/s | Mid 40% | Low $0.06 | 388.5M | $50 | **$3.04** |
| 30.8 tok/s | Mid 40% | High $0.25 | 388.5M | $210 | **$3.45** |

`cost_per_million_tokens = ($1,129.48 + electricity_cost) / (annual_tokens/1,000,000)`.

**Read:** at home scale, capital+financing dominates the cost curve — electricity is a rounding error (~$13-$420/yr vs. ~$1,130/yr financing). Utilization is by far the biggest lever: going from 10% to 80% utilization at the same throughput cuts $/M-tokens by roughly 7x, because the fixed financing cost is spread over far more tokens.

### 2.5 Home tier — $/AI-working-hour (mid scenario: 30.8 tok/s, 40% utilization, $0.12/kWh → $3.17/M tokens)

| Usage-intensity band (see Section 6) | Tokens/hour | **$/AI-working-hour (DERIVED)** |
|---|---|---|
| Chat/advisor | 10,000-30,000 | $0.032-$0.095 |
| Active AI coworker/copilot | 60,000-120,000 | $0.190-$0.380 |
| Delegated single agent | 200,000-600,000 | $0.633-$1.900 |
| Heavy multi-agent orchestration | 1,000,000-12,000,000 | $3.17-$38.00 |

At high-utilization scenario ($1.71/M tokens), the same bands run roughly 46% lower; at low-utilization scenario ($11.89/M tokens), roughly 3.75x higher. Always state which utilization scenario a $/working-hour figure assumes.

---

## 3. COOPERATIVE TIER — 50 members, 10 DGX Sparks

### 3.1 Capital and financing (10 machines)

Same per-unit price/financing terms as Section 2.1, scaled ×10 (**DERIVED**):

| Item | Per machine | ×10 machines |
|---|---|---|
| Capital+financing/yr | $1,129.48 | **$11,294.76/yr** |

### 3.2 Electricity (10 machines)

Aggregate max continuous draw: `0.240kW × 10 = 2.4kW` (**DERIVED** from OBSERVED per-unit spec).

### 3.3 Admin/overhead — cooperative-specific cost layer

| Scenario | $/yr | Class |
|---|---|---|
| Low | $1,000 | **ASSUMPTION** — light self-managed coordination |
| Mid | $3,000 | **ASSUMPTION** — part-time admin, basic networking/switch gear |
| High | $6,000 | **ASSUMPTION** — dedicated coordinator time, redundant networking |

### 3.4 Cooperative tier — production cost curve ($/million tokens), aggregate throughput 10×30.8 tok/s = 308 tok/s

| Utilization | Annual tokens (DERIVED) | Electricity/yr ($0.12/kWh, DERIVED) | Total/yr (incl. $3,000 admin) | **$/million tokens (DERIVED)** |
|---|---|---|---|---|
| Low 20% | 1.94B | $505 | $14,799 | **$7.62** |
| Mid 50% | 4.86B | $1,261 | $15,556 | **$3.20** |
| High 85% | 8.26B | $2,144 | $16,439 | **$1.99** |

### 3.5 Cooperative tier — $/member/month (DERIVED)

`total_cost_per_year / 50 members / 12 months`:

| Utilization | Total/yr | **$/member/month** | €/member/month (FX ASSUMPTION: 1 USD = 0.92 EUR) |
|---|---|---|---|
| Low 20% | $14,799 | **$24.67** | €22.69 |
| Mid 50% | $15,556 | **$25.93** | €23.85 |
| High 85% | $16,439 | **$27.40** | €25.21 |

### 3.6 Cooperative tier — $/AI-working-hour (mid scenario, $3.20/M tokens)

| Usage-intensity band | Tokens/hour | **$/AI-working-hour** |
|---|---|---|
| Chat/advisor | 10,000-30,000 | $0.032-$0.096 |
| Active AI coworker/copilot | 60,000-120,000 | $0.192-$0.384 |
| Delegated single agent | 200,000-600,000 | $0.641-$1.922 |
| Heavy multi-agent orchestration | 1,000,000-12,000,000 | $3.20-$38.44 |

### 3.7 The €42/member/month figure — resolved, see Token-Factory Scenario Workbook §1

**Corrected 2026-08-13:** an earlier version of this section treated the author's published ~€42/member/month figure and this workbook's ~€23-25/member/month DGX Spark recomputation as an unresolved discrepancy requiring reverse-engineering (the previous content of this section attempted exactly that, without success). The author has since clarified that €42/member/month was never based on DGX Spark pricing — it was built on his own illustrative €100,000-excluding-VAT capital assumption for a shared workstation-class machine (e.g., an NVIDIA DGX Station-type system), for which NVIDIA publishes specs but no retail price. The two figures describe two different hardware tiers, not one measurement with an uncertain source.

**See the Token-Factory Scenario Workbook (Release Asset #10), §1/§1a/§1b, for the full corrected explanation, the €100,000 capital-base arithmetic, and the side-by-side comparison of both hardware tiers.** This workbook's own ~€23-25/member/month figure (§3.5-3.6 above) remains valid and unchanged as the DGX Spark-tier scenario.

---

## 4. PROFESSIONAL TIER — single NVIDIA HGX B300 (8-GPU) node

**Important caveat up front:** NVIDIA's official HGX B300 product page (OBSERVED specs below) does **not** publish a power-draw figure or a price for this SKU. Both are therefore **ASSUMPTION**, not OBSERVED, in this tier — a materially different confidence level from the Home and Hyperscale tiers, where hardware price and/or power are directly sourced.

### 4.1 Specs (OBSERVED) vs. cost inputs (ASSUMPTION)

| Item | Value | Class |
|---|---|---|
| GPUs | 8× NVIDIA Blackwell Ultra (SXM) | **OBSERVED** — nvidia.com/en-us/data-center/hgx/ |
| Total memory | 2.1 TB | **OBSERVED** |
| NVFP4 inference | 144 PFLOPS sparse / 108 PFLOPS dense | **OBSERVED** |
| NVLink5 bandwidth | 1.8 TB/s per GPU-link, 14.4 TB/s total | **OBSERVED** |
| Networking | 1.6 TB/s | **OBSERVED** |
| Power draw | Low 8kW · Mid 11kW · High 15kW | **ASSUMPTION** — no primary source; scaled illustratively from GB300 NVL72's 135kW/72-GPU rack ratio plus host overhead margin |
| Capital cost | Low $250,000 · Mid $350,000 · High $500,000 | **ASSUMPTION** — no public price found for this SKU; placeholder range only |

### 4.2 Throughput — derived by linear GPU-count scaling from OBSERVED per-GPU MLPerf figures

| Basis | Per-GPU tok/s (OBSERVED, MLPerf v6.0 DeepSeek-R1) | ×8 GPUs (DERIVED) |
|---|---|---|
| Offline scenario | 9,821 | 78,568 tok/s |
| Server (interactive) scenario | 8,064 | 64,512 tok/s |

**Caveat (carried from source register):** the 9,821/8,064 per-GPU figures were measured inside a 72-GPU NVL72 NVLink domain with Grace CPUs and rack-scale memory coherence — an 8-GPU HGX box (no NVL72 rack-scale fabric, no Grace CPU tier) will very likely NOT reproduce this per-GPU rate at the same precision/model. Treat this DERIVED figure as an optimistic upper bound, not a confirmed HGX B300 benchmark.

### 4.3 Professional tier — production cost curve ($/million tokens), mid capex $350,000, mid power 11kW, offline-derived throughput 78,568 tok/s, $0.10/kWh electricity

**Scope correction, added 2026-08-13: the figures in this table are capital + financing + electricity ONLY — no opex/overhead layer is included.** This makes them structurally incomparable to the Hyperscale tier's canonical figure (§5.6), which explicitly includes $200,000–$1,000,000/rack/yr of opex (facility, cooling beyond raw electricity, staffing, networking, replacement reserve). An earlier version of this workbook and the parent whitepaper compared Professional's $0.044–$0.146/M directly against Hyperscale's $0.091–$0.312/M as if both were full-layer figures, which made Professional look artificially cheaper. It is not shown here as cheaper than Hyperscale — see the illustrative opex sensitivity immediately below.

| Utilization | Annual tokens (DERIVED) | Electricity/yr (DERIVED) | Capital+financing/yr (5yr@8%, DERIVED) | **$/million tokens, NO OPEX (DERIVED)** |
|---|---|---|---|---|
| Low 25% | 619.4B | $2,409 | $87,660 | **$0.146** |
| Mid 60% | 1,486.6B | $5,782 | $87,660 | **$0.064** |
| High 90% | 2,229.9B | $8,672 | $87,660 | **$0.044** |

`annuity_payment($350,000, 8%, 5yr) = $87,660/yr` using the same formula as Section 1.

**Illustrative opex sensitivity (SCENARIO ASSUMPTION, added 2026-08-13 — not derived from any verified single-node opex figure, since none exists in this project's source register):** a single 8-GPU node plausibly requires far less facility/staffing/networking overhead than a full rack, but is very unlikely to require zero. Using an illustrative $10,000/$25,000/$50,000-per-year low/mid/high opex band — deliberately not scaled proportionally from Hyperscale's per-rack opex, since staffing and networking costs do not scale linearly with node count — the mid-utilization (60%) cost becomes:

| Opex scenario | Opex/yr | Total annual cost (capital+financing+electricity+opex) | **$/million tokens, WITH OPEX** |
|---|---|---|---|
| Low | $10,000 | $103,442 | **$0.070** |
| Mid | $25,000 | $118,442 | **$0.080** |
| High | $50,000 | $143,442 | **$0.096** |

This remains a SCENARIO ASSUMPTION, not a verified figure — the point is not that $0.070–$0.096/M is "the" correct Professional-tier cost, but that adding any plausible opex allowance narrows the apparent gap to Hyperscale's canonical $0.133/M mid-case substantially, and the no-opex figures above should never be quoted as if they were a complete cost.

### 4.4 Professional tier — $/AI-working-hour (mid scenario, $0.064/M tokens, NO OPEX — see scope correction above)

| Usage-intensity band | Tokens/hour | **$/AI-working-hour** |
|---|---|---|
| Chat/advisor | 10,000-30,000 | $0.0006-$0.0019 |
| Active AI coworker/copilot | 60,000-120,000 | $0.0038-$0.0076 |
| Delegated single agent | 200,000-600,000 | $0.0127-$0.0382 |
| Heavy multi-agent orchestration | 1,000,000-12,000,000 | $0.064-$0.764 |

**Read, corrected 2026-08-13:** the professional tier's no-opex $/M-tokens figure is roughly 25-70x lower than the Home tier's figure at comparable utilization — but this comparison is not on equal footing, since Home's figure already includes its full (if modest) cost structure while Professional's excludes opex entirely (see the scope correction above). Even after adding the illustrative opex sensitivity, Professional still comes out well below Home, consistent with GPU-generation efficiency (Blackwell Ultra vs. GB10) and better amortization of fixed cost across much higher throughput — but the specific 25-70x multiple should not be treated as a clean, like-for-like efficiency ratio, and should not be over-read given the unverified capex/power inputs. It is directionally informative, not a confirmed market price point.

---

## 5. HYPERSCALE/INDUSTRIAL TIER — GB300 NVL72 rack scale

### 5.1 Rack specs (OBSERVED)

| Item | Value | Source |
|---|---|---|
| GPUs/rack | 72× Blackwell Ultra | NVIDIA official GB300 NVL72 page |
| CPUs/rack | 36× Grace (2,592 Arm Neoverse V2 cores) | NVIDIA official page |
| GPU memory | 20 TB HBM3e @ up to 576 TB/s | NVIDIA official page |
| NVLink5 bandwidth | 130 TB/s | NVIDIA official page |
| FP4 dense | 1,440 PFLOPS (10,800 PFLOPS with sparsity) | NVIDIA official page |
| Rack power (TDP) | 135 kW | **OBSERVED**, Lenovo Press LP2357 OEM reference spec (NVIDIA's own page does not publish a power figure) |
| Rack power (peak) | up to 155 kW | Lenovo Press LP2357 |

### 5.2 Benchmark throughput — critical scaling caveat

NVIDIA's own MLPerf Inference v6.0 submission reports **2,494,310 tokens/sec** (rounded to "2.5M tok/s" in NVIDIA's own captioning) for DeepSeek-R1 — but this is an **aggregate across 4 interconnected GB300 NVL72 racks (288 GPUs)**, not one rack. Dividing evenly (**DERIVED**):

```
per_rack_offline_tokps = 2,494,310 / 4 racks = 623,578 tok/s (derived, even split assumption)
```

Cross-check against NVIDIA's directly-published per-GPU figures (**OBSERVED**, more granular and arguably more reliable than the even-split derivation above):

| Scenario | Per-GPU tok/s (OBSERVED) | ×72 GPUs (DERIVED, rack total) |
|---|---|---|
| Offline | 9,821 | 707,112 |
| Server (interactive) | 8,064 | 580,608 |

These three per-rack estimates (623,578 / 707,112 / 580,608) bracket a plausible ~580,000-710,000 tok/s per-rack range depending on exact scenario and derivation method — this workbook uses **623,578 tok/s** (the even-split figure) as its primary working number for continuity with the 4-rack aggregate benchmark, and flags the ~14% spread against the per-GPU-derived figures explicitly rather than picking one silently.

### 5.3 Tokens/kWh (DERIVED) — electricity-only layer

| Basis | tok/s/kW | Tokens/kWh |
|---|---|---|
| 623,578 tok/s @ 135kW TDP | 4,619 | 16,628,733 |
| 623,578 tok/s @ 155kW peak | 4,023 | 14,483,090 |
| 580,608 tok/s (server-scenario, per-GPU-derived) @ 135kW | 4,301 | 15,482,880 |

**Electricity-ONLY cost per million tokens (DERIVED)** — this is the bottom layer only, before any hardware/financing/opex:

| Electricity price | $/M tokens (at 16.6M tok/kWh basis) |
|---|---|
| $0.06/kWh | $0.0036 |
| $0.10/kWh | $0.0060 |
| $0.25/kWh | $0.0150 |

**This confirms the source-register finding: raw electricity is a rounding error at hyperscale — a small fraction of a cent per million tokens at typical electricity prices, and still under two cents even at the high end of the range shown ($0.015, i.e. 1.5 cents, at $0.25/kWh).** All of the meaningful cost at this tier comes from capital, financing, and operating overhead, not power.

### 5.4 Rack capital cost — two very different reference points, kept explicitly separate

**Reference point A — implied all-in infrastructure cost from Huang/Fink's on-air $50-60B/GW figure (ATTRIBUTED, CNBC, Aug 10 2026):**

```
rack_share_of_1GW = 135kW / 1,000,000kW = 0.000135
implied_allin_cost_per_rack = $50-60B × 0.000135 = $6.75M-$8.1M
```

This is a full-infrastructure figure — land, shell, power delivery, cooling, and compute together, per Huang's and Fink's own framing on the CNBC segment — **not** a hardware-only rack price.

**Reference point B — illustrative hardware-only capex (ASSUMPTION, analyst-anchored, explicitly NOT an official NVIDIA price):** $4,000,000/rack. No official NVIDIA rack price was found in this check; this figure sits below Reference Point A because it excludes land/shell/power-delivery infrastructure, consistent with A being the "full buildout" number and B being "compute hardware only."

**Financing sensitivity on the $4M hardware-only scenario (DERIVED, 8% rate):**

| Term | Annuity payment/yr | Straight-line depreciation/yr |
|---|---|---|
| 3 yr | $1,552,134 | $1,333,333 |
| 4 yr | $1,207,683 | $1,000,000 |
| 5 yr | $1,001,826 | $800,000 |
| 7 yr | $768,290 | $571,429 |

### 5.5 Opex/overhead layer (ASSUMPTION — facility, cooling beyond raw electricity, staffing, networking, replacement reserve)

| Scenario | $/yr per rack |
|---|---|
| Low | $200,000 |
| Mid | $500,000 |
| High | $1,000,000 |

### 5.6 Hyperscale tier — full production cost curve ($/million tokens), 5yr@8% financing on $4M hardware capex, mid opex $500,000/yr, $0.10/kWh

| Utilization | Annual tokens (DERIVED) | Raw electricity/M tok | Capital+financing/M tok | Opex(mid)/M tok | **TOTAL $/million tokens (DERIVED)** |
|---|---|---|---|---|---|
| Low 25% | 4.92T | $0.0060 | $0.204 | $0.102 | **$0.312** |
| Mid 60% | 11.80T | $0.0060 | $0.085 | $0.042 | **$0.133** |
| High 90% | 17.70T | $0.0060 | $0.057 | $0.028 | **$0.091** |

### 5.7 Cross-check against NVIDIA's own published figure — now independently verified, with a correction to its scope

**Correction (2026-08-13):** an earlier version of this workbook flagged "$0.123/M tokens" as UNVERIFIABLE. It is now independently confirmed directly on NVIDIA's own site: NVIDIA states GB300 NVL72 delivers AI inference at **$0.123 per million tokens at 116 tokens/sec/user interactivity, using NVIDIA Dynamo and TensorRT-LLM**, attributed to SemiAnalysis InferenceX benchmarks as of April 2026 (**[FACT]** — nvidia.com/en-gb/solutions/ai/inference/, checked 2026-08-13).

**The correction that matters is scope, not existence.** This figure describes a **72-GPU GB300 NVL72 rack-scale system** running a specific software stack (Dynamo + TensorRT-LLM) at a specific interactivity setting (116 tok/s/user) — it is a hyperscale/industrial-tier figure and belongs only in this section's comparison, cross-checked against this workbook's own $0.091–$0.312/M-tokens hyperscale range above (same order of magnitude, consistent with a real, verified figure landing inside a modeled range built on different capex/opex assumptions). **It must never be used to estimate the economics of a single workstation, a DGX Spark, or a DGX Station** — those are entirely different hardware tiers (see Section 2 and the Token-Factory Scenario Workbook §1a/1b for the workstation-tier and desktop-tier figures respectively). Using a 72-GPU rack-scale benchmark to price a one-machine cooperative purchase would understate that tier's real cost by roughly two to three orders of magnitude, which is exactly the kind of cross-tier mixing this paper's core methodology rule warns against (Section 1, above).

SemiAnalysis's own live InferenceX dashboard separately shows a wider GB300 DeepSeek-R1 cost range of roughly **$0.065–$0.076/M tokens** at ~70 tok/s/user interactivity up to **$2.3–$3.3/M tokens** at ~219 tok/s/user (higher interactivity = fewer tokens batched together = higher cost) — the now-confirmed $0.123/M-tokens figure sits inside this same range, at a specific interactivity point (116 tok/s/user) that differs from either end of that spread, which is expected given "tokens per watt" is not one fixed number for a given chip (see Section 10's discussion of the same interactivity trade-off).

### 5.8 Hyperscale tier — $/AI-working-hour (mid scenario, $0.133/M tokens)

| Usage-intensity band | Tokens/hour | **$/AI-working-hour** |
|---|---|---|
| Chat/advisor | 10,000-30,000 | $0.0013-$0.0040 |
| Active AI coworker/copilot | 60,000-120,000 | $0.0081-$0.0161 |
| Delegated single agent | 200,000-600,000 | $0.0269-$0.0807 |
| Heavy multi-agent orchestration | 1,000,000-12,000,000 | $0.133-$1.614 |

### 5.9 Vera Rubin NVL72 — forward-looking comparison (not this workbook's baseline; shown for context only)

NVIDIA's own vendor claims (**ATTRIBUTED**, marketing material) for its next-generation Vera Rubin NVL72 (successor to GB300) claim "up to 10x more tokens per megawatt" and "one-tenth the cost per million tokens" vs. GB200 NVL72. SemiAnalysis's own independent benchmark-based analysis is more conservative and workload-dependent: **~1.5-8x** cost advantage and a throughput-per-MW gap that starts near 2x at low interactivity and reaches **~5.4x** at high interactivity, depending on which GB200/GB300 baseline generation is used. Do not use the vendor's "10x"/"one-tenth" figures as a confirmed multiplier in any forward projection without citing this more conservative independent range alongside it.

---

## 6. Usage-intensity → tokens-per-hour conversion bands (used in every tier's $/working-hour row)

| Usage mode | Tokens/AI-working-hour | Class |
|---|---|---|
| Chat/advisor mode | 10,000-30,000 | **ASSUMPTION** — illustrative band, informed by general usage patterns, not a single verified statistic |
| Active AI coworker/copilot | 60,000-120,000 | **ASSUMPTION** |
| Delegated single agent | 200,000-600,000 | **ASSUMPTION** |
| Heavy multi-agent orchestration | 1,000,000-12,000,000+ | **ASSUMPTION** |

**Supporting context (ATTRIBUTED, OpenAI's own self-reported internal telemetry, not independently audited):** OpenAI reports Codex reached 99.8% of its weekly internal output tokens by mid-2026; by May 2026, 70.2% of sampled Codex users made at least one request estimated above 1 human-hour of equivalent work, and 25.6% made one above 8 human-hours; by June 2026, 99th-percentile heavy users regularly generated 60+ hours of Codex agent-turn time per day across parallel agents. Source: OpenAI, "How agents are transforming work" (openai.com/index/how-agents-are-transforming-work/, June 25, 2026), retrieved via Wayback Machine archive. Independent press coverage explicitly notes "every number comes from OpenAI itself," with no third-party audit — treat these as directional context for why heavy-orchestration usage bands can run orders of magnitude above chat-mode usage, not as a calibration of the exact band boundaries above.

**A claimed NVIDIA reference agentic workload figure of "32K input + 8K output tokens/turn" could not be found anywhere** despite extensive searching (source register, Cluster J) and should not be cited as an NVIDIA figure in this or any other release asset.

---

## 7. Retail API pricing — comparison layer ONLY, not a production-cost input

Do not use these to price owned hardware. Shown only as the "buy from the grid" comparison point (per Section 1's methodology rule). All confirmed **OBSERVED** or **ATTRIBUTED** as of 2026-08-12 (see full source register for per-model confidence notes):

| Provider/tier | Input $/M tokens | Output $/M tokens | Class |
|---|---|---|---|
| Anthropic Claude Sonnet 5 | $2.00 | $10.00 | **OBSERVED** — Anthropic's own live pricing page; this is now the permanent standard price, not an expiring intro rate |
| Anthropic Claude Opus 5 | $5.00 | $25.00 | **OBSERVED** |
| Anthropic Claude Fable 5 | $10.00 | $50.00 | **OBSERVED** |
| OpenAI GPT-5.6 Luna | $0.20 | $1.20 | **ATTRIBUTED** — via AI-summarizing fetch tool, not raw primary text; treat as lower-confidence |
| OpenAI GPT-5.6 Terra | $2.00 | $12.00 | **ATTRIBUTED** |
| OpenAI GPT-5.6 Sol | $5.00 | $30.00 | **ATTRIBUTED** |
| Google Gemini 3.1 Pro (≤200K tokens) | $2.00 | $12.00 | **OBSERVED** — Google's own live pricing page; model still in "Preview," not GA |

**Read across tiers vs. retail, corrected 2026-08-13 (an earlier version of this passage stated an unsupported and directionally wrong "14-25x more expensive" claim — the actual comparison is more nuanced and depends heavily on both Home-tier utilization and which retail tier is used):** using the same 30% input / 70% output blend convention applied consistently elsewhere in this paper (see the AI Working-Capacity Conversion Workbook §C.0), the retail tiers above blend to approximately $0.90/M (Luna), $7.60/M (Sonnet 5), $9.00/M (Terra/Gemini), $19.00/M (Opus 5), $22.50/M (Sol), and $38.00/M (Fable 5) **[CALC]**.

Against the Home tier's **best-case** $/M-tokens (~$1.37 at 38.4 tok/s, 80% utilization): Home is *cheaper* than every retail tier except Luna (where Luna is instead roughly 1.5x cheaper than Home). Against the Home tier's **worst-case** $/M-tokens (~$11.89 at 10% utilization): Home is now more expensive than Luna, Sonnet 5, Terra, and Gemini, roughly comparable to Opus 5, and cheaper than Sol and Fable 5 **[CALC]**.

**The honest finding is therefore not a fixed multiplier in either direction — it is that Home-scale self-hosting's cost-competitiveness versus retail depends entirely on (a) how steadily the owner actually uses the machine and (b) which retail tier is the realistic alternative.** A well-utilized Home device can undercut most mid-to-premium retail tiers; a poorly-utilized one can be worse than all but the most expensive retail tiers. This is consistent with the wider whitepaper's ownership-architecture argument that self-hosting's case rests on data control, customization, and independence from a provider — but it is not true that self-hosting is categorically uncompetitive on raw $/token cost, and this workbook no longer claims that. Hyperscale production cost ($0.091-$0.312/M tokens, canonical mid $0.133/M) remains far below any retail API price shown here at every utilization scenario — consistent with the source-register finding that inference-serving margins for frontier labs are, per Huang's on-air framing, "incredibly profitable" (ATTRIBUTED, unverified against any lab's actual disclosed margins).

---

## 8. Localization note

All figures above use a global USD baseline with illustrative electricity-price scenarios. To localize:

1. Replace the $0.06/$0.12/$0.25 (or $0.10 mid, where used) per-kWh scenarios with your actual local commercial/industrial tariff — this is usually the largest source of legitimate cross-country variation.
2. Replace financing rate/term with your locally available credit terms (consumer credit, SME loan, or infrastructure project finance, depending on tier).
3. Convert USD to local currency using a stated FX rate and date — never silently blend currencies.
4. Re-run utilization scenarios against your own realistic usage pattern; the illustrative low/mid/high bands here are not calibrated to any specific country or organization.

---

## 9. Summary comparison table — mid-scenario $/million tokens across all four tiers

| Tier | Capital basis | Opex/overhead included? | Mid $/M tokens (DERIVED) | Confidence on capital/power inputs |
|---|---|---|---|---|
| Home (1× DGX Spark) | $4,699, OBSERVED price | Yes (§2, illustrative support/software allowance) | $3.17 | High — price and power OBSERVED, throughput OBSERVED community benchmark |
| Cooperative (50 members, 10× DGX Spark) | $46,990, OBSERVED price ×10 | Yes (§3.3, ASSUMPTION admin/networking band) | $3.20 | High on hardware; admin/overhead is ASSUMPTION |
| Professional (1× HGX B300 node) | $350,000, ASSUMPTION | **No — capital+financing+electricity only (§4.3); with an illustrative opex sensitivity added in §4.3, mid-case rises to ~$0.080/M** | $0.064 (no opex) | Low-medium — capex and power are unverified placeholders; throughput is a scaling derivation, not a direct benchmark |
| Hyperscale (1× GB300 NVL72 rack) | $4,000,000, ASSUMPTION (hardware-only) | Yes (§5.5, ASSUMPTION opex band, $200k-1M/yr) | $0.133 | Medium — rack specs and power OBSERVED; capex is analyst-anchored ASSUMPTION, not an official price |

**INTERPRETATION, corrected 2026-08-13:** the roughly 25-50x gap between Home/Cooperative and Professional/Hyperscale tiers is directionally consistent with expected economies of scale in AI infrastructure (higher-generation silicon, better amortization of fixed cost over vastly higher throughput) but should not be read as a precise multiplier given the mixed confidence levels above — the Home/Cooperative tiers rest on OBSERVED prices and OBSERVED community benchmarks, while the Professional tier in particular rests on ASSUMPTION-level capex and power inputs with no public price found for that specific hardware SKU. **The Professional-vs-Hyperscale comparison specifically is not apples-to-apples**: Professional's $0.064/M excludes opex entirely while Hyperscale's $0.133/M includes it, so part of the apparent 2x gap between them is a scope artifact, not a pure hardware-generation effect — see §4.3's illustrative opex sensitivity, which narrows this gap once a plausible (though unverified) opex allowance is added to Professional.
