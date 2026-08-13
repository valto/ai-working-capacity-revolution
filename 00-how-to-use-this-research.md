# How to Use This Research

*A one-page orientation note. Read this before anything else in the package.*

---

## What this is

A neutral-observer research synthesis reverse-engineering the economics of AI compute — energy, hardware, tokens, working capacity, ownership — from public statements by named executives, independently checked hardware specs and pricing, and the author's own prior published work. Every substantive claim is tagged with one of five evidence classes (Observed Fact, Attributed Statement, Derived Calculation, Scenario Assumption, Interpretation) so a reader can tell, at a glance, what is independently verified, what is someone's on-record claim, what is arithmetic, and what is an editable illustration.

## What this is not

- **Not investment, legal, tax, procurement, or policy advice.** Every scenario model here is an editable illustration built on stated, visible assumptions — not a forecast or recommendation. This boundary is restated in every scale/investment-bearing section of the whitepaper, not only here.
- **Not a verdict on "bubble or not."** The paper does not assert that current AI infrastructure spending is either obviously justified or obviously a bubble. It lays out what would need to be true for the spending to make economic sense, and separates the facts that are independently checkable from the claims that are not — then leaves the reader to weigh them.
- **Not a single-author opinion piece dressed as neutral research.** The author has disclosed commercial and advocacy interests in cooperative/ownership-based AI infrastructure (Method §3.4). Sections touching that model are flagged at the point of use, not just in a front-matter disclaimer.
- **Not a finished, unchallengeable model.** It is a starting point built to be forked, re-run with your own numbers, and argued with.

## What this research can establish

- What was actually said, by whom, on what date, and whether that statement is independently corroborated (the Observed Fact / Attributed Statement split).
- What a given cost or capacity figure *mechanically follows from*, given stated assumptions — every Derived Calculation in this package shows its formula, not just its result.
- Where the evidence is thin, contested, or genuinely unverifiable, named explicitly rather than smoothed over (see `20-appendix-known-limitations.md` for a consolidated list).

## What this research cannot establish

- Whether current AI infrastructure investment will prove justified by future demand or revenue. That depends on adoption, competition, regulation, and technology curves that have not happened yet.
- Whether any named executive's forward-looking claim (per-gigawatt cost, demand growth rate, future capital need) is *true* — only whether it was actually said, and how it compares with independent estimates where those exist.
- A single "right" cost figure for owning AI compute at any tier. Every dollar figure in this package is a scenario built on stated inputs (utilization, financing terms, electricity price) — change the inputs and the output changes. That is by design, not a weakness to be resolved into one number.
- Whether cheap AI working capacity translates into positive value for any specific reader. Working capacity and value are kept structurally separate throughout (Part IV) — cost tables never imply an outcome.

## How to challenge or extend this research

1. **Check the source register** (`02-source-register.md`, `10-appendix-source-register-formatted.md`) — every Observed Fact and Attributed Statement traces to a dated primary or secondary source. If a source has moved, been updated, or was misread, that is a legitimate finding — file it as such.
2. **Re-run the workbooks with your own numbers.** The companion workbooks (`03`–`08`) and the live-formula Excel model (`18-companion-data-model.xlsx`) expose every Scenario Assumption as an editable cell. A different electricity price, financing rate, or utilization assumption is not a rebuttal of the model — it is the model working as intended.
3. **Distinguish disagreement with an assumption from a factual correction.** "I think 60% utilization is unrealistic for my context" is a scenario disagreement (change the cell). "This benchmark figure is a 4-rack aggregate, not a single-rack figure" is a factual correction (file it against the source register). This package treats the two differently, and so should any critique of it.
4. **Watch for scope creep across production tiers.** A cost-per-token figure for one hardware tier (e.g., a hyperscale rack) must never be applied to a different tier (e.g., a desktop device) — the paper flags this explicitly wherever it is a live risk (Part II, Part VI). Any extension of this work should preserve that discipline.
5. **Report drift, not just disagreement.** If you find a number in one asset (whitepaper, deck, workbook, diagram) that contradicts the canonical figure in another, that is a defect in this package's own internal consistency, not a modeling choice — see `data/canonical-cost-model.csv` for the single source of truth these figures should trace to, `tools/check-canonical-consistency.py` for the automated check that enforces it, and `README.md`'s known-issues log for how such findings have been handled in past revisions.

## Where to start, depending on what you want

See "Reading paths" in `README.md` for lens-specific and depth-specific entry points — the whitepaper, executive brief, workbooks, and slide deck are built to serve different audiences at different depths from one shared factual base, not to be read end-to-end by everyone.

---

*Licensed under CC BY 4.0 for original prose and structure. Research synthesis and modelling by Valto Loikkanen, assisted by AI. Factual source cut-off: 2026-08-13.*
