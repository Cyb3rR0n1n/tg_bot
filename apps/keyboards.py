from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]],
    
    resize_keyboard=True, # изменение размер кнопок на маленькие
    input_field_placeholder='Выберите пункт меню' # прозрачный текст в поле ввода
    )