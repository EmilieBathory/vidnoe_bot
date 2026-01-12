from telethon import TelegramClient, events
import os

# 🔑 Вставь сюда свои реальные данные
api_id = 30888488
api_hash = "67f114b207708b57ab5f8d15138cfd9c"
bot_token = "8479804734:AAH1CdVRaW1Jobcikse5jB7r2ovMJUv1RWQ"

# Настройки каналов
source_chat = "Podslushano_Vidnoe"  # канал, откуда пересылаем сообщения
target_chat = -5230145354           # куда пересылаем сообщения

# Удаляем старую сессию, чтобы избежать проблем с ApiIdInvalidError
session_file = "bot.session"
if os.path.exists(session_file):
    os.remove(session_file)

# Создаем клиента
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Обработчик новых сообщений
@bot.on(events.NewMessage(chats=source_chat))
async def forward_message(event):
    try:
        await bot.send_message(target_chat, event.message)
        print(f"✅ Сообщение переслано: {event.message.id}")
    except Exception as e:
        print(f"❌ Ошибка пересылки: {e}")

print(f"🤖 Бот работает и слушает канал {source_chat}...")
bot.run_until_disconnected()
