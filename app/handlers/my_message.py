from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def message_text(message: Message):
    await  message.answer("Hello friend")