from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

import bot.keyboards as kb
import bot.inline as il
from bot import lists

from database.queries import *

import random

from bot.messages import *

rt = Router()


@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    chat_id = message.chat.id
    insert_user_to_languages_table(chat_id)
    await message.answer(f"Hello and welcome, <b>{message.from_user.first_name}</b>!"
                         f"✅\n\n<b>Выберите язык: 🌐\nChoose language: 🌐</b>", reply_markup=il.languages)
    await message.delete()


@rt.callback_query(lambda callback: callback.data in ["rus", "eng", "uzb"])
async def set_language(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    language = callback.data
    update_user_language(chat_id, language)
    chat_id = callback.message.chat.id
    language = get_user_language(chat_id)
    await callback.message.delete()
    await callback.message.answer(f"""{messages['message_1'][language]}""", reply_markup=kb.main_menu(language))


@rt.message(lambda message: message.text in ["Изменить язык", "Change language"])
async def command_start_handler(message: Message) -> None:
    await message.answer(f"✅\n\n<b>Выберите язык: 🌐\nChoose language: 🌐</b>", reply_markup=il.languages)
    await message.delete()


@rt.message(lambda message: message.text in ["Main menu", "Главное меню"])
async def back_to_menu(message: Message) -> None:
    chat_id = message.chat.id
    language = get_user_language(chat_id)
    await message.answer(f"{messages['message_2'][language]}!", reply_markup=kb.main_menu(language))


@rt.message(lambda message: message.text in ["Список аниме по годам", "List of anime by year"])
async def anime_list(message: Message) -> None:
    chat_id = message.chat.id
    language = get_user_language(chat_id)
    await message.answer(messages["anime_list"][language], reply_markup=kb.years_keyboard(language))


@rt.message(lambda message: message.text in [year[1] for year in get_all_years()])
async def anime_by_year(message: Message) -> None:
    year = message.text
    year_id = get_year_by_title(year)
    await message.answer_photo(photo="https://i.insider.com/61d786c637afc20019ac999b?width=700",
                               caption="Here they are! 👇", reply_markup=il.anime_by_year(year_id))


@rt.callback_query(lambda callback: callback.data.startswith("anime_"))
async def spy_family(callback: CallbackQuery) -> None:
    anime_data = get_anime_data(callback.data)
    await callback.message.answer(f"<b>{anime_data[0]}</b>\n <b><i>{anime_data[1]}</i></b>\n\n {anime_data[2]}")


@rt.callback_query(F.data == "like")
async def like(callback: CallbackQuery) -> None:
    await callback.answer("😁 You have liked the anime")


@rt.callback_query(F.data == "dislike")
async def dislike(callback: CallbackQuery) -> None:
    await callback.answer("😒 You have disliked the anime")


@rt.message(lambda message: message.text in ["Random location 📍", "Случайная локация 📍"])
async def random_location(message: Message) -> None:
    chat_id = message.chat.id
    language = get_user_language(chat_id)
    try:
        await message.answer_location(latitude=random.randint(1, 200), longitude=random.randint(1, 200))
    except TelegramBadRequest:
        await message.answer(messages["error"][language])


@rt.message(lambda message: message.text in ["Случайный эмодзи 😊", "Random emoji 😊"])
async def random_emoji(message: Message) -> None:
    await message.answer(f"{random.choice(lists.emoji)}")


@rt.message(lambda message: message.text in ["Случайный стикер 🥰", "Random sticker 🥰"])
async def random_sticker(message: Message) -> None:
    await message.answer_sticker(sticker=random.choice(lists.stickers))


@rt.message(F.text == "Description 🗒")
async def description(message: Message) -> None:
    await message.answer(DESCRIPTION)


@rt.message(Command(commands=["help"]))
async def help(message: Message) -> None:
    await message.answer(COMMANDS_LIST)


@rt.message(F.text == "List of commands 🕹")
async def description(message: Message) -> None:
    await message.answer(COMMANDS_LIST)



@rt.message()
async def echo_handler(message: Message) -> None:
    await message.answer("?")

