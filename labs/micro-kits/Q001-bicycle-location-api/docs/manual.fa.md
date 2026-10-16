# سؤال ۰۰۱ — راهنمای اجرای دستی در کنسول AWS

[English](manual.en.md) · [معرفی کیت](../README.fa.md) · [پیش‌بررسی](preflight.fa.md) · [پاک‌سازی](cleanup.fa.md)

**هدف:** شناخت ارتباط API Gateway ← Lambda ← CloudWatch با یک پیام GPS ساختگی. **بدون دیتابیس، بدون ردیابی واقعی، بدون ذخیره دائمی موقعیت.**

## ۰. انتخاب مسیر امن

پیش از ایجاد **هر منبع**، [پیش‌بررسی](preflight.fa.md) را کامل کن، یک Region واحد انتخاب کن (مثلاً `eu-central-1`)، با هویت غیر Root کار کن، وضعیت اعتبار/پلن رایگان حساب و هزینه احتمالی را بررسی کن. در صورت تردید، **بازدید فقط‌خواندنی از کنسول + تست محلی** را انتخاب کن.

**قاعده امنیتی:** هیچ مسیر HTTP API بدون احراز مجوز منتشر نشود. بعضی مراحل ساخت API در کنسول ممکن است Route را قبل از فعال‌کردن `AWS_IAM` خودکار منتشر کنند. **اگر نمی‌توانی پیش از قابل‌دسترسی‌شدن Stage مجوز IAM را تضمین کنی، انتشار دستی API را متوقف کن و مسیر Terraform را انتخاب کن.** موقت‌بودن آدرس به معنی امن‌بودن آن نیست.

## ۱. گردش فقط‌خواندنی در کنسول (بدون منابع ابری)

1. وارد **AWS Console** شو. انتخاب‌گر Region را پیدا کن و یک Region انتخاب کن.
2. سرویس **Amazon API Gateway** را جست‌وجو کن؛ در بخش **APIs** تفاوت HTTP API و REST API و قسمت‌های **Routes**، **Integrations**، **Stages** و **Authorization** را ببین.
3. وارد **AWS Lambda** شو؛ بخش‌های **Functions**، **Runtime**، **Configuration → Permissions**، **Monitoring** و **Test** را بررسی کن.
4. وارد **IAM → Roles** شو. نقش اجرایی Lambda را با مجوز `execute-api:Invoke` متعلق به کاربر فراخواننده اشتباه نگیر.
5. در **Amazon CloudWatch** بخش **Log groups** را پیدا کن.
6. در صورت تمایل صرفاً سرویس‌های **Kinesis Data Streams، Managed Service for Apache Flink، S3، Athena، Redshift و QuickSight** را پیدا کن؛ در این کیت هیچ منبع پرهزینه‌ای در آن‌ها ایجاد نکن.
7. یادداشت کن چرا API Gateway ورودی درخواست است و چرا Flink یک پایگاه داده ذخیره‌سازی نیست.

## ۲. تست محلی اولیه (بدون AWS)

```bash
cd labs/micro-kits/Q001-bicycle-location-api
python3 -m unittest discover -s tests -v
```

فایل‌های `lambda/handler.py` و `examples/valid-event.json` را بررسی کن. تابع از ساختار رویداد **HTTP API نسخه ۲** استفاده می‌کند و بدنه شامل `bike_id`، `latitude` و `longitude` است.

خروجی مورد انتظار:
- `POST` با مختصات ساختگی معتبر → **202**، `accepted=true`، `stored=false`.
- JSON نامعتبر → **400**.
- داده گمشده یا مختصات نامعتبر → **422**.
- متد اشتباه → **405**.

## ۳. ساخت و تست دستی Lambda (اختیاری؛ احتمال هزینه بسته به حساب)

1. مسیر **Lambda → Create function → Author from scratch**.
2. نام تابع: `aws-micro-q001-manual-receiver`؛ Runtime: یک نسخه پشتیبانی‌شده **Python 3.x** سازگار با کد؛ معماری پیش‌فرض.
3. در Execution permissions یک **نقش اجرایی پایه جدید** بساز؛ نقش Administrator یا Full Access استفاده نکن.
4. در بخش Code محتوای `lambda/handler.py` را وارد کن. نام Handler باید `handler.lambda_handler` باشد. روی **Deploy** در ویرایشگر Lambda بزن.
5. Memory را در صورت امکان 128 MB و Timeout را 5 ثانیه قرار بده؛ تگ پروژه و شماره کیت را هم ثبت کن.
6. از **Test** رویداد `examples/valid-event.json` را وارد کن و اجرا بگیر؛ انتظار 202 و `stored=false` داریم.
7. رویداد `examples/invalid-event.json` را اجرا کن؛ انتظار 422 داریم.
8. از **Monitor → View CloudWatch logs** گروه `/aws/lambda/aws-micro-q001-manual-receiver` را بررسی کن. باید اثر اجرای Lambda را ببینی. داده واقعی و مختصات را لاگ نکن.
9. اگر گروه لاگ ایجاد شده است و امکان دارد، Retention را یک روز قرار بده؛ وگرنه در پایان آن را حذف کن. نام نقش اجرایی و تابع را در یادداشت شخصی حفظ کن.

اگر مجوز یا وضعیت مالی برای API Gateway روشن نیست، **همین‌جا متوقف شو**. تا اینجا Lambda، IAM و لاگ‌ها را شناخته‌ای.

## ۴. مسیر اختیاری ساخت HTTP API امن با کنسول

**فقط وقتی ادامه بده که کنسول اجازه دهد IAM قبل از اولین انتشار Stage تنظیم شود.** در غیر این صورت از [مسیر Terraform](../terraform/README.md) استفاده کن؛ آن مسیر ابتدا Route امن می‌سازد.

1. در **API Gateway → Create API → HTTP API** نامی مانند `aws-micro-q001-manual-http` انتخاب کن.
2. Lambda ساخته‌شده را Integration کن و فقط Route **`POST /locations`** را بساز. از Route عمومی `ANY /{proxy+}` استفاده نکن.
3. Auto-deployment را **غیرفعال** نگه دار یا تا پیش از امن‌شدن Route هیچ Stage قابل‌فراخوانی نساز. اگر Wizard ابتدا آدرس عمومی ایجاد می‌کند، **لغو کن و به Terraform برو**.
4. در **Routes → POST /locations → Authorization** گزینه **AWS_IAM** را فعال و ذخیره کن. دوباره مقدار Authorization را بخوان.
5. تنها پس از تأیید IAM یک Stage موقت مثل `lab` بساز و Deploy کن. اگر کنسول درخواست کرد، به API Gateway اجازه فراخوانی Lambda بده.
6. در **Stages** آدرس فراخوانی، تنظیمات محدودکردن نرخ (هدف ۱ درخواست در ثانیه، Burst برابر ۲) و Auto-deployment را بررسی کن. Throttling سقف قطعی هزینه نیست.
7. هویت فراخواننده باید فقط برای همین API/Stage/Route مجوز `execute-api:Invoke` داشته باشد. اگر اجازه تنظیم آن را نداری، با مدیر حساب هماهنگ کن؛ دسترسی را گسترده یا Root استفاده نکن.
8. با AWS profile یا نشست SSO معتبر و کلاینت امضای IAM درخواست بفرست:

```bash
python3 -m pip install --user boto3  # در صورت نیاز
python3 scripts/invoke_iam.py --url "https://YOUR_API_ID.execute-api.eu-central-1.amazonaws.com/lab/locations" --region eu-central-1
```

**کلیدها را در کد قرار نده.** اسکریپت از اعتبارنامه موقت/پروفایل استفاده می‌کند، با SigV4 امضا می‌کند و فقط داده ساختگی ارسال می‌کند.

9. برای درخواست امضاشده مجاز انتظار 202 داریم. درخواست بدون امضا باید 401/403 شود؛ **تست بار انجام نده**. خطای احراز مجوز ممکن است ناشی از نداشتن `execute-api:Invoke` باشد.
10. در **Lambda → Monitor** و **CloudWatch Logs** نتایج اجرا را ببین و فوراً پاک‌سازی را شروع کن. دیتابیسی وجود ندارد.

**تفاوت آدرس:** Stage دستی `lab` معمولاً آدرس `/lab/locations` دارد؛ در Terraform از `$default` استفاده می‌شود و انتهای آدرس `/locations` خواهد بود.

## ۵. Draw.io — نمودار را خودت می‌کشی

[برگه تمرین دیاگرام](drawio.fa.md) را دنبال کن؛ اجزا، پیکان‌ها و مرزهای اعتماد را خودت رسم کن. نقش اجرایی Lambda، CloudWatch و **نبود ذخیره‌سازی پایدار** را نشان بده. CloudWatch Logs پایگاه داده تاریخچه موقعیت نیست.

## ۶. ثبت و پاک‌سازی

طبق [راهنمای پاک‌سازی](cleanup.fa.md)، API Gateway، Lambda، IAM Roles، CloudWatch Log groups و هر منبع دستی اضافه‌شده را در همان Region بررسی کن. نتایج **مشاهده‌شده** را در [فرم ثبت](record.fa.md) بنویس.

**شرط پایان:** ثبت نتیجه واقعی و تأیید مستقل حذف منابع در کنسول. اگر فقط تست محلی انجام دادی وضعیت `local-tested` است، نه `aws-tested`.
