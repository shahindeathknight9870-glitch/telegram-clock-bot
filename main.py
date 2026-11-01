import asyncio
from datetime import datetime
import os
from telethon import TelegramClient
import pytz

# دریافت اطلاعات از متغیرهای محیطی Render
api_id = int(os.environ.get('API_ID', 0))
api_hash = os.environ.get('API_HASH', '')
session_string = os.environ.get('SESSION_STRING', '')

async def main():
    client = TelegramClient(SessionString(session_string), api_id, api_hash)
    async with client:
        print("Bot started successfully and running 24/7...")
        while True:
            try:
                # تنظیم منطقه زمانی (تهران)
                Tehran_tz = pytz.timezone('Asia/Tehran')
                Now = datetime.now(tehran_tz)
                
                # فرمت ساعت (مثلا 14:35)
                Time_str = now.strftime("%H:%M")
                
                # نام نمایشی جدید (ترکیب نام شما و ساعت)
                New_name = f"Your Name | {time_str}"
                
                # آپدیت نام پروفایل در تلگرام
                # (تابع آپدیت پروفایل در تلگرام)
                
                print(f"Time updated to: {time_str}")
            except Exception as e:
                Print(f"Error: {e}")
                
            # صبر کردن برای دقیقاً ۶۰ ثانیه
            Await asyncio.sleep(60)

If __name__ == '__main__':
    Asyncio.run(main())
