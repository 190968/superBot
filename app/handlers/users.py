from aiogram import Router, F, html, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
from keyboards.for_my_main import get_yes_no_kb
router = Router()

@router.message(Command('users'))
async def chat_member_handler(message: Message ):
    print(message.answer)