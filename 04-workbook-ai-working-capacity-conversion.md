# Release Asset #9 — AI Working-Capacity Conversion Workbook
## The Usage-Intensity Ladder: Tokens/Hour → $/AI-Working-Hour, Across Production Tiers — Plus a Human-Work Comparison Table

**Part of:** *Why Are They Spending Trillions on AI?* — Valto Loikkanen, CC BY 4.0
**Workbook status:** v1.0 draft, built from the verified source register (cut-off 2026-08-13)
**Currency baseline:** Global USD
**Depends on:** Release Asset #7 (Global Baseline Workbook — production-cost curves per tier). This workbook does not re-derive hardware/electricity/financing costs; it takes Asset #7's already-derived $/million-tokens figures as inputs and converts them into $/AI-working-hour across a usage-intensity ladder.
**Not investment, legal, tax, procurement, or policy advice.** Every scenario below is an editable illustration built on stated assumptions, not a forecast or recommendation.

---

## Evidence-class legend (used throughout every table)

| Tag | Meaning |
|---|---|
| **OBSERVED** | Primary documentation, official spec/price page, filing, regulation, or direct recording/transcript, independently checked on/immediately before 2026-08-12. |
| **ATTRIBUTED** | A named person/organization's on-the-record statement. Not independently proven merely because it was said — including when the statement is itself well-documented. |
| **DERIVED** | Transparent arithmetic from cited OBSERVED/ATTRIBUTED inputs. Formula always shown, never just the result. |
| **ASSUMPTION** | A visible, editable scenario parameter — not a market fact. What it controls is always stated. |
| **INTERPRETATION** | A labelled explanation of how the above may connect. Never presented as if it were a fact. |

---

## Part A — What a "token" and an "AI-working-hour" are, and what they are not

**INTERPRETATION.** A token is a measurable unit of model processing/output — it meters AI *working capacity*, roughly the way a kWh meters energy capacity. A token is **not** equivalent to value, quality, correctness, or "an hour of work." An "AI-working-hour" as used in this workbook is a *usage-intensity band* (a rate of token consumption sustained across one clock-hour), not a unit of guaranteed human-equivalent output. Two agents can each burn identical tokens/hour and produce wildly different value — one useful, one wasted, one actively harmful. This workbook prices token throughput; it does not, and cannot, price outcomes. See Part D for the outcome/value boundary stated explicitly, and Release Asset #11 (or the paper's core value-framework section) for the fuller treatment of why working capacity ≠ value.

**Required economic-layer separation (never collapsed in this workbook):**

```
raw energy cost → hardware-amortized production cost → financed asset cost → full operating infrastructure cost
→ capacity/utilisation cost → token production cost → workload/AI-working-capacity cost
→ outcome and value  (NOT mechanically determined by anything above this line)
```

Everything in Parts B and C below lives at the "token production cost" and "workload/AI-working-capacity cost" layers. Part D restates explicitly that the step to "outcome and value" is never automatic.

---

## Part B — The usage-intensity ladder (tokens/AI-working-hour)

Four bands, low/mid/high, each an **ASSUMPTION** (illustrative range, not a single verified statistic) but informed where noted by OpenAI's Codex telemetry (**ATTRIBUTED**, self-reported, not independently audited).

| # | Usage-intensity band | What it describes | Tokens/AI-working-hour: Low | Mid | High | Class |
|---|---|---|---|---|---|---|
| 1 | **Chat/advisor** | Human asks, AI answers; human reads/decides/executes. AI never touches the world directly. | 10,000 | 20,000 | 30,000 | **ASSUMPTION** |
| 2 | **Active AI coworker** | Human and AI work the same task together in real time (co-editing, co-drafting, pair-programming style); continuous back-and-forth within the hour. | 60,000 | 90,000 | 120,000 | **ASSUMPTION** |
| 3 | **Delegated single agent** | Human defines an outcome/objective; one agent executes autonomously for a stretch, human supervises/reviews rather than co-drafts. | 200,000 | 400,000 | 600,000 | **ASSUMPTION** |
| 4 | **Heavy multi-agent orchestration** | Human directs a fleet — multiple parallel agents running simultaneously against one human clock-hour, not one agent running fast. | 1,000,000 | 5,000,000 | 12,000,000+ | **ASSUMPTION** |

**What each band's boundary controls:** moving a band's low/mid/high number up or down directly rescales every $/AI-working-hour figure in Part C for that row — these are the single most important editable inputs in this workbook. Replace them with your own organization's observed token logs if you have them; the numbers above are illustrative bands, not measured medians for any specific product or company.

### B.1 Why band 4 is stated as "1,000,000-12,000,000+" and not a tighter range

**ATTRIBUTED, OpenAI's own self-reported internal telemetry (source register Cluster J — treat as company self-report, not independently audited):**

- Codex reached **99.8%** of OpenAI's own weekly internal output tokens (vs. non-Codex chat usage) by mid-2026.
- By May 2026, **70.2%** of sampled individual Codex users had made at least one request OpenAI itself estimated as equivalent to more than **1 human-hour** of work; **25.6%** had made at least one request estimated above **8 human-hours**.
- By June 2026, users at the **99th percentile** regularly generated **more than 60 hours of Codex agent-turn time per single calendar day**, distributed across multiple parallel agents.

**Corrected 2026-08-13 — the inference below was invalid and has been removed.** An earlier version of this passage claimed that ">60 agent-turn-hours per calendar day" is evidence that a user generates 60 agent-hours *within one human clock-hour*. That does not follow: a calendar day contains 24 clock-hours, so 60 agent-turn-hours spread across a full day could be produced by as few as ~2.5 agents running continuously throughout the day — it says nothing on its own about how many agents run *simultaneously within any single hour*. The OpenAI statistic is retained below only for what it actually shows, not for the invalid extrapolation:

**What this statistic actually supports [ATTRIBUTED, OpenAI's self-report]:** it is strong evidence of sustained, heavy *parallel* usage by 99th-percentile users, aggregated across a full day, and of a long, fast-growing tail in request duration (the 8h+ share of requests reportedly grew "+1131%" over roughly six months per the same report). It does **not**, by itself, establish a specific tokens-per-human-clock-hour figure for band 4.

**Why band 4 remains anchored as an open-ended "1,000,000–12,000,000+" [SCENARIO ASSUMPTION, not DERIVED from the statistic above]:** the ceiling is illustrative, chosen to be wide enough to accommodate genuinely heavy parallel-orchestration scenarios without implying false precision — it is not calculated from the 60-hours/day figure. A reader who has actual token-consumption logs or concurrency data for a specific heavy-orchestration workflow should replace this band with a directly measured figure rather than relying on this illustrative ceiling (see Part G's recommendation to use your own measured token logs).

**Important scope caveats, stated plainly:**
- These figures describe OpenAI's own internal employee usage of its own coding-agent product (Codex). They are evidence that heavy multi-agent orchestration usage exists and can be extreme — they are **not** a general population statistic, not independently audited by any third party, and not necessarily representative of usage in other organizations, other tools, or non-coding work.
- A separately-claimed "NVIDIA reference agentic workload of 32,000 input + 8,000 output tokens per turn" **could not be verified anywhere** (source register Cluster J) and is explicitly **not used** as an input to this workbook's bands.

---

## Part C — $/AI-working-hour across production tiers

This is the core deliverable: cross the Part B usage-intensity ladder against Release Asset #7's already-derived production-cost tiers, at low/mid/high scenarios on both axes.

**Formula (DERIVED, used for every cell below):**

```
$/AI-working-hour = (tokens_per_working_hour / 1,000,000) × ($/million_tokens_at_that_production_tier)
```

Floor = best-case usage-band tokens/hr (Low) × best-case (cheapest) production-tier $/M tokens.
Central = mid-case tokens/hr (Mid) × mid-case production-tier $/M tokens.
Ceiling = worst-case usage-band tokens/hr (High) × worst-case (priciest) production-tier $/M tokens.
This intentionally pairs "best-with-best" and "worst-with-worst" to bound a plausible range — it is not claiming best-usage always coincides with best-production-economics in reality; treat floor/ceiling as an illustrative bracket, not a joint-probability forecast.

### C.0 Production-tier $/million-tokens inputs (carried directly from Release Asset #7 — not re-derived here)

| Production tier | Low (best-case) $/M tok | Mid $/M tok | High (worst-case) $/M tok | Confidence class (per Asset #7) |
|---|---|---|---|---|
| **Home** — 1× DGX Spark, owned production | $1.71 | $3.17 | $11.89 | High on hardware price/power (OBSERVED); throughput is an OBSERVED community benchmark; utilization is ASSUMPTION |
| **Cooperative** — 10× DGX Spark, 50 members, owned production | $1.99 | $3.20 | $7.62 | High on hardware; admin/overhead line is ASSUMPTION |
| **Professional** — 1× HGX B300 (8-GPU) node, owned production | $0.044 | $0.064 | $0.146 | Low-medium — capex and power are ASSUMPTION placeholders (no public price/power found for this SKU); throughput is a DERIVED scaling estimate, not a direct benchmark |
| **Hyperscale/Industrial** — 1× GB300 NVL72 rack, owned production | $0.091 | $0.133 | $0.312 | Medium — rack specs/power OBSERVED; capex is analyst-anchored ASSUMPTION, not an official NVIDIA price |
| **Retail API** — buy-from-market, NOT owned production (comparison layer only) | $0.90 | $9.00 | $38.00 | OBSERVED (Anthropic, Google) / ATTRIBUTED (OpenAI, via AI-summarizing fetch tool — see Asset #7 §7 confidence notes) |

**Retail API blend methodology (DERIVED):** each named model's "blended $/M tokens" = `0.3 × input_price + 0.7 × output_price` (**ASSUMPTION**: 30% input / 70% output token mix, illustrative of an agentic/generation-heavy workload rather than a short-question chat workload — a chat-heavy workload with more input than output tokens would shift this blend lower). Floor = OpenAI GPT-5.6 Luna blended ($0.90); Mid ≈ OpenAI GPT-5.6 Terra / Google Gemini 3.1 Pro blended (both $9.00); Ceiling = Anthropic Claude Fable 5 blended ($38.00). **Critical methodology reminder (carried from Asset #7 §1): retail API prices are the "buy electricity from the grid" comparison point for renting someone else's finished token-production capacity — they are never a valid input to price your own owned hardware, and are shown here only so a reader can see how self-hosted production cost compares to renting frontier-lab inference at the same usage intensity.**

### C.1 Full matrix — $/AI-working-hour (floor | central | ceiling)

| Usage-intensity band | Home | Cooperative | Professional | Hyperscale | Retail API (comparison only) |
|---|---|---|---|---|---|
| **1. Chat/advisor** | $0.0171 \| $0.063 \| $0.36 | $0.0199 \| $0.064 \| $0.23 | $0.00044 \| $0.0013 \| $0.004 | $0.00091 \| $0.0027 \| $0.009 | $0.009 \| $0.18 \| $1.14 |
| **2. Active AI coworker** | $0.103 \| $0.285 \| $1.43 | $0.119 \| $0.288 \| $0.91 | $0.0026 \| $0.0058 \| $0.018 | $0.0055 \| $0.012 \| $0.037 | $0.054 \| $0.81 \| $4.56 |
| **3. Delegated single agent** | $0.342 \| $1.268 \| $7.13 | $0.398 \| $1.280 \| $4.57 | $0.0088 \| $0.0256 \| $0.088 | $0.018 \| $0.053 \| $0.19 | $0.18 \| $3.60 \| $22.80 |
| **4. Heavy multi-agent orchestration** | $1.71 \| $15.85 \| $142.68 | $1.99 \| $16.00 \| $91.44 | $0.044 \| $0.32 \| $1.75 | $0.091 \| $0.665 \| $3.74 | $0.90 \| $45.00 \| $456.00 |

`$/AI-working-hour = (tokens/hr ÷ 1,000,000) × ($/M tokens)` — e.g., Hyperscale, band 3, central: `(400,000 ÷ 1,000,000) × $0.133 = $0.0532`, rounded to $0.053 above.

### C.2 Reading the matrix — what the spread means

**INTERPRETATION.**

1. **Across production tiers at the same usage band**, the spread is enormous — at "delegated single agent" (central case), Hyperscale ($0.053/hr) is roughly **24x cheaper** than Home ($1.268/hr) and roughly **68x cheaper** than the Retail-API comparison ($3.60/hr). This is the same conclusion as Asset #7's tier comparison, now expressed per working-hour instead of per million tokens — economies of scale in owned production infrastructure translate directly into economies of scale in AI-working-hour cost.
2. **Across usage bands at the same production tier**, the spread is also large by construction — moving from "chat/advisor" to "heavy multi-agent orchestration" multiplies $/AI-working-hour by roughly 100-250x at every tier, because the usage bands themselves span two-plus orders of magnitude in tokens/hour (Part B). This is not a claim that heavy orchestration is "worse value" — it is simply consuming far more raw working capacity per clock-hour, by definition.
3. **Home and Cooperative tiers are, at every usage band, more expensive per AI-working-hour than Retail API at its floor (Luna) but cheaper than Retail API at its ceiling (Fable 5).** This matters for the paper's ownership argument: self-hosting on consumer-grade hardware (DGX Spark) is not automatically the cheapest per-token option — its case for existing rests on data control, customization, and independence from a provider (per the ownership-architecture argument elsewhere in the paper), not on being the lowest $/token path. Professional and Hyperscale tiers, by contrast, undercut even the cheapest retail-API floor by 1-2 orders of magnitude — but those tiers require capital and scale far beyond an individual or small cooperative, and their capex/power inputs carry materially lower confidence (see C.0 table) than the Home/Cooperative or Retail rows.
4. **None of this matrix says anything about whether the work performed was worth doing.** See Part D.

---

## Part D — The outcome/value boundary (restated explicitly, not just once in front matter)

**INTERPRETATION, restated per the paper's required framing.** Working capacity → work → outcome → value is a chain, and the last step is never mechanically determined by the ones before it. A $/AI-working-hour figure in Part C tells you what it costs to *generate a given rate of AI output* at a given production tier — it says nothing about whether that output was correct, useful, well-directed, or net-positive. Value can be positive, zero, or negative regardless of how cheaply or expensively the underlying tokens were produced. A heavy-multi-agent-orchestration hour at $0.665 (Hyperscale, central case) that produces confidently-wrong code, poorly-targeted customer outreach, or a plausible-sounding but incorrect analysis is not "cheap good work" — it is cheap work of undetermined or negative value, and abundant cheap working capacity increases rather than decreases the importance of human judgment about *what* to direct that capacity toward. This boundary applies to every number in Part C and every number in Part E; it is not a disclaimer confined to front matter.

This workbook, and the paper it is part of, is **not investment, legal, tax, procurement, or policy advice.** Every scenario is an editable illustration built on stated, visible assumptions — not a forecast or a recommendation about which tier, provider, or usage pattern to adopt.

---

## Part E — Human-work comparison table

**Purpose and scope.** This table exists to make explicit *what is and is not meaningfully comparable* between human labor-hours and AI-working-hours, using the same visible-assumption discipline as the rest of this workbook. It deliberately does **not** produce a single "AI is worth X human-hours" conversion factor as a fact — any such multiplier below is shown as a SCENARIO ASSUMPTION or DERIVED calculation from a named, editable assumption, never as a settled equivalence. The dimensions explicitly marked "not comparable" are not filler — they are the paper's own required caveats about workload, quality, reliability, supervision, and context, kept visible rather than folded silently into a single number.

### E.1 Dimensions that ARE reasonably comparable (with stated method)

| Dimension | How AI side is measured | How human side is measured | Comparability basis | Class |
|---|---|---|---|---|
| **Raw throughput of a defined, mechanical sub-task** (e.g., transcribing a fixed-length recording, drafting a first-pass summary of a fixed document, running a fixed batch of similar classifications) | Tokens processed/produced per clock-hour, from Part B/C | Task-time studies or the requester's own estimate of "how long this would take a competent person," which is itself OpenAI's own internal methodology for its "human-hour equivalent" telemetry (**ATTRIBUTED**, source register Cluster J) — not an independently validated labor-economics standard | Both sides can be clocked against the same fixed, narrowly-scoped deliverable | **DERIVED** (when both sides are actually measured against the same task) |
| **Marginal cost of one additional unit of throughput, holding task type fixed** | $/AI-working-hour at a given production tier (Part C) | Fully-loaded hourly cost of a human worker at a given wage/benefits/overhead level (**ASSUMPTION** — see E.2) | Both are cost figures in the same currency, for the same nominal task category | **DERIVED** |
| **Availability / elasticity of capacity** | Additional AI-working-hours can typically be added by paying for more compute or more API calls, subject to real hardware/provider capacity limits (see Part C's production-tier ceilings) | Additional human-hours require hiring, training, or overtime, subject to real labor-market and calendar-time limits | Both are real, observable capacity-expansion constraints, even though their shapes differ sharply | **INTERPRETATION** |

### E.2 Illustrative $/hour comparison — human labor bands vs. AI-working-hour bands (SCENARIO_ASSUMPTION on the human side; do not read as a market wage survey)

**Human-side ASSUMPTION, explicitly editable, NOT sourced from any specific labor-market dataset in this workbook:**

| Human labor tier | Illustrative fully-loaded $/hour (wage + benefits + overhead) | Class |
|---|---|---|
| Entry-level / routine task labor | $15-$35 | **ASSUMPTION** — replace with your own local, role-specific fully-loaded cost; this is not a wage-survey figure |
| Skilled professional (e.g., mid-level analyst, developer, specialist) | $50-$150 | **ASSUMPTION** |
| Senior specialist / expert consultant | $150-$500+ | **ASSUMPTION** |

| Usage-intensity band | $/AI-working-hour, central case (Hyperscale tier, cheapest owned-production tier from Part C) | $/AI-working-hour, central case (Retail API, buy-from-market) | vs. Entry-level human ($15-35/hr) | vs. Skilled professional ($50-150/hr) |
|---|---|---|---|---|
| 1. Chat/advisor | $0.0027 | $0.18 | Far below either human band at this tier | Far below |
| 2. Active AI coworker | $0.012 | $0.81 | Below | Below |
| 3. Delegated single agent | $0.053 | $3.60 | Below | Below |
| 4. Heavy multi-agent orchestration | $0.665 | $45.00 | Hyperscale still below; Retail-API central case now inside/above the skilled-professional band | Retail-API ceiling ($456/hr, from Part C) exceeds even the senior-specialist band |

**INTERPRETATION, stated carefully:** at the cheapest owned-production tiers, $/AI-working-hour is dramatically below any human labor band shown here, at every usage intensity — this is a real, verifiable arithmetic comparison of *cost of generating tokens* vs. *cost of a human's time*. It is explicitly **not** a claim that an AI-working-hour and a human-labor-hour of the same duration produce equivalent, substitutable, or equally reliable output — that equivalence is exactly what Part E.3 below says cannot be assumed. The comparison in this table should be read as "cost of raw capacity," not "cost of equivalent finished outcome."

### E.3 Dimensions that ARE NOT comparable without an explicit, visible bridging assumption — the paper's required caveats, kept visible rather than hidden

| Dimension | Why a direct AI-hour ↔ human-hour comparison breaks down here | What would be needed to make it comparable (and why this workbook does not supply it) | Class |
|---|---|---|---|
| **Workload definition** | "One AI-working-hour" at 5,000,000 tokens/hour (band 4, mid) is not doing "the same kind of work" as one human-hour — it may represent dozens of parallel, narrow, mechanical sub-tasks rather than one continuous, integrated piece of judgment-requiring work. Token count measures processing volume, not task complexity or task count. | A task-by-task mapping (e.g., "this specific 500,000-token agent run = this specific 3-hour human task, independently timed") for the *specific* workload in question — this workbook supplies no such mapping; OpenAI's own "estimated human-hours" telemetry (Cluster J) is the closest available proxy, and even OpenAI does not disclose its estimation methodology in verifiable detail. | **CAVEAT (kept visible, not resolved)** |
| **Quality / correctness of output** | Nothing in Part B or C measures whether the tokens produced were accurate, appropriately-scoped, or fit for purpose. A human worker's output and an AI agent's output at the "same" nominal task can differ in error rate, hallucination risk, and appropriateness in ways no token count captures. | An independently-audited, task-specific quality/error-rate benchmark for both the AI system and the comparison human workforce, on the identical task distribution — out of scope for this workbook; the paper should not imply one exists. | **CAVEAT (kept visible, not resolved)** |
| **Reliability / consistency across repeated runs** | Human performance and AI-agent performance both vary run to run, but for different reasons (fatigue/skill variance vs. model stochasticity/prompt sensitivity/failure modes), and neither this workbook nor the wider source register contains a controlled repeated-trials study comparing the two. | A repeated-trials reliability study (e.g., variance in output quality across N runs of the same task, same prompt, same human vs. same agent config) — not available in the source register; do not assume AI is either more or less reliable than human labor from anything in this workbook. | **CAVEAT (kept visible, not resolved)** |
| **Supervision and review burden** | Delegated and orchestrated AI usage bands (3-4) explicitly assume "human supervises rather than co-drafts" (Part B) — but the supervision time itself is a real cost not counted anywhere in Part C's $/AI-working-hour figures. A human worker's hourly cost typically already includes some baseline of self-review; an AI agent's supervision cost is a separate, uncounted human-hour layered on top. | A measured supervision-time-per-agent-hour ratio, which would vary enormously by task risk and organizational maturity (see the paper's AI Maturity Framework, Advise→Cowork→Delegate→Lead progression) — not modeled here; any total-cost comparison that omits this is systematically understating the true cost of AI-produced work at bands 3-4. | **CAVEAT (kept visible, not resolved)** |
| **Context and organizational knowledge** | Per the paper's "information is AI's operating system" framing, the same model at the same token cost can produce very different effective working capacity depending on what context/information it has access to — a dimension with no analogue in a simple human hourly-wage figure, where accumulated tacit knowledge is priced implicitly into seniority/experience but not separately measured. | A context-completeness or information-access scoring methodology applied consistently to both the AI system and the human comparison — not available; this workbook prices raw token throughput only, explicitly not "AI working capacity as amplified or constrained by context," which is treated qualitatively elsewhere in the paper, not quantitatively here. | **CAVEAT (kept visible, not resolved)** |

**Required restatement (per the paper's core principle, not optional here):** working capacity is the ability to perform work, not the work itself, and not its outcome or value. Every row above is a reminder that a $/hour comparison between AI and human labor is a comparison of *raw capacity cost*, bounded by named and visible caveats — never a comparison of *guaranteed equivalent value produced*. Where the paper or any reader wants to make a stronger claim than "capacity costs less," the specific bridging assumption (task mapping, quality benchmark, reliability study, supervision ratio, or context-completeness measure) must be stated openly, exactly as this table does, rather than folded silently into a single multiplier.

---

## Part F — Worked example: converting a claimed productivity anecdote into this workbook's units (methodology demonstration only)

**Purpose:** show how a real, source-register-documented claim would be *converted* into this workbook's units, while being explicit about what is and is not verified in the process — not to assert a specific productivity multiplier as proven.

Sam Altman, at Y Combinator's Startup School closing session (Chase Center, San Francisco, 26 July 2026), is independently corroborated (via a CC BY 4.0 attendee-notes repository, not a verbatim official transcript — source register Cluster D) as having used language equivalent to "you can now do three months of work in seventeen minutes." This is an **ATTRIBUTED_STATEMENT** — a real claim, by a named person, in a real recorded setting — not an independently proven productivity ratio.

**DERIVED, methodology-only, explicitly not endorsing the underlying "three months = 17 minutes" claim as true:**

```
If "three months of work" ≈ 3 months × ~160 working-hours/month (ASSUMPTION, standard full-time month) ≈ 480 human-hours,
and this were compressed into 17 minutes = 0.283 hours of AI-working-time,
the implied ratio = 480 / 0.283 ≈ 1,696x
```

**What this DOES and DOES NOT show:**
- It **does** show how a vivid rhetorical claim could, in principle, be translated into a "human-hours compressed per AI-working-hour" ratio comparable in spirit to the tables in Part E.
- It **does not** show that this ratio is accurate, that it applies to any specific task type, at any specific usage-intensity band or production tier from Part C, or that "17 minutes of AI time" corresponds to any measurable token count in this workbook — Altman's statement, per the source register, appears in the context of an argument for founders to be *more ambitious* given AI-driven productivity gains, not as a calibrated benchmark, and no token count or task specification accompanies the original claim.
- Per Part E.3's caveats (workload definition, quality, reliability, supervision, context), a 1,696x-style ratio derived this way should not be presented anywhere in the paper as a validated productivity multiplier — it is included here strictly as a demonstration of *how* to convert a rhetorical claim into this workbook's framework transparently, flagging every assumption used, rather than as a number to be cited on its own.

---

## Part G — How to re-run this workbook with your own numbers

1. **Change the Part B usage-intensity bands** to match your own organization's measured token logs (if available) rather than the illustrative bands here.
2. **Swap in updated production-tier $/M-tokens figures** from a refreshed version of Release Asset #7 as hardware prices, electricity rates, or utilization assumptions change — this workbook's Part C table is entirely downstream of Asset #7 and should be regenerated whenever that workbook's tier figures change.
3. **Replace the Part E.2 human-hourly-cost bands** with your own local, role-specific, fully-loaded labor cost (wage + benefits + overhead + management burden) — the bands here are illustrative placeholders, not a wage survey.
4. **Do not delete or soften the Part E.3 caveats** when adapting this table for a specific claim — if you want to assert a specific human-to-AI equivalence for a specific task, add a new row with your own named, sourced bridging assumption rather than removing the caveat that a general one does not exist.
5. **Preserve the Part D outcome/value boundary language** in any derived or excerpted version of this table — per the paper's evidence standard, every investment-thesis or scale-scenario section must include this boundary explicitly, not merely once in front matter.

---

## Summary table — quick-reference $/AI-working-hour, central-case only

| Usage-intensity band | Home | Cooperative | Professional | Hyperscale | Retail API |
|---|---|---|---|---|---|
| Chat/advisor | $0.063 | $0.064 | $0.0013 | $0.0027 | $0.18 |
| Active AI coworker | $0.285 | $0.288 | $0.0058 | $0.012 | $0.81 |
| Delegated single agent | $1.268 | $1.280 | $0.0256 | $0.053 | $3.60 |
| Heavy multi-agent orchestration | $15.85 | $16.00 | $0.320 | $0.665 | $45.00 |

All central-case figures per `$/AI-working-hour = (mid tokens/hr ÷ 1,000,000) × (mid $/M tokens at that tier)`, tier inputs from C.0, usage bands from Part B. See Part C.1 for full floor/central/ceiling ranges and Part D/E for the outcome-value and human-comparison boundaries that apply to every figure in this table without exception.
