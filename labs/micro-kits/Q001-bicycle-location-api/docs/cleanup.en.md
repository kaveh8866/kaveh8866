# Q001 — Verified Cleanup (English)

[فارسی](cleanup.fa.md) · [Preflight](preflight.en.md)

A lab is **not finished** until you confirm both execution **and resource removal**. No claim of "$0 spent" is justified without billing confirmation; usage records can lag.

## Path A — Manually created AWS resources

In the **same Region** used to create them:

1. **API Gateway → APIs:** identify **only** `aws-micro-q001-manual-http`. Delete its Stage and API. Verify the API is absent; check no custom domain, integration or API Gateway log group created by you remains.
2. **Lambda → Functions:** delete `aws-micro-q001-manual-receiver`. Verify the function is absent.
3. **CloudWatch → Logs → Log groups:** delete `/aws/lambda/aws-micro-q001-manual-receiver`. Confirm absence. Deleting Lambda **does not automatically guarantee** deleting its log group.
4. **IAM → Roles:** remove **only** the lab-specific execution role created for this Lambda (note its exact name from the creation step); detach the managed basic policy if necessary before deletion. Do not delete shared roles.
5. If you manually added `execute-api:Invoke` permission to your own IAM principal, remove only that lab-specific statement/policy.
6. Inspect **CloudWatch**, **API Gateway**, **Lambda**, and **IAM** again. Search by names and tags and note any missing permissions or residual resource.

## Path B — Terraform-managed AWS resources

From this kit's `terraform/` directory with the **same workspace/state, account and Region** used for `apply`:

```bash
terraform plan -destroy
terraform destroy
terraform state list
```

Expected: the Terraform state has no lab resources after destroy. **Do not erase the `.tfstate` file to "remove" cloud resources.** A missing state is a reason to stop and recover it, not to blindly re-apply or delete unrelated resources.

Then repeat an independent AWS console check:
- API Gateway: `aws-micro-q001-http` no longer exists.
- Lambda: `aws-micro-q001-receiver` no longer exists.
- CloudWatch: log group `/aws/lambda/aws-micro-q001-receiver` no longer exists.
- IAM: role `aws-micro-q001-lambda-role` no longer exists.
- Check Region is correct; compare other resources against original inventory.

**If some resources remain:** record exact names and errors privately, do not mark cleanup verified, and inspect ownership/state before taking targeted actions. If you have unexpected charges, inspect Billing/Cost Explorer after reporting delay and ask AWS Support if needed.

## Evidence to record (without secrets)

- Date, Region and **manual** or **Terraform** path.
- Sanitized HTTP results, local test results, confirmed names of removed services (redact account identifiers).
- Cleanup checklist complete? Yes / No; if No, what remains?
- Delayed billing follow-up done? Pending / Done.
- Optional sanitized screenshots (never publicize account number, URL signatures, identity data).

**Nothing in this repository performs automatic cleanup on your account. You must actually run the steps.**
