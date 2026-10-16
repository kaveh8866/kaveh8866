# Q001 · Bicycle Location API — AWS Micro-Lab Kit

**English** | [فارسی](README.fa.md) · **Kit standard:** 1.0 · **Status:** Ready to follow; **not AWS-tested** · **Exam:** SAA-C03

**Target duration:** 35–60 minutes after preparation (varies with access) · **Cloud resources:** Optional, short-lived · **Region:** selected by the learner

## Purpose

Learn **where** Amazon API Gateway, AWS Lambda, IAM and CloudWatch live in the AWS Console, **what** they do, how to send one synthetic bicycle GPS event, and **how to tear everything down safely**. A reusable kit, not a finished bicycle-tracking app.

### Original question (paraphrased)

A bicycle-sharing service anticipates peak traffic for location updates. Its architecture must expose a RESTful interface for location data and feed an existing analytics platform. The multiple-choice alternatives mention **Athena + S3**, **API Gateway + Lambda**, **QuickSight + Redshift**, and **API Gateway + Kinesis Data Analytics (now Managed Service for Apache Flink)**. The screenshot highlights **D**, but that highlighting is **not independent confirmation** of the correct answer.

**Architectural nuance:** API Gateway + Lambda handles *request ingress and processing*, not durable **storage** or **historical retrieval** by itself. Managed Service for Apache Flink performs **stream processing**, not operational durable storage. A full tracking design needs a datastore and possibly a stream/analytics pipeline, both deliberately excluded here to avoid cost and scope.

> **What this kit proves:** A SigV4-authorized HTTP API routes one signed POST request into Lambda, the handler validates synthetic coordinates and returns a response. **No coordinates are persisted. No real bicycles or people are tracked.**

## Learning outcomes

- Identify API Gateway HTTP API, routes, stages, integration and IAM authorization in the console.
- Identify Lambda handler, execution role, invocation and CloudWatch log group.
- Invoke an IAM-protected `POST /locations` endpoint; compare 202, 400/422 and 403 outcomes.
- Draw the data flow yourself in draw.io; label trust boundaries and missing persistence.
- Run local tests, optional Terraform provisioning, and **verify deletion** after the lab.

## Kit contents

| Learning item | English | فارسی |
| --- | --- | --- |
| Complete hands-on manual | [Manual](docs/manual.en.md) | [راهنمای دستی](docs/manual.fa.md) |
| Cost and permissions gate | [Preflight](docs/preflight.en.md) | [پیش‌بررسی](docs/preflight.fa.md) |
| Draw.io exercise | [Draw.io](docs/drawio.en.md) | [تمرین دیاگرام](docs/drawio.fa.md) |
| Safe resource removal | [Cleanup](docs/cleanup.en.md) | [پاک‌سازی](docs/cleanup.fa.md) |
| Architecture reasoning | [ADR](docs/decision.en.md) | [تصمیم معماری](docs/decision.fa.md) |
| Experiment record | [Record](docs/record.en.md) | [ثبت نتایج](docs/record.fa.md) |

**Executable materials:** [Lambda Python](lambda/handler.py) · [offline unit tests](tests/test_handler.py) · [example HTTP events](examples/) · [Terraform](terraform/) · [signed IAM client](scripts/invoke_iam.py).

## Choose one execution path

**A — Console first:** follow the manual, observe service controls, test Lambda, add an IAM-protected API only when you can verify a secure route **before publishing a stage**. If the console wizard publishes an unsecured route automatically, **stop** and use Path B for the API.

**B — Terraform:** from `terraform/`, `terraform init`, `terraform plan`, inspect resources/cost, `terraform apply`. Then use the signed request script and `terraform destroy`. Do not mix manual and Terraform management for the same resources.

**C — Free exploration:** read-only AWS console inspection and local Python unit tests. No cloud provisioned.

## Quick local test (no AWS account or network needed)

```bash
cd labs/micro-kits/Q001-bicycle-location-api
python3 -m unittest discover -s tests -v
```

**Evidence gate:** Until a learner runs the lab, `docs/record.en.md` and `docs/record.fa.md` remain blank; published kit ≠ verified cloud experiment. After running, note the actual Region, sanitized results, cost, cleanup confirmations and diagram.

**Security:** API route uses `AWS_IAM` and SigV4. No public unauthenticated route. No permanent access keys in code. Throttling is **best effort**, not a financial hard cap. Cloud credits and Free Tier vary by account.

## Official documentation

- [AWS HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html)
- [IAM authorization for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control-iam.html)
- [Lambda proxy payload v2](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)
- [Lambda and CloudWatch logs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-loggroups.html)
- [API Gateway pricing](https://aws.amazon.com/api-gateway/pricing/)

**Not affiliated with or endorsed by AWS.** Practice-question paraphrase used for educational discussion.
