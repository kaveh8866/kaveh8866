# ADR-Q001 — API ingress versus stream processing and durable storage

[فارسی](decision.fa.md) · **Status: Educational decision (not a production design)**

## Context

Paraphrased question: a bicycle-sharing fleet needs location updates at peak times, analytics integration and retrieval through a RESTful interface. Options: Athena + S3; API Gateway + Lambda; QuickSight + Redshift; API Gateway + Kinesis Data Analytics (now Amazon Managed Service for Apache Flink). Screenshot marks D but **a highlighted answer is not independent verification**.

## Decisions and boundaries

1. **For a minimal ingress lab:** choose **API Gateway HTTP API + AWS Lambda**. This teaches routing, input validation, integration, IAM and logging.
2. **No durable storage:** the response says `stored=false`; historical retrieval is **not implemented**. CloudWatch execution logs are not the business location database.
3. **Production design alternatives:** introduce DynamoDB (or another fitting database) for reads/writes; optionally Kinesis Data Streams and Managed Service for Apache Flink for high-volume streaming analytics, plus an analytics sink. Those services are **not provisioned**.
4. **Exam ambiguity:** No option clearly provides all of REST ingress, durable storage and immediate historical retrieval alone. Option D's Flink engine is not a durable operational datastore; option B lacks persistent storage. Discuss and verify the original source rather than claiming official exam certainty.

## Why other options do not solve the same interface

- **Athena + S3**: analytics over stored objects, not a ready-made transactional update API.
- **QuickSight + Redshift**: BI/warehouse, not a GPS ingestion REST endpoint.
- **API Gateway + Managed Service for Apache Flink**: API layer plus stream processor, but requires a suitable stream source and output sink; no location history database is implied.
- **API Gateway + Lambda**: fit for entry and transformation; still needs storage for the complete use case.

## Testable acceptance

Signed request → HTTP 202; invalid JSON → 400; invalid coordinate → 422; unsigned route request → 401/403; no stored location anywhere in the kit. Cleanup verifies no lab resources remain.

## Caveats

This lab is intentionally not a full bicycle solution. HTTP API supports REST-like operations but differs in features/pricing from API Gateway REST API. The AWS examination domain most closely involved is D3 (high-performing architectures), with D1/D2/D4 secondary trade-offs. No performance, scale or storage capability can be inferred from this tiny test.

## Official references

- https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html
- https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control-iam.html
- https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html
- https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html
