# bot.py

from telethon import TelegramClient, events

# Вставляем значения напрямую (только для теста, потом лучше через переменные окружения)
api_id = 30888488
api_hash = "67f114b207708b57ab5f8d15138cfd9c"
bot_token = "8479804734:AAH1CdVRaW1Jobcikse5jB7r2ovMJUv1RWQ"
target_chat = -5230145354

client = TelegramClient('bot', api_id, api_hash)

async def main():
    await client.start(bot_token=bot_token)
    print("🤖 Бот работает и слушает канал Podslushano_Vidnoe...")
    # пример пересылки новых сообщений
    @client.on(events.NewMessage(chats='Podslushano_Vidnoe'))
    async def handler(event):
        await client.send_message(target_chat, event.message.text)

    await client.run_until_disconnected()

import asyncio
asyncio.run(main())
