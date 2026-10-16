<div dir="rtl" align="right">

# سؤال ۰۰۱ — گردش آموزشی در تمام سرویس‌ها (بدون ساخت منابع)

[English](service-tour.en.md) · [مقایسه هزینه](cost-comparison.fa.md) · [راهنمای دستی](manual.fa.md)

**هدف:** هیچ‌یک از سرویس‌های گزینه‌های سؤال یا نموداری که خودت کشیده‌ای حذف نمی‌شود. مسیر پیش‌فرض **فقط مشاهده** است. نام تب‌ها ممکن است با Region، مجوز یا نسخه کنسول تغییر کند. اگر بخشی را ندیدی، به مستندات رسمی مراجعه کن؛ **برای ادامه آموزش لازم نیست دکمه نهایی ایجاد منبع یا تأیید اشتراک را بزنی.**

## چک‌لیست گردش در سرویس‌ها

### ۱. API Gateway — گزینه‌های B و D (۸ تا ۱۰ دقیقه)
۱. از کنسول AWS نام **API Gateway** را جست‌وجو کن و وارد **APIs** شو.
۲. تفاوت **HTTP API** و **REST API** و بخش‌های **Routes/Resources**، **Integrations**، **Stages**، **Authorization**، **Monitoring** و تنظیمات محدودسازی درخواست را پیدا کن؛ اگر API قبلی متعلق به خودت داری، فقط بخوان.
۳. اگر API نداری، صفحه **Create API** را برای شناخت انواع API ببین اما **ایجاد را تا انتها تأیید نکن**.
۴. با زبان خودت توضیح بده چرا API Gateway درخواست HTTP را می‌گیرد ولی به‌تنهایی تاریخچه موقعیت را ذخیره نمی‌کند.

**مسیر عملی اختیاری:** در [کیت کوچک](manual.fa.md) یا [Terraform](../terraform/README.fa.md)، API امن با مجوز IAM و Lambda اجرا می‌شود.

### ۲. AWS Lambda — گزینه B (۵ تا ۸ دقیقه)
۱. سرویس **Lambda → Functions** را باز کن. اگر تابع متعلق به خودت موجود است، قسمت‌های **Configuration → Permissions**، **Monitor**، **Runtime settings** و **Test** را بدون تغییر بررسی کن.
۲. در نبود تابع، فرم **Create function** را تا مرحله تنظیم Runtime، معماری پردازنده، Execution role، Memory و Timeout بررسی کن؛ **تا تکمیل پیش‌بررسی، دکمه Create function را نزن**.
۳. توضیح بده که Lambda کد را اجرا می‌کند؛ برای نگهداری دائمی موقعیت‌ها، دیتابیس دیگری لازم است.

**مسیر عملی اختیاری:** [راهنمای ساخت و تست Lambda](manual.fa.md) و پاک‌سازی فوری.

### ۳. Kinesis Data Streams — در دیاگرام خودت (۸ تا ۱۰ دقیقه)
۱. **Kinesis → Data Streams** را جست‌وجو کن؛ فهرست **Data streams** و در صورت وجود Stream متعلق به خودت، **Stream details** را ببین.
۲. فرم **Create data stream** را فقط بررسی کن: نام، ظرفیت **On-demand / Provisioned**، Retention، Encryption و Tags. **قبل از Create data stream متوقف شو**.
۳. برای Stream موجود و با دسترسی مجاز، بخش‌های **Monitoring**، **Data viewer**، **Configuration** و Consumerها را ببین؛ Shard، ظرفیت، نگهداری یا Consumer را تغییر نده.
۴. کاربرد **PutRecord**، **Partition key**، نگهداری موقت و Consumer پایین‌دستی را برای خودت توضیح بده.

**چرا در آزمایش کوچک اجرا نمی‌شود؟** حالت On-demand Standard علاوه بر مصرف، هزینه **ساعتی هر Stream** دارد؛ حالت Provisioned هم بابت **Shard-hour** و رکوردها هزینه دارد. بنابراین Stream بی‌استفاده نیز می‌تواند هزینه بسازد. [تعرفه رسمی AWS](https://aws.amazon.com/kinesis/data-streams/pricing/).

### ۴. Managed Service for Apache Flink — نام جدید Kinesis Data Analytics در گزینه D (۸ تا ۱۰ دقیقه)
۱. سرویس **Managed Service for Apache Flink** را جست‌وجو کن؛ نام قدیمی **Kinesis Data Analytics** را هم بشناس.
۲. بخش **Apache Flink applications / Streaming applications** و فرم **Create streaming application** را فقط بازدید کن.
۳. **Application name**، نسخه Flink، نقش IAM، مسیر کد برنامه، شبکه، تنظیمات Parallelism و گزینه‌های Monitoring / Checkpoint را در صورت وجود بررسی کن.
۴. **دکمه Create streaming application یا Start application را نزن.** بعضی مسیرهای ایجاد برنامه، IAM و CloudWatch هم می‌سازند. برنامه در حال اجرا بر اساس KPU هزینه دارد و برای هر شروع، حداقل **۱۰ دقیقه** محاسبه می‌شود؛ ذخیره‌سازی هم ممکن است هزینه داشته باشد.
۵. توضیح بده Flink چرا یک پردازشگر جریان است، نه دیتابیس دائمی بازیابی موقعیت دوچرخه. [مستندات هزینه](https://docs.aws.amazon.com/managed-flink/latest/java/how-pricing.html).

### ۵. Amazon S3 — گزینه A (۳ تا ۵ دقیقه)
۱. وارد **S3 → General purpose buckets** شو؛ در یک باکت متعلق به خودت می‌توانی **Objects**، **Properties**، **Permissions** و **Management** را فقط بخوانی.
۲. اگر باکت نداری، صفحه **Create bucket** را برای شناخت تنظیمات ببین، ولی **ساخت را کامل نکن**.
۳. توضیح بده S3 برای فایل و آبجکت‌های ماندگار است، اما به‌تنهایی API ثبت زنده GPS نیست. نگهداری، درخواست و انتقال داده هزینه‌های جدا دارند.

### ۶. Amazon Athena — گزینه A (۳ تا ۵ دقیقه)
۱. در **Athena** بخش‌های **Query editor**، **Data sources**، **Workgroups** و **Recent queries** را تا حد دسترسی بررسی کن.
۲. **SQL اجرا نکن، Workgroup نساز و ظرفیت رزرو نکن**.
۳. Athena برای پرس‌وجوی تحلیلی است؛ در مدل معمول SQL هزینه به **حجم داده اسکن‌شده** بستگی دارد و نتایج Query ممکن است در S3 آبجکت ایجاد کنند. [قیمت](https://aws.amazon.com/athena/pricing/).

### ۷. Amazon Redshift — گزینه C (۳ تا ۵ دقیقه)
۱. بخش‌های **Provisioned clusters**، **Redshift Serverless**، **Workgroups**، **Namespaces**، **Monitoring** یا **Query editor** را پیدا کن.
۲. **Cluster، Workgroup یا Namespace نساز و Query را اجرا نکن.** حتی اجرای کوتاه Compute ممکن است هزینه داشته باشد و Storage/Snapshot باقی بماند.
۳. Redshift انبار داده تحلیلی است، نه API عملیاتی دریافت GPS. [تعرفه](https://aws.amazon.com/redshift/pricing/).

### ۸. Amazon Quick Sight — نام قدیمی QuickSight در گزینه C (۳ تا ۵ دقیقه)
۱. **Amazon Quick / Quick Sight** را جست‌وجو کن. نام قدیمی **Amazon QuickSight** اکنون به قابلیت BI با عنوان **Amazon Quick Sight** در خانواده **Amazon Quick** تبدیل شده است.
۲. اگر قبلاً دسترسی داری، **Dashboards**، **Analyses**، **Datasets**، **Data sources** و بخش مدیریت را فقط ببین.
۳. **Sign up، Start trial، Create account، Add user، Buy یا Subscribe را صرفاً برای مشاهده تأیید نکن**؛ ساخت حساب یا اشتراک می‌تواند هزینه داشته باشد.
۴. Quick Sight ابزار تجسم و گزارش است، نه API دریافت GPS. [مستندات AWS](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html).

## بخش تکمیلی: IAM و CloudWatch

از **IAM → Roles / Policies** و **CloudWatch → Logs / Log groups / Metrics** بازدید کن. مجوز فراخوانی API و نقش اجرایی Lambda دو موضوع متفاوت‌اند. در مسیر فقط‌خواندنی هیچ Policy یا Log Retention را تغییر نده.

## خروجی این گردش بدون هزینه ایجاد منابع

- برای هر سرویس یک **تب مشاهده‌شده** و یک **دکمه‌ای که عمداً نزدی** ثبت کن.
- دیاگرام کامل خودت را با مسیر **API Gateway → Kinesis Data Streams → Flink → Analytics** به عنوان **معماری مرجع / اجرا‌نشده** نگه دار.
- دیاگرام کوچک دوم را با **API Gateway → Lambda → CloudWatch** به عنوان زیرمجموعه اختیاری آزمایش‌پذیر مشخص کن.
- سه تفاوت درباره هزینه، ماندگاری داده و تحلیل لحظه‌ای را با زبان خودت بنویس.

**پایان گردش فقط‌خواندنی به معنی ایجادنشدن منابع توسط این کیت است؛ درباره هزینه سایر منابع موجود در حساب، ادعایی نمی‌کند.**

</div>
