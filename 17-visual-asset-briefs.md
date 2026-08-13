# Visual Asset Briefs — Diagram Specifications for "Why Are They Spending Trillions on AI?"

**Status:** Diagrams 1–10 have been built as finished PNG images (see `assets/diagrams/`); the briefs below remain the specification each was built from, kept for anyone editing or re-deriving them. **Diagram 11** (added 2026-08-14, alongside the new "From AI working capacity to new value" conceptual bridge section) is specification-only as of this release — no image has been produced for it yet.

**Governing rules for every diagram (apply to all 11 briefs below, not restated per-brief except where a specific exception matters):**
- Every number, label, or data point pulled onto a diagram must carry the same evidence-class tag used in the source text — OBSERVED FACT, ATTRIBUTED STATEMENT, DERIVED CALCULATION, SCENARIO ASSUMPTION, or INTERPRETATION. Use a small legend (color-coded or icon-coded) rather than prose footnotes wherever the diagram has room; where it doesn't, a numbered footnote keyed to a legend block is acceptable.
- No diagram may rank, size, or visually privilege one of the six reader lenses (Individual, SME/owner-manager, Finance/infrastructure investor, Government/region/community, AI builder/operator, Educator/researcher/journalist) over another. Where a lens appears (Diagrams 1, 6, 8, 10), use a neutral, unordered layout (e.g., a ring, a grid, or alphabetical/equal-width columns) — never a numbered ranking, size gradient, or "priority" arrow.
- No diagram may visually endorse or rank Huang, Altman, and Zuckerberg's positions relative to one another (Diagrams 1, 6, 10). Where their statements appear together, use equal visual weight (same box size, same typographic treatment, neutral placement — e.g., three parallel columns, not a hierarchy).
- Every diagram touching a cost, price, financing, or scenario figure (Diagrams 2, 3, 8, 9) must carry a visible "SCENARIO ASSUMPTION — editable illustration, not a forecast; not investment/legal/tax/procurement/policy advice" boundary tag, per the paper's requirement that this boundary appear in every scale/investment-bearing section, not only once in front matter.
- No diagram may present open-weight/cooperative/decentralized ownership as superior to centralized/proprietary ownership, or vice versa (Diagrams 6, 7, 8). Trade-off diagrams must show gains and costs on both sides.
- Where a figure is flagged UNVERIFIABLE in the source text (e.g., "2.8M tokens/sec/MW," the NVIDIA "32K/8K reference workload"), it must NOT appear on any diagram as if confirmed — either omit it entirely or show it struck through/greyed with an "UNVERIFIABLE — not used" tag if its exclusion itself needs explaining. Note: "$0.123/M tokens" was corrected to CONFIRMED on 2026-08-13 (directly on NVIDIA's own site) and may now appear on diagrams, but only when explicitly scoped to the 72-GPU GB300 NVL72 rack tier — never applied to a workstation or desktop-class device.
- Standard footer for every diagram: "Licensed under CC BY 4.0. Suggested attribution: Research synthesis and modelling by Valto Loikkanen, assisted by AI." plus the paper's factual source cut-off date, 2026-08-13.

---

## Diagram 1 — The End-to-End Working-Capacity Chain

**Suggested type:** Horizontal flow/process diagram (a "conversion chain"), 10 linked nodes, with a secondary parallel branch beneath for the physical/humanoid variant.

**What it shows:** The paper's core analytical chain, stated in the Executive Summary and re-invoked at every Part boundary: **energy → hardware → compute → models → tokens → AI working capacity → digital work → outcomes → value → agency.** Beneath it, offset and visually distinguished (dashed connector, not a continuation of the same arrow), the parallel physical-work chain from Part V/VI: **capital + energy + maintenance + utilisation + orchestration → humanoid physical working capacity.**

**Data/sections visualized:** Executive Summary (chain statement); Section 15's 8-layer table (energy→outcome walk-through, Part II); Section 25 (value is not mechanically determined); Section 36 (humanoid chain, Part VI).

**Structural requirements:**
- Each node in the main chain is a labeled box; arrows between nodes are labeled with the *conversion cost/uncertainty* the paper attaches to that link (e.g., the energy→hardware arrow references Section 10's power/PUE caveat; the tokens→AI working capacity arrow references Section 16's usage-intensity bands; the working capacity→outcomes arrow and outcomes→value arrow must be visually distinguished — e.g., a different arrow style (dotted, thinner, or a "?" glyph) from every other arrow in the chain — to carry the paper's single most repeated warning: **"value can be positive, zero, or negative; it is not mechanically determined by anything upstream."** This is the one visual emphasis point that should NOT be neutral — it is the paper's own stated thesis, not an evaluative judgment this diagram is adding.
- A small inset box or callout at the "tokens" node should state: "A token measures AI working capacity, not value — see Section 14."
- The physical-capacity branch must carry its own boundary note: "Narrower, earlier-stage, less certain than the digital chain — Section 36 scope statement."
- Do not add a "value" number, dollar sign, or completion state at the end of the chain — the chain terminates in "agency," described in Part I/Part VII as open, not resolved.

**Evidence-class labeling:** The chain itself is [INTERPRETATION] — the author's own organizing framework, stated as such in the Method section and Executive Summary. Label the whole diagram accordingly in a corner tag: "Organizing framework — INTERPRETATION, per Method §3.1."

---

## Diagram 2 — Energy-to-Token Stack and Cost Waterfall

**Suggested type:** Waterfall/stacked-bar chart (vertical), 8 bars left-to-right, each bar showing cumulative cost added by that layer, with a companion small multiples version showing the same waterfall at 3 financing terms.

**What it shows:** Part II's required economic-layer separation, most concretely tabulated in Section 15's worked EUR example (Token-Factory Scenario Workbook) and restated as the general rule in Section 12: raw energy cost → hardware-amortized production cost → financed asset cost → full operating infrastructure cost → capacity/utilisation cost → token production cost → workload/AI-working-capacity cost → outcome and value (this last bar deliberately empty/unfillable — see below).

**Data/sections visualized:** Section 15's 8-row table (€0.154/M → €0.580/M → €0.688/M → €0.794/M → €1.435/M at 50% utilisation → final €/M figure → €/hr conversion → outcome/value); Section 12's financing-term sensitivity table (3/4/5/7-year terms, $0.094/$0.074/$0.063/$0.050 per M tokens); Section 10's rack power and MLPerf throughput figures as the physical basis for the first bars.

**Structural requirements:**
- Bars 1–7 stack cumulatively (each bar's top = the running €/M-token or $/M-token total); bar 8 ("outcome and value") must be rendered as an **empty/hatched/question-marked segment**, not a bar with a height — with a caption: "Not mechanically derived from layers 1–7 — Section 15, row 8."
- A secondary small-multiples strip beneath the main waterfall shows the same layers 2–3 recomputed at 3-year / 5-year / 7-year financing terms (Section 12 table), demonstrating that longer terms lower per-token cost but should carry a paired annotation: "trades lower per-token cost against longer lock-in to today's hardware generation — Section 11/12."
- Every bar must be individually tagged [CALC] except bar 1 (which rests on an [ASSUMPTION] electricity price) and bar 8 (untagged/[INTERP] only, since it is explicitly not calculated).
- Include a callout box distinguishing **owned-production cost** (this whole waterfall) from **retail API price** (a single reference line or marker overlaid at the top, e.g., "$2–$50/M tokens retail benchmark, Section 14 table" — rendered as a horizontal reference line crossing the whole waterfall, NOT as another stacked segment, to visually reinforce Section 3.2's rule that the two must never be collapsed into one column).

**Evidence-class labeling:** Full legend required (5 classes); this diagram uses at least 4 of the 5 (FACT for hardware/benchmark specs feeding bar 1–2, ASSUMPTION for electricity/financing inputs, CALC for every bar height, INTERP for the bar-8 callout).

---

## Diagram 3 — Token-to-Working-Capacity Intensity Ladder

**Suggested type:** Logarithmic-scale horizontal ladder/bracket chart (tokens/hour on a log-x-axis), 4 usage-intensity bands as horizontal bracket bars, crossed against a small matrix table beneath showing $/AI-working-hour by production tier.

**What it shows:** Section 16's 4-band usage-intensity ladder (chat/advisor, active coworker, delegated single agent, heavy multi-agent orchestration) and Section 17's cross-tabulation of those bands against Part II/III's production tiers to produce $/AI-working-hour.

**Data/sections visualized:** Section 16 table (tokens/hour Low–Mid–High per band, all tagged ASSUMPTION); Section 17's full matrix table (Home/Cooperative/Hyperscale/Retail-API-Luna-floor/Retail-API-central/Retail-API-Fable-ceiling × 4 bands); the OpenAI Codex telemetry callout (99.8% weekly output tokens, 70.2%/25.6% hour-equivalence stats, 60+ hrs/day at p99) as a supporting annotation justifying band 4's open-ended ceiling.

**Structural requirements:**
- X-axis: tokens/hour, log scale, spanning roughly 10,000 to 12,000,000+. Four horizontal bracket bars (one per band), each spanning its Low–High range, with the Mid value marked. Band 4's bar must visually indicate open-endedness (an arrow or fade at the right edge, not a hard stop), captioned "open-ended ceiling — Section 16."
- Beneath the ladder, a small heat-map-style matrix (rows = production tier, columns = band) showing $/AI-working-hour, using color intensity or a simple numeric grid — NOT a single "cheapest wins" color scale that implies a value judgment; use a neutral sequential palette keyed only to magnitude, with a note that lower cost ≠ better outcome (cross-reference to Diagram 4/Section 25).
- A separate annotated callout box, visually separated from the main chart, carries the OpenAI Codex telemetry figures with their full caveat: "OpenAI's own internal, self-reported, unaudited telemetry on its own employees using its own product — not a general-population statistic. ATTRIBUTED STATEMENT."
- The Professional tier row must be shown as blank/greyed with a note "— unofficial/no verified spec, Section 17 table-note" rather than populated with any number, matching the whitepaper's own explicit removal of that column.

**Evidence-class labeling:** Bands = [ASSUMPTION]; matrix cells = [CALC] (formula: tokens/hr ÷ 1,000,000 × $/M-tokens); Codex callout = [ATTR] with explicit self-reported/unaudited caveat text visible on the diagram itself, not only in a linked footnote.

---

## Diagram 4 — Human and AI Work-Value Multipliers

**Suggested type:** Two-part diagram: (a) a factor wheel/radial diagram of the 8 interacting quality factors from Section 18, with "reliability" and "information" visually flagged as multiplicative rather than additive; (b) three side-by-side paired-comparison cards (professor/entrepreneur; new CEO/veteran employee; investor/salesperson) illustrating Section 25's human-analogy argument, extended to an AI/orchestration panel.

**What it shows:** Section 18's 8-factor framework (capability, reliability, initiative, judgment, creativity, context, tools/harness, information) and Section 25's core argument that working capacity ≠ value, that orchestration multiplies capacity not value, and that raw capability/intelligence does not predict who produces usable value in a given situation.

**Data/sections visualized:** Section 18 (8 factors, reliability/information as multipliers); Section 25 (3 human-analogy pairs + AI-orchestration parallel); Section 17 point 2 (cost-per-band spread) as a supporting note that price and value are separate axes.

**Structural requirements:**
- Part (a): a radial/wheel diagram with 8 labeled spokes (equal visual weight — do not size spokes by "importance," since the paper does not rank the 8 factors against each other beyond flagging reliability and information as structurally different in kind). Use a distinct visual treatment (e.g., a doubled ring or bold outline) only for reliability and information, with the caption: "these two act as multipliers on the other six — not additive bonuses, Section 18."
- Part (b): three equal-sized comparison cards, each showing two human roles side by side with a simple 2×2 or Venn treatment of "capability high / fit-to-task variable," each captioned with the paper's own line: "raw capability and fit-to-task are different things." A fourth card, visually equal to the other three, extends the same logic to AI: "orchestration multiplies capacity, not value — a cheap, fast, wrong answer scaled across a multi-agent team is still cheap and wrong at scale (Release Asset #10 §6 / Release Asset #11 Part 8)."
- Do NOT resolve any of the four comparison cards with a "winner" — each card must visually terminate in an open question mark or balanced scale icon, not a checkmark on either side.

**Evidence-class labeling:** Entire diagram is [INTERPRETATION] (Section 18 explicitly self-identifies as the author's own conceptual synthesis, not benchmarked). Tag prominently: "Framework: author's own conceptual synthesis, not independently benchmarked — INTERPRETATION."

---

## Diagram 5 — AI Maturity and Information Evolution Framework

**Suggested type:** Two-axis progression matrix/staircase diagram — X-axis: "how work gets done" (Advise → Cowork → Delegate → Lead); Y-axis: "scale of orchestration" (Individual AI worker → AI team → AI workforce) — with a diagonal "information architecture maturity" band overlay.

**What it shows:** Section 23's two-axis maturity framework and Section 21–22's argument that information/context is a distinct axis from model capability ("information as AI's operating system"), plus the explicit, stated uncertainty about the public form of this framework (Section 23's finding that the exact three-stage/three-dimension structure originally anticipated was not confirmed on LinkedIn, and no CC BY 4.0 license was found on the public posts).

**Data/sections visualized:** Section 23 (2-axis framework, advise/cowork/delegate/lead × individual/team/workforce); Section 21–22 (information as multiplier/operating system, Zuckerberg's personal-agent privacy commitment and Altman's 1,000,000× usage-growth anecdote as supporting, differently-sourced data points, NOT as validation of the framework itself); Section 24 (the "how do we get it done" → "what should we do" shift as work moves rightward/upward on the matrix).

**Structural requirements:**
- A 4×3 grid (Advise/Cowork/Delegate/Lead × Individual/Team/Workforce), each cell a plain labeled box — no cell should be shaded to imply "better" or "more mature is more valuable"; use a simple directional arrow (bottom-left to top-right) labeled "increasing delegation and orchestration scale" with a neutral caption, not an "improvement" arrow.
- Overlay a diagonal band or gradient strip labeled "information architecture and data control — Section 21/22, INTERP" running across the grid, to show information maturity as a separate, cross-cutting axis rather than a third grid dimension (avoiding a false 3D grid the source text itself could not confirm existed in the original public framework).
- A callout box, clearly separated, must carry the finding-integrity note verbatim in spirit: "Public version of this framework (2 LinkedIn videos, dated 2026-06-20) does not exactly match the structure summarized here; no CC BY 4.0 license was found on the public posts. This diagram adapts the framework for this paper's own use — see Section 23."
- A secondary small annotation track along the bottom: "as this matrix moves rightward/upward, the human question shifts from 'how do we get it done' to 'what should we do' — Section 24, INTERPRETATION."

**Evidence-class labeling:** Grid axes/structure = [INTERPRETATION], explicitly the author's own adapted framework; any Codex telemetry or Altman/Zuckerberg data points used as illustrative markers on the grid must retain their own [ATTR] tags individually — do not let the grid's INTERP tag absorb them.

---

## Diagram 6 — Ownership Stack and Alternative Architectures

**Suggested type:** Vertical layered-stack diagram (8 layers) paired with a horizontal comparison strip of 6 access/ownership models — essentially two linked diagrams sharing one legend.

**What it shows:** Section 26's 8-layer ownership stack (energy, hardware, compute/access, models, information, agents, identity, governance) with each layer's observed concentration pattern, and Section 27's 6 coexisting access models (centralized public platform, enterprise dedicated system, open models on owned/rented hardware, private/individual ownership, cooperative, local/regional capacity), explicitly presented as coexisting rather than competing.

**Data/sections visualized:** Section 26 table (8 layers × concentration pattern × evidence class); Section 27 (6 models, each with its own cost/control profile); Section 30's trade-off table (scale/performance/cost/privacy/resilience/convenience/access/control per model — feed this into a secondary small radar/spider chart per model if space allows, using identical axis scaling across all 6 so no model's radar is visually "bigger").

**Structural requirements:**
- The 8-layer stack: each layer is a horizontal band, with a short concentration-pattern label and its evidence-class tag inline (most are [FACT]/[ATTR]/[INTERP] per Section 26's table — preserve exactly, do not upgrade any [INTERP] row, e.g. "Information" and "Identity," to [FACT]).
- The 6-model strip: six equal-width columns, explicitly captioned "coexisting access patterns — none universally superior, Section 27/30," each showing: cost range (the cooperative column shows two hardware-tier figures side by side — €19.50–23/member/month for a DGX Spark pool, €42/member/month for a shared workstation-class machine, Section 27/32 — clearly labeled as two different tiers, not an unresolved range), control/portability/exit/governance/continuity icons from Section 29's 5-question framework.
- If a radar/spider chart is used for Section 30's trade-offs, all 6 models must use identical axis scales (Low/Medium/High mapped to the same radial distance) and equal color-weight — no model's shape should be larger or bolder by default styling.
- Explicit disclosure callout, visually present (not buried in a footnote): "The cooperative/ownership architecture discussed here is one candidate model among several, argued on its own numbers by an author with a stated commercial and advocacy interest in it — Method §3.4 disclosure."

**Evidence-class labeling:** Mixed per-layer/per-model as specified in Sections 26/27/30 — do not apply one blanket tag to the whole diagram; preserve the source table's per-cell tags exactly.

---

## Diagram 7 — Electricity-Grid / Solar / Cooperative Analogy

**Suggested type:** Side-by-side five-tier analogy diagram (two parallel columns: "Electricity precedent" vs. "AI-compute analogue"), with a distinct visual "weak link" flag on the fifth tier.

**What it shows:** Section 28's 5-tier electricity-grid analogy (home solar → energy cooperative → commercial power producer → utility-scale power plant → electricity grid/exchange, mapped to home AI factory → AI infrastructure cooperative → commercial inference provider → hyperscale AI factory → distributed inference marketplace), including the paper's own explicit flag that this analogy could not be verified against a single dated primary source and that its fifth-tier mapping (a frictionless AI-compute spot market) does not yet exist.

**Data/sections visualized:** Section 28 table (5 tiers); the Bitcoin-hashprice-vs-AI-token-value comparison (Section 14/28, Luxor spot hashprice ~$31.73–32.05/PH/s/day vs. the token-value swing between retail-priced and production-cost-priced tokens) as a supporting inset illustrating why tier 5 is the weakest link; OpenRouter's self-reported 200T+ monthly tokens / 10M+ users as the "closest currently-existing partial analogue" for tier 5.

**Structural requirements:**
- Five paired rows, left column = electricity precedent (plain, everyday icons: solar panel, cooperative building, power plant icon, grid pylon icon), right column = AI-compute analogue (DGX Spark icon, cooperative server rack, contracted cluster icon, hyperscale rack icon, a dashed/incomplete network icon for tier 5).
- Tier 5 row must be visually distinct — e.g., a dashed border or hatched fill — with the caption: "Weakest link in the analogy: no frictionless, protocol-level AI-compute spot market currently exists — Section 28. OpenRouter is a partial, provider-routing analogue only, not a compute spot market."
- A small inset chart (bar or dumbbell) comparing Bitcoin hashprice (~$31.73–32.05/PH/s/day, OBSERVED FACT) against the illustrative AI-token value range (~$0.45–$1.50/MWh-equivalent at production cost vs. ~$4,500/MWh at retail price) — with an explicit caption that this is NOT a profitability claim about either activity, but an illustration of why token *price* and token *value* are separate questions (Section 14).
- Explicit boundary tag on the whole diagram: "Structural comparison to make an unfamiliar asset class legible via a familiar one — not a claim that AI-compute markets will evolve identically to electricity markets. Not investment or infrastructure-planning advice — Section 28."

**Evidence-class labeling:** Whole analogy = [INTERPRETATION] (explicitly flagged in source as an analogy the author has used in commentary, not independently verified against one dated publication). Bitcoin hashprice figure = [FACT]; AI-token value range = [CALC] on [ASSUMPTION] inputs; OpenRouter figures = [FACT, self-reported].

---

## Diagram 8 — Scale Spectrum (Home → Cooperative → Professional → Hyperscale)

**Suggested type:** Horizontal scale spectrum / stepped bar chart with four tiers, dual-axis (capital cost on one axis, $/M-token or $/AI-working-hour on a secondary inverse axis), plus a small multiples utilization-sensitivity strip.

**What it shows:** Part VI's 4-tier scenario comparison (Section 35's summary table): Home (1× DGX Spark), Cooperative (10×, 50 members), Professional (HGX B300/GB300 rack, least-evidenced), Hyperscale (4-rack/288-GPU cluster) — showing capital cost, owned-production $/M-tokens, $/AI-working-hour at the relevant usage band, and the governing lever for each tier (utilization / utilization+overhead / interactivity setting / financing term).

**Data/sections visualized:** Section 35 summary table (all 4 tiers); Section 31 (Home tier detail + utilization curve); Section 32 (Cooperative tier + the two-hardware-tier table: €19.50–23 for a DGX Spark pool vs €42 for a shared workstation-class machine, shown side by side); Section 33 (Professional tier, explicitly flagged as least-evidenced/ASSUMPTION-heavy); Section 34 (Hyperscale tier + financing-term-sensitivity table); Section 12's utilization-lever point (2,000→8,000 hrs/yr cuts cost 3.5–4×, same pattern reused in Diagram 9).

**Structural requirements:**
- Four equal-width vertical panels, left to right, ordered strictly by scale (Home→Cooperative→Professional→Hyperscale) — this left-to-right ordering is a factual scale ordering, not a value ranking, and should be labeled as such ("ordered by capital scale, not by recommended choice").
- Each panel shows: capital cost (FACT/ASSUMPTION as applicable — Home's $4,699 is FACT; Professional's capex is explicitly ASSUMPTION/unofficial, and must be rendered visually distinct, e.g. dashed box, from the other three panels' capital figures), owned-production $/M-tokens range (CALC), and $/AI-working-hour range at that tier's "relevant band" (CALC) — reproduce Section 35's table values exactly, including ranges (not single points) to preserve the paper's own utilization/interactivity/financing sensitivity.
- Beneath the four panels, a shared small-multiples strip shows "cost-per-hour vs. utilization" curves for at least the Home and Cooperative tiers (Section 31's canonical $0.014–$1.427/hr chat/copilot-band figure and Section 32's cooperative reconciliation), reinforcing "utilization is the single largest lever at every scale — Section 35 point 1."
- The Professional panel must carry a visible flag: "Least-evidenced tier — NVIDIA publishes no official price/power spec for this SKU. Figures are illustrative placeholders — Section 33/17 table-note."
- The Cooperative panel must show both hardware-tier figures explicitly, not averaged, with a short note: "two hardware tiers — DGX Spark pool (€19.50–23) vs. shared workstation-class machine (€42) — Section 27/32."
- Every panel carries the visible boundary tag: "SCENARIO ASSUMPTION — editable illustration, not a forecast; not investment/legal/tax/procurement/policy advice."

**Evidence-class labeling:** Mixed and explicit per panel as above — this diagram most directly needs the full 5-class legend visible at all times, since it mixes FACT (hardware specs), ASSUMPTION (Professional capex, financing/electricity inputs), and CALC (all derived $/M-token and $/hour figures) within a single visual frame.

---

## Diagram 9 — Humanoid Physical-Capacity Extension

**Suggested type:** Parallel-structure diagram mirroring Diagram 2's waterfall logic, adapted to Section 36's capital+energy+maintenance+utilisation+orchestration chain, plus a small-multiples utilization-sensitivity table (identical visual grammar to the digital-tier utilization curves in Diagram 8, to make the cross-domain parallel legible).

**What it shows:** Section 36's humanoid working-capacity model: real market price range across 4 named platforms (Unitree G1, 1X NEO, Agility Digit, the author's own illustrative €25,000/$27,000 base case), the cost-per-productive-hour table at 4 utilization levels (2,000/4,000/6,000/8,000 hrs/yr), the finding that electricity is NOT the binding cost driver here (unlike the digital tiers), and the explicit list of excluded cost categories (supervision, software/subscription, insurance, workspace modification, consumables, downtime beyond a flat reserve).

**Data/sections visualized:** Section 36 (platform price table: Unitree $13.5K FACT, 1X NEO $20K/$499mo ATTR-unconfirmed, Agility Digit ~$250K ATTR-secondary, Tesla Optimus $20–30K ATTR-unconfirmed-target, Figure 03 no data, author's own €25,000/$27,000 illustrative base case INTERP); the 4×4 cost-per-hour matrix; the 1X NEO battery-derived electricity estimate (~$0.03/hr) contrasted with financing/maintenance as the dominant cost.

**Structural requirements:**
- A horizontal price-range bar showing all 5 named reference points (Unitree low end, author's illustrative point, 1X NEO, Optimus target, Agility Digit high end, in ascending price order) — each point tagged individually with its evidence class (do not let the illustrative €25,000 figure visually appear more "real" than the FACT-tagged Unitree figure; use identical marker style, distinguished only by the class-legend color/icon).
- The cost-per-hour table (4 utilization rows × 5 price columns from Section 36) reproduced as a small heat-grid, using the same utilization-lever framing as Diagram 8's strip, with an explicit cross-reference caption: "same 3.5–4× utilization effect observed at every digital production tier in Section 35 — Section 36."
- A distinct callout, visually separated, for the electricity-vs-financing/maintenance finding: a small pie or stacked-bar breakdown at one reference utilization level (e.g., 4,000 hrs/yr) showing financing + maintenance reserve dominating over the ~$0.03/hr electricity estimate — captioned "unlike token production (Diagram 2), electricity is not the binding cost here — Section 36."
- A clearly boxed "excluded from this model" list (supervision labor, software fees, insurance, workspace modification, consumables, extra downtime) with the caption: "every figure above is a floor, not a full commercial cost — Section 36."
- Mandatory scope-boundary banner across the top of the whole diagram: "Narrow model of ownership cost only. NOT a general claim about robotics economics, a product recommendation, or a forecast. Industrial arms/AMRs and other categories are out of scope — Section 36 scope statement."
- A brief closing note/icon reiterating Section 36's value-boundary point: "capacity ≠ value — a fleet costing $1/hour to own says nothing about whether its work is worth $1, $100, or nothing (cross-reference Diagram 4)."

**Evidence-class labeling:** Mixed per data point as specified — this diagram has the highest concentration of ATTR/unconfirmed and INTERP/illustrative tags of any brief in this set and must not visually smooth that over; the legend should be prominent, not decorative.

---

## Diagram 10 — Final Transition: Abundant Working Capacity → "What Should We Do?"

**Suggested type:** A single large closing composition — a converging funnel/arrow diagram feeding into an open question mark, with a six-panel unordered ring or grid beneath representing the six reader lenses each facing the same open question.

**What it shows:** The paper's closing argument (Sections 43–45): that trillions in committed capital and falling cost curves (Parts II–IV) represent opportunity, not destiny; that orchestration multiplies capacity, not judgment; and that the central unresolved human question, as working capacity becomes abundant, shifts from "how do we get it done" (increasingly answered by AI) to "what should we do" (a question the paper explicitly does not answer for the reader).

**Data/sections visualized:** Section 43 (six-lens opportunities-without-inevitability list, explicitly unranked); Section 44 (adoption/organizational-change/time as unresolved variables — the Codex telemetry, the AI Maturity Framework's "learning→internalizing→AI-native" progression, and Altman's cost-decline-vs-demand-growth distinction, all reused here strictly as previously-established evidence, not new claims); Section 45 (the closing "how" vs. "what" framing, explicitly marked INTERPRETATION and not attributed to any named executive).

**Structural requirements:**
- Top portion: a converging funnel bringing together small labeled tributaries representing the paper's major forward-looking threads (Huang/Fink's financing and per-GW claims, Altman's cost-decline and demand claims, Zuckerberg's personal-agent claims, the falling $/M-token curves) — each tributary retains its own evidence-class tag and must NOT be merged into a single unlabeled "AI progress" arrow; the funnel converges toward a single node labeled "Abundant, cheap AI working capacity (if the trend continues — not proven, Section 44)."
- That convergence node feeds one arrow downward into a large, deliberately open/unfilled question-mark shape labeled "What should we do?" — this shape must be visually incomplete/open (outline only, or a fragmented/dashed glyph) to avoid implying the paper supplies an answer.
- Beneath, six equal-sized panels arranged in a ring or 2×3/3×2 grid (no lens first, no lens largest, no numbered order beyond what's needed for alphabetical or layout neutrality) — each panel names one reader lens and one open-ended, unresolved opportunity/question from Section 43, phrased as a question, not a recommendation (e.g., Individual: "private-by-default personal agent, or deeper dependence?"; SME: "delivery-innovation upside — conditioned on adoption capacity"; Finance: "real infrastructure and mispriced risk, from the same facts"; Government: "opportunity distributed, or concentrated, by default?"; Builder/Operator: "cheap tokens expand what's buildable — and what's buildably wrong at scale"; Educator/Researcher/Journalist: "cheap tokens expand access to explanation and to confident error alike").
- A small side annotation reproducing Section 45's closing INTERPRETATION line verbatim, clearly boxed and tagged: "[INTERPRETATION — author's own closing synthesis, not attributed to any named executive]: as working capacity becomes abundant, 'how do we get it done' is increasingly answered by AI, while 'what should we do' becomes the single most important human question."
- Explicit closing boundary text on the diagram itself: "This paper does not answer this question for any reader. No lens's version of the question is prioritized over another's."

**Evidence-class labeling:** Mixed per tributary (ATTR for each named executive's claim, CALC for cost-curve tributaries, INTERP for the funnel's convergence framing and the closing "how/what" line) — the open question-mark node itself carries no evidence tag, since it represents an unresolved question, not a claim.

---

## Diagram 11 — Creating Growth Based on New Value

**Status:** Added 2026-08-14, alongside the new "From AI working capacity to new value" conceptual bridge section (placed between Parts IV and V of the whitepaper). No source image was supplied for this brief — unlike Diagrams 1–10, there is no pre-existing author visual to redraw from; this brief describes the diagram to be designed from scratch, following the same structural discipline as the rest of this set.

**Suggested type:** A two-stage horizontal conversion diagram (not a funnel, not a ranking) — Stage A ("Creating new value") feeding into Stage B ("Creating growth from new value") — visually distinct from, but positioned to echo, Diagram 1's chain-of-nodes grammar, so a reader recognizes it as the same family of diagram applied to a different link in the paper's overall chain.

**What it shows:** The whitepaper's new conceptual-bridge section's core distinction: that AI working capacity (the output of Parts I–IV's cost/capacity model) is not economic value by itself, and that converting capacity into growth requires a separate chain — idea/invention → innovation → verified new value → value proposition and communication → revenue model → productivity — which this paper's cost tables and workbooks do not, and cannot, model on their own.

**Data/sections visualized:** The whitepaper's "From AI working capacity to new value" section (unnumbered, between §25 and Part V): the full extended conversion chain (electricity → compute infrastructure → AI working capacity → useful work outputs → human and organizational integration → idea/invention → innovation → verified new value → value proposition and communication → revenue model → productivity and growth), and its two-question framing ("can the capacity be created" vs. "can that capacity create and capture new value").

**Structural requirements:**
- The full 11-node chain from the whitepaper section should appear once, in full, at the top of the diagram as a single horizontal or wrapped-horizontal reference strip — using the same node/arrow visual grammar as Diagram 1, so the two diagrams read as companions. The first six nodes (electricity → compute infrastructure → AI working capacity → useful work outputs → human and organizational integration → idea/invention) should be visually grouped as "capacity" (cool/neutral color, matching Diagram 1's digital-chain color); the remaining five (innovation → verified new value → value proposition and communication → revenue model → productivity and growth) should be visually grouped as "value and growth" (a distinct but equally neutral color — not a "better" color, since this is a conversion, not an upgrade).
- Beneath that reference strip, two clearly separated, equal-sized panels:
  - **Panel A — "Creating new value":** idea/invention → innovation → verifying new value. Caption: "This paper's cost/capacity model (Parts I–IV) supplies inputs to this chain — cheap tokens, available agent capacity — but does not perform it."
  - **Panel B — "Creating growth from new value":** new value → value proposition and communication → revenue model → productivity. Caption: "Growth requires all four steps; verified new value alone is not yet growth."
- A visible boundary callout, styled consistently with the "SCENARIO ASSUMPTION" tags used in Diagrams 2/3/8/9, but using this section's own tag instead: "INTERPRETATION — conceptual framework, not a numerical finding or a causal law. Introduces no new cost figures."
- A small annotation tying this diagram to the planned Scenario Explorer, worded closely to the whitepaper section's own language: "The Scenario Explorer (built on this paper's cost workbooks) can model the 'capacity' half of this chain — $/M tokens, $/AI-working-hour, utilization, financing. It cannot model the 'value and growth' half without separate assumptions about users, adoption, and revenue model."
- Do not imply that any one production tier (Home/Cooperative/Professional/Hyperscale, Diagram 8) or ownership model (Diagram 6/7) is more likely to successfully complete the "value and growth" half of the chain than another — this diagram's job is to show the conversion exists and is separate from the cost model, not to score any tier or model against it.

**Evidence-class labeling:** The entire diagram is **[INTERPRETATION]** — the author's own conceptual framework, not derived from any named executive's statement or from this paper's cost workbooks. Label it as such once, prominently, rather than per-node, since no individual node carries a different evidence class here.

---

**Cross-diagram consistency notes for the designer (apply across all 11 briefs):**
- Use one consistent 5-class legend (icon + color) across the entire asset set (#15) so a reader moving between diagrams doesn't have to relearn the code each time.
- Use one consistent typographic/color treatment for "SCENARIO ASSUMPTION — not a forecast, not advice" boundary tags across Diagrams 2, 3, 8, 9 (and the financing/scenario portions of 1, 6).
- Do not introduce color-coding that implies a preferred ownership model, executive, or reader lens anywhere in the set — palette choices should be functional (evidence class, tier, or axis) not evaluative.
- All 10 diagrams should carry the same footer block: factual source cut-off (2026-08-13) and the CC BY 4.0 attribution line.

---

Licensed under CC BY 4.0. Suggested attribution: Research synthesis and modelling by Valto Loikkanen, assisted by AI.