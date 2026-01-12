import os
import asyncio
from telethon import TelegramClient, events

# Получаем переменные из окружения
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
target_chat = int(os.getenv("TARGET_CHAT"))  # если чат числовой

# Создаем клиента бота
bot = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

async def main():
    print("🤖 Бот запущен и слушает канал...")

    # Обработчик новых сообщений из всех чатов
    @bot.on(events.NewMessage())
    async def handler(event):
        # Пересылаем любое сообщение в целевой чат
        await bot.send_message(target_chat, event.message)
        print(f"Переслано сообщение: {event.message.text}")

    # Ждем бесконечно, пока бот работает
    await bot.run_until_disconnected()

if __name__ == "__main__":
    # Запуск основного цикла один раз
    asyncio.run(main())
