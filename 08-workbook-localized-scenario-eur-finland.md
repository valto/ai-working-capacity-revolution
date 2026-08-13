# Localized Scenario Workbook — EUR / Finland Template
### Release Asset #8, companion to *"Why Are They Spending Trillions on AI?"* (Valto Loikkanen, CC BY 4.0)

---

## 0. What this document is — and is not

This workbook takes the global-USD-baseline cost-model structure used elsewhere in this research package and reworks it **once, fully, in EUR, using Finland as the illustrative country**.

**It is:**
- **One worked template among many possible localizations.** Any reader in any country can copy the method and substitute their own electricity price, financing terms, currency, and hardware-sourcing reality.
- A demonstration of how sensitive "AI factory" economics are to *local* inputs that global USD headline figures never show.

**It is not:**
- A claim that Finland's actual current electricity price, loan rate, or hardware reseller price has been independently verified against a live primary Finnish source. **It has not.** The verified source register behind this project covers global AI-industry facts (chip specs, model pricing, corporate announcements) — it contains **no verified Finnish energy-market or Finnish credit-market figures**. Every Finland-specific number below is therefore explicitly marked as a **SCENARIO ASSUMPTION**, not a market fact, and is designed to be overwritten by the reader with a number they've checked themselves.
- Investment, legal, tax, procurement, or policy advice. Every scenario table in this workbook is an editable illustration built on stated assumptions, not a forecast or recommendation.

### Evidence-class legend (used throughout)

| Code | Meaning |
|---|---|
| **OBSERVED FACT** | Checked against a live/primary source on or immediately before 2026-08-12 (per the project's source register). |
| **ATTRIBUTED STATEMENT** | A named person/org said this; not independently proven as market fact. |
| **DERIVED CALCULATION** | Transparent arithmetic from cited inputs — formula always shown. |
| **SCENARIO ASSUMPTION** | A visible, editable parameter, explicitly not a verified market figure. |
| **INTERPRETATION** | A labelled explanation of how facts/statements/assumptions may connect — never a fact. |

---

## 1. The four things every localization must swap

| Parameter | Global USD baseline (illustrative) | This workbook's Finland/EUR value | Class | What it controls |
|---|---|---|---|---|
| Currency | USD | EUR | SCENARIO ASSUMPTION | Denomination of every cost figure |
| FX rate USD→EUR | n/a | **1 USD = €0.93** (i.e. 1 EUR ≈ $1.075) | SCENARIO ASSUMPTION — **not a checked live rate**; the source register contains no verified current FX quote | Converts every hardware/API price quoted in USD |
| Electricity price (home/prosumer tier) | $0.20/kWh (illustrative) | **€0.15/kWh** | SCENARIO ASSUMPTION — illustrative placeholder, not a verified current Finnish retail rate | Electricity line of every per-token and per-hour cost |
| Electricity price (industrial tier) | $0.10/kWh (illustrative) | **€0.09/kWh** | SCENARIO ASSUMPTION | Industrial-scale token production cost |
| Financing rate & term | 8% APR, 5-year amortization | **8% APR, 5-year amortization (unchanged)** | SCENARIO ASSUMPTION — kept identical to the USD baseline for comparability; **not a verified Finnish consumer/business loan rate**. In Finland, business loans are typically quoted as a Euribor reference rate plus a bank margin rather than a flat APR — see §2 for how to substitute this correctly. | Annual capital cost of every hardware/robot scenario |
| Hardware price basis | US direct/MSRP | **US MSRP converted at the FX assumption above, NOT a verified EU reseller price** | See §3 — explicit non-canonical flag | Capital cost input to every model |

---

## 2. Reader's substitution guide — do this for your own country

1. **Pick your currency and get a live FX rate** from a source you trust at the moment you're building your own version. Replace the €0.93/$1 placeholder above. Every dollar figure in this workbook is multiplied by that single number — nothing else needs to change structurally.
2. **Get your own electricity price**, in your currency per kWh, from an actual bill or your national/regional retail-tariff regulator, *not* from this document. Note whether it's a residential, commercial, or industrial tariff — they usually differ by 2–5x, and this workbook keeps that distinction (§1's two separate rows) on purpose.
3. **Get your own financing terms.** If you're in the Eurozone, a realistic template is: *(current Euribor reference rate, e.g. 3- or 12-month) + (your bank's margin, typically 1–4 percentage points depending on collateral/credit)*. This workbook uses a flat 8% only because that is what the (also-illustrative) global USD baseline used — swap it for whatever rate you can actually get quoted, and re-run the same amortization formula shown in §5–§7.
4. **Check hardware price locally, not from this document.** See §3 immediately below — this is the single most common way localization goes wrong.
5. Re-run the formulas (shown explicitly, not just the results, in every table below) with your four substituted numbers. The *structure* — fixed capital/financing cost vs. variable electricity cost vs. token output — does not change; only the four inputs do.

---

## 3. Hardware-price localization caveat (DGX Spark case study) — read this before using any price below

**OBSERVED FACT:** NVIDIA's official DGX Spark Founders Edition MSRP, sold direct in the US, is **$4,699** as of 2026-08-12 (raised from $3,999 in a price change NVIDIA itself announced on 2026-02-25, citing memory supply constraints). Source: NVIDIA Developer Forums official price-change notice, forums.developer.nvidia.com, checked 2026-08-12.

**What this workbook does NOT claim:** any specific EU or Finland reseller price for DGX Spark. NVIDIA's own product page does not display a price at all and routes to third-party "Buy Now" marketplace links; no EU/Finland reseller listing was checked or verified in the source register behind this project.

**Explicit non-canonical flag, per the task requirement for this asset:** *outside-US hardware pricing for products like DGX Spark is reseller-dependent — shaped by import duty, VAT, logistics, local demand, and individual reseller margin — and should never be treated as a universal fact equivalent to the manufacturer's home-market MSRP.* If you are building your own version of this workbook, get a real quote from an actual EU reseller at the time you build it, and expect it to be higher than the FX-converted US MSRP shown below, not equal to it.

| Reference point | Value | Class |
|---|---|---|
| US direct MSRP | $4,699 | OBSERVED FACT |
| FX-converted "floor reference" (NOT a real EU quote) | $4,699 × 0.93 = **€4,370** | DERIVED CALCULATION (mechanical FX conversion only) |
| Local VAT | *[blank — insert your own country's rate; not verified in this workbook]* | reader to fill in |
| Import/logistics/reseller margin | *[blank — insert your own local reseller quote]* | reader to fill in |
| **Realistic EU landed price** | **likely higher than €4,370 — get a real quote** | not modeled here |

For the worked examples below, we use the **€4,370 FX-floor figure** purely so the arithmetic is traceable back to the OBSERVED-FACT US MSRP. Anyone reading this should assume their actual purchase price in Finland (or elsewhere in the EU) will be higher, and should re-run §5's formulas with their real quote.

---

## 4. Financing-convention note

This workbook uses two different (both legitimate) amortization conventions, and says so explicitly rather than hiding the difference:

- **Annual-payment convention** (§5, §6 — DGX Spark tiers): `Annual payment = P × r / (1 − (1+r)^-n)`, with r = 8%/yr, n = 5 years. Simpler for an at-a-glance annual TCO.
- **Monthly-payment convention** (§7 — humanoid robot tier, matching a typical consumer/business loan structure): `Monthly payment = P × r_m / (1 − (1+r_m)^-n_m)`, with r_m = 8%/12 monthly rate, n_m = 60 months; annualized by ×12.

The two conventions produce slightly different totals for an identical principal and rate (monthly compounding is marginally more expensive in total interest paid per year in the way it's shown here). If your own loan is quoted one way, use that formula — don't mix them within one comparison.

---

## 5. Worked Model A — Home AI factory (single DGX Spark), EUR

Inputs: Capital €4,370 (§3 floor reference — not a real EU quote) · financing 8%/5yr, annual convention · power draw 240W continuous max (OBSERVED FACT spec, NVIDIA product page) · electricity €0.15/kWh (SCENARIO ASSUMPTION) · throughput range **corrected 2026-08-13**: 30.8–38.4 tok/s directly confirmed in the underlying community forum thread (Qwen3.5-122B-A10B on DGX Spark), with a separate, unconfirmed "51 tok/s+" headline claim by the same poster not independently re-confirmed — **an earlier version of this section used an 83 tok/s figure that does not trace to any source in this project's register and has been removed.** Both the confirmed 30.8–38.4 tok/s range and the unconfirmed 51 tok/s ceiling are shown below, clearly labeled by confidence, rather than collapsing them into one unlabeled range.

**Financing:** `A = 4,370 × 0.08 / (1 − 1.08⁻⁵) = €1,095/yr`
**Electricity at 100% utilization:** `240W × 8,760h/yr × €0.15/kWh = 2,102.4 kWh × €0.15 = €315/yr`

| Utilization | Tokens/yr @ 38.4 tok/s (confirmed) | Tokens/yr @ 51 tok/s (unconfirmed) | Total cost/yr (financing + electricity) | Cost/M tokens @ 38.4 tok/s | Cost/M tokens @ 51 tok/s |
|---|---|---|---|---|---|
| 100% | 1,211.0M | 1,608.3M | €1,410 | €1.16 | €0.88 |
| 75% | 908.3M | 1,206.2M | €1,331 | €1.47 | €1.10 |
| 50% | 605.5M | 804.2M | €1,253 | €2.07 | €1.56 |
| 25% | 302.8M | 402.1M | €1,174 | €3.88 | €2.92 |

Formula for every cell: `Tokens/yr = tok/s × 86,400s × 365 × utilization`; `Cost/M tokens = (€1,095 + €315×utilization) / (Tokens/yr ÷ 1,000,000)`. **The 51 tok/s column should be treated as an optimistic, unconfirmed scenario ceiling — the 38.4 tok/s column is the confirmed figure to rely on for any real planning use.**

**Boundary note:** this is a scenario illustration of one machine's amortized + electricity cost per token, at an assumed local electricity price and an assumed hardware landed price. It excludes maintenance, software, networking, supervision time, and any real EU reseller markup (see §3). It is not a forecast of what running a home AI factory will actually cost you, and it is not investment or procurement advice.

---

## 6. Worked Model B — Cooperative AI factory (50 members, 10 DGX Sparks), EUR

Inputs: Capital 10 × €4,370 = **€43,700** (§3 floor reference) · financing 8%/5yr annual convention · electricity €0.15/kWh · aggregate throughput 500–827 tok/s (10 × the single-unit range).

**Financing:** `A = 43,700 × 0.08 / (1 − 1.08⁻⁵) = €10,946/yr`
**Electricity at 100% utilization:** `10 × 2,102.4 kWh × €0.15 = €3,154/yr`

At **70% utilization** (a plausible steady-state assumption, not a verified figure):
Electricity = €3,154 × 0.70 = €2,208/yr → **Total = €10,946 + €2,208 = €13,154/yr**

| Aggregate tok/s | Tokens/yr @ 70% util | Cost/M tokens |
|---|---|---|
| 500 | 500 × 31,536,000 × 0.70 = 11,037.6M | €13,154 ÷ 11,037.6 = **€1.19/M** |
| 827 | 827 × 31,536,000 × 0.70 = 18,266.2M | €13,154 ÷ 18,266.2 = **€0.72/M** |

**Per-member cost:** `€13,154/yr ÷ 12 months ÷ 50 members = €21.92/member/month`.

### CORRECTED: €42/member/month vs. ~€22/member/month were never competing estimates of the same thing

An earlier version of this section treated €42/member/month and this workbook's ≈€22/member/month DGX Spark rebuild as two conflicting measurements needing reconciliation. On 2026-08-13 the author clarified the actual origin of the €42 figure, which resolves this rather than leaving it open:

**€42/member/month was built on an illustrative €100,000-excluding-VAT capital assumption for a shared workstation-class machine (e.g., an NVIDIA DGX Station-type system) — never on DGX Spark pricing, and never on any verified retail price, since NVIDIA does not publish one for that class of machine** (**[FACT]** — nvidia.com/en-us/products/workstations/dgx-station/, checked 2026-08-13: the DGX Station product page has no listed price and directs buyers to a partner/marketplace). At 50 members sharing a €2,092/month total cost base (€1,957/month financing on €100,000 at 6.5%/5yr, plus €108/month electricity at an illustrative 1kW average draw, plus €27/month cooling/power overhead), €42/member/month is simple, fully auditable arithmetic — see the Token-Factory Scenario Workbook (Release Asset #10), §1a, for the complete worked recomputation.

**This workbook's ≈€22/member/month figure describes a different, cheaper hardware tier** — 10× NVIDIA DGX Spark units at $4,699 each, not a €100,000 workstation-class system. The two figures were never meant to converge, because they price different equipment. There is no remaining gap to explain: **both are correct for the specific machine and member count each one assumes.**

**Boundary note:** repeated per requirement — both cooperative models above are editable scenario illustrations, not forecasts of actual cooperative running costs, and not financial or procurement advice. A reader evaluating a real cooperative must first decide which hardware tier (DGX Spark-class desktop devices vs. DGX Station-class shared workstation) fits their actual use case before either figure becomes meaningful.

---

## 7. Worked Model C — Humanoid robot working capacity, EUR

### 7a. The illustrative base case (already EUR-native — and explicitly a scenario, not a real product price)

**SCENARIO ASSUMPTION, restated plainly:** the €25,000 robot price used below is an illustrative example, not a verified market price for any specific real product (per source register cluster G). Down payment 20% (€5,000); €20,000 financed 5yr @ 8%, monthly convention.

**Financing (monthly convention):** `Monthly payment = 20,000 × 0.006667 / (1 − 1.006667⁻⁶⁰) = €405.5/month → €4,866/yr`
Down payment spread over 5 years: €5,000 ÷ 5 = €1,000/yr
**Total capital + financing cost = €4,866 + €1,000 = €5,866/yr**
Electricity: €0.10/operating hour (SCENARIO ASSUMPTION, bundles an unstated power-draw figure — not separately verified)
Maintenance reserve: €2,500/yr (10% of purchase price, SCENARIO ASSUMPTION)

| Annual productive hours | Cost/h (financing + electricity only) | Cost/h (incl. maintenance) |
|---|---|---|
| 2,000 | €5,866/2,000 + €0.10 = **€3.03** | + €2,500/2,000 = **€4.28** |
| 4,000 | €5,866/4,000 + €0.10 = **€1.57** | + €2,500/4,000 = **€2.19** |
| 6,000 | €5,866/6,000 + €0.10 = **€1.08** | + €2,500/6,000 = **€1.49** |
| 8,000 | €5,866/8,000 + €0.10 = **€0.83** | + €2,500/8,000 = **€1.15** |

Formula: `Cost/h = (annual financing+down-payment cost ÷ annual hours) + electricity/h [+ maintenance/annual hours]`.

### 7b. Real-market price cross-check (converted to EUR at the §1 FX assumption)

| Platform | USD price | Class | EUR equivalent (× 0.93) |
|---|---|---|---|
| Unitree G1 (entry) | $13,500 | **OBSERVED FACT** (official Unitree page) | €12,555 |
| 1X NEO (early-access) | $20,000 (or $499/month subscription) | ATTRIBUTED STATEMENT (Engadget, corroborated by several outlets; not confirmed on 1X's own pricing page in the content fetched) | €18,600 |
| Tesla Optimus (long-term target, no commercial price yet) | $20,000–$30,000 | ATTRIBUTED STATEMENT (repeated Musk target; Tesla has not opened orders as of 2026-08-12) | €18,600–€27,900 |
| Figure 03 (rumored target, unofficial) | ~$20,000 | ATTRIBUTED STATEMENT (third-party aggregators only; Figure AI publishes no price) | €18,600 |
| Agility Digit (outright purchase) | ~$250,000 | ATTRIBUTED STATEMENT (convergent secondary sources; no primary Agility price sheet found) | €232,500 |

**INTERPRETATION:** the €25,000 illustrative figure used in §7a sits within, but toward the lower-middle of, the real observed/targeted market range once converted to EUR — close to Unitree G1's real price, well below Agility Digit's enterprise price, and in the same band as Tesla's/Figure's unconfirmed consumer targets. This does not mean €25,000 is "the" correct robot price; it means the illustration is not wildly unrealistic as a placeholder.

### 7c. Re-run using a real observed price (Unitree G1, €12,555) instead of the illustrative €25,000

Down payment 20% = €2,511; financed €10,044, 5yr @ 8% monthly convention.
**Financing:** `10,044 × 0.020275/month = €203.7/month → €2,444/yr`; down-payment spread = €2,511/5 = €502/yr → **Total = €2,946/yr**
Maintenance reserve (10%): €1,255/yr. Electricity: same €0.10/h placeholder (G1's actual power draw was not separately verified — reader should substitute if known).

| Annual productive hours | Cost/h (financing + electricity) | Cost/h (incl. maintenance) |
|---|---|---|
| 2,000 | €1.57 | €2.20 |
| 4,000 | €0.84 | €1.15 |
| 6,000 | €0.59 | €0.80 |
| 8,000 | €0.47 | €0.63 |

**Boundary note (repeated, as required for every scale/investment-type scenario in this document):** both §7a and §7c are editable illustrations built on stated assumptions about price, financing, utilization, and electricity — not forecasts, and not investment, procurement, or operational advice. Real total cost of ownership would also include supervision, software/subscription fees, insurance, workspace adaptation, consumables, and downtime, none of which are modeled here.

---

## 8. Economic-layer separation, illustrated with the localized Home AI Factory (§5) numbers at 34.6 tok/s, 100% utilization

Per the project's required methodology, these layers are never collapsed into one number. **Corrected 2026-08-13:** an earlier version of this section used tok/s = 65 as the "midpoint of the 50–83 range" — but 83 tok/s did not trace to any source in this project's register (see §5's correction) and has been removed. Using tok/s = 34.6 (midpoint of the confirmed 30.8–38.4 tok/s range from §5) for a single readable worked path:

`Tokens/yr @ 100% = 34.6 × 31,536,000 = 1,091.1M`

| Layer | What's included | Formula | Result (€/M tokens) | Class |
|---|---|---|---|---|
| 1. Raw energy cost | Electricity only | €315 ÷ 1,091.1M | **€0.289/M** | DERIVED CALCULATION |
| 2. Hardware-amortized production cost | + straight-line capital depreciation (€4,370 ÷ 5yr = €874/yr, no interest) | (€874+€315) ÷ 1,091.1M | **€1.090/M** | DERIVED CALCULATION |
| 3. Financed asset cost | Straight-line capital replaced with 8%/5yr financed payment (€1,095/yr) | (€1,095+€315) ÷ 1,091.1M | **€1.292/M** | DERIVED CALCULATION |
| 4. Full operating infrastructure cost | + illustrative 5%/yr of capital for support/software/space (€218.5/yr, SCENARIO ASSUMPTION) | (€1,095+€315+€218.5) ÷ 1,091.1M | **€1.492/M** | DERIVED CALCULATION on a SCENARIO ASSUMPTION input |
| 5. Capacity/utilisation cost | Same stack, but at 50% utilization instead of 100% (fixed costs unchanged, electricity and tokens both halve) | (€1,095+€218.5+€157.5) ÷ 545.6M | **€2.696/M** | DERIVED CALCULATION — shows utilization sensitivity |
| 6. Token production cost | = the €/M-token figure itself at whichever layer/utilization you've chosen | — | (one of the above) | DERIVED CALCULATION |
| 7. Workload / AI-working-capacity cost | Convert token cost into a cost per usage-band hour, using illustrative usage-intensity bands (chat/advisor 10k–30k tokens/hr; copilot 60k–120k; delegated agent 200k–600k; heavy multi-agent 1M–12M+ tokens/hr — bands drawn from the project's own conceptual framework, not independently re-verified per-band in this pass) | tokens/hr × (€/M-token rate) ÷ 1,000,000 | e.g. at €1.492/M and 60k tokens/hr: €0.090/hr; at 1M tokens/hr: €1.49/hr | DERIVED CALCULATION on an unverified band assumption |
| 8. Outcome and value | Whether that hour of AI working capacity produced anything worth more, less, or nothing compared to its cost | **not mechanically derived from layers 1–7** | — | INTERPRETATION only — value can be positive, zero, or negative; more tokens/hours is not automatically better |

---

## 9. Brief industrial-tier note (GB300 NVL72 scale), EUR, for completeness

This workbook's main localization focus is the home/cooperative/robot tiers above, since those are what an individual or SME reader would actually price locally. For completeness, two industrial-scale facts and their key caveats, restated in EUR terms:

- **OBSERVED FACT:** NVIDIA's own MLPerf v6.0 submission recorded **2,494,310 tokens/sec ("2.5M tok/s") on DeepSeek-R1** — but this is an aggregate across **four interconnected GB300 NVL72 systems (288 GPUs total)**, not a single 72-GPU rack. Per-GPU throughput for one rack in the Offline scenario was 9,821 tokens/sec/GPU. (developer.nvidia.com blog, checked 2026-08-12.)
- **CORRECTED — now VERIFIED, with scope caveat:** the "$0.123/M tokens" figure is confirmed directly on NVIDIA's own site: GB300 NVL72 delivers inference at **$0.123 per million tokens at 116 tokens/sec/user, using NVIDIA Dynamo and TensorRT-LLM**, per SemiAnalysis InferenceX benchmarks as of April 2026 (**[FACT]** — nvidia.com/en-gb/solutions/ai/inference/, checked 2026-08-13). This applies specifically to a **72-GPU rack-scale system at that interactivity setting** — it must not be used to price a single workstation, a DGX Spark, or a DGX Station; doing so would understate that tier's real cost by roughly two to three orders of magnitude (see §6's cooperative reconciliation above, which corrects exactly this kind of cross-tier mixing). The separately-cited "2.8M tok/s/MW" GB300 throughput figure remains **UNVERIFIABLE** — it could not be located verbatim on SemiAnalysis's InferenceX site as of this check; the closest confirmed adjacent data points there are roughly 1.67M–3.89M tok/s/MW depending on the interactivity point chosen.
- **Illustrative-only, EUR-converted capex reference (explicitly not official NVIDIA pricing — analyst-estimate based):** ~$4M/rack ($16M for a 4-rack/288-GPU installation) × 0.93 FX = **≈€3.72M/rack (≈€14.9M for 288 GPUs)**, financed 5yr@8% → ≈€3.73M/yr financing payment. At 90% utilization and ~71 trillion tokens/yr, financing premium alone ≈ €0.0106/M tokens on top of depreciation — an order-of-magnitude sensitivity check, not a TCO claim.

**Boundary note:** as above — illustrative scenario only, not investment or procurement guidance, and explicitly built on an unverified analyst-style capex-per-rack estimate rather than an official NVIDIA price.

---

## 10. Quick-reference: the only cells you need to change to make this your own country's workbook

| Cell to edit | Where it appears | Current placeholder |
|---|---|---|
| FX rate | §1, all currency conversions | 1 USD = €0.93 |
| Home/prosumer electricity price | §5, §7 | €0.15/kWh |
| Industrial electricity price | §9 | €0.09/kWh |
| Financing rate & term | §5, §6, §7 | 8% / 5 years |
| Local hardware landed price (VAT+import+margin) | §3 | *blank — not modeled, get a real quote* |

Everything downstream of these five cells is a formula, shown explicitly in each section above, so changing any one of them re-derives every dependent number without needing to rebuild the model from scratch.

---

*This workbook is one of potentially many national/currency adaptations of the same underlying method. It is released under the same CC BY 4.0 license as the parent whitepaper. It is educational research and scenario analysis only — not investment, legal, tax, procurement, or policy advice.*