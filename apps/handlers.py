from aiogram import F, Router, types
from aiogram.filters import CommandStart


router = Router()

@router.message(CommandStart())
async def start_cmd(message: types.Message): # анотируем типы для удобства работы с методами и св-ми
    """метод answer отвечает за ответ (можно ответить документом) await message.answer_document"""
    await message.answer('Привет!')