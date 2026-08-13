# Investment-Thesis Scenario Notes — Release Asset #12
### Companion to "Why Are They Spending Trillions on AI?" (Valto Loikkanen, CC BY 4.0)

**Status of this note:** These are educational scenario notes, not investment, procurement, tax, or policy advice. Every number below is either an OBSERVED FACT (cited to a primary source), an ATTRIBUTED STATEMENT (a named person/org's claim, not independently proven), a DERIVED CALCULATION (shown with formula), a SCENARIO ASSUMPTION (an editable illustrative input, not a market figure), or an INTERPRETATION (a labelled possible reading of the above). This boundary applies separately to **every tier section below** — none of the four tiers below is a recommendation to buy, build, or invest in anything.

**Canonical source note (2026-08-13):** every cost figure below is cited directly from the Global Baseline Workbook (Release Asset #7) and the AI Working-Capacity Conversion Workbook (Release Asset #9) — the two workbooks that carry this paper's authoritative production-cost curves — rather than re-derived here. Where an earlier draft of this note used provisional or differently-sourced figures, those have been replaced with the canonical numbers.

### Evidence-class legend
| Code | Meaning |
|---|---|
| OBSERVED FACT | Checked against a live/primary source |
| ATTRIBUTED STATEMENT | A named person/org's on-record claim; not independently proven |
| DERIVED CALCULATION | Transparent arithmetic from cited inputs; formula shown |
| SCENARIO ASSUMPTION | Editable illustrative parameter, not a market figure |
| INTERPRETATION | Labelled possible reading connecting facts/statements/scenarios |

---

## Tier 1 — Home (single-device compute)

A home-scale "factory" is one prosumer AI workstation (illustrative reference device: NVIDIA DGX Spark) run by an individual or household for personal/small-project use. The economics only make sense if the owner's own usage — or a small resold/shared slice of it — is high enough, and steady enough, to absorb the fixed financing cost; below is a short scenario table, not a recommendation.

| Item | Value | Class |
|---|---|---|
| Reference device | NVIDIA DGX Spark, GB10 Superchip, 128GB unified memory | OBSERVED FACT — nvidia.com/en-us/products/workstations/dgx-spark/ |
| Capital required (current MSRP) | $4,699 (Founders Edition; raised from $3,999 in Feb 2026) | OBSERVED FACT — NVIDIA Developer Forums price-change notice |
| Illustrative financed capital+electricity cost | ~$1,129/yr (5yr @ 8% financing) + $25–$210/yr electricity depending on utilization/price scenario | DERIVED CALCULATION — see Global Baseline Workbook §2.1–2.2 for the full derivation |
| Cost per M tokens, full utilization range (low/mid/high scenarios) | **$1.37–$11.89/M tokens** (best case: 38.4 tok/s, 80% utilization; worst case: 30.8 tok/s, 10% utilization) | DERIVED CALCULATION, canonical figure per Global Baseline Workbook §2.4 |
| $/AI-working-hour, mid scenario ($3.17/M tokens, 30.8 tok/s, 40% utilization) | Chat/advisor $0.032–$0.095/hr; active copilot $0.190–$0.380/hr; delegated agent $0.633–$1.900/hr; heavy orchestration $3.17–$38.00/hr | DERIVED CALCULATION, canonical figure per Global Baseline Workbook §2.5 |

**Versus retail API pricing (corrected 2026-08-13):** at best-case utilization, Home is cheaper than every retail tier except OpenAI's cheapest (Luna); at worst-case utilization, Home is more expensive than most retail tiers except the priciest ones (Sol, Fable 5). This is a genuine range, not a fixed multiplier in either direction — see Global Baseline Workbook §7 for the full corrected comparison table.

**Demand-side factors that would justify it:** sustained personal or small-team usage well above occasional-chat levels (i.e., regular coworker/copilot-band use, not sporadic queries); a privacy, latency, or offline-availability requirement that API access can't meet; willingness to run open-weight models rather than paying frontier-lab retail API prices for the same workload.

**Key risks:** hardware depreciates against a fast-moving frontier (a device bought today may be capability-obsolete before it's financially amortized); community-reported throughput (the DGX Spark Qwen3.5-122B-A10B forum benchmark, ATTRIBUTED STATEMENT, ~38.4 tok/s confirmed / ~51 tok/s claimed-but-unverified) is well below what enterprise-grade racks achieve, so per-token cost is structurally higher than larger tiers; idle time is pure sunk cost since financing accrues whether or not the device is used; utilization is the single biggest lever on cost (a ~7x swing between 10% and 80% utilization at the same throughput, per Global Baseline Workbook §2.4).

**What would have to be true for this tier to make sense:** the owner's actual usage must land near the top of the "active copilot" band or above, consistently, for multiple years, at a utilization rate that keeps $/M-tokens well below the $11.89 worst-case figure — occasional or exploratory use makes retail API pricing from a frontier lab cheaper than owning hardware in most scenarios. This is a scenario illustration of a break-even logic, not a claim that home ownership beats renting for any particular buyer.

*Non-advice boundary: this tier's numbers are an editable illustration of a break-even structure, not a recommendation to purchase a DGX Spark or any other device.*

---

## Tier 2 — Cooperative (shared multi-device or shared workstation-class machine)

A cooperative factory pools capital across members to get below individual per-unit cost through shared utilization, at the cost of coordination overhead and a governance/access-allocation problem. Two hardware tiers exist for this scenario, describing two different pieces of equipment, not two competing estimates of one thing.

| Item | Value | Class |
|---|---|---|
| **DGX Spark pool** — 10 units, 50 members | Capital ~$46,990; financed+electricity ~$14,000–15,770/yr before admin/networking | DERIVED CALCULATION — 10 × $4,699 (OBSERVED FACT unit price); see Global Baseline Workbook §3.1–3.4 |
| Cost per M tokens (DGX Spark pool, 20–85% utilization) | **$1.99–$7.62/M tokens** | DERIVED CALCULATION, canonical figure per Global Baseline Workbook §3.4 |
| $/member/month (DGX Spark pool, 50 members) | **$24.67–$27.40/member/month** | DERIVED CALCULATION, canonical figure per Global Baseline Workbook §3.5 |
| $/AI-working-hour, mid scenario ($3.20/M tokens) | Chat/advisor $0.032–$0.096/hr; active copilot $0.192–$0.384/hr; delegated agent $0.641–$1.922/hr; heavy orchestration $3.20–$38.44/hr | DERIVED CALCULATION, canonical figure per Global Baseline Workbook §3.6 |
| **Shared DGX Station-class machine** — 1 unit, 50 or 100 members | Capital, illustrative €100,000 excl. VAT (no official NVIDIA price exists for this class of machine); financed 5yr @ 6.5% | SCENARIO ASSUMPTION — see Token-Factory Scenario Workbook §1a for the full build |
| $/member/month (shared workstation-class machine) | **€42/member/month at 50 members; €21/member/month at 100 members** | DERIVED CALCULATION on the €100,000 illustrative base, per Token-Factory Scenario Workbook §1a |

**Both figures are correct for the hardware they describe, not competing estimates of one cooperative.** The DGX Spark pool prices ten smaller, independent desktop-class devices; the shared workstation-class machine prices one larger system with substantially more memory and compute per unit. See the Token-Factory Scenario Workbook (Release Asset #10) §1/§1a/§1b for the full corrected explanation of why these were never in conflict.

**Demand-side factors that would justify either tier:** enough members with genuinely complementary usage schedules (peak-shaving each other) to keep aggregate utilization high; a shared trust/governance structure that can fairly allocate scarce capacity at peak; a cooperative's usage profile skewing toward the copilot/delegated bands rather than occasional chat (per-capita chat-only usage does not amortize shared hardware well).

**Key risks:** free-rider and allocation-fairness problems (heavy users vs. light payers); coordination/admin overhead not fully modeled in either headline figure above; membership churn destabilizing the utilization assumption both tiers depend on; choosing the wrong hardware tier for actual member demand (a DGX Spark pool may under-serve members needing large-context or trillion-parameter-class local inference, while a single DGX-Station-class machine may be underutilized for a cooperative whose members mostly need light, parallel, low-context workloads).

**What would have to be true for this tier to make sense:** whichever tier is chosen (DGX Spark pool at $24.67–27.40/member/month, or a shared DGX-Station-class machine at €42/member/month at 50 members / €21 at 100) must beat the member's realistic alternative — either individual home ownership (Tier 1) or metered API/cloud access — at that member's actual usage level and actual capability needs (memory/context size, model scale, concurrency), not at an assumed average.

*Non-advice boundary: the cooperative figures above are illustrative scenario computations for two different hardware tiers, not a validated cooperative-formation business case.*

---

## Tier 3 — Professional / SME (dedicated business-scale capacity)

This tier sits between the cooperative and hyperscale tiers and is the least precisely bounded in the current source material — treat it as a scenario sketch, not a derived model. It covers a business, agency, or mid-size enterprise that needs dedicated, higher-interactivity inference capacity beyond what a cooperative pool typically delivers, either by owning enterprise-grade hardware or, more commonly, by contracting dedicated cloud/co-location capacity.

| Item | Value | Class |
|---|---|---|
| Capital path A — owned enterprise hardware | Single NVIDIA HGX B300 (8× Blackwell Ultra GPU) node; illustrative capex $250,000–$500,000 (mid $350,000) and power draw 8–15kW (mid 11kW) — **NVIDIA publishes no price or power spec for this SKU**, so both figures are explicitly placeholders | SCENARIO ASSUMPTION — explicitly not official pricing, per Global Baseline Workbook §4.1 |
| Capital path B — contracted dedicated capacity | Example of scale: IBM Cloud + Together AI multi-year $240M agreement for a dedicated NVIDIA HGX B300 inference cluster, available Q1 2027 | OBSERVED FACT — IBM Newsroom press release, Aug 11 2026 (this is a shared/multi-customer deal illustrating the scale of the professional-tier market, not one buyer's own spend) |
| Cost per M tokens, HGX B300 node (25–90% utilization) | **$0.044–$0.146/M tokens** — built on a DERIVED linear GPU-count scaling from OBSERVED per-GPU MLPerf figures, which the source workbook flags as an optimistic upper bound since it assumes an 8-GPU box reproduces NVL72 rack-scale per-GPU throughput | DERIVED CALCULATION, canonical figure per Global Baseline Workbook §4.3; low confidence on the underlying capex/power inputs |
| $/AI-working-hour, mid scenario ($0.064/M tokens) | Chat/advisor $0.0006–$0.0019/hr; active copilot $0.0038–$0.0076/hr; delegated agent $0.0127–$0.0382/hr; heavy orchestration $0.064–$0.764/hr | DERIVED CALCULATION, canonical figure per Global Baseline Workbook §4.4 |

**Important scope note:** the $0.044–$0.146/M-tokens range above is specific to the Professional tier's smaller HGX B300 (8-GPU) node. It must not be confused with the Hyperscale tier's $0.123/M-tokens figure (confirmed directly on NVIDIA's own site, 2026-08-13) or the broader $0.065–$3.3/M-tokens GB300 interactivity curve — those describe the 72-GPU GB300 NVL72 rack, a different, larger hardware tier (Tier 4 below).

**Demand-side factors that would justify it:** a business whose product genuinely requires high-interactivity, low-latency inference at volume (not just occasional use); a workload profile matching the delegated-agent or early multi-agent band rather than light chat; a compliance, data-residency, or customization need that off-the-shelf frontier-lab APIs don't meet as cheaply at that volume.

**Key risks:** the underlying capex and power-draw inputs for this tier are unverified placeholders (no public NVIDIA/reseller price exists for the HGX B300 node), so this tier's whole cost curve carries materially lower confidence than Tiers 1, 2, or 4; committing to a multi-year dedicated-capacity contract (Capital path B) locks in today's hardware generation against a fast-depreciating performance curve (Vera Rubin-class hardware is already claimed, per NVIDIA's own marketing — an ATTRIBUTED STATEMENT, not independently proven — to cut cost per token by up to 10x versus GB200, though SemiAnalysis's independent analysis is more conservative at roughly 2–5.4x).

**What would have to be true for this tier to make sense:** the business's actual, sustained token volume and required interactivity level must be known (not guessed) before comparing owned/dedicated capacity against renting frontier-lab APIs or cooperative-tier access; a verified HGX B300 price/power quote should replace the placeholder inputs above before this tier is used for any real sizing exercise.

*Non-advice boundary: this tier is the least-verified of the four sketches here and should not be used to size any real capital commitment; it illustrates a cost-and-risk shape, not a business case.*

---

## Tier 4 — Hyperscale (multi-gigawatt AI infrastructure)

This tier is the one explicitly discussed by named financial and industry executives (Jensen Huang, Larry Fink, and five other CEOs on CNBC, Aug 10 2026) as the target of new multi-hundred-billion-dollar financing structures. Everything about scale, deployment intent, and total future capital here comes from named, on-the-record but forward-looking statements — not from an audited market total.

| Item | Value | Class |
|---|---|---|
| Newly announced financing structure | Six MOUs (Apollo, Blackstone, BlackRock, Brookfield, Goldman Sachs, KKR) aiming to mobilize >$500B in third-party capital for hyperscalers, frontier labs, and enterprises | OBSERVED FACT — CNBC transcript & article, Aug 10 2026, corroborated by Fortune |
| Per-gigawatt build cost | "something like $50, $60 billion" per gigawatt (energy, land, power/shell, compute) | ATTRIBUTED STATEMENT — Jensen Huang, CNBC broadcast, Aug 10 2026; independent analyst estimates (Morgan Stanley ~$49B/GW, Bernstein ~$35B/GW, Foxconn ~$47B/GW, Epoch.ai ~$38B/GW) bracket this as plausible-to-high, not confirmed |
| Longer-run capital scale | "trillions of dollars over the coming years"; >70GW of new US power demand implied | ATTRIBUTED STATEMENT — Larry Fink, same broadcast; directionally consistent with, but not identical to, independent BCG (50–80GW US shortfall by 2030) and S&P Global (64.4GW hyperscale draw in 2025) figures |
| Cost per M tokens — full production cost curve, 25–90% utilization | **$0.091–$0.312/M tokens (canonical mid: $0.133/M)** — capital + financing + electricity + opex, all layers included | DERIVED CALCULATION, canonical figure per Global Baseline Workbook §5.6 |
| Cross-check: NVIDIA's own confirmed figure | $0.123/M tokens at 116 tokens/sec/user, using NVIDIA Dynamo and TensorRT-LLM, attributed to SemiAnalysis InferenceX (April 2026) | OBSERVED FACT — confirmed directly on nvidia.com/en-gb/solutions/ai/inference/, checked 2026-08-13; sits within the canonical range above, at a specific interactivity point |
| $/AI-working-hour (heavy multi-agent band, 1M–12M+ tokens/hr, full range) | **$0.091–$3.74/hr** across the low-to-high utilization range | DERIVED CALCULATION — formula: $/hr = ($/M tokens) × (tokens/hour ÷ 1,000,000); low end 0.091×1=$0.091, high end 0.312×12=$3.74 |

**Demand-side factors that would justify it (as argued by the named executives, not verified independently):** Huang's claim that "AI tokens are... incredibly profitable" for frontier labs (ATTRIBUTED STATEMENT); OpenAI's own internal telemetry that Codex now accounts for 99.8% of its weekly internal output tokens (ATTRIBUTED STATEMENT, OpenAI's own self-reported, unaudited data); Altman's blog-post claim that AI cost falls ~10x every 12 months, which he links to a Jevons-paradox-style demand response (ATTRIBUTED STATEMENT, not a demand-growth-rate figure despite sometimes being paraphrased as one).

**Key risks:** the entire financing thesis rests on forward-looking, on-the-record but unaudited statements by the parties who benefit from the capital being raised (Huang sells the chips; Fink's firm would help place the capital); the $50–60B/GW figure is Huang's own stated estimate, at the higher end of independent analyst ranges, not an audited cost; hardware depreciation risk is structural at this scale too — capital committed today at GB300-era economics is being locked in against hardware that its own maker claims will be substantially cheaper per token within the same multi-year financing horizon; the >70GW US power-demand figure requires real-world grid buildout that is itself contested and slow-moving infrastructure, independent of capital availability.

**What would have to be true for this tier to make sense:** token demand growth and per-token profitability for frontier labs would need to continue at something resembling the rates Altman and Huang describe, for years, across multiple hardware generations, without a sustained collapse in per-token pricing outpacing the offsetting demand growth — none of which is independently provable today; it is a bet on the ATTRIBUTED STATEMENTS above being directionally correct, not settled fact.

*Non-advice boundary: nothing in this tier's table or discussion is a signal to invest in, lend to, or contract with any of the named companies, executives, or financing vehicles; it summarizes what named parties have publicly claimed and what independent benchmarks show, for educational purposes only.*

---

**Cross-tier note (INTERPRETATION):** moving from home → hyperscale trades falling $/M-token cost for rising capital concentration, rising dependence on named-party forward statements rather than independently audited figures, and a shift from individual/small-group control (Tiers 1–2) toward financing structures controlled by a small number of infrastructure and asset-management firms (Tier 4) — this concentration-vs-cost tradeoff is the same ownership-architecture question raised elsewhere in the whitepaper, not a separate finding.

---

This deliverable is Release Asset #12, part of the "Why Are They Spending Trillions on AI?" research package (CC BY 4.0, Valto Loikkanen).
