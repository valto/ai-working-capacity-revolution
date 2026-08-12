# Investment-Thesis Scenario Notes — Release Asset #12
### Companion to "Why Are They Spending Trillions on AI?" (CC BY 4.0)

**Status of this note:** These are educational scenario notes, not investment, procurement, tax, or policy advice. Every number below is either an OBSERVED FACT (cited to a primary source, checked on/around 2026‑08‑12), an ATTRIBUTED STATEMENT (a named person/org's claim, not independently proven), a DERIVED CALCULATION (shown with formula), a SCENARIO ASSUMPTION (an editable illustrative input, not a market figure), or an INTERPRETATION (a labelled possible reading of the above). This boundary applies separately to **every tier section below** — none of the four tiers below is a recommendation to buy, build, or invest in anything.

**On the "global-baseline workbook" instruction:** the task asked me to cite the companion global-baseline workbook's cost figures rather than re-deriving them. I do not have that workbook as a file in front of me in this task — only the project's shared background research corpus (the unverified assumptions/derivations block under "OWNERSHIP / PRODUCTION COST-CURVE MODEL" in the task's background material). I am treating those already-computed ranges as the provisional baseline and citing them as such below, doing only the token→hour conversion here. **Before publication, these ranges must be reconciled against the actual global-baseline workbook release asset** — if the two differ, the workbook is authoritative, not this note.

### Evidence-class legend
| Code | Meaning |
|---|---|
| OBSERVED FACT | Checked against a live/primary source on or immediately before 2026-08-12 |
| ATTRIBUTED STATEMENT | A named person/org's on-record claim; not independently proven |
| DERIVED CALCULATION | Transparent arithmetic from cited inputs; formula shown |
| SCENARIO ASSUMPTION | Editable illustrative parameter, not a market figure |
| INTERPRETATION | Labelled possible reading connecting facts/statements/scenarios |

---

## Tier 1 — Home (single-device compute)

A home-scale "factory" is one prosumer AI workstation (illustrative reference device: NVIDIA DGX Spark) run by an individual or household for personal/small-project use. The economics only make sense if the owner's own usage — or a small resold/shared slice of it — is high enough, and steady enough, to absorb the fixed financing cost; below is a short scenario table, not a recommendation.

| Item | Value | Class |
|---|---|---|
| Reference device | NVIDIA DGX Spark, GB10 Superchip, 128GB unified memory | OBSERVED FACT — nvidia.com/en-us/products/workstations/dgx-spark/, checked 2026-08-12 |
| Capital required (current MSRP) | $4,699 (Founders Edition; raised from $3,999 in Feb 2026) | OBSERVED FACT — NVIDIA Developer Forums price-change notice, checked 2026-08-12 |
| Illustrative financed capital+electricity cost | ~$1,600/yr (5yr @ 8% financing + ~$420/yr electricity at $0.20/kWh, 240W continuous) | SCENARIO ASSUMPTION / DERIVED CALCULATION — formula: (loan payment on $4,699 @ 8%/5yr) + (0.24 kW × 8,760h × utilization × $0.20/kWh); see global-baseline workbook for full derivation |
| Cost per M tokens (near-full utilization) | ~$0.6–$2/M tokens | DERIVED CALCULATION cited from background cost-curve model, not re-derived here |
| $/AI-working-hour (chat/copilot bands, 10K–120K tokens/hr) | ~$0.006–$0.24/hr | DERIVED CALCULATION — formula: $/hr = ($/M tokens) × (tokens/hour ÷ 1,000,000); e.g. $2/M × 120,000/1,000,000 = $0.24/hr |

**Demand-side factors that would justify it:** sustained personal or small-team usage well above occasional-chat levels (i.e., regular coworker/copilot-band use, not sporadic queries); a privacy, latency, or offline-availability requirement that API access can't meet; willingness to run open-weight models rather than paying frontier-lab retail API prices for the same workload.

**Key risks:** hardware depreciates against a fast-moving frontier (a device bought today may be capability-obsolete before it's financially amortized); community-reported throughput (e.g., the DGX Spark Qwen3.5-122B-A10B forum benchmark, ATTRIBUTED STATEMENT, ~38.4 tok/s confirmed / ~51 tok/s claimed-but-unverified) is well below what enterprise-grade racks achieve, so per-token cost is structurally higher than larger tiers; idle time is pure sunk cost since financing accrues whether or not the device is used.

**What would have to be true for this tier to make sense:** the owner's actual usage must land near the top of the "active copilot" band or above, consistently, for multiple years — occasional or exploratory use makes retail API pricing from a frontier lab (Section B pricing, OBSERVED FACT) cheaper than owning hardware. This is a scenario illustration of a break-even logic, not a claim that home ownership beats renting for any particular buyer.

*Non-advice boundary: this tier's numbers are an editable illustration of a break-even structure, not a recommendation to purchase a DGX Spark or any other device.*

---

## Tier 2 — Cooperative (shared multi-device, e.g. 10-unit / 50-member pool)

A cooperative factory pools capital across members (illustrative: 50 members financing ~10 DGX-Spark-class units) to get below individual per-unit cost through shared utilization, at the cost of coordination overhead and a governance/access-allocation problem. Two independently-produced figures for the same idea exist in the source material and should be shown side by side rather than reconciled away.

| Item | Value | Class |
|---|---|---|
| Illustrative capital (10 units at current DGX Spark MSRP) | ~$46,990 | DERIVED CALCULATION — 10 × $4,699 (OBSERVED FACT unit price) |
| Financed capital + electricity (5yr @ 8%, ~$2–4K/yr power) | ~$14,000–15,000/yr before admin/networking | SCENARIO ASSUMPTION / DERIVED CALCULATION, cited from background model |
| Cost per M tokens (~70% utilization) | ~$0.77–$1.20/M tokens | DERIVED CALCULATION cited from background cost-curve model |
| $/AI-working-hour (copilot–delegated bands, 60K–600K tokens/hr) | ~$0.046–$0.72/hr | DERIVED CALCULATION — formula as above; e.g. $1.20/M × 600,000/1,000,000 = $0.72/hr |
| DGX Spark cooperative recomputation | ~€19.50–23/member/month (50 members, 10 units) | DERIVED CALCULATION, same background model |
| Author's own published cooperative-cost figure (DGX Station-class tier) | ~€42/member/month (50 members); ~€21/member/month (100 members) | DERIVED CALCULATION on an illustrative €100,000-excluding-VAT capital assumption for a shared workstation-class machine — CORRECTED 2026-08-13: not a DGX Spark-based figure, and not based on any published NVIDIA list price (NVIDIA publishes no retail price for DGX Station-class systems) |

**Corrected (2026-08-13): the two figures describe different hardware tiers, not a discrepancy in one estimate.** €42/member/month prices a single, larger shared workstation-class machine (illustrative €100,000 capital base) split across 50 members; €19.50–23/member/month prices a pool of 10 much smaller NVIDIA DGX Spark units ($4,699 each, verified current price) split across the same member count. Both are internally consistent scenario outputs for the hardware tier each one actually describes — see the Token-Factory Scenario Workbook (Release Asset #10) §1a/§1b for the full corrected build.

**Demand-side factors that would justify either tier:** enough members with genuinely complementary usage schedules (peak-shaving each other) to keep aggregate utilization high; a shared trust/governance structure that can fairly allocate scarce capacity at peak; a cooperative's usage profile skewing toward the copilot/delegated bands rather than occasional chat (per-capita chat-only usage does not amortize shared hardware well).

**Key risks:** free-rider and allocation-fairness problems (heavy users vs. light payers); coordination/admin overhead not fully modeled in either headline figure above; membership churn destabilizing the utilization assumption both tiers depend on; choosing the wrong hardware tier for actual member demand (a DGX Spark pool may under-serve members needing large-context or trillion-parameter-class local inference, while a single DGX-Station-class machine may be underutilized for a cooperative whose members mostly need light, parallel, low-context workloads).

**What would have to be true for this tier to make sense:** whichever tier (DGX Spark pool, ~€19.50–23/member/month, or a shared DGX-Station-class machine, ~€42/member/month at 50 members / ~€21 at 100) is chosen must beat the member's realistic alternative — either individual home ownership (Tier 1) or metered API/cloud access — at that member's actual usage level and actual capability needs (memory/context size, model scale, concurrency), not at an assumed average.

*Non-advice boundary: the cooperative figures above are illustrative scenario computations for two different hardware tiers, not a validated cooperative-formation business case.*

---

## Tier 3 — Professional / SME (dedicated business-scale capacity)

This tier sits between the cooperative and hyperscale tiers and is the least precisely bounded in the current source material — treat it as a scenario sketch, not a derived model. It covers a business, agency, or mid-size enterprise that needs dedicated, higher-interactivity inference capacity beyond what a cooperative pool typically delivers, either by owning enterprise-grade hardware or, more commonly, by contracting dedicated cloud/co-location capacity.

| Item | Value | Class |
|---|---|---|
| Capital path A — owned enterprise hardware | Single/few NVIDIA HGX B300 (8× Blackwell Ultra GPU) nodes or a GB300 NVL72 rack; illustrative rack capital ~$4M/rack is an unofficial analyst-style estimate carried in the source model, **not** an NVIDIA-published price | SCENARIO ASSUMPTION — explicitly not official pricing |
| Capital path B — contracted dedicated capacity | Example of scale: IBM Cloud + Together AI multi-year $240M agreement for a dedicated NVIDIA HGX B300 inference cluster, available Q1 2027 | OBSERVED FACT — IBM Newsroom press release, Aug 11 2026, checked 2026-08-12 (this is a shared/multi-customer deal illustrating the scale of the professional-tier market, not one buyer's own spend) |
| Cost per M tokens (GB300-class, interactivity-dependent) | ~$0.065–$3.3/M tokens across the interactivity curve (low-latency to high-throughput settings); the specific "$0.123/M tokens at 116 tok/s/user" point is now CONFIRMED directly on NVIDIA's own site (nvidia.com/en-gb/solutions/ai/inference/, checked 2026-08-13), attributed to SemiAnalysis InferenceX benchmarks (April 2026), using NVIDIA Dynamo and TensorRT-LLM | OBSERVED FACT — corrected 2026-08-13 (previously flagged UNVERIFIABLE from an InferenceX-only check). **This figure describes the 72-GPU GB300 NVL72 rack tier only — it must not be applied to the Professional tier's smaller HGX B300 (8-GPU) node above, or to any workstation/desktop-class hardware.** |
| $/AI-working-hour (delegated-agent band, 200K–600K tokens/hr) | ~$0.013–$1.98/hr, wide range driven mainly by interactivity choice | DERIVED CALCULATION — formula: $/hr = ($/M tokens) × (tokens/hour ÷ 1,000,000); low end 0.065×0.2=$0.013, high end 3.3×0.6=$1.98 |

**Demand-side factors that would justify it:** a business whose product genuinely requires high-interactivity, low-latency inference at volume (not just occasional use); a workload profile matching the delegated-agent or early multi-agent band rather than light chat; a compliance, data-residency, or customization need that off-the-shelf frontier-lab APIs (Section B pricing) don't meet as cheaply at that volume.

**Key risks:** the cost-per-token curve is highly sensitive to the interactivity setting chosen (a >50x range across the same hardware, per SemiAnalysis's own live data) — an under-specified workload assumption can make the investment case look far better or worse than reality; owned-hardware capital estimates in this tier ($4M/rack) are analyst-style, unofficial, and could be materially wrong; committing to a multi-year dedicated-capacity contract (Capital path B) locks in today's hardware generation against a fast-depreciating performance curve (Vera Rubin-class hardware is already claimed, per NVIDIA's own marketing — an ATTRIBUTED STATEMENT, not independently proven — to cut cost per token by up to 10x versus GB200).

**What would have to be true for this tier to make sense:** the business's actual, sustained token volume and required interactivity level must be known (not guessed) before comparing owned/dedicated capacity against renting frontier-lab APIs or cooperative-tier access; absent that, this tier is easy to over- or under-invest in.

*Non-advice boundary: this tier is the least-verified of the four sketches here and should not be used to size any real capital commitment; it illustrates a cost-and-risk shape, not a business case.*

---

## Tier 4 — Hyperscale (multi-gigawatt AI infrastructure)

This tier is the one explicitly discussed by named financial and industry executives (Jensen Huang, Larry Fink, and five other CEOs on CNBC, Aug 10 2026) as the target of new multi-hundred-billion-dollar financing structures. Everything about scale, deployment intent, and total future capital here comes from named, on-the-record but forward-looking statements — not from an audited market total.

| Item | Value | Class |
|---|---|---|
| Newly announced financing structure | Six MOUs (Apollo, Blackstone, BlackRock, Brookfield, Goldman Sachs, KKR) aiming to mobilize >$500B in third-party capital for hyperscalers, frontier labs, and enterprises | OBSERVED FACT — CNBC transcript & article, Aug 10 2026, corroborated by Fortune, checked 2026-08-12 |
| Per-gigawatt build cost | "something like $50, $60 billion" per gigawatt (energy, land, power/shell, compute) | ATTRIBUTED STATEMENT — Jensen Huang, CNBC broadcast, Aug 10 2026; independent analyst estimates found via search (Morgan Stanley ~$49B/GW, Bernstein ~$35B/GW, Foxconn ~$47B/GW, Epoch.ai ~$38B/GW) bracket this as plausible-to-high, not confirmed |
| Longer-run capital scale | "trillions of dollars over the coming years"; >70GW of new US power demand implied | ATTRIBUTED STATEMENT — Larry Fink, same broadcast; directionally consistent with, but not identical to, independent BCG (50–80GW US shortfall by 2030) and S&P Global (64.4GW hyperscale draw in 2025) figures found via aggregated search, not individually re-verified |
| Cost per M tokens — electricity-only floor | ~$0.0063/M tokens (DeepSeek-R1, GB300 NVL72 cluster benchmark, illustrative $0.10/kWh) | DERIVED CALCULATION cited from background model, itself built on NVIDIA's own MLPerf v6.0 result of 2,494,310 tok/s aggregate across 288 GPUs / 4 racks (OBSERVED FACT, NVIDIA developer blog, checked 2026-08-12) — note this is a 4-rack aggregate, not one rack |
| Cost per M tokens — full infrastructure TCO | ~$0.065–$0.40/M tokens at typical interactivity points (the oft-cited "$0.123" point is UNVERIFIABLE as an exact published figure but sits within this observed range) | OBSERVED FACT-adjacent, SemiAnalysis InferenceX live data, checked 2026-08-12 |
| $/AI-working-hour (heavy multi-agent band, 1M–12M+ tokens/hr) | ~$0.0063–$4.8/hr across the electricity-floor-to-full-TCO and low-to-high orchestration range | DERIVED CALCULATION — formula: $/hr = ($/M tokens) × (tokens/hour ÷ 1,000,000); low end 0.0063×1=$0.0063, high end 0.40×12=$4.80 |

**Demand-side factors that would justify it (as argued by the named executives, not verified independently):** Huang's claim that "AI tokens are... incredibly profitable" for frontier labs (ATTRIBUTED STATEMENT); OpenAI's own internal telemetry that Codex now accounts for 99.8% of its weekly internal output tokens and that heavy internal users run 60+ agent-hours/day (ATTRIBUTED STATEMENT, OpenAI's own self-reported, unaudited data, per its June 2026 blog post); Altman's blog-post claim that AI cost falls ~10x every 12 months, which he links to a Jevons-paradox-style demand response (ATTRIBUTED STATEMENT, not a demand-growth-rate figure despite sometimes being paraphrased as one).

**Key risks:** the entire financing thesis rests on forward-looking, on-the-record but unaudited statements by the parties who benefit from the capital being raised (Huang sells the chips; Fink's firm would help place the capital); the $50–60B/GW figure is Huang's own stated estimate, at the higher end of independent analyst ranges, not an audited cost; hardware depreciation risk is structural at this scale too — NVIDIA's own Vera Rubin marketing claims up to 10x more tokens/MW than GB200 (ATTRIBUTED STATEMENT), meaning capacity committed today at GB300-era economics could be underpriced relative to next-generation hardware within the financing structure's own multi-year horizon; the >70GW US power-demand figure requires real-world grid buildout that is itself contested and slow-moving infrastructure, independent of capital availability.

**What would have to be true for this tier to make sense:** token demand growth and per-token profitability for frontier labs would need to continue at something resembling the rates Altman and Huang describe, for years, across multiple hardware generations, without a sustained collapse in per-token pricing outpacing the offsetting demand growth — none of which is independently provable today; it is a bet on the ATTRIBUTED STATEMENTS above being directionally correct, not settled fact.

*Non-advice boundary: nothing in this tier's table or discussion is a signal to invest in, lend to, or contract with any of the named companies, executives, or financing vehicles; it summarizes what named parties have publicly claimed and what independent benchmarks show, for educational purposes only.*

---

**Cross-tier note (INTERPRETATION):** moving from home → hyperscale trades falling $/M-token cost for rising capital concentration, rising dependence on named-party forward statements rather than independently audited figures, and a shift from individual/small-group control (Tiers 1–2) toward financing structures controlled by a small number of infrastructure and asset-management firms (Tier 4) — this concentration-vs-cost tradeoff is the same ownership-architecture question raised elsewhere in the whitepaper, not a separate finding.

---

Files/paths relevant to this task: none were created outside this response — this deliverable is the requested Investment-Thesis Scenario Notes text itself (release asset #12). No workbook file was available in this environment to cite directly; the note explicitly flags that its cost figures are provisional pending reconciliation against the actual global-baseline workbook.