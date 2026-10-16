#!/usr/bin/env python3
"""Validate bilingual Q001 files and GitHub-safe RTL HTML wrappers offline."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
KITS = ROOT / "labs" / "micro-kits"
missing = []
validated = 0
for kit in sorted(KITS.iterdir()):
    if not kit.is_dir():
        continue
    for persian in sorted(kit.rglob("*.fa.md")):
        text = persian.read_text(encoding="utf-8")
        relative = persian.relative_to(ROOT)
        if not text.startswith('<div dir="rtl" align="right">\n\n'):
            missing.append(f"{relative}: missing top-level RTL wrapper")
        if not text.rstrip().endswith("</div>"):
            missing.append(f"{relative}: missing closing RTL wrapper")
        if re.search(r"(?m)^\x60{3}", text):
            missing.append(f"{relative}: use explicit LTR pre/code HTML for multiline code")
        en_path = (persian.parent / (
            "README.md" if persian.name == "README.fa.md"
            else persian.name.replace(".fa.md", ".en.md")))
        if not en_path.exists():
            missing.append(f"{relative}: English counterpart missing ({en_path.name})")
        validated += 1

    must = ["docs/service-tour.fa.md", "docs/service-tour.en.md",
            "docs/cost-comparison.fa.md", "docs/cost-comparison.en.md",
            "docs/manual.fa.md", "docs/manual.en.md"]
    for item in must:
        if not (kit / item).exists():
            missing.append(f"{kit.name}: missing core file {item}")

standard = ROOT / "docs/BILINGUAL_MARKDOWN_STANDARD.fa.md"
if not standard.exists() or not standard.read_text(encoding="utf-8").startswith('<div dir="rtl" align="right">'):
    missing.append("Persian project authoring standard missing or not RTL")
if missing:
    raise SystemExit("Bilingual/RTL issues:\n" + "\n".join(missing))
print(f"Validated {validated} Persian documents, English counterparts, RTL wrappers, and required service/cost tours.")
