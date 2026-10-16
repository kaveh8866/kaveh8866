# Getting Started

This is the **public GitHub profile repository** for @kaveh8866; its root `README.md` appears at <https://github.com/kaveh8866>. The folder tree also hosts a small AWS SAA-C03 learning portfolio.

1. Review [the roadmap](ROADMAP_30_DAYS.md) and [protocol](LEARNING_PROTOCOL.md).
2. Check [cloud safety](CLOUD_SAFETY.md) before signing into AWS or deploying anything.
3. Pick a scenario, fill in [a question card](../templates/QUESTION_CARD.md), and start one lab.
4. Produce an editable architecture diagram in `diagrams/source/` and an exported image in `diagrams/exported/`.
5. Capture *sanitized* local / AWS evidence and record reasoning in an ADR.
6. Update `data/labs.json` only after verifying the status, then regenerate `docs/PROGRESS.md`.

## Offline validation (standard library only)

```bash
python3 scripts/validate_repo.py
python3 scripts/progress.py --check
python3 -m unittest discover -s tests -v
```

To update progress after new evidence:

```bash
python3 scripts/progress.py --write
```

No AWS credentials or cloud expenses are needed to run these commands. **First lab:** `labs/week-01-foundation/D1-L1-iam-least-privilege/README.md`.
