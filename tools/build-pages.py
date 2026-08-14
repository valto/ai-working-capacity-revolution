#!/usr/bin/env python3
"""
Build native HTML pages for every markdown document in this repository, so
the GitHub Pages site can be read end-to-end without jumping to GitHub's own
markdown viewer.

For each `NN-name.md` (and a few unnumbered docs: README.md, CHANGELOG.md),
this script:
  1. Runs pandoc with a table-of-contents and the shared page template
     (tools/page-template.html) to produce `NN-name.html` at the repo root.
  2. Rewrites every occurrence of another tracked markdown filename (in link
     hrefs, inline code, or plain text) to point at its `.html` counterpart,
     so cross-references between documents stay inside the Pages site.

Run from the repo root: python3 tools/build-pages.py
Requires: pandoc on PATH.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "tools", "page-template.html")

# (source markdown filename, nav breadcrumb label, page <title>)
DOCS = [
    ("00-how-to-use-this-research.md", "How to Use This Research", "How to Use This Research"),
    ("01-whitepaper.md", "Whitepaper", "Whitepaper"),
    ("02-source-register.md", "Source Register", "Source Register"),
    ("03-workbook-global-baseline.md", "Global Baseline Workbook", "Global Baseline Workbook"),
    ("04-workbook-ai-working-capacity-conversion.md", "AI Working-Capacity Conversion Workbook", "AI Working-Capacity Conversion Workbook"),
    ("05-workbook-token-factory-scenarios.md", "Token-Factory Scenario Workbook", "Token-Factory Scenario Workbook"),
    ("06-investment-thesis-notes.md", "Investment-Thesis Notes", "Investment-Thesis Notes"),
    ("07-workbook-humanoid-working-capacity.md", "Humanoid Working-Capacity Workbook", "Humanoid Working-Capacity Workbook"),
    ("08-workbook-localized-scenario-eur-finland.md", "Localized Scenario Workbook (EUR/Finland)", "Localized Scenario Workbook (EUR/Finland)"),
    ("09-appendix-glossary.md", "Glossary", "Glossary"),
    ("10-appendix-source-register-formatted.md", "Source Register (formatted)", "Source Register (formatted)"),
    ("11-appendix-assumption-register.md", "Assumption Register", "Assumption Register"),
    ("12-executive-brief.md", "Executive Brief", "Executive Brief"),
    ("13-slide-deck-outline.md", "Slide Deck Outline", "Slide Deck Outline"),
    ("14-shortform-general.md", "Short-Form: General Explainer", "Short-Form: General Explainer"),
    ("15-shortform-ownership.md", "Short-Form: Ownership", "Short-Form: Ownership"),
    ("16-shortform-value.md", "Short-Form: Value", "Short-Form: Value"),
    ("17-visual-asset-briefs.md", "Visual Asset Briefs", "Visual Asset Briefs"),
    ("20-appendix-known-limitations.md", "Known Limitations", "Known Limitations"),
    ("README.md", "README", "README"),
    ("CHANGELOG.md", "Changelog", "Changelog"),
]

# Filenames eligible for cross-reference rewriting (all tracked docs, by basename).
MD_FILENAMES = {name for name, _, _ in DOCS}


def rewrite_cross_references(html, current_filename):
    """Rewrite href="NN-name.md" and bare `NN-name.md` mentions in the
    rendered HTML to point at the corresponding .html file instead."""
    def replace_href(match):
        fname = match.group(1)
        if fname in MD_FILENAMES:
            return f'href="{fname[:-3]}.html"'
        return match.group(0)

    html = re.sub(r'href="([\w.-]+\.md)"', replace_href, html)

    # Bare filename mentions inside <code>NN-name.md</code> (from backtick
    # spans in the source markdown) — relink the code span itself.
    def replace_code_span(match):
        fname = match.group(1)
        if fname in MD_FILENAMES:
            return f'<code><a href="{fname[:-3]}.html">{fname}</a></code>'
        return match.group(0)

    html = re.sub(r'<code>([\w.-]+\.md)</code>', replace_code_span, html)
    return html


def build_one(src_filename, nav_label, title):
    src_path = os.path.join(ROOT, src_filename)
    if not os.path.exists(src_path):
        print(f"  SKIP (not found): {src_filename}")
        return False

    out_filename = src_filename[:-3] + ".html"
    out_path = os.path.join(ROOT, out_filename)

    cmd = [
        "pandoc", src_path,
        "-f", "markdown",
        "-t", "html5",
        "--template", TEMPLATE,
        "--toc", "--toc-depth=2",
        "-V", f"navlabel={nav_label}",
        "-V", f"ghsource={src_filename}",
        "-M", f"title={title}",
        "-o", out_path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  FAILED: {src_filename}\n{result.stderr}")
        return False

    with open(out_path, encoding="utf-8") as f:
        html = f.read()
    html = rewrite_cross_references(html, src_filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  built {out_filename}")
    return True


def main():
    print("Building HTML pages from markdown sources...")
    ok = 0
    for src_filename, nav_label, title in DOCS:
        if build_one(src_filename, nav_label, title):
            ok += 1
    print(f"\n{ok}/{len(DOCS)} pages built.")
    return 0 if ok == len(DOCS) else 1


if __name__ == "__main__":
    sys.exit(main())
