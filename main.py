import asyncio
import logging
import sys
import time
from datetime import datetime

import requests
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.methods.get_my_name import GetMyName
import aiogram.types.chat
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher, types, html, Router
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters.command import Command, CommandStart
from aiogram_broadcaster import Broadcaster
from aiogram_broadcaster.storages.file import FileMailerStorage
from handlers import help, my_main, coord, photo, exchange, broad

logging.basicConfig(level=logging.INFO)

from config import TOKEN

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher(bot=Bot, storage=MemoryStorage())
dp["started_at"] = time.strftime('%d/%b/%Y %H:%M')
dp["developer"] = "Ivanopulo and Zuz"
user_ids = {}


class CurrencyForm(StatesGroup):
    count = State()
    like_bots = State()
    language = State()


mylist = set()


@dp.message(F.text.startswith('test'))
async def cmd_test1(message: types.Message):
    bot_name = await bot(GetMyName())
    print(bot_name)
    mylist.add(message.from_user.first_name)
    for z in mylist:
        print(z)
    info_chat = message.from_user.language_code
    await message.answer(f"Hello {message.from_user.first_name}. My {bot_name}. Test is good")

@dp.message(F.text.startswith('message'))
async def webhook(message: types.Message):
    bot_name = await bot(GetMyName())
    response = requests.post('https://bobozeranski.app.n8n.cloud/webhook-test/APIsssi', json={'message': message.from_user.first_name})
    data = response.json()
    my_message = data.get('message', 'No message found')
    print(my_message)
    await message.answer(f"Hello {message.from_user.first_name}. My {my_message}. Test is good")

@dp.message(Command("info"))
async def info(message: types.Message, started_at: str, developer: str):
    await message.answer(f"Bot started in {started_at} .\nDevelopers : {developer}. ")


@dp.message(Command("send_span"))
async def send(message: types.Message):
    print(message.date, message.from_user.first_name, mylist)
    await message.answer('czxczxcxzczxc')

@dp.message(Command("list"))
async def cmd_test1(message: types.Message, mylist: set[str]):
    mylist.add(message.from_user.first_name)
    print(message.date, message.from_user.first_name)
    await message.answer(f" The users this bot: <b> {', '.join(mylist)} </b>",

                         parse_mode=ParseMode.HTML)

@dp.message(Command("buy"))
async def buy_shoes(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(f"Привет мой друг <b>{html.bold(message.from_user.full_name)}!</b>\n Хочешь купить валюту?",
                         reply_markup=builder.as_markup(),
                         parse_mode=ParseMode.HTML)
@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    f = open("id.txt", "a")
    f.write(str(message.chat.id) + ',')
    await message.answer(f"Привет мой друг  <b>{html.bold(message.from_user.full_name)}!</b> "
                         f"\n Используй команду  /help , чтобы узнать список доступных команд!",
                         parse_mode=ParseMode.HTML)


@dp.message(Command('setstate'))
async def periodic(message: types.Message, state: FSMContext):
    await state.set_state(CurrencyForm.count)

    await bot.send_message(message.from_user.id, f"Hello, enter count ", disable_notification=True)


current_time = time.strftime('%d/%b/%Y %H:%M')


async def main():
    print('Current time:', current_time)
    dp.include_routers(help.router, my_main.router, coord.router, photo.router, exchange.router, broad.router)
    # loop = asyncio.get_running_loop()
    # loop.call_later(10, periodic)
    storage = FileMailerStorage()
    broadcaster = Broadcaster(bot, storage=storage)
    broadcaster.setup(dispatcher=dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, mylist=set())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
