# Changelog

All notable changes to this research package are documented here. Versioning follows [Semantic Versioning](https://semver.org/) in spirit — a major version bump indicates a change to canonical figures or conclusions, not just prose.

## [Unreleased] — targeted as v1.0.1

Content and release-mechanics work on `main` since the v1.0.0 GitHub release/Zenodo archive. Not yet cut as a new tagged release — pending author sign-off. See `README.md`'s Status line for the current relationship between `main` and the last tagged release.

### Added — content
- Replaced the front-matter "About the author and method" section with an expanded "About the author, perspective and method" — covers the author's broader entrepreneurship/innovation-ecosystem and advisory background (30+ ecosystems, government/EU/university advisory work) alongside the AI-infrastructure-specific disclosure, and names ValtoAI and the EIOS reference framework (organizations/governed information/agent-ready context) alongside the previously-named Prifina, Digiole, and PIOS. Propagated the same venture list to Method §3.4's disclosure, `12-executive-brief.md`, `15-shortform-ownership.md`, `13-slide-deck-outline.md`/`19-slide-deck.pptx` (slide 15), and `README.md`, replacing all remaining "peecos/PIOS" references.
- Added a new conceptual-bridge section, "From AI working capacity to new value," between Part IV (§25) and Part V of the whitepaper — explicitly tagged INTERPRETATION throughout, introduces no new cost figures. Distinguishes "can the capacity be created" (this paper's cost/capacity model, Parts I–IV) from "can that capacity create and capture new value" (invention, innovation, adoption, and revenue-model questions this paper's cost tables cannot answer), and notes the same boundary applies to any future Scenario Explorer built on this paper's workbooks. Added a corresponding paragraph to `12-executive-brief.md` and a new slide 18 to `13-slide-deck-outline.md`/`19-slide-deck.pptx` (deck is now 26 slides, up from 25; slides 18–25 renumbered to 19–26).
- Added Diagram 11 ("Creating Growth Based on New Value") — the author's own pre-existing framework diagram, supplied directly and used as-is at `assets/diagrams/diagram-11-creating-growth-from-new-value.jpg`. Unlike Diagrams 1–10, this was not built from a from-scratch designer brief; `17-visual-asset-briefs.md`'s Diagram 11 entry instead documents the actual image's structure (two columns converging on a shared "New Value" band) for editors and consistency checking. A provenance-framed PNG derivative (`diagram-11-creating-growth-from-new-value.png`, evidence-class tag, attribution, source note, standard footer) was added for use in the PDF, deck, and Pages site; the original JPG is kept as the raw source.
- Fixed a stale cross-reference in `README.md`'s disclosure line (pointed to whitepaper "§4," which no longer exists as a numbered section; corrected to "Method §3.4").

### Added — release mechanics (in response to external audit)
- `tools/requirements.txt` — pinned dependency versions (openpyxl, python-pptx, pypdf) for a reproducible consistency-check environment.
- Rewrote `tools/check-canonical-consistency.py`: required figures are now derived at runtime from `data/canonical-cost-model.csv` rather than hard-coded; added a PDF-text check (previously only markdown/xlsx/pptx were checked, so a stale PDF that wasn't regenerated after a markdown fix could pass silently); every check now fails closed — a missing dependency or a broken Python environment (e.g. a `pyexpat` symbol mismatch) is reported as a failure, never silently skipped, and an unexpected exception inside any check is caught and reported rather than crashing the script.
- `index.html` + `.nojekyll` — a GitHub Pages landing page: reading paths, full package-contents tables, version/citation/licence links, and setup instructions for the consistency checker. Markdown documents link to their GitHub-rendered view; binaries (PDF/xlsx/pptx/checksums/diagrams) are served directly from the Pages site.
- `01-whitepaper.pdf` now embeds its four most load-bearing diagrams (end-to-end chain, ownership stack, scale spectrum, new-value bridge) directly at their point of use in the text, so a reader holding only the PDF sees them without the repository; fixed a `pdf-style.css` gap (no `img` sizing rule existed) that was causing embedded images to overflow the page width before this was caught and corrected.
- `CHECKSUMS.sha256` no longer contains comment/header lines, so it validates without warnings under both macOS `shasum -a 256 -c` and GNU `sha256sum -c`; the explanatory header moved to `README.md`.

### Fixed
- `main` had drifted from `CITATION.cff`/`CHECKSUMS.sha256`/`README.md`'s v1.0.0 version claims after the content additions above — this is the discrepancy this v1.0.1 entry and cut resolves; see `README.md`'s Status line for how `main` related to the tagged release at any given point.

## [1.0.0] — 2026-08-13

Initial public release.

### Package
- Full whitepaper (`01-whitepaper.md` / `.pdf`, 45 sections, 82 pages) tracing energy → hardware → compute → tokens → AI working capacity → work → outcomes → value → agency, from public statements by Jensen Huang, Sam Altman, and Mark Zuckerberg plus independently verified hardware specs and pricing.
- Six companion workbooks with fully shown formulas (Global Baseline, AI Working-Capacity Conversion, Token-Factory Scenarios, Investment-Thesis Notes, Humanoid Working-Capacity, Localized EUR-Finland template).
- A live-formula Excel workbook (`18-companion-data-model.xlsx`, 10 sheets), a 25-slide deck (`19-slide-deck.pptx`), and 10 diagrams (`assets/diagrams/`).
- A full source register (67 checks across 10 research clusters) and a consolidated assumption register.
- Five evidence classes (Observed Fact, Attributed Statement, Derived Calculation, Scenario Assumption, Interpretation) applied consistently across every asset.

### Fixed during pre-release verification (three external review rounds)
- Corrected a Hyperscale-tier cost/scope error: the paper's canonical full-layer figure ($0.091–$0.312/M tokens, mid $0.133/M) was, in earlier drafts, inconsistently compared against a partial-layer figure that excludes opex — now clearly separated everywhere with explicit scope labels.
- Corrected an invalid extrapolation from OpenAI's own self-reported "60+ agent-hours/day" telemetry that had been used to imply a general-population usage statistic.
- Resolved an apparent ~2x discrepancy between two previously published cooperative-cost figures (€42 vs. €19.50–23/member/month) — they describe two different hardware tiers, not competing estimates of one cooperative.
- Confirmed the previously UNVERIFIABLE "$0.123/M tokens" GB300 inference figure directly against NVIDIA's own site, with an explicit scope note restricting it to the specific rack/interactivity configuration it describes.
- Unified a cluster of stale Home-tier ($0.6–$2/M, superseded) and Cooperative-tier ($0.77–$1.20/M, superseded) figures across the whitepaper, workbook, slide deck, and diagrams to the single canonical Home ($1.37–$11.89/M) and Cooperative ($1.99–$7.62/M) ranges, and recomputed every dependent $/AI-working-hour figure from the canonical ranges.
- Fixed a 1,000x unit error in the Bitcoin-mining energy-monetization comparison; the corrected arithmetic inverts that passage's original illustrative conclusion (production-cost-valued AI tokens exceed, rather than fall below, efficient Bitcoin-mining revenue per MWh).
- Fixed two prose-label cells in the companion Excel workbook that were stored as broken formulas (would render `#NAME?` in Excel).
- Fixed one Hyperscale-tier utilization assumption in the Excel workbook that was set to the high-case (90%) instead of the mid-case (60%) the canonical figure is built on.
- Fixed five diagram layout defects found during visual verification (label/caption collisions, an empty grid missing its cell labels, subplot overlap, off-canvas clipped content) across diagrams 1, 2, 3, 5, 9, and 10.

### Added for this release
- `00-how-to-use-this-research.md` — one-page orientation note.
- `20-appendix-known-limitations.md` — consolidated list of live uncertainties (model performance, utilization, financing, power pricing, adoption timing, Professional-tier evidence gap).
- `data/canonical-cost-model.csv` — the single canonical source for every tier's cost figures.
- `tools/check-canonical-consistency.py` — automated drift check across the whitepaper, workbooks, deck, and xlsx.
- `CITATION.cff` — machine-readable citation metadata.
- `LICENSE` — full CC BY 4.0 legal text plus a scope note distinguishing this author's original content from quoted third-party statements, trademarks, and external data.
- `CHECKSUMS.sha256` — SHA-256 manifest for every release asset.
- Reframed the paper's opening question from an implicit bubble/transition binary to "what would need to be true for this spending to make economic sense" (whitepaper §6/§7, executive brief, slide deck).
- Added reading-path guidance to the README distinguishing the whitepaper (authoritative map), executive brief (entry point), workbooks (audit/exploration layer), and slide deck (conversation starter).

### Known limitations
See `20-appendix-known-limitations.md` for the full list. Highlights: DGX Spark throughput figures rest on a single unaudited community benchmark; all utilization, financing, and electricity-price inputs are Scenario Assumptions, not measured or quoted real-world figures; the Professional tier (HGX B300 node) has no public price or power spec and is flagged throughout as the least-evidenced tier; adoption-timing claims from named executives are Attributed Statements, not independently verified forecasts.
