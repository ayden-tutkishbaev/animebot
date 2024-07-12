from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="List of all anime of 2022-2024 period")],
        [KeyboardButton(text="Random sticker 🥰"), KeyboardButton(text="Random location 📍"),
         KeyboardButton(text="Random emoji 🤩")],
        [KeyboardButton(text="Description 🗒")],
        [KeyboardButton(text="List of commands 🕹")],
    ], resize_keyboard=True, input_field_placeholder='Choose option'
)

years_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="2022"), KeyboardButton(text="2023"), KeyboardButton(text="2024")],
        [KeyboardButton(text="MAIN MENU")]
    ], resize_keyboard=True, input_field_placeholder='Choose a year'
)