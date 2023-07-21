from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

answer_cats_button = KeyboardButton(text='Дай кота')

cats_dogs_keyboard = ReplyKeyboardMarkup(keyboard=[
    [answer_cats_button],
], resize_keyboard=True)