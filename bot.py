import os
import asyncio
from telethon import TelegramClient, events

# ======== ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ (CAPS) ========
# Попробуем взять из переменных окружения
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
target_chat = os.getenv("TARGET_CHAT")

# ======== ДЛЯ ТЕСТА (если env не передались, подставляем вручную) ========
if api_id is None:
    api_id = 30888488  # замените на свой ID
else:
    api_id = int(api_id)

if api_hash is None:
    api_hash = "67f114b207708b57ab5f8d15138cfd9c"  # замените на свой HASH

if bot_token is None:
    bot_token = "8479804734:AAH1CdVRaW1Jobcikse5jB7r2ovMJUv1RWQ"  # замените на свой токен

if target_chat is None:
    target_chat = -5230145354  # замените на свой ID чата
else:
    target_chat = int(target_chat)

# ======== СОЗДАЕМ КЛИЕНТА ========
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# ======== ОБРАБОТКА СООБЩЕНИЙ ========
@client.on(events.NewMessage(chats='Podslushano_Vidnoe'))
async def handler(event):
    try:
        message = event.message
        # Пересылаем в целевой чат
        await client.send_message(target_chat, message)
        print("Сообщение переслано")
    except Exception as e:
        print("Ошибка при пересылке:", e)

# ======== ЗАПУСК БОТА ========
async def main():
    print(f"🤖 Бот работает и слушает канал Podslushano_Vidnoe...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
