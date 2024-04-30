import asyncio

import schedule
from aiogram.types import Message, ContentType
import logging

from aiogram import Bot, Dispatcher, F

from core.handlers.basic import roots_show, get_photo, get_location, start_work
from core.settings import settings
from aiogram.filters import Command
from core.utils.commands import set_commands
from functions import get_values


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Bot has just started working')


async def end_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, "Bot finished it's work")


async def start():
    bot = Bot(token=settings.bots.bot_token)
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(end_bot)
    dp.callback_query.register(roots_show, F.data == "roots")
    dp.message.register(get_location, F.location)
    dp.message.register(get_photo, F.photo)
    dp.message.register(start_work, Command(commands=['start', 'run']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
