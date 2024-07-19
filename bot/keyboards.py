from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.messages import *
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from database.queries import *


def main_menu(language):
    main_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=buttons['button_anime'][language])],
            [KeyboardButton(text=buttons['button_sticker'][language]), KeyboardButton(text=buttons['button_location'][language]),
             KeyboardButton(text=buttons['button_emoji'][language])],
            [KeyboardButton(text=buttons['button_description'][language])],
            [KeyboardButton(text=buttons['button_commands'][language])],
            [KeyboardButton(text=buttons['button_lang'][language])],
        ], resize_keyboard=True, input_field_placeholder='Choose option'
    )

    return main_keyboard


def years_keyboard(language):
    all_years = get_all_years()
    keyboard = ReplyKeyboardBuilder()
    for year in all_years:
        keyboard.button(text=f"{year[1]}")
    keyboard.button(text=buttons['button_menu'][language]).adjust(1)
    return keyboard.as_markup()


