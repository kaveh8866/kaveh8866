#!/usr/bin/env python3
"""Offline structure validator; no network or AWS calls."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DOMAINS = {f"D{i}" for i in range(1, 5)}
ALLOWED = {"planned", "in-progress", "local-tested", "aws-tested", "design-only", "published"}


def validate():
    data = json.loads((BASE / "data/labs.json").read_text(encoding="utf-8"))
    labs = data["labs"]
    assert len(labs) == 16, f"Expected 16 labs, got {len(labs)}"
    assert len({x["id"] for x in labs}) == len(labs), "Duplicate lab ID"
    for week in range(1, 5):
        within = [x for x in labs if x["week"] == week]
        assert len(within) == 4, f"Week {week} has {len(within)} labs"
        assert {x["domain"] for x in within} == DOMAINS, f"Week {week}: missing domain"
    for lab in labs:
        assert lab["status"] in ALLOWED, lab
        assert type(lab["aws_tested"]) is bool
        assert lab["id"] == f'{lab["domain"]}-L{lab["week"]}'
        assert (BASE / lab["path"] / "README.md").is_file(), lab["path"]
        if lab["aws_tested"]:
            assert lab["status"] in {"aws-tested", "published"}
    assert (BASE / "README.md").is_file()
    print(f"Validated {len(labs)} labs across four domains and four weeks")


if __name__ == "__main__":
    validate()
