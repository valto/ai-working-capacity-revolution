#!/usr/bin/env python3
"""
Build perspectives.html from every YAML entry in perspectives/.

Each perspectives/*.yaml file (except _template.yaml) describes one
Perspectives/Writeups entry — see perspectives/README.md for the field
schema. This script reads all of them, sorts by date (newest first), and
renders a static HTML index grouped with filterable topic/type metadata
(client-side filtering via a small inline script — no build-time framework).

Only entries with status: published are rendered. Entries with
status: pending-review (e.g. from an automated backlink-discovery pipeline,
not yet wired up — see docs/backlink-discovery.md) are counted but not shown,
so a partially-classified pipeline can never silently publish unreviewed
material.

Run from the repo root: python3 tools/build-perspectives.py
Requires: pyyaml on PATH.
"""
import glob
import html
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERSPECTIVES_DIR = os.path.join(ROOT, "perspectives")
OUT_PATH = os.path.join(ROOT, "perspectives.html")

REQUIRED_FIELDS = ["title", "author", "date", "publication", "url", "topic",
                   "description", "relationship", "type", "language", "scope",
                   "discovery", "status"]

TYPE_LABELS = {
    "original": "Original — by Valto Loikkanen",
    "independent": "Independent — third party",
    "critical": "Critical — third party",
}


def load_entries():
    entries = []
    paths = sorted(glob.glob(os.path.join(PERSPECTIVES_DIR, "*.yaml")))
    paths += sorted(glob.glob(os.path.join(PERSPECTIVES_DIR, "_pending", "*.yaml")))
    for path in paths:
        if os.path.basename(path).startswith("_"):
            continue
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        missing = [field for field in REQUIRED_FIELDS if field not in data]
        if missing:
            print(f"  WARNING: {path} missing fields {missing} — skipping")
            continue
        data["_file"] = os.path.relpath(path, PERSPECTIVES_DIR)
        entries.append(data)
    return entries


def render_card(e):
    topics = " ".join(f'<span class="tag">{html.escape(t)}</span>' for t in e["topic"])
    type_label = TYPE_LABELS.get(e["type"], e["type"])
    return f"""
<div class="perspective-card" data-type="{html.escape(e['type'])}" data-topics="{html.escape(','.join(e['topic']))}">
  <h3><a href="{html.escape(e['url'])}" target="_blank" rel="noopener">{html.escape(e['title'])}</a></h3>
  <p class="p-meta">{html.escape(e['author'])} &nbsp;·&nbsp; {html.escape(e['publication'])} &nbsp;·&nbsp; {html.escape(e['date'])} &nbsp;·&nbsp; <em>{html.escape(type_label)}</em></p>
  <p>{html.escape(e['description'])}</p>
  <p class="p-tags">{topics}</p>
</div>"""


def main():
    print("Building perspectives.html...")
    entries = load_entries()
    published = [e for e in entries if e.get("status") == "published"]
    pending = [e for e in entries if e.get("status") != "published"]
    published.sort(key=lambda e: e["date"], reverse=True)

    all_topics = sorted({t for e in published for t in e["topic"]})
    cards_html = "\n".join(render_card(e) for e in published)
    topic_buttons = "\n".join(
        f'<button class="filter-btn" data-topic="{html.escape(t)}">{html.escape(t)}</button>' for t in all_topics
    )

    template_path = os.path.join(ROOT, "tools", "perspectives-template.html")
    with open(template_path, encoding="utf-8") as f:
        template = f.read()

    output = template.replace("{{CARDS}}", cards_html).replace("{{TOPIC_BUTTONS}}", topic_buttons)
    output = output.replace("{{COUNT}}", str(len(published)))

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"  {len(published)} published entries rendered to perspectives.html")
    if pending:
        print(f"  {len(pending)} entries with status != published were NOT rendered "
              f"(pending review): {[e['_file'] for e in pending]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
