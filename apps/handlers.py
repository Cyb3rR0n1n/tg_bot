from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import apps.keyboards as kb


router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message): # анотируем типы для удобства работы с методами и св-ми
    """метод answer отвечает за ответ (можно ответить документом) await message.answer_document"""
    await message.answer(f'Привет!', reply_markup=kb.main)
    # await message.reply(text='Привет!', reply_markup=kb.main)

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы открыли каталог', show_alert=True)  # Обязательно отвечаем на callback
    await callback.message.edit_text('Каталог', reply_markup=await kb.inline_catalog())

@router.callback_query(F.data == 'basket')
async def basket(callback: CallbackQuery):
    await callback.answer()  # Обязательно отвечаем на callback
    await callback.message.answer('Ваша корзина')

@router.callback_query(F.data == 'contacts')
async def contacts(callback: CallbackQuery):
    await callback.answer()  # Обязательно отвечаем на callback
    await callback.message.answer('Наши контакты')

    