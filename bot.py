from telethon import TelegramClient
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
import pytz
tz = pytz.timezone("Asia/Tashkent")
now = datetime.now(tz).strftime("%H:%M")

# Bu yerga o'zingizning ma'lumotlaringizni kiriting
API_ID = 12345678  # My.telegram.org saytidan olingan API_ID
API_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaa" # My.telegram.org saytidan olingan API_HASH
CHAT_ID = 1264164165  # Guruh yoki foydalanuvchi ID
SESSION_NAME = "my_session"  # Sessiyani saqlash uchun nom

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def update_name():
    while True:
        now = datetime.now().strftime("%H:%M")
        me = await client.get_me()
        new_name = f"{me.first_name.split()[0]} {now}"

        await client(UpdateProfileRequest(first_name=new_name))
        print(f"✅ Ism yangilandi: {new_name}")

        await asyncio.sleep(60)  # Har 60 soniyada yangilash

async def main():
    await client.start()
    await update_name()

print("🤖 Bot ishga tushdi...")
asyncio.run(main())
