# Q001 — All-services console discovery tour (NO-CREATE track)

[فارسی](service-tour.fa.md) · [Cost comparison](cost-comparison.en.md) · [Manual](manual.en.md)

**Purpose:** explore *every service appearing in the exam answer options and learner diagram*. The default pathway is **read-only**. Console labels vary by Region, permissions and AWS interface version. If the named menu is absent, find its equivalent in official AWS documentation—**never click a billing or resource-creation confirmation simply to continue this tour**.

## Checklist by service

### 1. API Gateway — appearing in B and D (8–10 minutes)
1. AWS Console → search **API Gateway** → open **APIs**.
2. Identify **HTTP APIs** versus **REST APIs**; inspect **Routes/Resources**, **Integrations**, **Stages**, **Authorization**, **Monitoring** and any available throttling settings for existing APIs.
3. With no existing API, open the **Create API** landing page to see the types, but **do not submit a Create/API wizard**.
4. Explain: the API receives HTTP requests and integrates with Lambda or other backends; it does not itself store location history.
**Optional active path:** [Q001 manual](manual.en.md) or [Terraform](../terraform/README.md) uses an IAM-protected API Gateway HTTP API.

### 2. AWS Lambda — appearing in B (5–8 minutes)
1. Search **Lambda** → **Functions**; if functions already exist, inspect (read-only) **Configuration → Permissions**, **Monitor**, **Runtime settings** and **Test**.
2. If none exist, examine **Create function** settings—runtime, architecture, execution role, memory, timeout—but **do not click Create function** until the cost/permission gate is complete.
3. Explain: Lambda runs code only when invoked and **requires another storage service** for a persistent location database.
**Optional active path:** the [manual kit](manual.en.md) runs one synthetic Lambda test and cleans up.

### 3. Amazon Kinesis Data Streams — in the learner's reference diagram (8–10 minutes)
1. Search **Kinesis** → **Data Streams**. Look for **Data streams**, current stream list and **stream details** on a stream you own (if any).
2. Inspect the creation form as a **preview only**: stream name, **on-demand versus provisioned capacity**, retention, encryption and tags. **Stop before Create data stream**.
3. Review, on an existing stream if authorized: **Monitoring**, **Data viewer**, **Configuration**, **Enhanced fan-out/consumers** (exact tabs vary). Do not change shard counts, mode, retention or consumers.
4. Think about the role of `PutRecord`, partition keys, temporary retention and downstream consumers.
**Why not provisioned in Q001:** on-demand Standard includes a **per-stream-hour** charge plus usage; provisioned mode charges for **shard-hours** and records. Creating an idle stream can still cost money. [Official pricing](https://aws.amazon.com/kinesis/data-streams/pricing/).

### 4. Amazon Managed Service for Apache Flink (formerly Kinesis Data Analytics) — in D (8–10 minutes)
1. Search **Managed Service for Apache Flink** (also search the older name **Kinesis Data Analytics**).
2. Inspect **Apache Flink applications** (or **Streaming applications**) and the **Create streaming application** setup *without submitting Create*.
3. Find application name, runtime/version, IAM role, code location, networking, parallelism, monitoring/checkpoints/metrics where shown.
4. **Do not click Create streaming application or Start application.** Some application creation workflows also create IAM and CloudWatch resources; a running application bills KPUs (minimum **10 minutes per start**) plus other storage charges.
5. Explain Flink's role as a stateful stream processor: a consumer of events, **not** a durable operational bike-location database. [AWS billing documentation](https://docs.aws.amazon.com/managed-flink/latest/java/how-pricing.html).

### 5. Amazon S3 — in A (3–5 minutes)
1. Search **S3** → **General purpose buckets**; if you own a test bucket, inspect **Objects**, **Properties**, **Permissions**, **Management** without changing them.
2. Preview **Create bucket**, but **do not complete it** for this Q001 discovery tour.
3. Explain S3 as durable object storage for analytic files, not a live REST ingestion system. Storage, requests and transfer have separate charges.

### 6. Amazon Athena — in A (3–5 minutes)
1. Search **Athena** → locate **Query editor**, **Data sources**, **Workgroups**, **Recent queries** as access allows.
2. **Do not run SQL**, create a workgroup, run a sample query or activate provisioned capacity in this tour.
3. Explain Athena as an analytic querying layer (often S3 data); on-demand SQL usually costs by **data scanned**, and query results can create S3 objects. [Pricing](https://aws.amazon.com/athena/pricing/).

### 7. Amazon Redshift — in C (3–5 minutes)
1. Search **Amazon Redshift** → find **Provisioned clusters**, **Redshift Serverless**, **Workgroups**, **Namespaces**, **Monitoring** or **Query editor**.
2. **Do not create a provisioned cluster, serverless workgroup, namespace or launch a query.** Even a short compute operation can incur charges; persistent storage/snapshots may remain.
3. Explain Redshift as analytic data warehousing, not a bike tracker REST API. [Pricing](https://aws.amazon.com/redshift/pricing/).

### 8. Amazon Quick Sight — named QuickSight in C (3–5 minutes)
1. Search **Amazon Quick** / **Quick Sight**. The older name **Amazon QuickSight** is now presented as **Amazon Quick Sight**, a BI feature of **Amazon Quick**.
2. If an account already has access, inspect **Dashboards**, **Analyses**, **Datasets**, **Data sources**, **Users/Manage** read-only.
3. **Do not select Sign up, Start trial, Create account, Add user, Buy, Subscribe or any confirmation** merely to view the interface: a subscription/account/user can be billable.
4. Explain Quick Sight as BI visualization, not an operational ingestion REST API. [AWS documentation](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html).

## Bonus: IAM + CloudWatch without creation

Search **IAM → Roles / Policies**, and **CloudWatch → Logs / Log groups / Metrics**. Observe the difference between a Lambda execution role and a caller permission to invoke an IAM-protected API. **Do not change permissions** or retention in read-only mode.

## Learning evidence (no cloud creation required)

- A table listing each service, its role, **one tab inspected** and **one button you deliberately did not press**.
- A hand-drawn diagram with the user's full streaming path (API Gateway → Kinesis Data Streams → Flink → analytics) clearly marked **reference / not deployed**.
- A different small lab diagram showing **API Gateway → Lambda → CloudWatch**, which is the optional deployable subset.
- Three written trade-offs about costs, persistence and real-time analytics.

**Read-only tour completion: zero resources intentionally created**; it does **not** establish what the actual account's billing might already be charging.
