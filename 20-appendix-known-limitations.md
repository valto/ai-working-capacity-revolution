# Appendix — Known Limitations and Live Uncertainties

**Companion to:** "Why Are They Spending Trillions on AI?" (v1.0 research package)
**Factual source cut-off:** 2026-08-13

This appendix consolidates, in one place, the uncertainties this package's own evidence-class discipline surfaces throughout the whitepaper and workbooks. None of these are new findings — each is already flagged at the point of use — but a reader evaluating whether to trust this package's conclusions should be able to see the whole list at once rather than assembling it section by section. This is deliberately a limitations list, not a defects list: the items below are open questions the evidence cannot currently close, not errors to be fixed.

---

## 1. Model/hardware performance

- **DGX Spark throughput is a single unaudited community benchmark, not a vendor or peer-reviewed figure.** The confirmed 30.8–38.4 tok/s range (Qwen3.5-122B-A10B) comes from one forum thread; the further-claimed 51 tok/s ceiling traces to an unretrieved later post in the same thread and is treated as unconfirmed throughout. A different workload, a different quantization scheme, or a different model would very likely produce a different number.
- **The "$0.123/M tokens" GB300 figure applies at one specific interactivity setting (116 tok/s/user) on one specific 72-GPU rack configuration.** SemiAnalysis's own live dashboard shows a much wider range ($0.065–$3.3/M) depending on interactivity — any single cited figure from that dashboard should be treated as a point-in-time snapshot, not a fixed cost.
- **Vendor-claimed hardware-generation improvements (e.g., Nvidia's "up to 10x more tokens/MW" for Vera Rubin vs. GB200) are marketing claims from the seller of that hardware.** Independent benchmark-based estimates (SemiAnalysis: 2–5.4x) are lower and workload-dependent. Any capital commitment made today is a bet against a curve neither figure fully resolves.

## 2. Utilization

- **Utilization is the single largest lever in every cost model in this package** — and every utilization figure used (10%/40%/80% at Home, 20%/50%/85% at Cooperative, 60%/90% at Hyperscale) is a **Scenario Assumption chosen for illustration, not a measured or forecast real-world utilization rate** for any actual deployment. Real-world utilization for any specific facility is unknown until it is operated and measured.
- **No public utilization telemetry exists for any of this package's reference hardware tiers** (DGX Spark in the field, a real cooperative, a real HGX B300 node, or a real hyperscale rack under this paper's specific cost assumptions). OpenAI's own Codex telemetry (Section 16) describes OpenAI's internal usage of OpenAI's own product — not a general usage rate applicable to any of the hardware tiers modeled here.

## 3. Financing

- **All financing rates and terms (5yr/8%, 5yr/6.5%, financing-term sensitivity tables) are illustrative assumptions**, not quoted credit terms from any lender for any of the hardware described. Real financing terms vary by borrower, jurisdiction, collateral structure, and credit market conditions at the time of borrowing.
- **The financing-term trade-off (longer terms lower annual cost but lock in aging hardware for longer) is a real structural trade-off, but this package does not — and cannot — determine the "right" term for any actual buyer.** That depends on that buyer's own capital cost, risk tolerance, and expectations about the next hardware generation, none of which this package can observe.

## 4. Power/electricity pricing

- **Every electricity price used (from $0.06/kWh to $0.25/kWh, and the EUR-Finland localization's illustrative €0.09–€0.15/kWh) is a Scenario Assumption**, not a live-quoted commercial/industrial tariff for any specific location. Electricity prices vary enormously by country, tariff class, time of use, and contract structure — readers localizing this model should replace every rate with their own actual, dated quote.
- **The Hyperscale-tier and Professional-tier power-draw figures rest on a mix of OBSERVED hardware specs and ASSUMPTION-level facility/PUE overhead** that has no public, verified figure for the specific configurations modeled. Real hyperscale facility overhead varies by climate, cooling architecture, and facility age.

## 5. Adoption timing

- **This package makes no claim about when — or whether — the demand growth described by Altman, Huang, and Fink will materialize at the pace they describe.** The "roughly a millionfold token-consumption growth, 2019→2026" figure is a Derived Calculation from OpenAI's own reported usage figures at two points in time — it says nothing about the trajectory between or beyond those points, and Altman's own claim of a further millionfold expansion still to come is an Attributed Statement from an interested party, not an independently modeled forecast.
- **The financing commitments described in Part I (the >$500B Nvidia/six-firm MOUs) are real, signed commitments — but a signed MOU to mobilize capital is not the same as capital already deployed, infrastructure already built, or demand already realized.** This package does not track deployment against these commitments over time; a reader relying on this package for a current view of deployment progress should check for a more recent primary source.

## 6. The Professional tier specifically (the least-evidenced tier in this model)

- **NVIDIA publishes no public price or power-draw specification for the HGX B300 (8-GPU) node used as this tier's reference hardware.** Both capex and power draw for this tier are Scenario Assumptions, not Observed Facts — a materially different confidence level than the Home tier (OBSERVED $4,699 price) or the Hyperscale tier (OBSERVED rack specs, though still ASSUMPTION-level capex).
- **The Professional tier's headline $/M-token figure excludes the opex/overhead layer that the Hyperscale tier's canonical figure includes**, making a direct comparison between the two tiers structurally misleading unless the reader adds a comparable opex allowance (an illustrative sensitivity is provided in the Global Baseline Workbook, but it is itself unverified against any real 8-GPU-node opex figure).
- **No real reseller quote, deployment case study, or operational benchmark for this specific hardware configuration was located during this research.** Any business case built on this tier's numbers should be treated as illustrative only, pending a real quote.

## 7. Author disclosure and its bearing on the ownership-architecture discussion

- **The author has a disclosed commercial and advocacy interest in cooperative/ownership-based AI infrastructure models** (Method §3.4). While the cooperative-tier figures in this package are calculated the same way as every other tier — transparent formulas, stated assumptions — a reader should weigh the framing choices in Part V (which access models are discussed, in what order, with what emphasis) against that disclosed interest.
- **The author's own previously published cooperative-cost figures (€42/member/month and €19.50–23/member/month) were reconciled during this project's own research process** after initially appearing to conflict; the reconciliation (two different hardware tiers, not one contested number) is itself now a load-bearing claim in this package, resting on the author's own after-the-fact clarification of his own prior work rather than independent third-party verification of which hardware tier he originally intended.

---

**How this list should be used:** none of the items above invalidate the arithmetic in this package — every Derived Calculation still correctly follows from its stated inputs. They constrain how much weight any of this package's *outputs* (a specific $/M-token figure, a specific break-even claim) should carry as a description of real-world costs, as opposed to a description of what those costs would be under stated, editable assumptions. Readers building their own version of any model in this package should treat this list as a checklist of inputs to replace with their own verified figures before relying on the output.

---

*Licensed under CC BY 4.0. Research synthesis and modelling by Valto Loikkanen, assisted by AI. Factual source cut-off: 2026-08-13.*
