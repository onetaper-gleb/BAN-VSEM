import asyncio

import schedule
from aiogram.types import Message, ContentType
import logging

from aiogram import Bot, Dispatcher, F

from core.handlers.basic import roots_show, get_photo, get_location, start_work, next_show, show_root, sort_roots, \
    show_sorted_list, show_result, offer_root, send_root, organised, send_root_2, warning, \
    subscribed, unsubscribed, wait, anons, prnt, pnt, dl, coms
from core.settings import settings
from aiogram.filters import Command
from core.utils.commands import set_commands
from functions import get_values
from core.utils.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, 'Bot has just started working')


async def end_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, "Bot finished it's work")


async def start():
    bot = Bot(token=settings.bots.bot_token)
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(end_bot)
    dp.callback_query.register(show_root, F.data.startswith("variant"))
    dp.callback_query.register(offer_root, F.data.startswith("offer"))
    dp.callback_query.register(subscribed, F.data.startswith("subscribe"))
    dp.callback_query.register(unsubscribed, F.data.startswith("unsubscribe"))
    dp.callback_query.register(organised, F.data.startswith("organise"))
    dp.callback_query.register(show_sorted_list, F.data.startswith("sort"))
    dp.callback_query.register(show_result, F.data.startswith("check"))
    dp.callback_query.register(next_show, F.data.startswith("nine_variant"))
    dp.callback_query.register(warning, F.data.startswith("="))
    dp.callback_query.register(sort_roots, F.data == "sor")
    dp.callback_query.register(roots_show, F.data == "roots")
    dp.message.register(get_location, F.location)
    dp.message.register(get_photo, F.photo)
    dp.message.register(send_root, F.text.startswith("Я хочу"))
    dp.message.register(wait, F.text == 'anons')
    dp.message.register(prnt, F.text == '+')
    dp.message.register(pnt, F.text == '-')
    dp.message.register(dl, F.text == 'del')
    dp.message.register(coms, F.text == 'comers')
    dp.message.register(send_root_2, F.text.startswith("Я организую"))
    dp.message.register(start_work, Command(commands=['start', 'back']))
    dp.message.register(anons)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
