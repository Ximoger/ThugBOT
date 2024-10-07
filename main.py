import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram import Router
import asyncio

API_TOKEN = '7763672643:AAEuTYtcfsuBVBhO0ovz7zVX6LjawK8OsXI'
GROUP_ID = -4583634691  # Замените на ID вашей группы

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бота
bot = Bot(token=API_TOKEN)

# Инициализируем диспетчер и роутер
dp = Dispatcher()
router = Router()

# Обработчик для всех входящих видео сообщений
@router.message(lambda message: message.content_type == ContentType.VIDEO)
async def forward_video(message: Message):
    try:
        # Пересылаем видео в указанную группу
        await bot.forward_message(chat_id=GROUP_ID, from_chat_id=message.chat.id, message_id=message.message_id)
        await message.answer("Спасибо за видео! Отправил админу / Thanks for the video! I sent it to the admin")
    except Exception as e:
        logging.error(f"Ошибка при пересылке видео: {e}")
        await message.answer("Произошла ошибка при отправке видео.")

# Регистрация роутеров
dp.include_router(router)

# Функция удаления вебхука
async def delete_webhook():
    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("Webhook успешно удален.")

# Запуск бота
async def main():
    # Удаляем вебхук перед началом polling
    await delete_webhook()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
