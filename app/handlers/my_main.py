from aiogram import Router, F, html, Dispatcher
from aiogram.types import Message, CallbackQuery
import time
from aiogram import F
from aiogram import Bot, types
from aiogram.filters import Command
router = Router()
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup
import keyboards as kb
TOKEN = '6700779699:AAGw3dk2xDbj0-ThSiJjWukhxcBkapYmUY0'
bot = Bot(token=TOKEN)
dp = Dispatcher()



@router.message(Command("hello"))
async def message_text(message: types.Message):
    print('hello')
    keyboard = [
            [InlineKeyboardButton(text = "Привет друг", callback_data="myhello")],
            [InlineKeyboardButton(text = "Hello friend", callback_data="button2")],
            [InlineKeyboardButton(text='Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/')]
        ]
    inline_kb1 = InlineKeyboardMarkup(inline_keyboard=keyboard)
    current_time = time.strftime('%A %B, %d %Y %H:%M')
    await  message.reply(f"Привет мой друг ,{ html.bold(message.from_user.full_name) }! \n"
                          f"Сегодня: {current_time} \n", reply_markup=inline_kb1)

@dp.callback_query(F.data == "myhello")
async def button1_one(callback_query: types.CallbackQuery):   
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )
