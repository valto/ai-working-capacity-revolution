# Perspectives / Writeups — entry format

Each file in this directory (except this README) is one Perspectives entry, in YAML, with these fields:

```yaml
title: "Article or piece title"
author: "Author name"
date: "YYYY-MM-DD"
publication: "Where it was published (e.g., LinkedIn, Substack, a named outlet)"
url: "https://..."
topic: ["Economics", "Ownership"]   # one or more of the categories below
description: "One to three sentences describing what the piece says."
relationship: "supports | interprets | applies | criticizes | extends"
type: "original | independent | critical"   # see definitions below
language: "en"
scope: "external | internal"        # internal = by the author, external = third party
discovery: "manual | submitted | backlink-auto"
status: "published"                  # published | pending-review (for auto-discovered items awaiting classification)
```

**Type definitions** (per the repository's publishing guidelines):
- **original** — written directly from this research by Valto Loikkanen.
- **independent** — a third party referencing, interpreting, or applying the work, without necessarily agreeing or disagreeing.
- **critical** — a third party challenging assumptions, calculations, or conclusions. Included where relevant — inclusion does not imply endorsement, and exclusion is not used simply because a piece disagrees.

**Relationship values**: `supports`, `interprets`, `applies`, `criticizes`, `extends` — a piece can combine more than one; list the primary relationship.

## Adding an entry manually

Copy `_template.yaml`, fill in the fields, save it as `perspectives/<short-slug>.yaml`, then run:

```bash
python3 tools/build-perspectives.py
```

This regenerates `perspectives.html` from every `.yaml` file in this directory.

## Submitting a perspective

See the "Submit a perspective" section on the [Perspectives page](https://valto.github.io/ai-working-capacity-revolution/perspectives.html) of the live site.

## Automated discovery (designed, not yet wired up)

`_pending/` holds candidate entries with `status: pending-review` — from a future automated backlink-discovery pipeline, or draft entries not yet ready to publish. Files here are never rendered to the public site (`tools/build-perspectives.py` only publishes `status: published` entries). See `docs/backlink-discovery.md` for the full pipeline design.
