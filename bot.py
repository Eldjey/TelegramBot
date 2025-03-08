from telethon import TelegramClient, events
import asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import pytz
tz = pytz.timezone("Asia/Tashkent")
now = datetime.now(tz).strftime("%H:%M")

# Bu yerga o'zingizning ma'lumotlaringizni kiriting
API_ID = 28010610  # My.telegram.org saytidan olingan API_ID
API_HASH = "a1b56de78820ebae4c46e9392768b56d"  # My.telegram.org saytidan olingan API_HASH
CHAT_ID = -1002416060887  # Guruh yoki foydalanuvchi ID
SESSION_NAME = "my_session"  # Sessiyani saqlash uchun nom

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# # Faqat guruh ichidagi xabarlarga javob berish
# @client.on(events.NewMessage(incoming=True, chats=CHAT_ID))
# async def handler(event):
#     if event.is_group:
#         text = event.raw_text.lower()

#         if "kim gey?" in text:
#             await event.reply("@Lochinbekovv")
#         elif "Km gey" in text:
#             await event.reply("@Lochinbekovv")
#         elif "Kim gey?" in text:
#             await event.reply("@Lochinbekovv")
#         else:
#             await event.reply("xato yozdiz. \n✅To'g'ri shakl: `kim gey?`")

# print("🤖 Bot faqat guruhlarda ishlash uchun ishga tushdi...")
# client.start()
# client.run_until_disconnected()

async def update_name():
    while True:
        now = datetime.now().strftime("%H:%M")  # Hozirgi vaqt (soat:daqiqa)
        me = await client.get_me()  # O'zingizning profil ma'lumotlarini olish
        new_name = f"{me.first_name.split()[0]} {now}"  # Ism + vaqt

        # Faqat ismni o'zgartiramiz, familiyani o‘zgartirmaymiz
        await client(UpdateProfileRequest(first_name=new_name))
        print(f"✅ Ism yangilandi: {new_name}")

        await asyncio.sleep(60)  # Har 60 soniyada yangilash

async def main():
    await client.start()
    await update_name()

print("🤖 Bot ishga tushdi...")
asyncio.run(main())