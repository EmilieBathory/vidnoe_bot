import os
from telethon import TelegramClient, events

# --- ПЕРЕМЕННЫЕ ---
api_id = int(os.getenv("API_ID") or 30888488)
api_hash = os.getenv("API_HASH") or "67f114b207708b57ab5f8d15138cfd9c"
bot_token = os.getenv("BOT_TOKEN") or "8479804734:AAH1CdVRaW1Jobcikse5jB7r2ovMJUv1RWQ"
target_chat = int(os.getenv("TARGET_CHAT") or -5230145354)

# --- Создаём клиента ---
bot = TelegramClient('vidnoe_bot', api_id, api_hash).start(bot_token=bot_token)

# --- Функция пересылки сообщений ---
@bot.on(events.NewMessage(chats='Podslushano_Vidnoe'))
async def forward_messages(event):
    try:
        await bot.forward_messages(target_chat, event.message)
        print(f"✅ Переслано сообщение: {event.message.id}")
    except Exception as e:
        print(f"❌ Ошибка при пересылке: {e}")

# --- Запуск бота ---
print("🤖 Бот работает и слушает канал Podslushano_Vidnoe...")
bot.run_until_disconnected()
