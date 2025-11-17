# import logging # логирование на время раработки
import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from apps.handlers import router

from dotenv import find_dotenv, load_dotenv # библиотеки для хранения токенов, url в отдельных файлах .env

load_dotenv(find_dotenv()) # найти файл в виртуальном окружении и загрузить

ALLOWED_UPDATES = ['message', 'edited_message'] # типы обрабатываемых updates

bot = Bot(token=os.getenv('TOKEN')) # через библиотеку os найти файл с токеном
dp = Dispatcher() # класс обрабатывает сообщения которые получает Бот


async def main():
    dp.include_router(router) # from apps.handlers import router
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES) # опрашивает сервер на наличие НОВЫХ сообщений

if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO) # логирование на время разработки
    
    # для устранения except KeyboardInterrupt при завершении работы бота через Ctrl + C
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')