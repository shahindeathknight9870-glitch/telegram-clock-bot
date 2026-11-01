from datetime import datetime
import os
import pytz
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_string = os.environ.get("SESSION_STRING")


async def main():
    client = TelegramClient(StringSession(session_string), api_id, api_hash)
    await client.connect()

    tehran_tz = pytz.timezone("Asia/Tehran")
    base_name = "Shanice"

    try:
        now_tehran = datetime.now(tehran_tz)
        current_time = now_tehran.strftime("%H:%M")
        new_name = f"{base_name} | {current_time} 🕒"

        await client(UpdateProfileRequest(first_name=new_name))
        print(f"Profile name updated successfully to: {new_name}")
    except Exception as e:
        print(f"Error updating time: {e}")
    finally:
        await client.disconnect()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
