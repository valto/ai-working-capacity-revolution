# Backlink discovery → Perspectives pipeline (design)

**Status: designed, not wired up.** The manual and submitted intake paths described in Part 2 are live today (`perspectives/*.yaml`, built by `tools/build-perspectives.py`). The automated crawler in Part 1 requires a paid API subscription and credentials this repository does not have — it is documented here so it can be wired in later without redesigning the data model around it.

## Why not auto-publish from a crawler directly

Backlink crawlers surface a lot of noise: mirrors, navigation links, scraped/aggregator pages, social shares with no actual content, and spam. Piping that directly into a public "who's writing about this" page would erode trust in the Perspectives section faster than it would grow it. The pipeline is therefore designed in two clearly separated stages — **discovery** (cheap, automatic, over-inclusive) and **classification** (the actual judgment call about whether something is a real writeup) — with nothing crossing from the first stage to the public site without passing through the second.

## Part 1 — Discovery (not yet implemented; requires a paid API)

```
Scheduled job (daily/weekly)
  → query backlinks to valto.github.io/ai-working-capacity-revolution/
    and to specific deep pages (the whitepaper, key workbooks)
  → diff against a stored "known backlinks" table (by source_url)
  → for each genuinely new source_url:
      → fetch title/page metadata (or use what the backlink API already returned)
      → write a candidate record to perspectives/_pending/<hash>.yaml
        with status: pending-review
  → (optional) an LLM call drafts a 1-2 sentence description + topic tags
    for each candidate, still under status: pending-review
  → stop. Nothing here touches perspectives.html or the published index.
```

**API options, both viable, neither free:**

| | Ahrefs Backlinks API | Semrush Backlinks API (v4) |
|---|---|---|
| Returns | Backlinks for a domain or specific URL | source_url, source_title, target_url, anchor text, first-seen/last-seen dates |
| New/lost tracking | Yes | Yes — explicit new/lost backlink filters |
| Cost | Subscription + API add-on | Subscription with API units; units consumed per call |
| Fit for this use | Good | Slightly better fit — the v4 endpoint's per-backlink metadata (title, anchor, dates) maps directly onto the `perspectives/*.yaml` schema with less post-processing |

**Decision needed before building this part:** which provider (cost/quota trade-off), who holds the API key (this should not live in the git repo — use a GitHub Actions repository secret if run via CI, or a local-only credentials file if run manually), and how often to poll (daily is standard for a `git`-tracked candidate queue; weekly is likely sufficient for a research reference site's actual traffic).

## Part 2 — Classification (design; can be implemented without the crawler)

Whether a candidate comes from the crawler above or a manual submission, it goes through the same classification step before becoming a published Perspectives entry:

```
candidate (pending-review)
  → classify: actual-writeup | mention | citation | social-share | navigation/mirror | spam
  → if actual-writeup:
      → confirm/edit the auto-drafted description and topic tags
      → set type: independent (default) or critical (if the piece disagrees)
      → set status: published
  → else: delete the candidate file (do not keep a "rejected" archive of spam/mirrors —
    it serves no purpose and risks accidentally publishing it later by mistake)
```

This can be done by a human maintainer reading each `_pending/*.yaml` file and either editing it in place (removing the leading `_pending/` path, setting `status: published`, moving it to `perspectives/`) or deleting it. An LLM-assisted first pass (draft the classification label, description, and tags) is reasonable to speed this up, but the **publish decision itself should stay a human "approve" action** until the classifier's false-positive rate is known — per the repository's own evidence-discipline principle (Method §3.1), an unreviewed automatic classification is exactly the kind of ATTRIBUTED-not-yet-VERIFIED claim this project's methodology is built to keep separate from a confirmed fact.

An explicit confidence threshold (e.g., "auto-publish only candidates classified as actual-writeup with >90% confidence, everything else queues for manual review") is a reasonable later refinement once the classifier exists — not a starting assumption.

## Part 3 — What's actually live today (no API dependency)

- **Manual entries**: any maintainer copies `perspectives/_template.yaml`, fills it in, and runs `tools/build-perspectives.py`. This is how the three seed entries (the author's own prior LinkedIn/Substack pieces, already verified in `02-source-register.md`) were added.
- **Submitted entries**: the "Written something based on, referencing, or challenging this work?" call-to-action on `perspectives.html` points readers to open a GitHub issue/PR with the same fields. A maintainer reviews and adds the file the same way as a manual entry.

Both of these already produce the exact same output format (`perspectives/*.yaml` → `perspectives.html`) that an eventual automated pipeline would feed into — so wiring in Part 1 later is additive, not a redesign.
