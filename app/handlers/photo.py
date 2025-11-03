from aiogram import Router, F, types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.methods import  send_photo
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.utils.formatting import as_line, Text, Bold
from aiogram.enums import ParseMode
import requests
import shutil
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


count = {'n':1060}
response = 'https://masters.place/images/{}.jpg'.format(count['n'])


TOKEN = '6700779699:AAGw3dk2xDbj0-ThSiJjWukhxcBkapYmUY0'
bot = Bot(token=TOKEN)
router = Router()
dp = Dispatcher()

@router.message(Command("photo"))

async def process_photo_command(message: types.Message):
    print(message.from_user.id)
    kb = [
        [
            InlineKeyboardButton(text="Next image", callback_data='next')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    caption = f"This {count['n']} image"
    count['n'] = count['n'] - 1
    print(count['n'])
    await bot.send_photo(message.from_user.id, response,caption=caption, reply_markup=keyboard)
@router.callback_query(F.data == 'next')
async  def next_image(message: types.Message):
    kb = [
        [
            InlineKeyboardButton(text="Prev image", callback_data='prev'),
            InlineKeyboardButton(text="Next image", callback_data='next')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    caption = f"This {count['n']} image"
    count['n'] = count['n'] - 1

    print(count)
    await bot.send_photo(message.from_user.id, 'https://masters.place/images/{}.jpg'.format(count['n']), caption=caption, reply_markup=keyboard)
@router.callback_query(F.data == 'prev')
async  def next_image(message: types.Message):
    kb = [
        [
            InlineKeyboardButton(text="Prev image", callback_data='prev'),
            InlineKeyboardButton(text="Next image", callback_data='next')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    caption = f"This {count['n']} image"
    count['n'] = count['n'] + 1

    print(response)
    await bot.send_photo(message.from_user.id, 'https://masters.place/images/{}.jpg'.format(count['n']), caption=caption, reply_markup=keyboard)