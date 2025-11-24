import asyncio
import logging
import os
import sys
import time
from datetime import datetime, timezone
import sqlite3
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
from handlers import help, my_main, coord, photo, exchange, broad, users
from dotenv import load_dotenv
logging.basicConfig(level=logging.INFO)

from config import TOKEN
# load_dotenv()
# TOKEN = os.getenv("TOKEN")
# conn = sqlite3.connect("mydatabase.db")
# cursor = conn.cursor()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     date DATETIME DEFAULT CURRENT_TIMESTAMP,
#     name INTEGER,
#     message TEXT           
# )
# """)
# conn.commit()
# conn.close()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher(bot=Bot, storage=MemoryStorage())
dp["started_at"] = time.strftime('%d/%b/%Y %H:%M')
dp["developer"] = "Ivanopulo and Zuz"
user_ids = {}


class CurrencyForm(StatesGroup):
    count = State()
    like_bots = State()
    language = State()





@dp.message(F.text.startswith('test'))
async def cmd_test1(message: types.Message):    
    me = await bot.get_me()   
    # print(f"Bot name: {me.first_name}")
    # print(f"Bot username: @{me.username}")
    # conn = sqlite3.connect("mydatabase.db")
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM users")
    # rows = cursor.fetchall()   
    
    await message.answer(f"Hello my friend {message.from_user.first_name}. My name {me.first_name}. Test passed")



# @dp.message(Command("info"))
# async def info(message: types.Message, started_at: str, developer: str):
#     await message.answer(f"Bot started in {started_at} .\nDevelopers : {developer}. ")

@dp.message(Command("start"))
async def handle_start(message):
    lang = message.from_user.language_code

    if lang.startswith("es"):
        text = "Hola 👋 Soy tu asistente de IA."
    elif lang.startswith("ru"):
        text = "Привет 👋 Я твой AI-ассистент."
    else:
        text = "Hi 👋 I'm your AI assistant."

    await message.answer(text=text)


# @dp.message(Command("list"))
# async def cmd_test1(message: types.Message, mylist: set[str]):
#     mylist.add(message.from_user.first_name)   
#     await message.answer(f" The users this bot: <b> {', '.join(mylist)} </b>",

#                          parse_mode=ParseMode.HTML)

# @dp.message(Command("buy"))
# async def buy_shoes(message: types.Message):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="Click if YES",
#         callback_data="random_value")
#     )
#     await message.answer(f"Привет мой друг <b>{html.bold(message.from_user.full_name)}!</b>\n Хочешь обменять валюту?",
#                          reply_markup=builder.as_markup(),
#                          parse_mode=ParseMode.HTML)
# @dp.message(CommandStart())
# async def send_welcome(message: types.Message):
    
#     await message.answer(f"Привет мой друг  <b>{html.bold(message.from_user.full_name)}!</b> "
#                          f"\n Используй команду  /help , чтобы узнать список доступных команд!",
#                          parse_mode=ParseMode.HTML)


# @dp.message(Command('setstate'))
# async def periodic(message: types.Message, state: FSMContext):
#     await state.set_state(CurrencyForm.count)

#     await bot.send_message(message.from_user.id, f"Hello, enter count ", disable_notification=True)


# current_time = time.strftime('%d/%b/%Y %H:%M')


@dp.message()
async def webhook(message: types.Message):   
    # conn = sqlite3.connect("mydatabase.db")
    # cursor = conn.cursor()
    # cursor.execute("INSERT INTO users (date, name, message) VALUES (?, ?, ?)", (    
    # message.date,
    # message.from_user.first_name, 
    # message.text
    # ))
    # conn.commit()
    
    user_lang = message.from_user.language_code
    print(user_lang)
    response = requests.post('http://144.124.245.103/n8n/webhook/APIsssi',
                              json ={"sender": f"{message.from_user.first_name}",
  	                            "instance": f"{message.from_user.username}",
  	                            "message": f"{message.text}",
                                "lang": f"{user_lang}"},
                              )
    data = response.json()
    ii_message = data.get('response')    
    await message.answer(f"{ii_message}")

async def main():    
    # dp.include_routers(help.router, my_main.router, users.router, coord.router, photo.router, exchange.router, broad.router)
    # # loop = asyncio.get_running_loop()
    # loop.call_later(10, periodic)
    storage = FileMailerStorage()
    broadcaster = Broadcaster(bot, storage=storage)
    broadcaster.setup(dispatcher=dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, mylist=set())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
