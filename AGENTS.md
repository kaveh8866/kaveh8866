# Repository instructions for AI code assistants

This repository is a **public personal learning portfolio**. Do not misrepresent planned work as implemented or tested.

- Keep human-owned decisions and draw.io diagrams separate from agent-generated implementation drafts.
- Work local-first. No live AWS deployment, IAM change, cloud account access, paid resource, marketplace sign-up or destructive operation without explicit human approval for that exact action.
- Treat all credentials as secrets. No access keys, tokens, account IDs, personal billing details or unredacted logs in commits.
- Document test commands and use Python standard library for scaffold tooling.
- Keep 16 planned labs in `data/labs.json` until actual evidence merits a status change.
- After a verified status update, run `python scripts/progress.py --write`, `python scripts/validate_repo.py`, and `python -m unittest discover -s tests -v`.
- Prioritize explanation, repeatability, cost transparency and human review.
