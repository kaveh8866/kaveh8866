# Q001 — Why the lab is smaller than the exam architecture

[فارسی](cost-comparison.fa.md) · [Service tour](service-tour.en.md)

This kit **does not replace Kinesis with Lambda in the exam answer**. It selects a *separate, minimal teaching exercise* to learn API routing and Lambda invocation safely while also touring **all services from every answer choice**, including the user's Kinesis/Flink diagram.

## Service-by-service cost drivers (not a quote)

| Service / exam option | Main function | Main billing drivers | Can inspect without creation? | Q001 mode |
| --- | --- | --- | --- | --- |
| API Gateway — B, D | HTTP endpoint and routing | Requests, transfer, feature/tier | Yes | Optional tiny deployed example |
| AWS Lambda — B | Validate/handle requests | Invocations, duration/memory, logs | Yes | Optional tiny deployed example |
| Kinesis Data Streams — learner diagram | Buffered event stream | On-demand Standard: stream-hour, data-in/out; provisioned: shard-hour + record units; retention extras | Yes | Read-only |
| Managed Service for Apache Flink — D | Stateful streaming analytics | KPU usage with **10-minute minimum per start**; application storage/backup | Yes | Read-only; do not start |
| Amazon S3 — A | Durable object storage | GB-month, requests, transfer | Yes | Read-only |
| Athena — A | Analytical queries | Data scanned/compute; S3 results | Yes | Read-only; no query |
| Amazon Redshift — C | Data warehouse | Provisioned node-hours or serverless RPU compute, storage/snapshots | Yes | Read-only; no cluster |
| Amazon Quick Sight (formerly QuickSight) — C | BI dashboards | Per-user subscription/usage/capacity | Landing page yes; avoid sign-up | Read-only |

## Three permitted paths

**Path 0 — Read-only ($0 resources created by this kit):** inspect all eight services, record screenshots only after privacy review, draw both architectures. Does not imply the entire AWS account costs $0.

**Path 1 — Minimal live micro-lab (small but not guaranteed free):** IAM-protected HTTP API + Python Lambda + CloudWatch Logs. Send 1–5 synthetic calls, delete all lab resources. **Reason for choosing Lambda:** simple setup and rapid deletion to demonstrate HTTP integration; not a claim that Lambda can replace stream aggregation.

**Path 2 — Full streaming reference (DESIGN ONLY by default):** API Gateway → Kinesis Data Streams → Managed Service for Apache Flink → analytics sink, with a separate operational store/query API if actual location retrieval is needed. Complexity and running charges make it inappropriate as the default short lab; use [the console tour](service-tour.en.md) to learn services without deploying them.

## Example cost logic, without inventing a euro figure

- **Path 0:** no new AWS resources or requests other than browsing console. No active service deployments initiated by this kit.
- **Path 1:** cost depends on the number of API calls, Lambda runtime/requests, and CloudWatch log size/duration. Existing AWS credit or service allowances may cover it—but **never promise zero**.
- **Path 2:** add Kinesis stream running time and data volume, Flink KPU runtime (ten-minute minimum per start) and application storage, plus any output system. Even idle/micro streams may have running-time charges. A larger bill is *possible*, not a specific prediction.

**Comparison:** This is a comparison of **cost models and risk**, not a verified region-specific quotation. To calculate exact costs, choose Region and account first and use AWS Pricing Calculator, including any tier credits. Estimate every service before creating resources.

## Official AWS sources

- [API Gateway pricing](https://aws.amazon.com/api-gateway/pricing/)
- [Lambda pricing](https://aws.amazon.com/lambda/pricing/)
- [Kinesis Data Streams pricing](https://aws.amazon.com/kinesis/data-streams/pricing/)
- [Managed Flink billing](https://docs.aws.amazon.com/managed-flink/latest/java/how-pricing.html)
- [S3 pricing](https://aws.amazon.com/s3/pricing/)
- [Athena pricing](https://aws.amazon.com/athena/pricing/)
- [Redshift pricing](https://aws.amazon.com/redshift/pricing/)
- [Quick Sight pricing](https://aws.amazon.com/quick/quicksight/pricing/)

**Answer-key caveat:** The user's screenshot marks option D, but a streaming processor alone does not provide durable historical location retrieval. We record the ambiguity instead of silently substituting a new official answer.
