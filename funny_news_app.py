# مشروع: مولّد أخبار فكاهية مع صورة (جلسة واحدة فقط – قابل للنشر على Render)

import os
import feedparser
import openai
from flask import Flask, render_template_string

# استخدام متغير البيئة لمفتاح OpenAI
openai.api_key = os.getenv("KEY")

app = Flask(__name__)

@app.route("/")
def funny_news():
    # 1. جلب أول خبر من RSS
    feed_url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(feed_url)
    if not feed.entries:
        return "<h1>❌ لا توجد أخبار متاحة حاليًا. حاول لاحقًا.</h1>"
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

    # 5. عرض النتائج (بواجهة محسّنة)
    html = f"""
    <html>
    <head>
        <title>خبر ساخر</title>
        <style>
            body {{
                background-color: #f7f7f7;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #333;
                text-align: center;
                padding: 50px;
            }}
            h1 {{
                color: #d63384;
            }}
            h3 {{
                margin-top: 40px;
                color: #444;
            }}
            p {{
                max-width: 800px;
                margin: auto;
                line-height: 1.8;
                font-size: 18px;
            }}
            img {{
                margin-top: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}
            .reload-button {{
                display: inline-block;
                margin-top: 50px;
                padding: 10px 25px;
                font-size: 18px;
                background-color: #20c997;
                color: white;
                border: none;
                border-radius: 8px;
                text-decoration: none;
                transition: background 0.3s;
            }}
            .reload-button:hover {{
                background-color: #17a589;
            }}
        </style>
    </head>
    <body>
        <h1>📢 {title}</h1>
        <h3>الخبر المترجم:</h3>
        <p>{translated_text}</p>
        <h3>😂 النسخة الفكاهية:</h3>
        <p>{funny_text}</p>
        <img src='{image_url}' alt='صورة ساخرة' width='512'/>

        <br>
        <a href="/" class="reload-button">🔁 خبر جديد</a>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
