# Portfolio Evidence Standard

Every completed lab should include:

1. Scenario paraphrase and source citation (URL + timestamp, no copyrighted answer dump).
2. Human answer before AI, plus later corrected reasoning and confidence.
3. Architecture diagram created or reviewed by the learner (editable `.drawio` and readable export).
4. Hypothesis, architecture decision record, alternatives and trade-offs.
5. Reproducible local commands and passing/failing test evidence.
6. Distinction between local emulation and measured AWS service output.
7. Cost estimate, observed spend if applicable, and resource cleanup confirmation.
8. AI contribution disclosure, limitations and next improvement.

## Status rules

- `planned`: not started.
- `in-progress`: design or implementation started but unverified.
- `local-tested`: local experiment verified; no claim about cloud execution.
- `aws-tested`: a real AWS test with sanitized evidence exists.
- `design-only`: documented architecture without cloud test.
- `published`: curated evidence is ready to show; `aws_tested` remains independently true/false.

Never publish credentials, personal information, account IDs or misleading 'production-ready' claims.
