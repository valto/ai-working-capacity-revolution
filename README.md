# Why Are They Spending Trillions on AI?

*The numbers and economics behind the AI working-capacity revolution—from electricity and infrastructure to tokens, robots, value, ownership, and agency.*

**Author:** Valto Loikkanen
**Status:** v1.0 research package (draft — not yet publicly released)
**Research initiated:** August 12, 2026
**Factual source cut-off:** 2026-08-12
**Licence:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — copy, redistribute, remix, adapt, and build upon this material for any purpose, including commercially, with attribution.
**Suggested attribution:** "Research synthesis and modelling by Valto Loikkanen, assisted by AI."

## What this is

A neutral-observer research synthesis reverse-engineering a connected economic model — energy → hardware → compute → models → tokens → AI working capacity → digital work → outcomes → value → agency — from public statements by Jensen Huang (and the Nvidia/Wall Street financing panel), Sam Altman, and Mark Zuckerberg, combined with independently verified hardware specs, pricing, and benchmarks, plus the author's own prior published work on AI infrastructure ownership and cooperative models.

It is not a vendor report, a political programme, or an investment recommendation. Six reader lenses — Individual, SME/owner-manager, Finance/infrastructure investor, Government/region/community, AI builder/operator, and Educator/researcher/journalist — are given **equal weight and no priority ordering**, by deliberate editorial decision.

Every substantive claim is tagged with one of five evidence classes (Observed Fact / Attributed Statement / Derived Calculation / Scenario Assumption / Interpretation) so a reader can tell, at a glance, what is independently verified, what is someone's on-record claim, what is arithmetic, and what is an editable illustration.

**Disclosure:** the author has commercial and advocacy interests in personal AI infrastructure and cooperative/ownership-based AI models through Prifina, Digiole, and the peecos/PIOS reference framework. See §4 of the whitepaper (`01-whitepaper.md`) for the full disclosure and non-advice boundary.

## Package contents

| File | What it is | For |
|---|---|---|
| `01-whitepaper.md` | The full whitepaper — front matter, Parts I–VII, closing (45 sections) | Everyone; start here |
| `02-source-register.md` | Raw fact-check ledger from the verification pass — every claim checked, its evidence class, and how it was checked | Anyone auditing a specific number or quote |
| `03-workbook-global-baseline.md` | Release Asset #7 — full energy-to-tokens cost curves for Home / Cooperative / Professional / Hyperscale tiers, global USD baseline | Anyone modeling their own AI-factory economics |
| `04-workbook-ai-working-capacity-conversion.md` | Release Asset #9 — the usage-intensity ladder (chat → copilot → delegated agent → heavy orchestration) and human-work comparison tables | Anyone converting $/token into $/AI-working-hour |
| `05-workbook-token-factory-scenarios.md` | Release Asset #10 — token/AI-factory scenarios, the corrected €42 vs. €19.50–25/member/month cooperative-cost breakdown (two different hardware tiers, not a discrepancy), and the Bitcoin-mining energy-monetization comparison | Cooperative/community infrastructure planners |
| `06-investment-thesis-notes.md` | Release Asset #12 — educational, non-advice investment-scenario notes by scale tier | Investors and capital allocators (read the non-advice boundary first) |
| `07-workbook-humanoid-working-capacity.md` | Release Asset #11 — the humanoid-robot embodied working-capacity extension, illustrative €25,000 example plus real market price range | Anyone extending the model to physical labor |
| `08-workbook-localized-scenario-eur-finland.md` | Release Asset #8 — a worked EUR/Finland localization template | Anyone adapting the global baseline to their own country |
| `09-appendix-glossary.md` | Definitions and notation — every technical/economic term used in the paper, plain-language | New readers |
| `10-appendix-source-register-formatted.md` | Publication-formatted version of the source register, organized by source with verification methodology | Fact-checkers, journalists, researchers |
| `11-appendix-assumption-register.md` | Every editable scenario assumption across all workbooks, consolidated into one table with cross-workbook consistency notes | Anyone re-running the models with their own numbers |
| `12-executive-brief.md` | A standalone, self-contained summary of the whole paper | Readers who won't read the full paper |
| `13-slide-deck-outline.md` | Slide-by-slide presentation script covering the whole paper | Anyone presenting this material |
| `14-shortform-general.md` | ~300-word general-audience explainer | Social/short-form sharing |
| `15-shortform-ownership.md` | ~300-400 word piece on the ownership question (Part V) | Social/short-form sharing |
| `16-shortform-value.md` | ~300-400 word piece on why cheap tokens ≠ cheap value (Part IV) | Social/short-form sharing |
| `17-visual-asset-briefs.md` | Diagram specifications for the 10 required visualizations — specs for a designer, not finished images | Whoever builds the final graphics |

## Status and known open items

This is a complete v1.0 draft produced by an AI-assisted research and modelling workflow, with an independent verification pass, per-section fact-consistency audits, and a deterministic (non-AI-regenerated) final assembly step to guarantee no content was dropped or truncated during compilation.

Known items flagged transparently within the package itself:

- **Resolved (2026-08-13):** the earlier "€42 vs €19.50–25/member/month" cooperative-cost item was not actually a discrepancy — the two figures describe two different hardware tiers (an illustrative €100,000 shared workstation-class machine vs. a pool of $4,699 NVIDIA DGX Spark units), not competing estimates of the same cooperative. See `05-workbook-token-factory-scenarios.md` §1a/§1b and `11-appendix-assumption-register.md` row 6a for the corrected, fully auditable breakdown.
- **Resolved (2026-08-13):** the "$0.123/M tokens" GB300-class inference figure is now confirmed directly on NVIDIA's own site (previously flagged UNVERIFIABLE). It applies specifically to a 72-GPU GB300 NVL72 rack at 116 tokens/sec/user using NVIDIA Dynamo and TensorRT-LLM — it must not be used to price any workstation or desktop-class device. See `03-workbook-global-baseline.md` §5.7.
- Several hardware/price inputs (Professional-tier HGX B300 node pricing/power, hyperscale rack capex, the illustrative €100,000 DGX-Station-class and €25,000 humanoid robot prices) have no public source and are flagged ⚠ throughout as placeholders, not verified figures — NVIDIA does not publish retail prices for DGX Station or HGX B300.
- This package has **not** been deployed to a public site (no GitHub Pages) — it exists as a reviewable Markdown package, with a generated PDF (`01-whitepaper.pdf`), in this repository pending author review.

Before any public release, a human review pass of the full whitepaper and workbooks is recommended, particularly for the reconciliation and placeholder items above.
