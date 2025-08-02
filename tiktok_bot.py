
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import os
BOT_TOKEN = os.getenv("8376473809:AAGh7qmqIrrZNsW6n01woJTNjerju2k7d0c")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if "tiktok.com" not in text:
        await update.message.reply_text("📎 تکایە لینکێکی دروست بنێرە (TikTok only).")
        return

    await update.message.reply_text("⏳ چاوەڕوان بە... دایگرتنی ڤیدیۆکە...")

    try:
        lookup_url = f"https://api.tikmate.app/api/lookup?url={text}"
        response = requests.get(lookup_url)
        result = response.json()

        video_token = result["token"]
        video_id = result["id"]
        video_url = f"https://tikmate.app/download/{video_token}/{video_id}.mp4"

        await update.message.reply_video(video=video_url, caption="📥 ئەمەیە ڤیدیۆکە!")

    except Exception as e:
        print("Error:", e)
        await update.message.reply_text("❌ نەتوانرا ڤیدیۆکە دابگرێت. تکایە لینکەکە دووبارە سەیربکە.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🤖 بۆتی تیکتۆک دامەزرابوو. چاوەڕوانی پەیامێک بکە...")
app.run_polling()
