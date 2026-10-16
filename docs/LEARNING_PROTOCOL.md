# Question → Lab → Portfolio Protocol (v1)

Every exam scenario gets a **learning record**. Only questions suitable for safe reproducible experiments become full hands-on labs.

## Phase A — Human-led analysis

1. **YouTube/source:** link and timestamp; paraphrase the scenario in your own words. Do not republish copyrighted question banks.
2. **Independent answer:** record choice, reasoning, rejected options and confidence (1–5) before asking AI.
3. **Gemini six-step analysis:** requirements/keywords; service comparison; decision trade-offs; architecture; mental walkthrough; practical tutorial. Validate uncertain claims against current AWS docs.

## Phase B — Engineering

4. **Testable hypothesis:** state a falsifiable architecture claim, acceptance criteria, cost cap and cleanup plan.
5. **Human architecture:** sketch and redraw an editable .drawio diagram yourself.
6. **Local-first coding:** collaborate with a code agent on small Python/Docker experiments; read the code and run local tests.
7. **Controlled AWS verification:** only if service is available and cost approved. Record evidence and delete resources. Local emulation is **not proof** of actual AWS behavior.

## Phase C — Evidence and learning

8. **Decision record:** why the selected design fits and when alternatives would be better.
9. **GitHub evidence:** code, diagram, test output, error cases, limitations, cost notes, AI disclosure.
10. **Independent recall:** answer the question again without AI, then vary one requirement and justify the changed solution.

## Experiment classes

| Class | Appropriate use |
| --- | --- |
| Micro experiment | Quickly test one AWS behavior |
| Full lab | Reproducible integrated example |
| Design-only | Live cloud test would be expensive, unsafe or unnecessary |

**Definition of done:** status **published** requires meaningful documented test/design evidence, reviewed architecture, scope and limitations; it does not imply a cloud deployment.

## Responsibilities

- **Human:** scenario interpretation, original answer, design decisions, final diagram and review of AI code.
- **Gemini / AI tutor:** conceptual explanation, option comparisons and tutorial drafts.
- **Code agent:** proposes local code/tests and documentation; never creates cloud resources without explicit approval.
- **Reviewer:** ensures evidence claims, exam domain mapping, costs and safe operation are accurate.
