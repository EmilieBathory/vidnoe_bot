import asyncio
from telethon import TelegramClient, events

# === Вставь сюда свои данные ===
api_id = 30888488  # твой API_ID
api_hash = "67f114b207708b57ab5f8d15138cfd9c"  # твой API_HASH
bot_token = "8479804734:AAH1CdVRaW1Jobcikse5jB7r2ovMJUv1RWQ"  # токен бота
target_chat = -5230145354  # ID чата, куда бот будет пересылать новости

# Канал, откуда берем новости
source_channel = "Podslushano_Vidnoe"

# Ключевые слова для фильтрации новостей
keywords = [
    "Видное", "Ленинский округ", "администрация", "погода", "льготы",
    "выплаты", "социальная поддержка", "экология", "ЧП", "криминал",
    "транспорт", "дороги", "строительство", "инфраструктура",
    "мероприятия", "события", "здоровье"
]

# Создаем клиента Telethon
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

async def main():
    print(f"🤖 Бот работает и слушает канал {source_channel}...")
    async for message in client.iter_messages(source_channel, limit=10):
        if message.text:
            # проверяем, есть ли ключевое слово в тексте
            if any(keyword.lower() in message.text.lower() for keyword in keywords):
                await client.send_message(target_chat, message.text)
        # пересылаем медиа (картинки, видео)
        if message.media:
            await client.send_file(target_chat, message.media)

# Запуск бота
asyncio.run(main())
