import os
import asyncio
from telethon import TelegramClient, events, types

# --- Загружаем переменные окружения ---
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
target_chat = os.getenv("TARGET_CHAT")  # ID чата или username (@chatname)

# --- Создаем клиента ---
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

async def forward_last_messages():
    # Канал, откуда берём новости
    channel = "Podslushano_Vidnoe"

    async for message in client.iter_messages(channel, limit=10):
        # Пересылаем текст
        if message.message:
            await client.send_message(target_chat, message.message)

        # Пересылаем фото
        if message.photo:
            await client.send_file(target_chat, message.photo, caption=message.text)

        # Пересылаем видео
        if message.video:
            await client.send_file(target_chat, message.video, caption=message.text)

    print("✅ Последние 10 сообщений пересланы.")

# --- Обработчик новых сообщений ---
@client.on(events.NewMessage(chats="Podslushano_Vidnoe"))
async def new_message_handler(event):
    # Пересылаем новое сообщение сразу
    msg = event.message

    if msg.message:
        await client.send_message(target_chat, msg.message)
    if msg.photo:
        await client.send_file(target_chat, msg.photo, caption=msg.text)
    if msg.video:
        await client.send_file(target_chat, msg.video, caption=msg.text)

# --- Основная функция ---
async def main():
    print("🤖 Бот работает и слушает канал Podslushano_Vidnoe...")
    await forward_last_messages()
    await client.run_until_disconnected()

# --- Запуск ---
asyncio.run(main())
