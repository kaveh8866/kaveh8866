# Q001 — Terraform execution guide

[فارسی](README.fa.md) · [Kit](../README.md)

**Creates:** an AWS_IAM-protected HTTP API POST /locations, a 128 MB / 5 s Python Lambda, a log group with one-day retention, a Lambda IAM role and invoke integration. No database, Kinesis, Flink or VPC resources. **Not tested on a real AWS account.**

1. Complete [preflight](../docs/preflight.en.md) and choose your account, Region, cost limit, non-root identity and unique suffix. Inspect for existing resources; do not overwrite them.
2. Configure temporary AWS SSO/profile credentials. Keep state files secure and outside Git.
3. From the terraform directory:

```bash
terraform init
terraform fmt -check
terraform validate
terraform plan -out=q001.tfplan
terraform show q001.tfplan
# Only after reviewing all changes, costs and authorization:
terraform apply q001.tfplan
terraform output -raw api_url
```

4. Ensure Route authorization is `AWS_IAM`; caller also needs narrowly scoped `execute-api:Invoke` permission for this API's `$default/POST/locations` ARN. Do not enable anonymous access.
5. From this directory use:

```bash
python3 ../scripts/invoke_iam.py --region eu-central-1 --url "$(terraform output -raw api_url)"
python3 ../scripts/invoke_iam.py --region eu-central-1 --url "$(terraform output -raw api_url)" --invalid
```

Requires `boto3`, supported AWS credentials and correct Region. No secrets are printed by the script. Expect 202 on valid and 422 on invalid coordinates.
6. View Lambda and CloudWatch Logs; **then destroy using the same Terraform state**:

```bash
terraform plan -destroy
terraform destroy
terraform state list
```

Use [cleanup](../docs/cleanup.en.md) to verify console deletion of API, function, role and log group. Do not delete state before destroy. Throttling is best-effort, not a price cap. CI must never `terraform apply`.

**IAM trade-off:** AWS-managed `AWSLambdaBasicExecutionRole` grants broader logging permissions than a tightly scoped custom policy; callers still use separate IAM authorization. Document this difference in the ADR.

**No location storage:** Handler returns `stored=false`.
