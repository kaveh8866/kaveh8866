# Q001 — Cost and Permissions Preflight

[فارسی](preflight.fa.md)

**STOP before deploying until every item is answered.** API Gateway, Lambda and CloudWatch may charge for API requests, compute duration and log storage. A free-plan label or credits are **not** universal guarantees; inspect your current account, AWS Pricing Calculator and official pricing pages: [API Gateway](https://aws.amazon.com/api-gateway/pricing/), [Lambda](https://aws.amazon.com/lambda/pricing/), [CloudWatch](https://aws.amazon.com/cloudwatch/pricing/).

## Checklist

- [ ] I know if my account is Free or Paid, its remaining credits and their expiration date.
- [ ] I reviewed pricing for this Region and checked that HTTP API, Lambda, IAM and CloudWatch are available in my account.
- [ ] I am using a **non-root** AWS principal/SSO session with MFA and suitable rights to create **and delete** only lab resources.
- [ ] I chose one Region and checked whether there are already resources with the planned `aws-micro-q001-*` names. I will not overwrite unrelated resources.
- [ ] I know I may need authorization to grant a caller `execute-api:Invoke`. My request will be signed with SigV4, no access keys committed.
- [ ] I will create **no** DynamoDB, Kinesis, Flink, Redshift, NAT Gateway, VPC endpoints or other additional billable services for this kit.
- [ ] I have decided a conservative **time limit** (e.g. 20 minutes of cloud execution) and a maximum number of requests (e.g. 5). These are behavioral limits, **not automated billing caps**.
- [ ] I have a cleanup plan and will verify deletion of API/stage, Lambda, its role/policies and any CloudWatch log groups.
- [ ] If this is not safely possible or account billing status is uncertain, I will use read-only console and offline tests.

**Expected experimental cloud spend:** Low for a handful of tiny requests in an eligible account, **not guaranteed zero**. Do not publish a fixed price or rely on credits without verifying eligibility. A disabled endpoint is safer than one relying only on throttling. CloudWatch retention is 1 day in Terraform but the log group should still be explicitly destroyed.

## Minimal policies concept

- **Lambda execution role**: trust `lambda.amazonaws.com` and permissions to write *its* logs, not broad access to data.
- **API caller identity**: `execute-api:Invoke` limited to one ARN such as `arn:aws:execute-api:REGION:ACCOUNT_ID:API_ID/$default/POST/locations`. Replace these placeholders with your **private** values; do not commit IDs.
- **Terraform operator**: separately needs rights to create/delete API Gateway v2, Lambda, IAM Role/Policy Attachment and CloudWatch Log Group. This is not the same as the API caller.

## Stop signals

Unexpected charge, missing permissions, public route without IAM, resources not clearly owned by this lab, or inability to run cleanup: **stop deployment or testing and resolve before proceeding**.
