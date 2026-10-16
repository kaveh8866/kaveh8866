# کیت آزمایش آموزشی ۰۰۱ — API موقعیت دوچرخه

[English](README.md) | **فارسی** · **استاندارد کیت:** ۱.۰ · **وضعیت:** آماده اجرا؛ **هنوز روی AWS آزمایش نشده** · **آزمون:** SAA-C03

**زمان پیشنهادی:** ۳۵ تا ۶۰ دقیقه پس از آماده‌سازی (بسته به دسترسی) · **منابع ابری:** اختیاری و موقت · **منطقه:** انتخاب کاربر

## هدف

یاد می‌گیریم **API Gateway، Lambda، IAM و CloudWatch** کجای کنسول AWS هستند، چه کاری انجام می‌دهند، چگونه یک پیام موقعیت ساختگی دریافت می‌کنند و چگونه **همه منابع آزمایشی را امن حذف کنیم**. این یک کیت ماندگار است، نه نرم‌افزار کامل ردیابی دوچرخه.

### صورت مسئله (بازنویسی آموزشی)

یک شرکت اشتراک دوچرخه در ساعت‌های شلوغ موقعیت دوچرخه‌ها را دریافت می‌کند. داده‌ها باید از طریق رابط REST قابل استفاده باشند و به سامانه تحلیل موجود برسند. گزینه‌ها شامل **Athena + S3**، **API Gateway + Lambda**، **QuickSight + Redshift** و **API Gateway + Kinesis Data Analytics (نام کنونی: Managed Service for Apache Flink)** هستند. در تصویر سؤال **D** سبز شده، اما این به‌تنهایی اثبات صحیح‌بودن پاسخ نیست.

**نکته معماری:** API Gateway و Lambda برای دریافت و پردازش درخواست‌اند؛ بدون پایگاه داده، ذخیره‌سازی پایدار و بازیابی تاریخچه فراهم نمی‌کنند. Flink پردازش جریان داده را انجام می‌دهد، نه نقش یک پایگاه داده عملیاتی را. در معماری کامل به ذخیره‌ساز و احتمالاً مسیر تحلیلی نیاز است؛ برای کوتاه و کم‌هزینه ماندن آزمایش، آن‌ها را عمداً حذف کرده‌ایم.

> **آنچه این کیت ثابت می‌کند:** یک HTTP API با مجوز IAM درخواست امضاشده POST را به Lambda می‌رساند؛ تابع مختصات ساختگی را اعتبارسنجی می‌کند و پاسخ می‌دهد. **هیچ موقعیتی ذخیره نمی‌شود و هیچ فرد یا دوچرخه واقعی ردیابی نمی‌شود.**

## اهداف یادگیری

- شناسایی HTTP API، مسیرها، Stage، Integration و IAM Authorization در API Gateway.
- آشنایی با Handler، نقش اجرایی Lambda، اجرای تابع و CloudWatch Logs.
- ارسال درخواست امضاشده به `POST /locations` و بررسی پاسخ‌های ۲۰۲، ۴۰۰/۴۲۲ و ۴۰۳.
- طراحی شخصی دیاگرام در Draw.io همراه با مرز امنیت و نبود ذخیره‌سازی.
- اجرای تست محلی، ساخت اختیاری با Terraform و **تأیید پاک‌شدن منابع**.

## محتویات کیت

| بخش | فارسی | English |
| --- | --- | --- |
| راهنمای کامل آزمایش | [راهنمای دستی](docs/manual.fa.md) | [Manual](docs/manual.en.md) |
| پیش‌بررسی مجوز و هزینه | [پیش‌بررسی](docs/preflight.fa.md) | [Preflight](docs/preflight.en.md) |
| تمرین Draw.io | [طراحی دیاگرام](docs/drawio.fa.md) | [Draw.io](docs/drawio.en.md) |
| حذف امن منابع | [پاک‌سازی](docs/cleanup.fa.md) | [Cleanup](docs/cleanup.en.md) |
| منطق تصمیم معماری | [تصمیم معماری](docs/decision.fa.md) | [ADR](docs/decision.en.md) |
| گزارش واقعی کاربر | [ثبت نتایج](docs/record.fa.md) | [Record](docs/record.en.md) |

**فایل‌های قابل اجرا:** [تابع Python](lambda/handler.py) · [تست‌های آفلاین](tests/test_handler.py) · [رویدادهای نمونه](examples/) · [Terraform](terraform/) · [کلاینت امضای IAM](scripts/invoke_iam.py).

## سه مسیر اجرای اختیاری

**الف — کنسول AWS:** مراحل دستی را دنبال کن؛ Lambda را تست کن و تنها زمانی API را منتشر کن که تنظیم IAM روی Route **پیش از انتشار Stage** بررسی شده باشد. اگر کنسول مسیر بدون احراز مجوز را خودکار منتشر می‌کند، **متوقف شو** و برای API از Terraform استفاده کن.

**ب — Terraform:** در پوشه `terraform/` دستورهای `terraform init`، `terraform plan`، بررسی منابع و هزینه، سپس `terraform apply` را اجرا کن. با اسکریپت درخواست امضاشده را تست کن و در پایان `terraform destroy` را اجرا کن. منابع یکسان را هم‌زمان با Terraform و کنسول مدیریت نکن.

**پ — شناخت بدون هزینه ابری:** فقط محیط کنسول را مشاهده کن و تست Python را محلی اجرا کن؛ هیچ منبعی ایجاد نمی‌شود.

## اجرای سریع تست محلی

```bash
cd labs/micro-kits/Q001-bicycle-location-api
python3 -m unittest discover -s tests -v
```

**قاعده شواهد:** تا پیش از آزمایش واقعی، فایل‌های گزارش انگلیسی و فارسی خالی از نتیجه‌اند. انتشار کیت به معنی اجرای موفق در Cloud نیست. پس از اجرا منطقه، نتایج بدون اطلاعات حساس، هزینه، تأیید حذف و دیاگرام خودت را اضافه کن.

**امنیت:** مسیر API با `AWS_IAM` محافظت می‌شود و درخواست SigV4 لازم دارد. کلید دائمی در کد قرار نمی‌دهیم. محدودسازی نرخ درخواست تضمین سقف هزینه نیست. اعتبار و سهمیه رایگان AWS به حساب بستگی دارد.

## منابع رسمی

- [معرفی HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html)
- [مجوز IAM در HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control-iam.html)
- [نسخه دوم رویداد Lambda](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)
- [لاگ‌های Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-loggroups.html)
- [قیمت API Gateway](https://aws.amazon.com/api-gateway/pricing/)

**این کیت وابسته به AWS یا مورد تأیید رسمی آن نیست.** متن سؤال برای آموزش بازنویسی شده است.
