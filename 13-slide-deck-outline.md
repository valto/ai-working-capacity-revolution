# Slide Deck Outline — "Why Are They Spending Trillions on AI?"
### Companion deliverable (Release Asset #5) — 26 slides, following the whitepaper's own Front Matter → Closing structure. Evidence-class tags used throughout: **[FACT]** = Observed Fact · **[ATTR]** = Attributed Statement · **[CALC]** = Derived Calculation · **[ASSUMPTION]** = Scenario Assumption · **[INTERP]** = Interpretation.

---

**Slide 1 — Title**
- "Why Are They Spending Trillions on AI?" — The numbers and economics behind the AI working-capacity revolution
- Author: Valto Loikkanen · v1.0 research package · Factual source cut-off 2026-08-13
- Licence: CC BY 4.0 — Attribution 4.0 International
- Speaker note: This is a neutral research synthesis, not a vendor report or investment recommendation — state that framing before anything else.

**Slide 2 — Method: Five Evidence Classes**
- Table: OBSERVED FACT (primary source, checked on/before 2026-08-12) · ATTRIBUTED STATEMENT (on-record claim, not auto-proven) · DERIVED CALCULATION (formula always shown) · SCENARIO ASSUMPTION (editable, not a market figure) · INTERPRETATION (labelled reading, never fact)
- Every claim in this deck carries one of these five tags, exactly as in the source paper.
- No fabricated quotes, figures, or URLs; unverifiable items are labelled UNVERIFIABLE rather than smoothed over.
- Speaker note: This slide is the contract with the audience — every number that follows is traceable to one of these five buckets.

**Slide 3 — How to Use This Research: Six Equal Lenses**
- Individual · SME/owner-manager · Finance/infrastructure investor · Government/region/community · AI builder/operator · Educator/researcher/journalist
- No lens is prioritized over any other — a deliberate editorial stance held throughout, not an oversight [INTERP, stated editorial policy].
- Each lens has a different entry point into the same chain: energy → hardware → compute → models → tokens → AI working capacity → work → outcomes → value → agency.
- Speaker note: Tell the room which lens they're likely reading from, but stress that the deck deliberately refuses to rank the six.

**Slide 4 — Executive Summary: The Chain**
- Chain: energy → hardware → compute → models → tokens → AI working capacity → digital work → outcomes → value → agency (Front Matter §1).
- Parallel physical chain: capital + energy + maintenance + utilisation + orchestration → humanoid working capacity (Part VI).
- Headline: Aug 10, 2026 — Nvidia + 6 firms (Apollo, Blackstone, BlackRock, Brookfield, Goldman Sachs, KKR) MOUs to mobilize >$500B [FACT]; Fink: "trillions of dollars over the coming years" [ATTR, Fink].
- Ten-second takeaway: trillions are committed on a belief that cheap AI working capacity is coming — working capacity is not value, and nothing here proves that belief right.
- Speaker note: This slide is the whole paper in miniature; everything after it is evidence for or against pieces of this one paragraph.

**Slide 5 — Part I: Why Are They Spending Trillions?**
- Aug 10, 2026: Nvidia signs MOUs with six asset managers/banks to mobilize >$500B in third-party AI-infrastructure capital [FACT, CNBC/Fortune].
- Huang: "each gigawatt is something like $50, $60 billion" [ATTR, Huang].
- Three structurally different, differently-incentivized answers on offer: compute as infrastructure (Huang), intelligence as utility (Altman), superintelligence as personal (Zuckerberg) — shown side by side, none endorsed.
- Speaker note: Frame this as the reader's actual question, not a rhetorical one — three interested parties, three different stakes.

**Slide 6 — Three Voices, Side by Side**
- Table:

| Source | Framing | Representative statement | Class |
|---|---|---|---|
| Huang (Nvidia) | Compute as infrastructure | Chips are an "investable asset" | ATTR |
| Altman (OpenAI) | Intelligence as utility | "Cost...falls about 10x every 12 months...lower prices lead to much more use" | ATTR |
| Zuckerberg (Meta) | Superintelligence as personal | "Individual empowerment as the source of prosperity" | FACT (verbatim) / ATTR (as claim) |
- None of the three claims is independently audited; that they were said is confirmed, whether they're true is not.
- Speaker note: Resist any temptation to declare a winner here — the paper's whole editorial stance depends on not doing so.

**Slide 7 — What Would Need to Be True: Bubble, Infrastructure Transition, or Both?**
- Supports "transition": signed $500B MOUs are real [FACT]; independent power-demand forecasts (BCG 50–80GW, S&P Global 64.4GW in 2025) are directionally consistent [ATTR, low-confidence sourcing].
- Supports "bubble caution": Huang/Fink's own per-GW and demand figures are self-interested ATTR statements; independent analyst estimates ($35–49B/GW) sit below Huang's $50–60B [ATTR].
- Disciplined position: both readings draw on overlapping, not competing, facts [INTERP] — the same MOU can be real infrastructure and include mispriced capital.
- Speaker note: The point is not to pick a side — it's to show the same facts support two different narratives simultaneously.

**Slide 8: Part II — Electricity, Power, and Tokens per Watt**
- GB300 NVL72 rack: 135kW TDP / 155kW peak per OEM spec [FACT, Lenovo]; NVIDIA itself publishes no power figure.
- MLPerf v6.0: "2.5M tokens/sec" is a 4-rack/288-GPU aggregate, not a single-rack figure — a common misattribution corrected here [FACT].
- Tokens/watt is not one number per chip — it ranges roughly 1.7M–5.2M tokens/sec/MW depending on latency tolerance [CALC/INTERP].
- Speaker note: Use this slide to show the paper's discipline in action — catching and correcting a benchmark misattribution rather than repeating it.

**Slide 9 — Hardware as Capital Equipment, and Its Financing**
- Huang frames Nvidia's platform as an "investable asset" [ATTR, Huang, CNBC Aug 10 2026].
- Capital stack observed vs. assumed: DGX Spark $4,699 MSRP [FACT]; HGX B300 has no public price [ASSUMPTION]; GB300 rack ~$4M is an illustrative analyst estimate [ASSUMPTION].
- Depreciation risk: Vera Rubin claimed "up to 10x more tokens/MW" vs GB200 [ATTR, vendor]; SemiAnalysis's independent figure is 2–5.4x [FACT-adjacent].
- Speaker note: Emphasize that today's capital is a bet against a hardware curve both the vendor and independent analysts agree is moving fast.

**Slide 10 — The Eight Cost Layers (Never Collapsed Into One Number)**
- Layers: raw energy cost → hardware-amortized cost → financed asset cost → full operating infrastructure cost → capacity/utilisation cost → token production cost → workload/AI-working-capacity cost → outcome and value (never mechanically derived).
- Worked EUR example: financing term alone moves cost from €0.688/M tokens to €1.435/M tokens at 50% utilisation [CALC].
- Utilisation is usually the single largest lever at every scale [INTERP, cross-workbook pattern].
- Speaker note: This ladder is the spine of the entire cost analysis — every dollar figure later in the deck sits on one specific rung, never blended with another.

**Slide 11 — Owned Production Cost vs. Retail API Price**
- Self-correction preserved deliberately: retail lab prices are a finished, marked-up product price, not a cost basis for owned hardware [method note].
- Retail benchmark: Claude Sonnet 5 $2/$10 per M tokens [FACT]; GPT-5.6 Terra ~$2/$12 [ATTR, via intermediary fetch]; Gemini 3.1 Pro Preview $2/$12 [FACT].
- Owned production: Home $1.37–$11.89/M tokens (canonical); Hyperscale ~$0.091–0.312/M tokens, canonical full-layer, mid $0.133/M [CALC] — Hyperscale sits 1–2 orders of magnitude below retail; Home sits closer to, and at low utilization inside, the cheapest retail floor. The gap is real everywhere but its size is tier- and utilization-dependent, by design, not error.
- Speaker note: This gap is the point, not a mistake to reconcile — "generate your own power" vs. "buy from the grid."

**Slide 12 — Part III: Usage-Intensity Bands**
- Four bands (tokens/AI-working-hour, all SCENARIO ASSUMPTION): Chat/advisor (10K–30K) · Active copilot (60K–120K) · Delegated agent (200K–600K) · Heavy multi-agent orchestration (1M–12M+).
- OpenAI's own unaudited telemetry: Codex = 99.8% of weekly internal output tokens; 99th-percentile users ran 60+ agent-hours/day [ATTR, OpenAI, self-reported].
- These describe OpenAI staff using OpenAI's own product — not a general-population statistic [caveat, stated explicitly].
- Orchestration does not create a different kind of hour — it creates multiple working hours in parallel: 1 hour = 1 agent/person × 1h; 10-team hour = 10 agents/people × 1h = 10 agent/human-hours; 1 day = 8 agent/human-hours; 10-team day = 80 agent/human-hours. Team capacity is workers × hours, on both sides, with no exception.
- Speaker note: Band 4's open-ended ceiling is informed by, not proven by, this one company's internal data. The 1-vs-10 table is the guardrail against reading a band-4 figure as "one very fast hour" instead of "many parallel ordinary hours."

**Slide 13 — From Tokens to $/AI-Working-Hour**
- Formula: $/AI-working-hour = (tokens/hour ÷ 1,000,000) × ($/M tokens at that tier) [CALC].
- At delegated-agent band, central case: Hyperscale $0.0252/hr vs. Home $1.268/hr vs. Retail-API $3.60/hr [CALC] — a ~150x spread across tiers at the same usage band.
- Self-hosting is not automatically the cheapest path — its case rests on control and independence, not undercutting retail [INTERP].
- Speaker note: The spread is arithmetic, not opinion — but which column matters depends entirely on which lens is asking.

**Slide 14 — Quality Multipliers and the Limits of Human/AI Comparison**
- Eight factors shape effective working capacity: capability, reliability, initiative, judgment, creativity, context, tools, information [INTERP, author's own framework].
- Reliability and information act as multipliers, not add-ons — unreliable capacity caps how much can safely be delegated.
- What IS comparable: throughput, marginal cost, capacity elasticity. What is NOT: workload complexity, quality/correctness, supervision burden, context completeness — kept visibly separate, not folded into one multiplier.
- The employer/billable split: owned AI pairs with human employer cost (fully loaded — wage+benefits+overhead); retail AI pairs with human billable/externally-purchased rate (agency/contractor/consultancy, which embeds its own margin and overhead on top). Comparing owned AI against a billable rate — or retail AI against employer cost — mixes the internal/external layers exactly as Part III warns against mixing owned-production cost with retail API price [INTERP].
- Speaker note: This is the guardrail slide against naive "$/hour AI vs. $/hour human" headlines — and against the narrower mistake of picking whichever AI number and whichever human number make the best-sounding comparison.

**Slide 15 — Part IV: Information as AI's Operating System**
- Author's own framing: information is "the operating system for AI" [FACT that phrase appears; INTERP as underlying claim] — disclosed author interest in this framing (Prifina/Digiole/ValtoAI/PIOS/EIOS).
- Same model + different information = very different effective working capacity.
- Zuckerberg: "fully private mode…even Meta cannot see" [ATTR]; Altman's usage anecdote implies ~1,000,000x token growth per heaviest user, 2019→2026 [CALC on ATTR inputs].
- Speaker note: Flag the disclosure here explicitly — this section sits closest to the author's own commercial stake.

**Slide 16 — AI Maturity and the Shifting Human Role**
- Two axes: how work gets done (Advise → Cowork → Delegate → Lead) and scale of orchestration (individual → team → workforce) [INTERP, author's framework, partially unverified public form].
- Three framings of the same shift: Altman on freedom/agency [ATTR]; Zuckerberg on balance of power [FACT/ATTR]; Huang on capital allocation [ATTR] — none more correct than the others.
- As execution gets cheap, "what should we do" replaces "how do we get it done" as the load-bearing human question [INTERP].
- Speaker note: Each of the six lenses experiences this shift differently — no priority ordering intended.

**Slide 17 — Value Can Be Positive, Zero, or Negative**
- Working capacity ≠ value. Orchestration multiplies capacity, not judgment [INTERP]: "a cheap, fast, wrong answer scaled across a multi-agent team is still cheap and wrong at scale."
- Three human analogies: brilliant professor vs. street-smart entrepreneur; new CEO vs. veteran employee; world-class investor vs. empathetic salesperson — each shows capability ≠ fit ≠ value.
- No production tier or ownership architecture is shown by this paper's evidence to be inherently more likely to produce positive value than another.
- Speaker note: This is the hinge slide — everything before it is cost/capacity; everything after assumes this boundary holds.

**Slide 18 — From AI Working Capacity to New Value**
- Conceptual bridge, not a numerical finding [INTERP throughout]: capacity created (Parts I–IV) is not automatically growth, income, or social benefit.
- Two separate questions: (1) can the capacity be created — this paper's cost/utilization model; (2) can that capacity create and capture new value — invention, adoption, trust, revenue model, none of which any $/token figure supplies.
- Visual: "Creating Growth Based on New Value" (Diagram 11) — two columns converging on a shared "New Value" band: Idea/Invention → Innovation → Verifying New Value descending on the left; Productivity → Revenue Model → Value Proposition & Communication ascending on the right.
- Note: the same boundary applies to any future Scenario Explorer built on this paper's workbooks — it models cost and capacity, not whether a deployment creates value.
- Speaker note: This slide is the second hinge — it stops the room from reading "cheaper tokens" as "more growth" without the missing middle step.

**Slide 19 — Part V: The Ownership Stack**
- Layers, each separately ownable: energy, hardware, compute (access), models, information, agents, identity, governance.
- Concentration varies sharply by layer: hardware manufacturing is extremely concentrated [FACT/INTERP]; information is the least standardized/portable layer [INTERP].
- No single actor owns "AI" end to end — ownership questions must be asked layer by layer.
- Speaker note: Use this to reframe "who owns AI" as a bad question — it's really six or seven different questions.

**Slide 20 — Six Coexisting Access Models**
- Table: Centralized platform · Enterprise dedicated (e.g., IBM Cloud/Together AI $240M deal [FACT]) · Open models on owned hardware · Private/individual ownership · Cooperative (€19.50–23/member/month for a DGX Spark pool, or €42/member/month for a shared workstation-class machine — two hardware tiers, not one contested figure [CALC/FACT]) · Local/regional capacity.
- None asserted as universally superior — trade-offs differ across scale, cost, privacy, resilience, convenience, control [INTERP].
- Ownership models only make arithmetic sense once usage sits consistently at copilot-band intensity or above [CALC-supported break-even].
- Speaker note: The two cooperative figures describe two different hardware tiers (a DGX Spark pool vs. a shared workstation-class machine), not a discrepancy in one estimate — shown explicitly as a worked example of assumption transparency.

**Slide 21 — Electricity-Grid Analogy and Digital Sovereignty Beyond Geography**
- Analogy: home solar → cooperative → commercial producer → utility-scale plant → grid exchange, mapped onto AI compute tiers [INTERP, author's own commentary, not independently sourced verbatim].
- Weakest link: no frictionless spot market for AI compute yet exists, unlike electricity or Bitcoin hashrate [FACT/INTERP].
- Sovereignty reframed via five questions: control, portability, exit, governance, continuity — not just server geography [INTERP, framework proposed in this paper].
- Speaker note: Note explicitly that this analogy is the author's own structural comparison, flagged as such rather than presented as settled.

**Slide 22 — Part VI: Scale Scenarios, Tier by Tier**
- Table: Home ($4,699, $1.37–11.89/M tokens) · Cooperative (~$47K, $1.99–7.62/M) · Professional (unofficial/ASSUMPTION, $0.044–0.146/M, no opex — least evidenced) · Hyperscale (~$16M/4-rack, canonical full-layer $0.091–0.312/M, mid $0.133/M) [CALC throughout].
- Governing levers: utilisation (3.5–4x swing), financing term, interactivity setting — all editable, none a forecast.
- Cost-per-hour of capacity is not value — a 500–800x swing between production cost and retail pricing shows how meaningless a bare figure is without its pricing assumption.
- Speaker note: State the non-advice boundary explicitly here — every number is a scenario, not a recommendation.

**Slide 23 — Humanoid Robots as Embodied Working Capacity**
- Real market range: Unitree G1 from $13.5K [FACT] to Agility Digit ~$250K [ATTR, secondary]; illustrative €25K base case sits within this spread [INTERP].
- Same utilisation pattern as digital tiers: 2,000→8,000 hrs/yr cuts cost/hour ~3.5–4x [CALC]; electricity is not the binding cost here (unlike token production).
- Scope explicitly narrow: excludes supervision, insurance, downtime — every figure is a cost floor, not a full commercial cost.
- Speaker note: Flag this as a "later, illustrative extension," not a general robotics-economics claim.

**Slide 24 — Part VII: Six Lenses, Equal Weight, No Ranking**
- Individual: rent vs. own break-even sits near the copilot band, not chat band.
- SME: delivery innovation, not product innovation, is the accessible opportunity [ATTR, author's prior work].
- Investor/Government/Builder/Educator: same MOU and cost figures, read through different risk lenses — interested-party statements (Huang, Fink) flagged consistently as ATTR, not audited fact.
- Speaker note: Reiterate — these are grouped for slide economy only, not because any lens outranks another.

**Slide 25 — Closing: Opportunity, Not Inevitability**
- Capital and infrastructure figures (Parts II–IV) support reading this as opportunity, not destiny [INTERP, editorial choice].
- The unknown variable: adoption, organizational change, and time — not model capability — appear to be the binding constraint [INTERP].
- Closing synthesis: "how do we get it done" is getting cheaper faster than most say plainly; "what should we do" has not gotten any easier at all.
- Speaker note: End on the open question, not a resolved answer — the paper deliberately does not decide this for the reader.

**Slide 26 — Licence and Attribution**
- Licensed under CC BY 4.0. Suggested attribution: Research synthesis and modelling by Valto Loikkanen, assisted by AI.
- This material is educational research and scenario analysis — not investment, legal, tax, procurement, or policy advice.
- Companion workbooks (Global Baseline, AI Working-Capacity Conversion, Token-Factory Scenarios, Investment-Thesis Notes, Humanoid Working-Capacity, Localized/EUR-Finland template) available for readers to rebuild any model with their own inputs.
- Speaker note: Close by pointing to the workbooks as the place where the audience can go build their own numbers.

---

Licensed under CC BY 4.0. Suggested attribution: Research synthesis and modelling by Valto Loikkanen, assisted by AI.