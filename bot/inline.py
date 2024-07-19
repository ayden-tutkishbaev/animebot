from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.queries import *

languages = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🇬🇧 ENGLISH", callback_data="eng")],
        [InlineKeyboardButton(text="🇷🇺 РУССКИЙ", callback_data="rus")]
    ],
)


def anime_by_year(year):
    anime_list = get_anime_by_year(year)
    keyboard = InlineKeyboardBuilder()
    for anime in anime_list:
        print(f"Name of anime: {anime[1]}, data: anime_{anime[0]}")
        keyboard.add(InlineKeyboardButton(text=anime[1], callback_data=f"anime_{anime[0]}"))
    return keyboard.adjust(2).as_markup()


rate_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❤️", callback_data="like", url=""), InlineKeyboardButton(text="👎",
                                                                                             callback_data="dislike",
                                                                                             url="")]
    ]
)