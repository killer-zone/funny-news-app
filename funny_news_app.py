# مشروع: مولّد أخبار فكاهية مع صورة (جلسة واحدة فقط)

import feedparser
import openai
from flask import Flask, render_template_string

openai.api_key = "YOUR_OPENAI_API_KEY"
app = Flask(__name__)

@app.route("/")
def funny_news():
    # 1. جلب أول خبر من RSS
    feed_url = "https://www.aljazeera.net/aljazeera/rss"
    feed = feedparser.parse(feed_url)
    entry = feed.entries[0]
    title = entry.title
    summary = entry.summary

    # 2. الترجمة إلى العربية
    translation_prompt = f"ترجم النص التالي إلى اللغة العربية بأسلوب صحفي:\n\n{summary}"
    translation_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": translation_prompt}
        ]
    )
    translated_text = translation_response['choices'][0]['message']['content']

    # 3. تحويل الخبر إلى فكاهي
    funny_prompt = f"حوّل هذا الخبر إلى صيغة فكاهية باللهجة المحكية وبأسلوب ساخر:\n\n{translated_text}"
    funny_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": funny_prompt}
        ]
    )
    funny_text = funny_response['choices'][0]['message']['content']

    # 4. توليد صورة فكاهية
    image_prompt = f"Funny cartoon image related to: {funny_text}"
    image_response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="512x512"
    )
    image_url = image_response['data'][0]['url']

    # 5. عرض النتائج (بدون تخزين دائم)
    html = f"""
    <html>
    <head><title>خبر ساخر</title></head>
    <body style='font-family: Arial; text-align: center; margin: 50px;'>
        <h1>📢 {title}</h1>
        <h3>الخبر المترجم:</h3>
        <p>{translated_text}</p>
        <h3>😂 النسخة الفكاهية:</h3>
        <p>{funny_text}</p>
        <img src='{image_url}' alt='صورة ساخرة' style='margin-top:20px; max-width: 100%;'/>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
