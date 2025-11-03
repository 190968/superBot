from aiogram import Router, F, html
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.for_my_main import get_yes_no_kb
router = Router()

@router.message(Command("coord"))
async def coord(message: Message):
    
    await  message.answer(f"Привет мой друг ,{ html.bold(message.from_user.full_name) }!",reply_markup=get_yes_no_kb())