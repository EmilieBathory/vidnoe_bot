from pyrogram import Client, filters

# 🔑 Вставь сюда свои реальные данные
api_id = 30888488
api_hash = "67f114b207708b57ab5f8d15138cfd9c"
bot_token = "8479804734:AAH1CdVRaW1Jobcikse5jB7r2ovMJUv1RWQ"

# Настройки каналов
source_chat = "Podslushano_Vidnoe"  # канал, откуда пересылаем
target_chat = -5230145354           # куда пересылаем

# Создаем клиента бота
bot = Client(
    "vidnoe_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# Обработчик новых сообщений
@bot.on_message(filters.chat(source_chat))
def forward(client, message):
    try:
        bot.send_message(target_chat, message.text)
        print(f"✅ Сообщение переслано: {message.message_id}")
    except Exception as e:
        print(f"❌ Ошибка пересылки: {e}")

print(f"🤖 Бот готов и слушает канал {source_chat}...")
bot.run()
