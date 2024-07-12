import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot import handlers

from dotenv import dotenv_values

dotenv = dotenv_values(".env")


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(token=dotenv["BOT_TOKEN"], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_routers(
        handlers.rt,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("STOPPED")
