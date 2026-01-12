import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

api_id = int(os.getenv("API_ID") or "YOUR_API_ID")
api_hash = os.getenv("API_HASH") or "YOUR_API_HASH"
bot_token = os.getenv("BOT_TOKEN") or "YOUR_BOT_TOKEN"
target_chat = int(os.getenv("TARGET_CHAT") or "YOUR_TARGET_CHAT")
source_chat = os.getenv("SOURCE_CHAT") or "Podslushano_Vidnoe"

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(chats=source_chat))
async def forward_message(event):
    await bot.send_message(target_chat, event.message)
    print(f"Сообщение переслано: {event.message.id}")

print(f"🤖 Бот работает и слушает канал {source_chat}...")
bot.run_until_disconnected()
