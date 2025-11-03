from aiogram import Router, F, html, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram import Bot, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup, InlineKeyboardBuilder

router = Router()
dp = Dispatcher()

@router.message(Command("exchange"))
async def change_currency(message: types.Message):
    kb = [
        [
            InlineKeyboardButton(text="€", callback_data='euro'),
            InlineKeyboardButton(text="$", callback_data='dollar'),
            InlineKeyboardButton(text="RU", callback_data='ru')
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer("Что хочешь купить? ",reply_markup=keyboard)

@router.callback_query(F.data.in_({'euro','dollar','ru'}))
async def currency(callback: types.CallbackQuery):
    print(callback.data , callback.chat_instance)
    items04 = ['0','1','2','3','4']
    items59 = ['5','6','7','8','9']
    kb = [
        [InlineKeyboardButton(text= item, callback_data=item) for item in items04 ],
        [InlineKeyboardButton(text=item, callback_data=item) for item in items59 ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.answer(f'Cколько {callback.data}?', reply_markup=keyboard)
