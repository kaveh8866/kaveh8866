#!/usr/bin/env python3
"""Generate docs/PROGRESS.md from data/labs.json without invented results."""
import argparse
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
STATUS = {"planned", "in-progress", "local-tested", "aws-tested", "design-only", "published"}
BT = chr(96)


def render(data):
    labs = data["labs"]
    pub = sum(x["status"] == "published" for x in labs)
    tested = sum(x["aws_tested"] for x in labs)
    lines = [
        "# Lab Progress", "",
        f"**Source of truth:** {BT}data/labs.json{BT}. All statuses reflect manually verified evidence.", "",
        f"**Progress:** {BT}{pub} / {len(labs)} published{BT} · {BT}{tested} / {len(labs)} AWS-tested{BT}", "",
        "| Week | Domain | Lab | Status | AWS tested |",
        "| --- | --- | --- | --- | --- |",
    ]
    for lab in labs:
        if lab["status"] not in STATUS:
            raise ValueError(f'Unknown status {lab["status"]}')
        name = lab["name"].replace("|", r"\|")
        lines.append(
            f'| {lab["week"]} | {lab["domain"]} | '
            f'[{name}](../{lab["path"]}/README.md) | '
            f'{lab["status"]} | {"Yes" if lab["aws_tested"] else "No"} |'
        )
    lines += ["", "## How to update", "",
              f"After confirming evidence, edit {BT}data/labs.json{BT}, then run {BT}python scripts/progress.py --write{BT} and commit the updated Markdown.",
              "", f"A local test is not an AWS test. Do not switch {BT}aws_tested{BT} to true without an actual verified AWS run."]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads((BASE / "data/labs.json").read_text(encoding="utf-8"))
    expected = render(data)
    dest = BASE / "docs/PROGRESS.md"
    if args.write:
        dest.write_text(expected, encoding="utf-8")
        print("Progress updated")
    elif dest.read_text(encoding="utf-8") != expected:
        raise SystemExit("Progress out of date: python scripts/progress.py --write")
    else:
        print("Progress up to date")


if __name__ == "__main__":
    main()
