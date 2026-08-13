# DEFINITIONS AND NOTATION

### Appendix — companion to "Why Are They Spending Trillions on AI?" (Valto Loikkanen, CC BY 4.0)

## How to read this appendix

This is a plain-language glossary of every technical and economic term used elsewhere in the whitepaper and its companion workbooks. Entries are alphabetized. Most entries are **definitions** — descriptions of what a term means and how it's used in this paper — and are not themselves factual claims requiring an evidence-class tag. Where a definition includes a specific number, spec, or example (a price, a benchmark result, a named product), that number is tagged inline using the same five-class system used throughout the rest of the paper, so a reader can tell a plain definition apart from an embedded factual claim. Terms are cross-referenced to the whitepaper part/section where they carry the most weight, where useful.

**Evidence-class legend** (defined fully in the front matter and Source Register; restated here because "evidence class" is itself a defined term below):

| Code | Meaning |
|---|---|
| **OBSERVED FACT** | Primary documentation, official specs/pricing, filings, regulation, or a direct recording/transcript, independently checked against a live/primary source on or immediately before 2026-08-12. |
| **ATTRIBUTED STATEMENT** | What a named executive, organization, or source says, publicly and on the record — not automatically treated as independently proven fact. |
| **DERIVED CALCULATION** | Transparent arithmetic from cited OBSERVED FACT or ATTRIBUTED STATEMENT inputs, with the formula shown. |
| **SCENARIO ASSUMPTION** | A visible, editable parameter used to explore a possible case — explicitly not a market figure. |
| **INTERPRETATION** | A clearly labelled explanation of how facts, statements, and scenarios may connect — never presented as fact. |

---

## A

**Agent / agentic AI.** Software built on top of one or more AI models that can take multi-step action toward a goal — calling tools, writing and running code, browsing, editing files — with limited or no human intervention between steps, rather than answering a single prompt and stopping. OpenAI's Codex is used throughout this paper as a worked example of an agentic coding tool. See *orchestration*.

**AI working capacity.** This paper's core intermediate concept, distinct from raw token output. Working capacity is the *actual ability to get something done* with AI — shaped jointly by model capability, infrastructure, information/context available to the model, tools it can call, orchestration, reliability, and human direction. A model producing tokens quickly is not automatically high working capacity; working capacity is what remains after all those multiplying and dividing factors are accounted for. Distinguished sharply, and deliberately, from *outcome* and *value* (see those entries) — working capacity is a capacity to act, not a guarantee that the action produced something worth having. Central to Part III.

**AI working hour ($/AI-working-hour).** A derived unit used throughout the companion workbooks to translate a $/million-token production cost into a cost per hour of a given usage-intensity band (chat/advisor, active copilot, delegated single agent, heavy multi-agent orchestration — see *usage-intensity band*). **Formula: $/hour = ($/million tokens) × (tokens consumed per hour ÷ 1,000,000).** Every $/AI-working-hour figure in this paper is a **DERIVED CALCULATION** built on a stated $/M-token input and a stated, editable tokens/hour assumption — it is not a market price quoted anywhere, and it says nothing about the value of the hour's output.

**Amortization / amortizing loan.** The standard method used in every cost tier in this paper to spread a hardware purchase's capital cost evenly (in payment terms) across a financing period, including interest. **Formula used throughout: M = P × i ÷ (1 − (1+i)⁻ⁿ)**, where P = principal (amount financed), i = periodic interest rate, n = number of payment periods. Changing the term length or rate — both **SCENARIO ASSUMPTIONS** in every workbook here — changes the annual financed-capital figure without changing the underlying hardware cost at all.

**ATTRIBUTED STATEMENT.** See evidence-class table above. The critical distinction this paper insists on: the fact that a named person said something on the record can itself be an **OBSERVED FACT** (i.e., independently confirmed against a transcript that they said those words), while the underlying claim they made remains only an ATTRIBUTED STATEMENT unless separately, independently proven. Example used repeatedly in this paper: it is an OBSERVED FACT that Sam Altman said demand would keep growing; it is not thereby proven that demand will actually keep growing at the rate he described.

---

## B

**Batch processing.** A discounted mode of API access (roughly half the standard per-token price for several labs cited in this paper) in which requests are queued and processed non-urgently rather than returned in real time. Relevant to *retail API pricing* comparisons in Part III/Part VI, never to *owned-production cost*.

**BF16 / FP16 / FP8 / FP4.** Numeric precision formats used to represent the weights and activations inside an AI model during training or inference. Lower-precision formats (FP8, FP4) use fewer bits per number, which increases throughput and lowers memory/power cost per token, at some risk to numerical accuracy depending on the model and task; this is why the same chip's headline "tokens per second" or "tokens per watt" figure can differ by several multiples depending on which precision is being quoted (see *sparsity*). NVIDIA's GB300 NVL72 rack, cited in Part II, reports FP4 performance roughly 4x its FP16/BF16 figure — this is a real characteristic of the format, not an inconsistency **[OBSERVED FACT, NVIDIA product page, cluster A]**.

---

## C

**Capex (capital expenditure).** The upfront purchase cost of hardware (a chip, a rack, a robot, a data center) — as opposed to *opex* (electricity, maintenance, staffing, financing interest, all of which recur). This paper's cost models consistently separate capex, financing cost, and operating cost into distinct rows rather than collapsing them into one blended number, per the "economic-layer separation" rule stated in Part II and enforced in every workbook.

**Cluster (source register).** A grouping label (A through J) used in this paper's Source Register / Fact-Check Ledger to organize related claims that were checked together (e.g., "Cluster A: NVIDIA hardware, benchmarks, TCO"). Not a technical AI term — purely a citation-organization device internal to this paper's methodology.

**Compute.** Generic shorthand for the processing capability — chips, memory, interconnect, and the electricity and cooling that keep them running — that turns electrical power into the ability to run AI models. The second link in this paper's core chain: energy → hardware → **compute** → models → tokens → AI working capacity → digital work → outcomes → value → agency.

**Context window.** The maximum number of tokens (see *token*) a model can hold "in view" at once across a single conversation or request — prior turns, documents, code, instructions, and the model's own output all share this budget. Frontier models discussed in Part III report context windows around 1 million tokens or more as of this paper's cut-off **[e.g., GPT-5.6 family reported at ~1.05M tokens — ATTRIBUTED STATEMENT via AI-summarized fetch, cluster B]**. A larger context window is not the same as more working capacity — it is one input among several.

**Cooperative infrastructure.** A model, examined in Part V and the companion Localized Scenario Workbook, in which a group of members jointly finances and shares access to compute hardware (illustrated at ~10 machines / ~50 members) rather than each member buying individually or renting from a hyperscaler. Its economics depend heavily on utilization, coordination/governance overhead, and financing terms — all **SCENARIO ASSUMPTIONS** in this paper's models — and this paper deliberately preserves, rather than resolves, a roughly 2x unreconciled gap between two independently produced cost estimates for the same cooperative structure (see Part V, Section 1 of the Token-Factory Scenario Workbook) as an example of how sensitive this kind of model is to unstated assumptions.

---

## D

**Data center.** The physical facility housing racks of compute hardware, along with the power delivery, cooling, and networking needed to run them. "Hyperscale" data centers (Part VI) run many megawatts to multiple gigawatts of continuous power draw.

**DERIVED CALCULATION.** See evidence-class table above. Every instance of this class in this paper shows its formula explicitly rather than presenting only a result — this is a hard requirement of the paper's methodology, not a stylistic choice.

**DGX Spark.** NVIDIA's prosumer/workstation-class AI compute device, used throughout this paper as the reference "Home tier" hardware. Specs: GB10 Grace Blackwell Superchip, up to 1 petaflop FP4 performance, 128GB unified memory, 240W power supply **[OBSERVED FACT, NVIDIA product page, cluster A]**. Its Founders Edition price rose from $3,999 to $4,699 in February 2026 **[OBSERVED FACT, NVIDIA Developer Forums price-change notice, cluster A]** — this paper uses the current $4,699 figure, not the superseded launch price, in every cost model.

---

## E

**Electricity price.** The $/kWh (or €/kWh) rate paid for power. Treated throughout this paper as a **SCENARIO ASSUMPTION**, not a verified market figure, in every localized or scenario workbook — because retail, commercial, and industrial electricity tariffs vary by region, contract, and time, and no single verified global figure exists. Readers are explicitly instructed to substitute their own checked local rate.

**Evidence class.** The five-part classification system (OBSERVED FACT, ATTRIBUTED STATEMENT, DERIVED CALCULATION, SCENARIO ASSUMPTION, INTERPRETATION) that every substantive statement in this whitepaper and its appendices must be sorted into. Defined in full at the top of this appendix and in the paper's front matter; the single methodological device that distinguishes this paper's approach from ordinary trend-forecasting writing.

---

## F

**Financed asset cost.** One of the eight cost "layers" this paper insists on separating (see *layer separation*): the annualized cost of a piece of hardware once interest/financing terms are added to its raw purchase price, as opposed to simple straight-line depreciation. See *amortization*.

**FLOP / PFLOPS.** A floating-point operation (a single arithmetic calculation); PFLOPS = one quadrillion (10^15) such operations per second, the standard unit for describing a chip's or rack's raw computational throughput. Distinct from *tokens per second* — FLOPS measures raw arithmetic capacity, tokens/sec measures the practical output of that capacity running a specific model and workload, and the ratio between the two varies enormously by model architecture and precision format.

**Frontier model.** Industry shorthand (used by labs and press, not a formally defined technical term) for the most capable models a given AI lab currently offers — e.g., OpenAI's GPT-5.6 family, Anthropic's Claude Opus/Fable/Sonnet 5, Google's Gemini 3.1 Pro, all named in Part III. "Frontier" is relative and moves forward continuously; a model called frontier in mid-2026 may not be a lab's top tier a year later.

---

## G

**GB300 NVL72.** NVIDIA's rack-scale AI system used throughout this paper as the reference "Hyperscale/Industrial tier": 72 Blackwell Ultra GPUs, 36 Grace CPUs, 20 TB HBM3e memory, 130 TB/s NVLink interconnect bandwidth, and roughly 135 kW rack power draw (TDP) per an OEM partner spec sheet, not NVIDIA's own page directly **[OBSERVED FACT — NVIDIA product page for compute/memory specs; Lenovo OEM reference document for power draw; cluster A]**. Important caveat carried throughout this paper: the widely repeated "2.5 million tokens/second" DeepSeek-R1 benchmark result for this hardware is an *aggregate across four interconnected GB300 NVL72 racks (288 GPUs total)*, not a single rack — a distinction this paper's cost models correct for explicitly rather than silently reusing the larger, easier-sounding number **[OBSERVED FACT, NVIDIA developer blog / MLPerf v6.0, cluster A]**.

**Gigawatt (GW) buildout.** The unit of scale used by the financial executives quoted in Part I and Part VI when describing AI infrastructure investment (e.g., Jensen Huang's and Larry Fink's ~$50–60 billion "per gigawatt" figure, and Fink's ">70 gigawatts" projected US demand) **[ATTRIBUTED STATEMENT, CNBC transcript, cluster C]**. One gigawatt = 1,000 megawatts = enough continuous power draw, roughly, for a mid-sized city; in this paper's context it refers to the sustained electrical capacity dedicated to AI data-center campuses, not a one-time energy quantity.

**GPU (graphics processing unit).** The class of chip (originally designed for rendering images) that turned out to be well suited to the parallel arithmetic AI models require, and which now underpins essentially all frontier AI training and inference. NVIDIA is the dominant GPU supplier discussed in this paper; AMD's MI-series chips are named as a secondary comparison point in some benchmark sources (cluster A).

---

## H

**Hashprice.** The Bitcoin-mining industry's standard revenue metric: expected daily USD revenue per unit of mining computational power (quoted in $ per petahash/second per day, $/PH/s/day). Used in Part IV/VI purely as a comparison point for "gross revenue per unit of electricity consumed" against illustrative AI-token revenue scenarios — not as a claim that AI compute and Bitcoin mining are economically equivalent activities. Spot hashprice was reported at roughly $31.73–$32.05/PH/s/day around August 10–12, 2026 **[OBSERVED FACT, Luxor Hashrate Index, cluster F]**.

**HGX B300.** NVIDIA's 8-GPU Blackwell Ultra-generation server platform, used in this paper's "Professional/SME tier" as an illustrative mid-scale option. NVIDIA does not publish an official retail price or power-draw figure for this SKU, which is why this tier is explicitly flagged as lower-confidence than the Home and Hyperscale tiers in every cost workbook here **[OBSERVED FACT for the specs themselves — nvidia.com HGX product page, cluster F; ASSUMPTION for any price/power figure used in this paper's models]**.

**Human-hour equivalent.** OpenAI's own internal, self-reported estimate of how long a given AI task would take a human to complete, used by OpenAI to characterize Codex usage (e.g., "70.2% of sampled users made a request estimated to exceed one hour of human work") **[ATTRIBUTED STATEMENT, OpenAI's own blog post, unaudited by any third party, cluster J]**. This paper uses this figure only as an illustration of one possible conversion method between token output and human-labor-equivalent framing (Part III/VI), explicitly not as a validated multiplier, and separately lists the many dimensions (quality, reliability, supervision burden, context) along which AI work and human work are *not* directly comparable.

**Humanoid working capacity.** The physical-robotics analogue to AI working capacity, explored as an illustrative extension in this paper's companion workbooks: *capital + energy + maintenance + utilisation + orchestration → humanoid physical working capacity.* Modeled using both an illustrative €25,000 SCENARIO ASSUMPTION robot price and a real observed/attributed market price range spanning roughly $13,500 (Unitree G1, OBSERVED FACT) to ~$250,000 (Agility Digit, ATTRIBUTED STATEMENT via convergent secondary sourcing) — see Part V and Release Asset #11.

**Hyperscaler.** A company that operates data-center infrastructure at a massive, "hyper" scale — commonly used for the small set of firms (and, in this paper's context, the AI labs and financing partners building out gigawatt-class AI campuses) whose infrastructure footprint dwarfs an ordinary enterprise data center.

---

## I

**Inference.** The stage at which a *trained* AI model is actually run to produce an output — answering a prompt, generating code, taking an agentic action — as opposed to *training* (see below), which is the earlier, far more compute-intensive process of building the model's weights in the first place. Nearly every cost figure, benchmark, and workbook in this paper (tokens/sec, $/M-tokens, tok/s/MW) describes **inference** cost and throughput specifically, not training cost, which is a separate and generally much larger expense not modeled in detail here.

**INTERPRETATION.** See evidence-class table above. Used throughout this paper to flag places where the text is explicitly connecting facts, statements, or assumptions into a possible reading — and explicitly *not* asserting that reading as settled fact. Readers should treat every INTERPRETATION-tagged passage as one plausible lens, open to disagreement.

---

## J

**Jevons paradox (as used here).** The general economic pattern in which making something cheaper and more efficient can increase total consumption of it enough that aggregate spending or resource use rises rather than falls (named for a 19th-century observation about coal efficiency and coal use). Referenced in Part I/IV as the implicit logic behind Sam Altman's argument that falling per-token AI cost drives higher, not lower, total AI spending — his own claim that "the cost to use a given level of AI falls about 10x every 12 months... and lower prices lead to much more use" is an **ATTRIBUTED STATEMENT**, and the Jevons-paradox framing applied to it in this paper is this paper's own **INTERPRETATION** of that statement, not a claim Altman used that specific term himself.

---

## L

**Layer separation (economic-layer separation).** This paper's core methodological rule, stated in Part II and enforced in every workbook: never collapse raw energy cost, hardware-amortized cost, financed-asset cost, full operating-infrastructure cost, utilization-adjusted cost, token-production cost, workload/working-capacity cost, and outcome/value into one blended number. Each is shown as its own row with its own formula, precisely because collapsing them is the most common way headline AI-cost claims mislead.

---

## M

**Maintenance reserve.** A recurring cost line (modeled in this paper's robotics workbook as a flat 10% of purchase price per year, a **SCENARIO ASSUMPTION**, not a manufacturer-quoted figure for any named platform) covering repair, servicing, and part replacement over a hardware asset's working life.

**MoE (Mixture of Experts).** A model architecture in which only a subset of the model's total parameters ("experts") are activated for any given input, rather than running the full parameter count on every token. This generally lowers the compute cost per token relative to an equivalently-sized "dense" model, which is why MoE architecture is referenced in Part II/III alongside throughput and cost-per-token comparisons (e.g., NVIDIA's own claim that its Vera Rubin platform needs "one-fourth the number of GPUs" to train MoE models in the same time versus GB200 — an **ATTRIBUTED STATEMENT**, cluster A). DeepSeek-R1, the model used in most of this paper's cited inference benchmarks, is an MoE model.

**MTok / million tokens.** The standard billing unit for AI API pricing (dollars per million input or output tokens) and the standard unit used throughout this paper's cost-per-token tables. Not to be confused with *tokens/sec* (a throughput rate) or *AI-working-hour* (a derived time-based unit).

**MW / MWh (megawatt / megawatt-hour).** Units of power (MW, an instantaneous rate) and energy (MWh, power sustained over an hour) used throughout Part II/VI's throughput-per-power comparisons (e.g., "tokens per second per MW"). One MW = 1,000 kW; one GW = 1,000 MW.

---

## N

**NVLink.** NVIDIA's proprietary high-speed chip-to-chip interconnect, used to link GPUs within a rack (e.g., 130 TB/s aggregate bandwidth across the GB300 NVL72's 72 GPUs) so they can act as one large pool of compute rather than isolated chips **[OBSERVED FACT, NVIDIA product page, cluster A]**. Interconnect bandwidth is one of the specs, alongside memory bandwidth and precision format, that determines real-world tokens/sec — not raw FLOPS alone.

---

## O

**OBSERVED FACT.** See evidence-class table above. The strictest class in this paper's system: it requires independent verification against a live or primary source on or immediately before the paper's 2026-08-12 cut-off, with an exact citation.

**Open-weight model.** A model whose trained parameters ("weights") are published and can be downloaded and run by anyone with sufficient hardware — e.g., DeepSeek-R1, Qwen, Kimi, all referenced in this paper's *owned-production cost* models — as distinct from a *proprietary model* accessible only through a lab's paid API. This paper's cost models deliberately price owned/cooperative hardware running open-weight models, never using a proprietary lab's retail API price as a stand-in cost basis for owned infrastructure (see *retail API pricing* below, and the explicit methodology correction in the Token-Factory Scenario Workbook, Section 2).

**Opex (operating expenditure).** Recurring costs — electricity, maintenance, staffing, networking, software — as opposed to the one-time *capex* of buying hardware. Kept in a separate row from capex and financing cost throughout this paper's models.

**Orchestration.** The layer of software and process design that coordinates multiple AI models, agents, and tools toward a task — scheduling, routing between models, managing parallel agent instances, handling retries and failures. Named explicitly as one of the multiplying/dividing factors that separates raw token output from real *AI working capacity* (Part III), and as one of the five inputs (alongside capital, energy, maintenance, utilization) in the humanoid working-capacity chain (Part V).

**Outcome.** In this paper's core chain (energy → hardware → compute → models → tokens → AI working capacity → digital work → **outcomes** → value → agency), the result that digital or physical work actually produces in the world — distinct from, and not mechanically guaranteed by, the working capacity that was applied to produce it. A cheap, fast, wrong answer scaled across a multi-agent team is still cheap and wrong at scale; this paper repeats this boundary deliberately in every workbook rather than stating it once.

---

## P

**PUE (Power Usage Effectiveness).** A standard data-center efficiency metric: total facility power draw divided by the power actually delivered to IT equipment (chips, servers). A PUE of 1.0 would mean zero overhead from cooling, lighting, and other facility loads; real-world data centers run higher. Note: this paper's own cost models do not independently verify a specific current PUE figure for any named hyperscale facility — where a "full operating infrastructure cost" layer is modeled (adding facility overhead on top of raw hardware and electricity), it uses an explicit illustrative percentage-of-capital **SCENARIO ASSUMPTION** rather than an unverified PUE figure, and this gap is stated plainly rather than papered over.

---

## R

**Retail API pricing.** What a lab (OpenAI, Anthropic, Google) charges a customer per million tokens to access its own proprietary, finished model — a price that bundles the lab's margin, R&D amortization, safety work, and reliability guarantees. This paper treats retail API pricing strictly as a **comparison benchmark**, never as a cost basis for modeling owned or cooperative infrastructure; every workbook table is explicitly labeled "OWNED PRODUCTION" or "RETAIL BENCHMARK" so the two are never collapsed into one column, after an earlier internal drafting error (documented and preserved, not smoothed over, in the Token-Factory Scenario Workbook, Section 2) made exactly that mistake.

---

## S

**SCENARIO ASSUMPTION.** See evidence-class table above. Every instance in this paper is stated plainly as an assumption, is editable, and specifies exactly what it controls (e.g., "20% down payment — controls how much capital is financed vs. paid up front").

**Sparsity (2:4 sparsity, sparse vs. dense throughput).** A hardware/model optimization technique that skips a structured subset of zero or near-zero values during computation to increase effective throughput. NVIDIA's headline PFLOPS figures are frequently the *sparse* (roughly 2x higher) number rather than the *dense* baseline figure — this paper's source register flags this distinction explicitly as a common place headline hardware marketing figures can mislead if the dense/sparse basis isn't specified (cluster A).

---

## T

**TCO (Total Cost of Ownership).** The all-in cost of operating a piece of hardware over its useful life — capital/financing + electricity + maintenance + facility overhead — as opposed to purchase price alone. This paper builds TCO from named, separated layers (see *layer separation*) rather than presenting a single blended TCO number. A frequently-cited TCO figure — "$0.123 per million tokens" for GB300 NVL72 at 116 tokens/sec/user, using NVIDIA Dynamo and TensorRT-LLM — is confirmed directly on NVIDIA's own site (checked 2026-08-13) **[cluster A]**, but describes a 72-GPU rack-scale system at a specific interactivity setting only; it must never be used to price a single workstation or desktop-class device, which would understate that tier's real cost by roughly two to three orders of magnitude.

**Token.** The basic unit AI language models process and generate — roughly a word-piece (sometimes a whole short word, sometimes part of a longer word), not a whole word or character. Every $/M-token, tokens/sec, and tokens/watt figure in this paper is built on this unit. Token counts for the *same* piece of text can vary slightly between different models' tokenizers, which is a real source of small inconsistency across cross-lab comparisons in Part III.

**Tokens/kWh, tokens/sec, tok/s/MW ("tokens per watt").** Throughput-efficiency metrics used throughout Part II to describe how many tokens a given piece of hardware can produce per unit of time or per unit of electricity consumed. Highly sensitive to which model, precision format, and "interactivity" setting (tokens delivered per second *per active user*, a latency/throughput trade-off) is being measured — this paper's source register found that a commonly-cited "2.8 million tok/s/MW" GB300 figure could not be confirmed as an exact published number, with directly observed adjacent figures ranging from roughly 1.67 million to 3.89 million tok/s/MW depending on the interactivity point chosen **[cluster A]** — illustrating why this paper insists any single-point efficiency figure state its interactivity/precision basis.

**Training.** The (generally far more compute- and energy-intensive) process of building a model's weights from data, as distinct from *inference* (running the already-trained model). This paper's cost and throughput models are inference-focused; training cost is referenced only qualitatively (e.g., NVIDIA's claim that its Vera Rubin platform needs "one-fourth the number of GPUs" to train MoE models in a given time versus GB200 — an **ATTRIBUTED STATEMENT**, cluster A) and is not separately modeled in dollar terms in this paper's workbooks.

---

## U

**Usage-intensity band.** A four-rung illustrative ladder used throughout Part III and the AI Working-Capacity Conversion Workbook to translate token throughput into working-capacity context: **chat/advisor** (~10,000–30,000 tokens/hour), **active copilot** (~60,000–120,000), **delegated single agent** (~200,000–600,000), and **heavy multi-agent orchestration** (~1,000,000–12,000,000+, open-ended). Every band is explicitly a **SCENARIO ASSUMPTION** — an illustrative bracketing, not a measured industry standard — informed loosely by OpenAI's own self-reported, unaudited Codex usage telemetry (cluster J) but not calibrated directly to it.

**Utilization (utilization rate).** The share of a piece of hardware's maximum available operating time or throughput that is actually used, as opposed to idle. The single most sensitivity-dominant variable in every cost-per-token and cost-per-hour model in this paper: fixed capital and financing costs accrue whether or not hardware is used, so lower utilization mechanically raises the effective cost per token or per hour, independent of any change in hardware price.

---

## V

**Value.** The final, deliberately-separated step in this paper's core chain — whether an outcome produced by AI working capacity is actually worth something (positive), worth nothing, or worth less than it cost (negative) to somebody. This paper's central methodological stance, repeated in every Part and every companion workbook: **value is never mechanically derived from any of the preceding cost or capacity layers.** No amount of cheap compute, high throughput, or low $/AI-working-hour proves the work performed was valuable.

---

## W

**Working capacity.** See *AI working capacity* and *humanoid working capacity* above — the general concept, of which the AI/digital and humanoid/physical versions are this paper's two worked instances.

---

*This glossary is released, like the rest of the whitepaper, under CC BY 4.0. Readers extending this paper's models to new tiers, currencies, or hardware are encouraged to add terms here using the same alphabetized, plain-language, evidence-class-aware format.*

---

This appendix cross-references the Global Baseline Workbook (Release Asset #7) and the AI Working-Capacity Conversion Workbook (Release Asset #9), both included in this release package.