from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Каталог')],
#     [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]],
    
#     resize_keyboard=True, # изменение размер кнопок на маленькие
#     input_field_placeholder='Выберите пункт меню' # прозрачный текст в поле ввода
#     )

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='basket'), 
     InlineKeyboardButton(text='Контакты', callback_data='contacts')]
     ])

# ------------------------------------------------------------------------------------------------#
catalog = ['Вынос границ участка', 'Топографическая съемка', 'Сопровождение строительства', 
           'Съемка для ландшафтного дизайна', 'Иное'] # каталог услуг

async def inline_catalog():
    """Формирует кнопки из списка catalog"""
    keyboard = InlineKeyboardBuilder()
    for item in catalog:
        keyboard.add(InlineKeyboardButton(text=item, url='https://www.youtube.com/'))
    return keyboard.adjust(2).as_markup()
# ------------------------------------------------------------------------------------------------#
