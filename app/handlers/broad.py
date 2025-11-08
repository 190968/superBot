from aiogram import Bot, Dispatcher, types, html, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

router = Router()

TOKEN = '6700779699:AAGw3dk2xDbj0-ThSiJjWukhxcBkapYmUY0'

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


# @router.message(Command('broad'))
# async def process_any_message(message: types.Message):
#     f = open("id.txt", 'r')
#     chat_ids = set(list(f.read()[:-1].split(',')))
#     for i in chat_ids:
#         await bot.send_photo(
#             chat_id=i,
#             photo="https://masters.place/images/90178.jpg",
#             caption= f"Hello {message.from_user.username}! This is her friend Bob")