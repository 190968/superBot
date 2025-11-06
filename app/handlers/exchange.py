from aiogram import Router, F, html, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram import Bot, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup, InlineKeyboardBuilder

router = Router()
dp = Dispatcher()
count = []
mycurrency = []
@router.message(Command("exchange"))
async def selector(message: types.Message):
    mycurrency.clear()
    count.clear()
    kb = [
        [
            InlineKeyboardButton(text="buy currency", callback_data='buy'),
            InlineKeyboardButton(text="view exchange rate ", callback_data='view'),
            InlineKeyboardButton(text="view my exchange", callback_data='mybuy'),
            
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(f'Что хочешь сделать {message.from_user.first_name}?',reply_markup=keyboard)

@router.callback_query(F.data == 'buy')
async def change_currency(callback: types.CallbackQuery):
   
    kb = [
        [
            InlineKeyboardButton(text="€", callback_data='euro'),
            InlineKeyboardButton(text="$", callback_data='dollar'),
            InlineKeyboardButton(text="RUB", callback_data='ruble'),
            InlineKeyboardButton(text="BLR", callback_data='blr')
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text('Что хочешь обменять ?',reply_markup=keyboard)

@router.callback_query(F.data == 'view')
async def change_currency(callback: types.CallbackQuery):   
    text = (
        "<b>Today currency rates</b>\n"
        "<pre>currency | $     | Euro\n"
        "$        | 1     | 0.86\n"
        "euro     | 1.23  | 1</pre>"
    )
    await callback.message.edit_text(text, parse_mode="HTML")

@router.callback_query(F.data.in_({'euro','dollar','ruble','blr'}))
async def currency(callback: types.CallbackQuery):
    mycurrency.append(callback.data)
    items04 = ['0','1','2','3','4']
    items59 = ['5','6','7','8','9']
    kb = [
        [InlineKeyboardButton(text= item, callback_data=item) for item in items04 ],
        [InlineKeyboardButton(text=item, callback_data=item) for item in items59 ],
       
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f'How maths {callback.data}?', reply_markup=keyboard)


@router.callback_query(F.data.in_({'0','1','2','3','4','5','6','7','8','9'}))
async def currency(callback: types.CallbackQuery):
    if callback.data == '0' and len(count) == 0:
        return
    count.append(callback.data)
    items04 = ['0','1','2','3','4']
    items59 = ['5','6','7','8','9']
    kb = [
        [InlineKeyboardButton(text= item, callback_data=item) for item in items04 ],
        [InlineKeyboardButton(text=item, callback_data=item) for item in items59 ],
        [InlineKeyboardButton(text="OK", callback_data='100')],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f'{"".join(count)}', reply_markup=keyboard)
   
@router.callback_query(F.data.in_({'100'}))
async def mycount(callback: types.CallbackQuery):
    print(f'result : {"".join(count)}')
    kb = [       
        [InlineKeyboardButton(text="YES", callback_data='YES'),
        InlineKeyboardButton(text="NO", callback_data='NO')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f' {"".join(count)} {mycurrency[0]}',reply_markup=keyboard)

@router.callback_query(F.data.in_({'100'}))
async def mycount(callback: types.CallbackQuery):
    print(f'result : {"".join(count)}')
    kb = [       
        [InlineKeyboardButton(text="YES", callback_data='YES'),
        InlineKeyboardButton(text="NO", callback_data='NO')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f' {"".join(count)} {mycurrency[0]}',reply_markup=keyboard)   