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

asyncio.run(main())



# echo "# tg_bot" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Cyb3rR0n1n/tg_bot.git
# git push -u origin main