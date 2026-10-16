# Q001 — Manual AWS Console Lab (English)

[فارسی](manual.fa.md) · [Kit overview](../README.md) · [Preflight](preflight.en.md) · [Cleanup](cleanup.en.md)

**Goal:** Learn API Gateway → Lambda → CloudWatch with a synthetic GPS update. **No database, no real bicycle tracking, no permanent location storage.**

## 0. Select a safe execution mode

Before **any** cloud resource: finish [preflight](preflight.en.md), choose one Region (example `eu-central-1`), use a non-root identity with appropriate access, check your free-plan/credit status and determine whether this is affordable. If in doubt, choose **read-only console tour + local tests**.

**Important security rule:** Never deploy an unauthenticated public HTTP API route. In some API Gateway wizard flows a route is auto-deployed before you can enable `AWS_IAM`. **If you cannot guarantee IAM authorization before a Stage is accessible, do not complete the manual API deployment. Use the Terraform path instead.** A public URL is not automatically safe because it is temporary.

## 1. Read-only console tour (0 AWS resources)

1. Open **AWS Console**. Inspect the Region selector and select your Region.
2. Search **Amazon API Gateway** → locate **APIs**. Look at HTTP API vs REST API, **Routes**, **Integrations**, **Stages** and **Authorization**. HTTP APIs support Lambda proxies at lower feature complexity.
3. Search **AWS Lambda** → locate **Functions**, **Runtime**, **Configuration → Permissions**, **Monitoring**, and the Test interface.
4. Search **IAM** → locate **Roles**. Distinguish the Lambda **execution role** from the caller's `execute-api:Invoke` permission.
5. Search **Amazon CloudWatch** → find **Log groups**.
6. Optionally locate **Kinesis Data Streams**, **Managed Service for Apache Flink**, **S3**, **Athena**, **Redshift** and **QuickSight**, but **do not create** paid or persistent resources in this kit.
7. In your notes, write why API Gateway is the entry point and why Flink is not a storage database.

## 2. Start locally (0 AWS resources)

```bash
cd labs/micro-kits/Q001-bicycle-location-api
python3 -m unittest discover -s tests -v
```

Inspect `lambda/handler.py` and `examples/valid-event.json`. The handler expects **HTTP API payload v2** with `requestContext.http.method`, body containing `bike_id`, `latitude`, and `longitude`.

Expected:
- `POST` + valid synthetic coordinates → HTTP **202**, `accepted=true`, `stored=false`.
- Invalid JSON → **400**.
- Missing/invalid GPS fields → **422**.
- Wrong method → **405**.

## 3. Create and test Lambda manually (optional, billable depending on account)

1. AWS Console → **Lambda → Create function → Author from scratch**.
2. Name: `aws-micro-q001-manual-receiver`, Runtime: a supported **Python 3.x** runtime compatible with the handler; Architecture: default.
3. Under execution permissions create a **new basic Lambda role**; use no admin/full-access role.
4. Create function; in **Code** replace the file with the contents of `lambda/handler.py` (handler name must be `handler.lambda_handler`). Click **Deploy** inside the Lambda editor.
5. Set **Memory** to 128 MB, **Timeout** to 5 seconds if available; add project/lab tags if offered.
6. **Test** → create a test event from `examples/valid-event.json` → **Test**. Check the response status 202 and `stored=false`.
7. Test `examples/invalid-event.json` → expect 422.
8. **Monitor → View CloudWatch logs** → find log group `/aws/lambda/aws-micro-q001-manual-receiver`. Confirm invocation metadata appears. Avoid logging location values; only synthetic data is used.
9. Configure one-day retention on the log group if it exists, if supported; otherwise remove it at cleanup. Note function name and execution role name in private notes.

**Stop here** if the account restricts API Gateway, IAM policy setup or any cost/permission requirement. You have already learned Lambda, IAM and logs.

## 4. Optional secured HTTP API through the console

**Only continue if the console supports setting IAM authorization on the route BEFORE first deployment.** When uncertain, use the [Terraform lab](../terraform/README.md), which creates the route with `AWS_IAM` before the auto-deployed stage.

1. **API Gateway → Create API → HTTP API**. Use a name like `aws-micro-q001-manual-http`.
2. Attach the Lambda function as the integration; choose an exact route **`POST /locations`**. Do not create an `ANY /{proxy+}` route.
3. Keep auto-deployment **OFF**, or do not create/enable an externally reachable Stage while the route is unauthenticated. If the wizard will expose it first, **cancel and choose Terraform**.
4. Open **Routes → POST /locations → Authorization**. Set **AWS_IAM** and save. Double-check the route reads **AWS_IAM**.
5. Add/deploy a short-lived Stage such as `lab` only after authorization is verified. If needed, add Lambda invoke permissions for this API Gateway integration as directed by the console.
6. In **Stages**, inspect the Stage invoke URL, throttling options (target 1 request/second, burst 2) and automatic deployment state. Rate limits are best-effort, **not cost guarantees**.
7. For the invoking principal, arrange a narrowly scoped IAM permission: `execute-api:Invoke` for **this API/Stage/POST/locations**. If you lack permission to grant it, stop and ask the account administrator; do not broaden access or use root.
8. Use the `scripts/invoke_iam.py` client from a local terminal with existing AWS profile/SSO credentials, the exact invocation URL ending in `/locations`, and your Region. For example:

```bash
python3 -m pip install --user boto3  # if not already installed
python3 scripts/invoke_iam.py --url "https://YOUR_API_ID.execute-api.eu-central-1.amazonaws.com/lab/locations" --region eu-central-1
```

**Never paste access keys into code.** The script obtains temporary/profile credentials with Boto3, signs with SigV4, sends only synthetic example GPS, and prints HTTP status/response.

9. Expected status: 202 for authorized valid input. An unsigned request should fail with 401/403; **do not run load tests**. An authorization error may also mean that your IAM principal lacks `execute-api:Invoke`.
10. Inspect **Lambda → Monitor** and **CloudWatch Logs**, then immediately start cleanup. No data store has been created.

**Manual Stage URL** usually includes `/lab/locations`; Terraform uses the `$default` Stage so it uses `/locations` without `/lab`.

## 5. Draw.io exercise — learner owns the final diagram

Follow [Draw.io worksheet](drawio.en.md); draw the components and arrows yourself. Mark the API authorization boundary, Lambda execution role, logs and **no persistence**. Do not confuse CloudWatch Logs with a location history datastore.

## 6. Document and clean up

Follow [manual cleanup](cleanup.en.md). Check **API Gateway, Lambda, IAM Roles, CloudWatch log groups**, and any resources you added manually in the selected Region. Record *observed*, not imagined, outputs in [record](record.en.md).

**Completion criterion:** experiment outcome recorded + independent console verification of cleanup. If you did only local tests, label the work `local-tested`, not `aws-tested`.
