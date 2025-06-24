# 📰 تطبيق الأخبار الفكاهية باستخدام الذكاء الاصطناعي – للنشر على Render

هذا المشروع يعرض خبرًا من موقع إخباري، ويترجمه للعربية، ثم يعيد صياغته بشكل فكاهي، ويولّد صورة مرحة مناسبة، ويعرضها في صفحة ويب بسيطة.

---

## ✅ خطوات تشغيل المشروع محليًا

1. فك الضغط عن الملفات:
   ```bash
   unzip funny_news_project.zip
   cd funny_news_project
   ```

2. تثبيت المتطلبات:
   ```bash
   pip install -r requirements.txt
   ```

3. ضع مفتاح OpenAI في الكود أو كمتغير بيئة:
   ```bash
   export KEY=your_openai_api_key
   ```

4. تشغيل التطبيق:
   ```bash
   python funny_news_app.py
   ```

5. افتح المتصفح على:
   ```
   http://localhost:5000
   ```

---

## 🌐 خطوات النشر على موقع Render

1. أنشئ حساب على [https://render.com](https://render.com)

2. ارفع ملفات المشروع إلى GitHub (يشمل: `funny_news_app.py`, `requirements.txt`, `render.yaml`)

3. في لوحة التحكم في Render:
   - اختر **New Web Service**
   - اربط حساب GitHub واختر المشروع
   - Render سيتعرف تلقائيًا على إعدادات `render.yaml`

4. أضف متغير بيئة:
   ```
   KEY = your_openai_api_key
   ```

5. أنشئ الخدمة، وانتظر حتى يتم النشر.

6. رابط التطبيق سيكون متاحًا بعد دقيقة تقريبًا 🎉

---

📌 *ملاحظة: يتم توليد خبر جديد وصورة في كل مرة يتم فيها فتح الصفحة، ولا يتم تخزين أي بيانات.*
