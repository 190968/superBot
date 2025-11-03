from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message,BackgroundFill
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.utils.formatting import as_line, Text, Bold
from aiogram.enums import ParseMode
router = Router()

@router.message(Command("help"))
async def help(message: Message):
    msg = text('<b>Я могу ответить на следующие команды :</b> \n',
              '/exchange - обмен валюты,\n /photo - просмотр фото ,'              
              '\n /hello - приветствие,\n /coord - координаты,\n /info' )
    await message.answer(msg, parse_mode=ParseMode.HTML)
