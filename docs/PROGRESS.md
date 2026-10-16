# Lab Progress

**Source of truth:** `data/labs.json`. All statuses reflect manually verified evidence.

**Progress:** `0 / 16 published` · `0 / 16 AWS-tested`

| Week | Domain | Lab | Status | AWS tested |
| --- | --- | --- | --- | --- |
| 1 | D1 | [IAM Least Privilege](../labs/week-01-foundation/D1-L1-iam-least-privilege/README.md) | planned | No |
| 1 | D2 | [S3 Versioning and Object Recovery](../labs/week-01-foundation/D2-L1-s3-versioning-recovery/README.md) | planned | No |
| 1 | D3 | [S3 Request Patterns](../labs/week-01-foundation/D3-L1-s3-request-patterns/README.md) | planned | No |
| 1 | D4 | [Budgets and Storage Cost Drivers](../labs/week-01-foundation/D4-L1-budgets-and-cost-drivers/README.md) | planned | No |
| 2 | D1 | [Lambda Execution Role](../labs/week-02-builder/D1-L2-lambda-role/README.md) | planned | No |
| 2 | D2 | [Idempotent Event Processing](../labs/week-02-builder/D2-L2-idempotent-events/README.md) | planned | No |
| 2 | D3 | [Lambda and DynamoDB Latency](../labs/week-02-builder/D3-L2-lambda-dynamodb-latency/README.md) | planned | No |
| 2 | D4 | [Lambda versus EC2 Economics](../labs/week-02-builder/D4-L2-lambda-vs-ec2/README.md) | planned | No |
| 3 | D1 | [Queue-based Threat Model](../labs/week-03-architect/D1-L3-queue-threat-model/README.md) | planned | No |
| 3 | D2 | [SQS Dead-Letter and Recovery](../labs/week-03-architect/D2-L3-sqs-dlq-recovery/README.md) | planned | No |
| 3 | D3 | [Batch and Concurrency Tuning](../labs/week-03-architect/D3-L3-batch-concurrency/README.md) | planned | No |
| 3 | D4 | [Synchronous versus Asynchronous Cost](../labs/week-03-architect/D4-L3-sync-vs-async-cost/README.md) | planned | No |
| 4 | D1 | [Encryption and Threat Model Review](../labs/week-04-professional/D1-L4-encryption-review/README.md) | planned | No |
| 4 | D2 | [Multi-AZ Recovery Design](../labs/week-04-professional/D2-L4-rto-rpo-design/README.md) | planned | No |
| 4 | D3 | [Database and Caching Decisions](../labs/week-04-professional/D3-L4-database-caching/README.md) | planned | No |
| 4 | D4 | [Architecture Cost Scenarios](../labs/week-04-professional/D4-L4-architecture-cost-scenarios/README.md) | planned | No |

## How to update

After confirming evidence, edit `data/labs.json`, then run `python scripts/progress.py --write` and commit the updated Markdown.

A local test is not an AWS test. Do not switch `aws_tested` to true without an actual verified AWS run.
