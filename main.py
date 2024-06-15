import asyncio
import logging
import sys
import time
from datetime import datetime

from aiogram import Bot, Dispatcher, types, html, Router
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram_broadcaster import Broadcaster
from aiogram_broadcaster.contents import MessageSendContent
from aiogram_broadcaster.storages.file import FileMailerStorage
from handlers import help, my_main, coord, photo, exchange, broad

logging.basicConfig(level=logging.INFO)

TOKEN = '6700779699:AAGw3dk2xDbj0-ThSiJjWukhxcBkapYmUY0'

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
dp["developer"] = "Ivanopulo and ZUZ"
# chat_ids = []
user_ids = {}


@dp.message(Command("test"))
async def cmd_test1(message: types.Message):
    info_chat = message.from_user.language_code
    print(info_chat)
    await message.answer_dice(emoji="🎲", content=info_chat)





@dp.message(Command("info"))
async def info(message: types.Message, started_at: str, developer: str):
    await message.answer(f"Bot started {started_at} , developer : {developer} ")


@dp.message(Command("list"))
async def cmd_test1(message: types.Message, mylist: set[str]):
    mylist.add(message.from_user.first_name)
    await message.answer(f" Users the bot: <b> {', '.join(mylist)} </b>", parse_mode=ParseMode.HTML)


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    # chat_ids.append(message.chat.id)
    f = open("id.txt", "a")
    f.write(str(message.chat.id) + ',')
    await message.answer(f"Привет мой друг ,{html.bold(message.from_user.full_name)}! "
                         f"\nИспользуй /help, чтобы узнать список доступных команд!")


@dp.message(Command('messaging'))
async def periodic(message: types.Message):
    # loop = asyncio.get_running_loop()
    # loop.call_later(10, periodic, message)
    await asyncio.sleep(10)
    await bot.send_message(message.from_user.id, f"Hello ", disable_notification=True)


@dp.message(F.text.lower() == "good")
async def good(message: types.Message):
    await message.reply("Yes. All right and well.")


@dp.message(F.text.lower() == "отличное")
async def with_puree(message: types.Message):
    await message.reply("Рад за тебя !")


@dp.message(F.text.lower() == "среднее")
async def without_puree(message: types.Message):
    await message.reply("Надейся на лучшее !")


@dp.message(F.text.lower() == "плохое")
async def without_puree(message: types.Message):
    await message.reply("Иди бухни чувак !")


current_time = time.strftime('%A %B, %d %Y %H:%M:%S')


def later():
    print('bcvbcv')


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
