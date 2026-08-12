# Appendix — Source Register and Methodology

### Companion appendix to *"Why Are They Spending Trillions on AI?"* (Valto Loikkanen, CC BY 4.0)
**Factual source cut-off: 2026-08-12. All retrieval dates below are on or immediately before this date unless otherwise noted.**

---

## A. Purpose and scope

This appendix is the fact-check ledger behind the whitepaper, reorganized for publication. Every substantive claim used anywhere in the whitepaper or its companion workbooks traces to one row in the tables below. For each claim, this register states: (1) which of the five evidence classes it belongs to, (2) *how* it was verified — the specific method used, not just "checked" — and (3) the retrieval date, geography, and currency/units context needed to use the figure correctly. Nothing here should be read as proof that an underlying prediction, forecast, or business claim is true; it documents only what was said, published, or independently observed, and by what method that was established.

This is a **verification register**, not a footnote list. Where a claim could not be independently confirmed, that is stated plainly and the claim is downgraded or marked **UNVERIFIABLE** rather than silently dropped or upgraded.

---

## B. Evidence-class legend

| Class | Definition |
|---|---|
| **OBSERVED FACT** | Primary documentation, official specs/pricing, filings, regulation, or a direct recording/transcript, independently checked against a live or primary source on/immediately before 2026-08-12. |
| **ATTRIBUTED STATEMENT** | What a named executive, organization, or source says, publicly and on the record. The *existence* of the statement may be an observed fact; the *substance* of what it claims is not automatically proven. |
| **DERIVED CALCULATION** | Transparent arithmetic from cited OBSERVED FACT or ATTRIBUTED STATEMENT inputs, formula always shown. |
| **SCENARIO ASSUMPTION** | A visible, editable parameter used to explore a possible case — explicitly not a market figure. |
| **INTERPRETATION** | A labelled explanation of how facts, statements, and scenarios may connect — never presented as fact. |
| **UNVERIFIABLE** | A specific figure or claim that was actively searched for and could not be located, confirmed, or corroborated by any method available in this research pass. Retained here so it is not silently reused elsewhere without this flag. |

---

## C. Verification-methodology glossary

Each entry below is tagged with the *method* actually used to reach its evidence class — this is distinct from the evidence class itself. Two claims can carry the same evidence class (e.g., ATTRIBUTED STATEMENT) while resting on very different levels of retrieval confidence.

| Method | What it means | Confidence implication |
|---|---|---|
| **Direct Fetch (Live)** | The primary source URL was fetched and its raw content parsed directly, on or immediately before 2026-08-12. | Highest confidence for the *existence and wording* of what's on the page; does not itself validate the underlying claim's truth. |
| **Direct Fetch (Archived)** | The primary source was retrieved via a Wayback Machine snapshot after the live page blocked automated access (typically a Cloudflare bot challenge). | High confidence — same primary text, retrieved through an archival intermediary rather than live serving. |
| **AI-Summarized Fetch** | A fetch tool rendered the page to markdown and an intermediate model summarized/extracted before returning it — the raw HTML/text was never read directly. | Reduced confidence on exact figures (dollar amounts, thresholds); cross-checked here against a second independent fetch or corroborating source wherever possible, and flagged individually where the two passes disagreed. |
| **Transcript Check (Broadcast)** | Verification against a published, primary broadcast/interview transcript — the authoritative record of what was said on air. | High confidence for exact wording of the statement; the statement's *substance* (a forecast, a claimed cost) remains attributed, not proven. |
| **Transcript Check (Auto-caption)** | Verification against a video's machine-generated caption transcript (e.g., schema.org JSON-LD `transcript` field) or a third party's own paraphrase of a machine transcript. | Moderate confidence; auto-captions can misrender words, and paraphrase sources may compress or reorder content. |
| **Search Corroboration (Fetched)** | A secondary or corroborating article was independently fetched and read directly, even though it is not the primary source of the claim. | Moderate-high confidence for the fact that multiple independent outlets carried the same story; does not independently audit the underlying numbers. |
| **Search Corroboration (Aggregated/Snippet)** | The claim was identified only via search-engine result snippets or headlines; the underlying article itself was not independently fetched (paywall, bot-block, or timeout). | Lower confidence — treat as directional corroboration only, not as an independently re-verified figure. |
| **Community/Forum Attribution** | A real, identifiable but non-institutional claim (e.g., a developer-forum benchmark post) where only part of the thread's content was directly visible to the fetch tool. | Attributed and real, but not independently reproducible from the visible content alone; the headline figure may exceed what was actually verified. |
| **Benchmark/API Query** | Querying a live, self-updating benchmark dashboard or its API directly, and reading the returned data points. | High confidence for the data returned at query time; results are time-sensitive (dashboards update nightly) and interactivity-setting-dependent. |

---

## D. How to read each cluster section

Each lettered cluster below (A–J) corresponds to a distinct research thread. Each section gives: (1) a short scope statement, (2) the dominant verification method(s) used and their limits, (3) a claim-level table with **Evidence Class**, **Method**, **Source**, **Retrieved**, **Geography**, **Currency/Units**, and a **Confidence Note**.

"Geography" indicates the jurisdiction/market the figure describes or the primary source's home base — relevant because prices, regulations, and power costs are not globally uniform. "Currency/Units" is stated explicitly because several figures in this project use USD in the global baseline and EUR in the localized-Finland workbook, and because token/second, kW, GW, and $/MTok are easy to conflate across tiers.

---

## E. Cluster-by-cluster source register

### Cluster A — NVIDIA hardware, benchmarks, and TCO

**Scope:** GB300 NVL72 rack specs; the DeepSeek-R1 "2.5M tokens/sec" benchmark; SemiAnalysis InferenceX TCO and tok/s/MW figures; Vera Rubin vs. GB200/GB300 performance claims; DGX Spark price/specs/community benchmark; the InferenceMAX/InferenceX benchmark itself.

**Methodology used:** Primarily **Direct Fetch (Live)** against NVIDIA's own product pages and developer blog, an OEM (Lenovo) spec sheet, and SemiAnalysis's live InferenceX comparison pages/API, supplemented by one **Community/Forum Attribution** (DGX Spark throughput) and a manufacturer's own **Direct Fetch (Live)** forum notice for a price change. No AI-summarized or search-only claims in this cluster — everything was read from primary text directly.

| Claim | Evidence Class | Method | Source | Retrieved | Geography | Currency/Units | Confidence Note |
|---|---|---|---|---|---|---|---|
| GB300 NVL72 compute/memory/interconnect specs (72 Blackwell Ultra GPUs, 36 Grace CPUs, 20TB HBM3e, 130TB/s NVLink, 1440 PFLOPS FP4 dense) | OBSERVED FACT | Direct Fetch (Live) | nvidia.com/en-us/data-center/gb300-nvl72/ | 2026-08-12 | Global (NVIDIA, Santa Clara, CA, USA) | n/a (specs, PFLOPS/TB/TB·s⁻¹) | NVIDIA's own page omits power draw. |
| GB300 NVL72 rack power draw (135kW TDP, ≤155kW peak) | OBSERVED FACT | Direct Fetch (Live), OEM reference doc | Lenovo Press LP2357 | 2026-08-12 | Global (OEM partner spec, not NVIDIA-published) | kW | Power figure sourced from an OEM partner document, not NVIDIA directly; a separate Sunbird DCIM ~150kW estimate is explicitly lower-confidence (pre-launch projection) and not used. |
| DeepSeek-R1 "2.5M tokens/sec" MLPerf v6.0 benchmark | OBSERVED FACT (with critical scope caveat) | Direct Fetch (Live) | developer.nvidia.com blog, "NVIDIA Platform Delivers Lowest Token Cost..." | 2026-08-12 | Global (MLPerf Inference v6.0 Offline scenario) | tokens/sec | This is a **4-system / 288-GPU aggregate**, not a single 72-GPU rack. Per-rack figure ≈ 9,821 tokens/sec/GPU × 72 ≈ 623,600 tok/s if divided evenly. Must not be presented as a single-rack number. |
| "$0.123/M tokens" TCO for GB300 NVL72 (DeepSeek-R1) | CONFIRMED (corrected 2026-08-13, was previously UNVERIFIABLE) | Direct Fetch (Live) | nvidia.com/en-gb/solutions/ai/inference/ | 2026-08-13 | Global | $/M tokens | Confirmed directly on NVIDIA's own site: "$0.123 per million tokens at 116 TPS/user interactivity using NVIDIA Dynamo and TensorRT-LLM," attributed to SemiAnalysis InferenceX benchmarks (April 2026). Applies specifically to the 72-GPU GB300 NVL72 rack at that interactivity setting — not to any workstation or desktop-class device. The earlier UNVERIFIABLE tag resulted from searching InferenceX's own dashboard directly rather than NVIDIA's page citing the headline figure; nearby InferenceX points independently range $0.065–$3.3/M tokens depending on interactivity setting, consistent with this confirmed figure. |
| "2.8M tok/s/MW" for GB300 NVL72 | UNVERIFIABLE | Benchmark/API Query | inferencex.semianalysis.com, compare-per-dollar page | 2026-08-12 | Global | tok/s per MW | Confirmed adjacent points: ~3.89M tok/s/MW (lowest latency) and ~1.67M tok/s/MW (117 tok/s/user); 2.8M is plausible as an interpolation but not confirmed as a published figure. |
| Vera Rubin NVL72 vs. GB200/GB300 performance claims ("10x tokens/MW," "one-tenth cost/token," etc.) | ATTRIBUTED STATEMENT (vendor) vs. independent benchmark (lower multiples) | Direct Fetch (Live), two sources | nvidia.com/en-us/data-center/vera-rubin-nvl72/ (vendor); newsletter.semianalysis.com (independent) | 2026-08-12 | Global | $/M tokens, tokens/MW | NVIDIA's multipliers are marketing claims; SemiAnalysis's own benchmark-derived multipliers are materially lower (peaking ~8x vs. 2025 GB200 baseline, ~1.5–5.4x vs. contemporaneous baselines) and workload-dependent. |
| DGX Spark specs (GB10 Superchip, 1 PFLOP FP4, 128GB unified memory, 240W PSU) | OBSERVED FACT | Direct Fetch (Live) | nvidia.com/en-us/products/workstations/dgx-spark/ | 2026-08-12 | Global (US MSRP market) | W, GB, PFLOPS | Product page has no visible price (routes to marketplace). |
| DGX Spark current price: $4,699 (Founders Edition, raised from $3,999 Feb 2026) | OBSERVED FACT | Direct Fetch (Live), official manufacturer forum notice | forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713 | 2026-08-12 | USA (direct MSRP) | USD | If the whitepaper cites $3,999 anywhere, that is now stale — current price is $4,699. Not verified for any EU/Finland reseller price (see Cluster-crossing note in localized workbook). |
| Community Qwen3.5-122B-A10B DGX Spark throughput (38.4 tok/s directly confirmed; "up to 51 tok/s" headline claim) | ATTRIBUTED STATEMENT | Community/Forum Attribution | forums.developer.nvidia.com, thread by user "Albond" | 2026-08-12 | Global (single-user benchmark, USA forum) | tokens/sec | 38.4 tok/s directly visible in fetched thread content; 51 tok/s is the same poster's own later claim, referenced in the thread's own summary line but not independently viewed in the underlying post. |
| InferenceMAX/InferenceX: what it is, who runs it, methodology | OBSERVED FACT | Direct Fetch (Live) | inferencex.semianalysis.com; newsletter.semianalysis.com | 2026-08-12 | Global (SemiAnalysis, US-based analyst firm) | n/a | Confirms benchmark provenance independent of whether the specific $/token and tok/s/MW figures could be pinned down. |

---

### Cluster B — Current frontier-model API pricing

**Scope:** Anthropic (Claude Fable 5 / Mythos 5 / Opus 5 / Sonnet 5 / Haiku 4.5), OpenAI (GPT-5.6 Sol/Terra/Luna), Google (Gemini 3.1 Pro) — naming, tiering, and per-million-token pricing.

**Methodology used:** Anthropic's pricing was verified by **Direct Fetch (Live)** against its own docs — highest confidence in this cluster. OpenAI's pricing/model pages could not be fetched raw (HTTP 403 on canonical URLs) and were instead accessed via **AI-Summarized Fetch**, cross-checked across two independent passes plus a Wikipedia summary — lower confidence, explicitly flagged. Google's pricing came via **AI-Summarized Fetch** of its own docs domain, cross-checked against a Wikipedia summary.

| Claim | Evidence Class | Method | Source | Retrieved | Geography | Currency/Units | Confidence Note |
|---|---|---|---|---|---|---|---|
| Anthropic current lineup/pricing: Fable 5 $10/$50, Mythos 5 $10/$50 (limited), Opus 5 $5/$25, Sonnet 5 $2/$10, Haiku 4.5 $1/$5 per MTok | OBSERVED FACT | Direct Fetch (Live) | platform.claude.com/docs/en/about-claude/pricing | 2026-08-12 | Global (Anthropic, USA) | USD per MTok | Anthropic's own live pricing docs, fetched directly; high confidence. |
| Sonnet 5's $2/$10 pricing is now the permanent standard price (the scheduled 2026-09-01 increase to $3/$15 has been cancelled) | OBSERVED FACT | Direct Fetch (Live) | platform.claude.com/docs/en/about-claude/pricing (footnote) | 2026-08-12 | Global | USD | Contradicts a stale cached pricing table elsewhere; this live page is authoritative as of the retrieval date. |
| OpenAI's flagship line is "GPT-5.6," in tiers Sol/Terra/Luna, previewed ~2026-06-26, wider release ~2026-07-09 | ATTRIBUTED STATEMENT (naming) | AI-Summarized Fetch (×2, cross-checked) + corroborating summary | developers.openai.com/api/docs/pricing and /models; en.wikipedia.org/wiki/GPT-5.6 | 2026-08-12 | Global (OpenAI, USA) | n/a | Canonical openai.com/api/pricing returned 403 to direct fetch; naming corroborated across three independent passes but none was a raw-text read. |
| GPT-5.6 standard pricing: Sol $5.00/$30.00, Terra $2.00/$12.00, Luna $0.20/$1.20 per MTok (cached rates ~10%); long-context ≈2x, exact threshold not found | ATTRIBUTED STATEMENT | AI-Summarized Fetch (two passes, inconsistent on long-context cache-write figures) | developers.openai.com/api/docs/pricing | 2026-08-12 | USA | USD per MTok | Two fetch passes disagreed on long-context cache-write numbers — treat as attributed-via-intermediary, not confirmed; a human should re-verify by opening the page directly in a browser. |
| GPT-5.6 tiers share ~1.05M-token context window, 128K max output, ~2026-02-16 knowledge cutoff | ATTRIBUTED STATEMENT | AI-Summarized Fetch (single pass) | developers.openai.com/api/docs/models | 2026-08-12 | USA | tokens | Single-source, not cross-checked against a second independent fetch. |
| Google's current top Pro model is "Gemini 3.1 Pro," status "Preview" (not GA); tiered pricing $2/$4 input, $12/$18 output per MTok at 200K threshold; no separate "Gemini 3 Pro" exists | OBSERVED FACT | AI-Summarized Fetch + corroborating summary | ai.google.dev/gemini-api/docs/pricing; en.wikipedia.org/wiki/Gemini_(language_model) | 2026-08-12 | Global (Google, USA) | USD per MTok | Read through AI-summarization rather than raw HTML, but figures and "Preview" status reported consistently and match expected Google page style. |
| Overall three-lab framing (naming/tiers) roughly holds but with two nuances (Anthropic has a 4th sibling model; Google's model is still Preview, not GA) | INTERPRETATION | — (synthesis, no independent citation) | Derived from the rows above | 2026-08-12 | Global | n/a | Editorial synthesis for the whitepaper author, not itself independently checkable. |

---

### Cluster C — NVIDIA/Wall Street $500B financing broadcast

**Scope:** The August 10, 2026 CNBC *Closing Bell Overtime* segment announcing Nvidia's six-firm financing platforms; surrounding independent corroboration; per-gigawatt cost claims; US power-demand context.

**Methodology used:** The core event was verified by **Transcript Check (Broadcast)** against CNBC's own published transcript — the authoritative primary record of what was said on air — plus **Search Corroboration (Fetched)** against Fortune's independent same-day article. Wider pickup (Reuters, Bloomberg, WSJ, Guardian, CNN, U.S. News) rests only on **Search Corroboration (Aggregated/Snippet)** since those articles were paywalled/blocked. Independent analyst per-GW estimates and US power-demand forecasts (BCG, S&P Global, IEA) are also **Search Corroboration (Aggregated/Snippet)** only — not individually re-fetched.

| Claim | Evidence Class | Method | Source | Retrieved | Geography | Currency/Units | Confidence Note |
|---|---|---|---|---|---|---|---|
| Aug 10, 2026: Nvidia + 6 firms (Apollo, Blackstone, BlackRock, Brookfield, Goldman Sachs, KKR) announce financing platforms to mobilize >$500B third-party capital | OBSERVED FACT | Transcript Check (Broadcast) + Search Corroboration (Fetched) | cnbc.com article (Hugh Son, Aug 10 2026); fortune.com (Aug 11 2026) | 2026-08-12 | USA (announced on US broadcast; global capital deployment) | USD billions | Wider pickup (Reuters/Bloomberg/WSJ/Guardian/CNN/US News) confirmed only via search-indexed headlines, not directly re-fetched. |
| Named panel participants: Huang, Solomon, Fink (remote), Gray, Szlezak, Zelter, Flatt | OBSERVED FACT | Transcript Check (Broadcast) | CNBC transcript page | 2026-08-12 | USA | n/a | Directly confirmed from Becky Quick's on-air introductions in the primary transcript. |
| Huang: "each gigawatt is something like $50, $60 billion" (energy, land, power/shell, compute) | ATTRIBUTED STATEMENT | Transcript Check (Broadcast) | CNBC transcript | 2026-08-12 | USA (stated on US broadcast; cost applies globally) | USD billions per GW | Independent analyst figures (Morgan Stanley ~$49B/GW, Foxconn ~$47B/GW, Bernstein ~$35B/GW, Epoch.ai ~$38B/GW) found only via Search Corroboration (Aggregated) — not individually re-verified in this pass; Huang's figure sits at the high end but not an outlier. |
| Fink: $50–60B/GW; >70GW new US power demand needed; "we're going to have to raise trillions of dollars over the coming years" | ATTRIBUTED STATEMENT | Transcript Check (Broadcast) | CNBC transcript | 2026-08-12 | USA | USD, GW | Statement's existence/wording confirmed against primary transcript; the underlying forecasts (future power need, future capital raised) remain unaudited projections. |
| Fink's >70GW figure is broadly consistent with independent US power-demand forecasts (BCG 50–80GW shortfall by 2030; S&P Global 64.4GW hyperscale draw in 2025; IEA ~130% rise by 2030) | INTERPRETATION | Search Corroboration (Aggregated/Snippet) | Aggregated search summary referencing BCG/S&P Global/IEA | 2026-08-12 | USA | GW | None of these reports individually fetched/verified in this session; different methodologies/timeframes/definitions, so directional support only. |
| Wide same-day pickup (Reuters, Bloomberg, WSJ, Guardian, CNN, U.S. News) citing an FT report | OBSERVED FACT (of pickup existing) | Search Corroboration (Aggregated/Snippet), one fetched (Fortune) | Search-indexed headlines; fortune.com directly fetched | 2026-08-12 | Global | n/a | Existence/headlines confirmed via indexing only for outlets beyond Fortune; treat as corroborating signal of pickup, not independently re-verified content. |

---

### Cluster D — Sam Altman, YC Startup School talk (July 26, 2026)

**Scope:** Four specific claims attributed to Altman's closing session at YC Startup School (Chase Center, San Francisco): the "three months in seventeen minutes" line; the dystopia framing; a "10x/year demand growth" claim; and a "100,000 tokens/month" historical anecdote.

**Methodology used:** No official recording/transcript of this specific talk was directly accessible. Verification rests entirely on **Transcript Check (Auto-caption/attendee-paraphrase)** — a CC-BY-licensed attendee-notes repository built from a machine transcript (Granola + Gemini re-transcription, per the repo's own README) — plus **Search Corroboration (Fetched)** of syndicated news coverage for one item. This is the lowest-confidence-by-method cluster in this register and is flagged as such throughout.

| Claim | Evidence Class | Method | Source | Retrieved | Geography | Currency/Units | Confidence Note |
|---|---|---|---|---|---|---|---|
| "Three months of work in seventeen minutes... so do three months of work," used against treating the present as "the end of history" | ATTRIBUTED STATEMENT | Transcript Check (Auto-caption/attendee-paraphrase) | github.com/Princeu3/yc-startup-school-2026-notes, sessions/09-sam-altman.md | 2026-08-12 | USA (San Francisco, Chase Center, 2026-07-26) | n/a | Explicitly labelled by its own author as paraphrase from a machine transcript, not verbatim — corroborates gist/placement only. |
| Dystopia framing: is it "abundance without freedom" OR "overreacting to AI safety"? | ATTRIBUTED STATEMENT | Search Corroboration (Fetched, syndicated) + Transcript Check (Auto-caption, corroborating) | news.com.au (syndicated via europesays.com); GitHub attendee notes | 2026-08-12 | USA/Australia (outlet) | n/a | The two framings are **not alternatives** — Altman's quote is causal: overreacting to AI safety → abundance-without-freedom "perfect surveillance state," which he frames as the outcome to avoid. news.com.au itself was blocked for direct fetch; reconstructed via syndicated copy. |
| Altman claimed AI/compute demand grows "10x per year" | ATTRIBUTED STATEMENT (different claim than framed) | Transcript Check (Auto-caption) + Direct Fetch (Live, blog) | blog.samaltman.com "Three Observations"; GitHub attendee notes; Forbes coverage | 2026-08-12 | USA | n/a | No primary source found for a direct "demand grows 10x/year" quote at this talk. The well-documented, heavily-cited Altman 10x figure is about **cost falling** ~10x/12 months (a different claim, from a different piece — his blog, not this talk), linked by him to higher usage via a Jevons-paradox argument. The talk itself, per attendee notes, used only unquantified, hedged "demand keeps growing for many years" language. |
| "100,000 tokens/month" historical anecdote (heaviest 2019 user vs. 2026 global per-capita average) | ATTRIBUTED STATEMENT | Search Corroboration (Fetched) | AOL/Yahoo-syndicated article reporting OpenAI's separate "Intelligence at Work" livestream, June 2, 2026 | 2026-08-12 | USA | tokens/month | Well corroborated in substance but traced most clearly to a **different event** (OpenAI's June 2, 2026 enterprise livestream), not confirmed as repeated verbatim at the Startup School talk; independent attendee notes for that session don't mention it. |
| Contextual OpenAI API pricing (independently checkable anchor, not part of the talk itself) | OBSERVED FACT | AI-Summarized Fetch | developers.openai.com/api/docs/pricing | 2026-08-12 | USA | USD per MTok | Included only as a sanity-check anchor for cost/demand claims; not itself Startup School content. |

---

### Cluster E — Mark Zuckerberg, "The Future Is for Everyone" (Meta, Aug 10, 2026)

**Scope:** Publish date; three-principles framing; personal-agent "private mode" claim; superintelligent-lawyer analogy; alignment-to-the-individual argument; open-source-as-safety framing; third-party reception.

**Methodology used:** The essay itself was verified by **Direct Fetch (Live)**, including reading embedded JSON-LD structured metadata for the exact publish timestamp — the highest-confidence method used anywhere in this register, since the full raw HTML was parsed directly (not summarized). Third-party reception was verified by **AI-Summarized Fetch** of a TechCrunch response; one further TechCrunch piece was only seen via **Search Corroboration (Aggregated/Snippet)** and is explicitly not used as a source of claims.

| Claim | Evidence Class | Method | Source | Retrieved | Geography | Currency/Units | Confidence Note |
|---|---|---|---|---|---|---|---|
| Publish date 2026-08-10T10:01:23+00:00 (JSON-LD), byline Mark Zuckerberg | OBSERVED FACT | Direct Fetch (Live), raw HTML + JSON-LD | about.fb.com/news/2026/08/the-future-is-for-everyone/ | 2026-08-12 | USA (Meta, Menlo Park) | UTC timestamp | Full HTML and structured metadata parsed directly. |
| "Three principles" framing (individual empowerment / invention / balance of power), stated verbatim twice | OBSERVED FACT | Direct Fetch (Live) | Same URL | 2026-08-12 | Global (Meta essay) | n/a | Essay doesn't use the literal label "three principles" but enumerates exactly three, twice, in parallel structure. |
| Personal-agent "fully private mode" (even Meta cannot see/access), likened to WhatsApp E2E encryption | OBSERVED FACT | Direct Fetch (Live) | Same URL | 2026-08-12 | Global | n/a | Verbatim, stated twice. |
| Superintelligent-lawyer analogy, extended to cybersecurity/business | OBSERVED FACT | Direct Fetch (Live) | Same URL | 2026-08-12 | Global | n/a | Verbatim thought experiment. |
| Alignment-to-the-individual argument ("share a person's goals and values, not our company's") | OBSERVED FACT (that the language appears) | Direct Fetch (Live) | Same URL | 2026-08-12 | Global | n/a | Verbatim; the essay's own embedded example (an unnamed model refusing a letter over standardized-testing ethics) is a separate, unattributed, unconfirmed anecdote — see next row. |
| Unnamed "one leading model refused..." anecdote | ATTRIBUTED STATEMENT | Direct Fetch (Live), no corroboration found | Same URL | 2026-08-12 | Global | n/a | No model, company, date, or independent report identified; Zuckerberg's own unverified claim. |
| Open source framed as anti-centralization/pro-security; Meta "will resume releasing some open source models soon" | OBSERVED FACT (existence of statement) / ATTRIBUTED STATEMENT (implied prior pause) | Direct Fetch (Live) | Same URL | 2026-08-12 | Global | n/a | The implied prior release pause is Zuckerberg's own framing, not independently corroborated against a separate dated announcement. |
| Third-party critical reception exists and engages with the same content | ATTRIBUTED STATEMENT | AI-Summarized Fetch | TechCrunch, Russell Brandom, ~2026-08-10 | 2026-08-12 | USA | n/a | Content approximated via automated summarization, not verbatim; it's an opinion piece, not proof of Zuckerberg's substantive claims. |
| A second TechCrunch piece on a "Glimmer" model ties into the same vision | UNVERIFIABLE (not independently confirmed) | Search Corroboration (Aggregated/Snippet) | TechCrunch site search result | 2026-08-12 | USA | n/a | Only a search snippet was seen; not fetched or read — do not cite specific claims from it. |
| Related Meta Newsroom items show this essay follows a July 30, 2025 predecessor post | OBSERVED FACT | Direct Fetch (Live) | Same URL, "Related News" footer module | 2026-08-12 | USA | n/a | Confirms the Aug 2026 essay expands on a named earlier post rather than standing alone. |

---

### Cluster F — Bitcoin hashprice, OpenRouter, and inference-market infrastructure

**Scope:** Luxor/Hashrate Index Bitcoin hashprice (~Aug 10, 2026); OpenRouter's scale claims and ranking methodology; IBM + Together AI's $240M NVIDIA HGX B300 inference-cluster deal.

**Methodology used:** **Direct Fetch (Live)** for Luxor's own roundup and live ticker, OpenRouter's own homepage/rankings/docs pages, and IBM's own newsroom press release — all primary-source, high-confidence retrieval. A Series B funding claim and an NVIDIA "30x output" marketing claim rest on **Search Corroboration (Fetched/Aggregated)** respectively.

| Claim | Evidence Class | Method | Source | Retrieved | Geography | Currency/Units | Confidence Note |
|---|---|---|---|---|---|---|---|
| Bitcoin spot hashprice ~$31.73–32.05/PH/s/Day around Aug 10–12, 2026 | OBSERVED FACT | Direct Fetch (Live) | hashrateindex.com/blog roundup (Aug 10, 2026) + live homepage ticker | 2026-08-12 | Global (Bitcoin network; Luxor, USA-based analytics firm) | USD per PH/s/Day | Figures extracted via automated tool rather than manual reading; day-to-day variance ($31.73 → $32.05) is normal fluctuation, not discrepancy. |
| OpenRouter self-reported scale: "200T+ Monthly Tokens," "10M+ Global Users," "70+ Providers," "400+ Models" | OBSERVED FACT (self-reported) | Direct Fetch (Live) | openrouter.ai; openrouter.ai/rankings | 2026-08-12 | Global | tokens/month | Company-disclosed, not independently audited; consistent with continued growth from a May 2026 disclosure of 25T tokens/week. |
| OpenRouter has been called "largest" LLM aggregation platform | ATTRIBUTED STATEMENT (third-party, not self-描述) | Direct Fetch (Live, no match found) + Search Corroboration (Aggregated/Snippet) | openrouter.ai (checked directly, no superlative found); Dataconomy Feb 2026 (snippet only) | 2026-08-12 | Global | n/a | OpenRouter's own site makes no such claim; "largest" language comes only from third-party press coverage — must not be attributed to OpenRouter itself. |
| OpenRouter raised $113M Series B (May 26, 2026), led by CapitalG, ~$1.3B valuation | OBSERVED FACT | Search Corroboration (Fetched) | Tech Times, May 29, 2026 | 2026-08-12 | USA | USD millions | Secondary news article; primary press release (BusinessWire) could not be fetched (blocked/timeout). |
| IBM + Together AI sign $240M multi-year deal for NVIDIA HGX B300 inference cluster on IBM Cloud, Q1 2027 availability | OBSERVED FACT | Direct Fetch (Live) + Search Corroboration (Fetched) | newsroom.ibm.com (Aug 11, 2026); Reuters coverage confirmed via search snippet | 2026-08-12 | USA | USD millions | IBM's own press release is the primary source; Reuters article itself blocked from direct fetch but confirmed via snippet + secondary wire pickups. |
| NVIDIA claims the cluster delivers "30x more AI factory output" | ATTRIBUTED STATEMENT | Search Corroboration (Aggregated/Snippet) | Press coverage snippet | 2026-08-12 | Global | n/a | No baseline, methodology, or primary NVIDIA document found; must be labeled as an NVIDIA-attributed marketing claim if used at all. |
| HGX B300 is a Blackwell Ultra-generation, 8-GPU system (144/108 PFLOPS sparse/dense NVFP4, 2.1TB memory) | OBSERVED FACT | Direct Fetch (Live) | nvidia.com/en-us/data-center/hgx/ | 2026-08-12 | Global | PFLOPS, TB | Refines generic press "Blackwell processors" framing to the more precise "Ultra" generation. |

---

### Cluster G — Humanoid robot market pricing

**Scope:** Real-world pricing/specs for Unitree G1, 1X NEO, Tesla Optimus, Agility Digit, and Figure AI's Figure 03, to bound the whitepaper's illustrative €25,000 example against actual market prices.

**Methodology used:** Manufacturer **Direct Fetch (Live)** for Unitree and 1X (highest confidence in this cluster). Tesla's own AI/Optimus page returned HTTP 403 and Figure AI's official pages returned 404 for pricing — both fall back to **Search Corroboration (Aggregated/Snippet)** across multiple independent secondary aggregator sites, which is the weakest method used in this cluster and is flagged accordingly.

| Claim | Evidence Class | Method | Source | Retrieved | Geography | Currency/Units | Confidence Note |
|---|---|---|---|---|---|---|---|
| Unitree G1: from $13,500 (tax/shipping excluded); 1320mm; ~35kg; 23–43 DOF | OBSERVED FACT | Direct Fetch (Live) | unitree.com/g1 | 2026-08-12 | China (manufacturer); price as listed for direct/global sale | USD | Manufacturer's own current page; high confidence. |
| 1X NEO: $20,000 early-access purchase or $499/month subscription, $200 refundable deposit | ATTRIBUTED STATEMENT | Search Corroboration (Fetched) + Direct Fetch (Live, partial) | Engadget, Oct 29, 2025; 1x.tech/neo (deposit only, checked directly) | 2026-08-12 | Norway/USA (1X Technologies) | USD | Purchase/subscription price corroborated across multiple outlets but not confirmed on 1X's own page in the content actually retrieved — only the $200 deposit was visible there. |
| 1X NEO specs: 168cm/66lbs, 154lb lift, 55lb carry, 4hr/842Wh battery, 1.4–6.2 m/s speed, Jetson Thor chipset | OBSERVED FACT | Direct Fetch (Live) | 1x.tech/neo | 2026-08-12 | Norway/USA | metric/imperial mixed as published | Manufacturer's own spec page; high confidence for physical specs specifically (separate from pricing above). |
| Tesla Optimus long-term target $20,000–$30,000; no commercial orders/confirmed retail price as of 2026-08-12 | ATTRIBUTED STATEMENT | Search Corroboration (Aggregated/Snippet); direct fetch of tesla.com/AI blocked (403) | Aggregated secondary reporting | 2026-08-12 | USA (Tesla) | USD | Musk's repeated target, not a list price; primary transcript of the remarks not independently re-verified in this session. |
| Tesla Optimus specs (~173cm, ~57kg, 65 DOF, ~8km/h, ~20kg payload, 8hr target battery) | ATTRIBUTED STATEMENT | Search Corroboration (Aggregated/Snippet) | Multiple aggregator sites (optimusk.blog, robottoday.com, etc.) | 2026-08-12 | USA | metric | No primary Tesla source accessible; low-to-moderate confidence. |
| Agility Digit: ~$250,000 outright purchase, or ~$8,500/month (~$30/hr) RaaS alternative | ATTRIBUTED STATEMENT | Search Corroboration (Aggregated/Snippet) | Multiple independent aggregator sites (GrabARobot, RoboSelect360, Humanoza, et al.) | 2026-08-12 | USA (Agility Robotics) | USD | Official Agility pricing page returned 404; moderate confidence from convergence across many independent secondary sources, but no primary confirmation. |
| Figure 03: no official pricing published; third-party specs (~168cm, ~60kg, 40–44 DOF, ~20kg payload, 5hr battery) and ~$20,000 rumored target | ATTRIBUTED STATEMENT | Search Corroboration (Aggregated/Snippet); Direct Fetch (Live, 404 on pricing/specs pages) | figure.ai (checked, no data); livium.com, aparobot.com, et al. (aggregators) | 2026-08-12 | USA (Figure AI) | USD | Figure AI explicitly discloses no pricing; low confidence on all numeric figures. |
| Real observed/targeted market spans ~$13,500–$250,000+; whitepaper's illustrative €25,000 sits in the lower-middle of this range | DERIVED CALCULATION | — (comparative synthesis of rows above) | See individual rows | 2026-08-12 | Global | USD/EUR (FX-comparative) | Several inputs (Optimus, Digit, Figure 03) rest only on secondary-source corroboration; treat the overall range as directionally reliable, not precisely audited at the high end. |

---

### Cluster H — Author's own published articles (accurate-representation and date check)

**Scope:** Three of Valto Loikkanen's own published pieces, checked for exact publish date and accurate content representation, plus corroboration of the industry framings ("services as software," "AI-native services") they reference.

**Methodology used:** **Direct Fetch (Live)** for all three of the author's own articles and for the Sequoia article that anchors the "services as software" thesis — self-citation was independently re-verified, not assumed. The Y Combinator "AI-native services" comparison could not be corroborated by any method available and is marked **UNVERIFIABLE**.

| Claim | Evidence Class | Method | Source | Retrieved | Geography | Currency/Units | Confidence Note |
|---|---|---|---|---|---|---|---|
| LinkedIn article "Who Owns Your AI" — publish date and content summary | OBSERVED FACT | Direct Fetch (Live) | linkedin.com/pulse/who-owns-your-ai-valto-loikkanen-nq4lc/ | 2026-08-12 | Finland (author) / Global (platform) | n/a | Tool-reported publish date Aug 11, 2026; content summary consistent with the article's stated argument. LinkedIn dates via automated extraction can occasionally be off by a day (timezone); author should confirm against own dashboard. |
| LinkedIn article "So the majority agrees... digital sovereignty" — Aug 5, 2026; contains ~€42/member/month figure | OBSERVED FACT | Direct Fetch (Live) | linkedin.com/pulse/so-majority-agrees-time-digital-sovereignty-has-come-now-loikkanen-vfgbf/ | 2026-08-12 | Finland (author) | EUR per member/month | Both the date and the exact figure ("50 members: approximately €42 per member/month") confirmed verbatim — no correction needed. |
| Substack article "The overlooked AI scale-up layer" — May 22, 2026; delivery-innovation/"globally local" thesis | OBSERVED FACT | Direct Fetch (Live) | startupcommons.substack.com/p/the-overlooked-ai-scale-up-layer-846 | 2026-08-12 | Finland (author) / Global (platform) | n/a | Date and thesis both independently confirmed via direct fetch. |
| Sequoia Capital has published a "services as software" thesis | OBSERVED FACT (thesis exists, embedded, not a standalone title) | Direct Fetch (Live) + Search Corroboration (Fetched) | sequoiacap.com/article/generative-ais-act-o1/ (Huang, Grady, "o1," Oct 9 2024); Substack secondary analysis | 2026-08-12 | USA (Sequoia Capital) | n/a | Concept lives inside "Generative AI's Act o1" (spelled "service-as-a-software" there), not as a separately-titled "Services as Software" piece — citation should point to this article, not an assumed distinct URL. |
| Y Combinator has published a comparable "AI-native services" framing | UNVERIFIABLE | Direct Fetch (Live, no match) + limited search (most engines blocked) | ycombinator.com/blog; ycombinator.com/rfs | 2026-08-12 | USA (Y Combinator) | n/a | No specific essay/framework titled or framed as "AI-native services" located, despite direct fetches of YC's own blog/RFS pages; YC's Fall 2026 RFS does include adjacent categories (e.g., "AI-Native Compliance Infrastructure"). Search tooling in this session was limited — absence is not proof of non-existence. Recommend softening or dropping this comparison unless the author supplies the specific source in mind. |

---

### Cluster I — AI Maturity Framework public findability

**Scope:** Whether a public "AI Maturity Framework" by Valto Loikkanen is independently findable, in the form (three-stage × three-dimension, CC BY 4.0) anticipated.

**Methodology used:** **Direct Fetch (Live)** of two LinkedIn video posts, reading each page's schema.org JSON-LD auto-caption **transcript** field (not the video itself — the visual diagram could not be inspected by any tool available). Licensing was checked by direct text search of the raw page source for license terms.

| Claim | Evidence Class | Method | Source | Retrieved | Geography | Currency/Units | Confidence Note |
|---|---|---|---|---|---|---|---|
| A public AI Maturity Framework by Valto Loikkanen exists, findable via two LinkedIn video posts dated 2026-06-20 | OBSERVED FACT | Direct Fetch (Live), JSON-LD auto-caption transcript | linkedin.com/posts/valto_activity-7474204985564598272-7RyS; linkedin.com/posts/valto_where-are-you-in-the-ai-maturity-map-activity-7474223638184058882-MbqI | 2026-08-12 | Finland (author) / Global (platform) | n/a | Structure found (4-layer ecosystem, 5 numbered stages) does not exactly match the brief's anticipated 3-stage × 3-dimension grid. |
| "Learning → Internalizing → AI Native" progression used, in that order | ATTRIBUTED STATEMENT | Transcript Check (Auto-caption) | Same first URL | 2026-08-12 | Finland/Global | n/a | Confirmed as spoken words in the transcript; whether these are the literal on-screen diagram labels (vs. narrative description) could not be confirmed — visual diagram not inspectable. |
| Dimension names "Working," "Role of AI," "Information" used as row labels | ATTRIBUTED STATEMENT (partial) | Transcript Check (Auto-caption) | Both URLs | 2026-08-12 | Finland/Global | n/a | "Role of AI" and "Information" clearly present in substance; literal word "Working" as a named dimension was NOT found in either transcript. |
| Framework is licensed CC BY 4.0 | UNVERIFIABLE | Direct Fetch (Live), text search of raw page source | Both URLs; supplementary web searches | 2026-08-12 | Finland/Global | n/a | No "CC BY," "Creative Commons," or "license" string found in either page's source; reported plainly as not found rather than assumed. |
| Overall assessment of findability and phase-naming | INTERPRETATION | — (synthesis) | Both URLs | 2026-08-12 | Finland/Global | n/a | A version of the framework is publicly findable but not in the exact static/licensed form anticipated; whitepaper should describe what was actually found, not assert an unconfirmed CC BY 4.0 static artifact. |

---

### Cluster J — OpenAI Codex usage statistics

**Scope:** OpenAI's self-reported internal Codex telemetry (99.8% of weekly internal output tokens; 70.2%/25.6% of users exceeding 1hr/8hr-equivalent requests; 99th-percentile users >60 agent-hours/day); and a claimed NVIDIA "32K/8K reference agentic workload" figure.

**Methodology used:** **Direct Fetch (Archived)** — the live OpenAI blog post returned a Cloudflare bot-challenge (403), so the primary text was retrieved via a Wayback Machine snapshot, which is treated as equivalent in text-fidelity to a live fetch since it is the same primary document. Independent press coverage was checked by **Search Corroboration (Fetched)** specifically to confirm that the underlying figures are OpenAI's own unaudited self-report. The NVIDIA reference-workload figure was searched for exhaustively and could not be found by any method — marked **UNVERIFIABLE**.

| Claim | Evidence Class | Method | Source | Retrieved | Geography | Currency/Units | Confidence Note |
|---|---|---|---|---|---|---|---|
| Codex = 99.8% of weekly output tokens generated internally at OpenAI | ATTRIBUTED STATEMENT (self-reported by OpenAI) | Direct Fetch (Archived) | openai.com/index/how-agents-are-transforming-work/ (June 25, 2026), via web.archive.org | 2026-08-12 | USA (OpenAI) | % of tokens | Verbatim confirmed. Independent press (The Next Web) explicitly notes "every number comes from OpenAI itself," no third-party audit exists. |
| By May 2026: 70.2% of sampled users exceeded a 1-human-hour-estimated request; 25.6% exceeded 8 hours | ATTRIBUTED STATEMENT | Direct Fetch (Archived) | Same source | 2026-08-12 | USA | % of users, hours | Verbatim confirmed, including growth-rate annotations (+98%, +1131% vs. Dec 2025 baseline). "Estimated human-hours" is OpenAI's own internal, undisclosed methodology. |
| By June 2026: 99th-percentile users regularly generated >60 hours of Codex agent turns per day, across parallel agents | ATTRIBUTED STATEMENT | Direct Fetch (Archived) | Same source | 2026-08-12 | USA | agent-hours/day | Verbatim confirmed; explicitly parallel/aggregate agent-time, not one person single-threading for 60 hours. |
| NVIDIA reference agentic workload of 32K input + 8K output tokens per turn | UNVERIFIABLE | Exhaustive search across multiple engines + Direct Fetch of NVIDIA developer blog + Benchmark/API Query of InferenceMAX | Multiple search engines; developer.nvidia.com/blog; inferencex.semianalysis.com | 2026-08-12 | Global | tokens | Not found anywhere despite extensive searching; SemiAnalysis's InferenceMAX uses different token-scenario labels (e.g., "8k/1k" for DeepSeek R1). Should be sourced properly or removed from the whitepaper, not presented as an NVIDIA figure. |
| Supporting context: ~98% internal Codex adoption (up from ~40% Aug 2025); non-developer usage grew 137x/189x; Legal/Finance/Recruiting token shares 88–91% | ATTRIBUTED STATEMENT | Search Corroboration (Fetched) | The Next Web, June 25 2026; Crypto Briefing | 2026-08-12 | USA | % | Secondary summaries of the same OpenAI report, not independently re-confirmed against the primary archived text in this pass — recommend re-confirming against primary text before use. |

---

## F. Cross-cluster methodology reliability summary

| Cluster | Dominant method(s) | Highest-confidence element | Lowest-confidence element |
|---|---|---|---|
| A — NVIDIA hardware/TCO | Direct Fetch (Live); Benchmark/API Query | GB300 core specs (NVIDIA's own page); "$0.123/M tokens" now CONFIRMED (2026-08-13, corrected scope: 72-GPU rack tier only) | "2.8M tok/s/MW" remains UNVERIFIABLE |
| B — Frontier-model pricing | Direct Fetch (Live) for Anthropic; AI-Summarized Fetch for OpenAI/Google | Anthropic pricing (own live docs) | OpenAI long-context pricing (two inconsistent AI-summarized passes) |
| C — Nvidia/Wall St. financing broadcast | Transcript Check (Broadcast); Search Corroboration | Existence/wording of on-air statements | "Trillions" total and >70GW figure (forward-looking, unaudited) |
| D — Altman YC talk | Transcript Check (Auto-caption/paraphrase); Search Corroboration | "100,000 tokens/month" historical comparison (from a different, better-documented event) | "10x/year demand" claim — not corroborated as stated for this talk |
| E — Zuckerberg Meta essay | Direct Fetch (Live), raw HTML/JSON-LD | Publish date and all six core verbatim claims | Third-party "Glimmer" TechCrunch piece (UNVERIFIABLE, snippet only) |
| F — Hashprice/OpenRouter/IBM | Direct Fetch (Live) | Luxor hashprice; IBM press release | NVIDIA "30x output" claim (Search Corroboration, Aggregated only) |
| G — Humanoid robot pricing | Direct Fetch (Live) for 2 of 5 platforms; Search Corroboration for 3 | Unitree G1, 1X NEO specs (manufacturer pages) | Tesla Optimus, Figure 03 pricing (no primary source accessible at all) |
| H — Author's own articles | Direct Fetch (Live) | All three date/content checks | YC "AI-native services" framing (UNVERIFIABLE) |
| I — AI Maturity Framework | Direct Fetch (Live), auto-caption transcript only | Existence of the framework, in some form | CC BY 4.0 licensing claim (UNVERIFIABLE) |
| J — OpenAI Codex telemetry | Direct Fetch (Archived) | The three core Codex percentage/hour figures (verbatim, but self-reported and unaudited) | "32K/8K" NVIDIA reference workload (UNVERIFIABLE) |

---

## G. Known limitations of this register

1. **Self-reported figures are not audited figures.** OpenAI's Codex telemetry (Cluster J), OpenRouter's scale claims (Cluster F), and NVIDIA's own marketing multipliers (Clusters A, F) are the originating party's own disclosures. This register verifies that they said it, not that it is true.
2. **AI-summarized fetches carry transcription risk.** Wherever a claim's Method column reads "AI-Summarized Fetch" (chiefly Cluster B, OpenAI/Google pricing; Cluster E, TechCrunch reception), the underlying figure was never read as raw text by a human or by direct parsing — only as a tool-generated summary. These entries should be re-verified directly before any high-stakes reuse.
3. **Search-only corroboration is directional, not confirmatory.** Rows using "Search Corroboration (Aggregated/Snippet)" (several in Clusters C, F, G, H) mean the underlying article was never independently opened and read — only its headline/snippet was seen. Treat these as "this appears to be widely reported," not as independently re-verified content.
4. **Bot-blocking shaped what could be checked live vs. archived.** Two primary sources in this project (OpenAI's blog, Cluster J; implicitly others) required a Wayback Machine detour due to Cloudflare challenges on direct fetch. This is treated as equivalent to a live fetch in text fidelity but is noted per-entry for transparency.
5. **Geography and currency are stated per-source, not normalized.** This appendix deliberately does not convert all figures to one currency or one jurisdiction — see the companion Localized Scenario Workbook (EUR/Finland) for one worked currency-conversion exercise, itself built on SCENARIO ASSUMPTIONS for any figure (FX rate, local electricity price, local financing rate) not present in this register.
6. **Retrieval dates cluster tightly around 2026-08-12** because this register was built as a single verification pass against the whitepaper's stated factual cut-off. Any reader relying on this appendix after that date should treat time-sensitive figures — API pricing, hashprice, benchmark-dashboard TCO figures, and hardware MSRPs in particular — as likely stale and should re-check them against the live primary sources listed.

---

*This appendix is released under the same licence as the parent whitepaper: CC BY 4.0 — Attribution 4.0 International. Suggested attribution: "Research synthesis and modelling by Valto Loikkanen, assisted by AI."*

---

**File/path note:** No file path was specified for this deliverable in the task; the appendix content above is the release asset itself, returned as markdown text. If a physical file location is needed (e.g., under `Storage-wiki/Storage/Other/why-trillions-ai-whitepaper/`, alongside Release Assets #7–#12), that path should be supplied so this can be written there as a standalone file.