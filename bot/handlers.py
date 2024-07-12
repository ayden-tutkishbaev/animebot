from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

import bot.keyboards as kb
import bot.inline as il
from bot import lists

import random

from bot.messages import *

rt = Router()


@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello and welcome, <b>{message.from_user.first_name}</b>! ✅", reply_markup=kb.main_keyboard)
    await message.delete()


@rt.message(F.text == "MAIN MENU")
async def back_to_menu(message: Message) -> None:
    await message.answer("You have gone back to the main menu!", reply_markup=kb.main_keyboard)


@rt.message(F.text == "List of all anime of 2022-2024 period")
async def anime_list(message: Message) -> None:
    await message.answer("Years of anime releases are presented below.", reply_markup=kb.years_keyboard)


@rt.message(F.text == "2022")
async def anime_2022(message: Message) -> None:
    await message.answer_photo(photo="https://i.insider.com/61d786c637afc20019ac999b?width=700",
                               caption="Here they are! 👇", reply_markup=il.anime2022_keyboard)


@rt.message(F.text == "2023")
async def anime_2023(message: Message) -> None:
    await message.answer_photo(photo="https://www.enter.co/wp-content/uploads/2023/03/temporada-primavera-2023.jpg",
                               caption="Here they are! 👇", reply_markup=il.anime2023_keyboard)


@rt.message(F.text == "2024")
async def anime_2024(message: Message) -> None:
    await message.answer_photo(photo="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/01/best-winter-2024-anime.jpg",
                               caption="Here they are! 👇", reply_markup=il.anime2024_keyboard)


@rt.callback_query(F.data == "spy_family")
async def spy_family(callback: CallbackQuery) -> None:
    await callback.message.answer_photo(photo="https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=85,width=480,height=720/catalog/crunchyroll/095217fdb4f228410df09b18f151be28.jpe",
                                        caption="<i><b>Spy Family</b></i>", reply_markup=il.rate_keyboard)


@rt.callback_query(F.data == "bocchi_the_rock")
async def bocchi_the_rock(callback: CallbackQuery) -> None:
    await callback.message.answer_photo(photo="https://m.media-amazon.com/images/M/MV5BMzg1Yzg1NjQtZmQyOC00N2MwLWFkYmEtNDI0NGI3ODMzMDExXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX1000_.jpg",
                               caption="<i><b>Bocchi the rock</b></i>", reply_markup=il.rate_keyboard)


@rt.callback_query(F.data == "date_a_live")
async def date_a_live(callback: CallbackQuery) -> None:
    await callback.message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/en/1/13/Date_a_Live_IV.jpg", caption="<i><b>Date a live</b></i>", reply_markup=il.rate_keyboard)


@rt.callback_query(F.data == "oshi_no_ko")
async def oshi_no_ko(callback: CallbackQuery) -> None:
    await callback.message.answer_photo(photo="https://m.media-amazon.com/images/M/MV5BZmM1M2E1ZDEtYTZiNy00NzFjLTk2NDUtODExMWM3OWQ2NGU3XkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg", caption="<i><b>Oshi no ko</b></i>", reply_markup=il.rate_keyboard)


@rt.callback_query(F.data == "horimiya")
async def horimiya(callback: CallbackQuery) -> None:
    await callback.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWrJoVIEV2k8f8KHs7VfftgUgeJXXdmpZZqw&s", caption="<b><i>Horimiya</i></b>", reply_markup=il.rate_keyboard)


@rt.callback_query(F.data == "tomozaki")
async def tomozaki(callback: CallbackQuery) -> None:
    await callback.message.answer_photo(photo="https://static.wikia.nocookie.net/yowa-chara-tomozaki-kun/images/f/fd/Heroines-Anime_1.png/revision/latest/scale-to-width-down/1200?cb=20201107162018", caption="<b><i>Low-tier character Tomozaki kun</i></b>", reply_markup=il.rate_keyboard)


@rt.callback_query(F.data == "cote")
async def cote(callback: CallbackQuery) -> None:
    await callback.message.answer_photo(photo="https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=85,width=480,height=720/catalog/crunchyroll/8b35b4a6cffe66004f752aa147351cab.jpe", caption="<i><b>Classroom of the elite</b></i>", reply_markup=il.rate_keyboard)


@rt.callback_query(F.data == "alya_russian")
async def alya_russian(callback: CallbackQuery) -> None:
    await callback.message.answer_photo(photo="https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=85,width=480,height=720/catalog/crunchyroll/a4b79dd3cf47803d2c51f562e40bac93.jpg", caption="<i><b>Alya sometimes hides her feelings in russian</b></i>", reply_markup=il.rate_keyboard)


@rt.callback_query(F.data == "rent_a_girlfriend")
async def rent_a_girlfriend(callback: CallbackQuery) -> None:
    await callback.message.answer_photo(photo="https://m.media-amazon.com/images/M/MV5BZDM0YWNjNGQtNWJjMS00YTliLWE4YjItOGQzNWQxMmNkZDg4XkEyXkFqcGdeQXVyMzgxODM4NjM@._V1_FMjpg_UX1000_.jpg", caption="<i><b>Rent-a-Girlfriend</b></i>", reply_markup=il.rate_keyboard)


@rt.callback_query(F.data == "like")
async def like(callback: CallbackQuery) -> None:
    await callback.answer("😁 You have liked the anime")


@rt.callback_query(F.data == "dislike")
async def dislike(callback: CallbackQuery) -> None:
    await callback.answer("😒 You have disliked the anime")


@rt.message(F.text == "Random location 📍")
async def random_location(message: Message) -> None:
    try:
        await message.answer_location(latitude=random.randint(1, 200), longitude=random.randint(1, 200))
    except TelegramBadRequest:
        await message.answer("Something went wrong! 😱\nTry again later!")


@rt.message(F.text == "Random emoji 🤩")
async def random_emoji(message: Message) -> None:
    await message.answer(f"{random.choice(lists.emoji)}")


@rt.message(F.text == "Random sticker 🥰")
async def random_emoji(message: Message) -> None:
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

