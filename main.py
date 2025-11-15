import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token='8312926902:AAHSKrucLLmrqN2JO-cZwwn83PTI4-KAtzg')
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет!')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')