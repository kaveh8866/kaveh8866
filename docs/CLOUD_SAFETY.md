# AWS Cost & Security Guardrails

**A free-plan label or cloud credit does not guarantee that every AWS service is free.** Validate your own account limits, Region availability, pricing and credit coverage before each run.

## Before an AWS experiment

- [ ] Confirm correct account and Region privately; never publish AWS account identifiers.
- [ ] Name each planned resource, its purpose and maximum runtime.
- [ ] Check current pricing, quotas, free-plan eligibility and estimated worst-case charge.
- [ ] Avoid NAT Gateways, provisioned database clusters, always-on load balancers and public endpoints by default.
- [ ] Use least-privilege roles. Never upload access keys, secrets or personal data.
- [ ] Only synthetic test data. Remove secrets/account IDs from logs and screenshots.
- [ ] Tag resources `project=aws-saa-c03-journey` and `lab=<id>`.
- [ ] Document cleanup and how to verify it, including storage versions, log retention and snapshots.

## After

- [ ] Capture sanitized outputs and observed test results.
- [ ] Distinguish local simulation from actual AWS observations.
- [ ] Delete temporary resources and **verify** deletion.
- [ ] Review billing after the experiment; cost alerts are not spending caps.
- [ ] Update the manifest only when evidence exists.

**No CI workflow or code agent in this repository is permitted to deploy AWS infrastructure automatically.**
