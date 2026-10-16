<div dir="rtl" align="right">

# سؤال ۰۰۱ — راهنمای اجرای Terraform

[English](README.md) · [کیت](../README.fa.md)

**می‌سازد:** یک HTTP API با `AWS_IAM` و مسیر `POST /locations`، Lambda پایتون با ۱۲۸ مگابایت/۵ ثانیه، گروه لاگ با نگهداری یک‌روزه، نقش IAM برای Lambda و Integration. دیتابیس، Kinesis، Flink و منابع VPC ایجاد نمی‌شوند. **هنوز در حساب واقعی AWS آزمایش نشده است.**

۱. [پیش‌بررسی](../docs/preflight.fa.md) را انجام بده؛ حساب، Region، هزینه، هویت غیر Root و پسوند نام یکتا را انتخاب و منابع موجود را بررسی کن.
۲. از نشست موقت SSO یا AWS Profile استفاده کن. State را امن و خارج از Git نگه دار.
۳. در پوشه Terraform اجرا کن:


<pre dir="ltr" align="left"><code>terraform init
terraform fmt -check
terraform validate
terraform plan -out=q001.tfplan
terraform show q001.tfplan
# فقط پس از بررسی هزینه، مجوز و تغییرات:
terraform apply q001.tfplan
terraform output -raw api_url</code></pre>


۴. مجوز Route باید `AWS_IAM` باشد. فراخواننده نیز برای `$default/POST/locations` همین API به مجوز محدود `execute-api:Invoke` احتیاج دارد. دسترسی ناشناس فعال نکن.
۵. با `boto3` و نشست AWS معتبر (Region درست) از همین پوشه اجرا کن:


<pre dir="ltr" align="left"><code>python3 ../scripts/invoke_iam.py --region eu-central-1 --url "$(terraform output -raw api_url)"
python3 ../scripts/invoke_iam.py --region eu-central-1 --url "$(terraform output -raw api_url)" --invalid</code></pre>


اسکریپت کلیدها را نشان نمی‌دهد؛ برای داده صحیح ۲۰۲ و برای مختصات نادرست ۴۲۲ انتظار داریم.
۶. نتیجه Lambda و CloudWatch را ببین و **با همان State** منابع را حذف کن:


<pre dir="ltr" align="left"><code>terraform plan -destroy
terraform destroy
terraform state list</code></pre>


طبق [چک‌لیست حذف](../docs/cleanup.fa.md)، نبود API، تابع، نقش و Log Group را در کنسول هم تأیید کن. State را قبل از Destroy پاک نکن. Throttling سقف قطعی هزینه نیست. در CI هرگز `terraform apply` اجرا نشود.

**Trade-off امنیتی:** Policy آماده `AWSLambdaBasicExecutionRole` دسترسی لاگ وسیع‌تری از Policy سفارشی محدود دارد؛ اما فراخواننده API مجوز IAM جداگانه می‌خواهد. این تفاوت را در ADR بنویس.

**ذخیره‌سازی نداریم:** Handler مقدار `stored=false` برمی‌گرداند.

</div>
