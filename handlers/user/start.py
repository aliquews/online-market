from aiogram import Router
from aiogram.types import Message

from marketdb import db
from config import include_sticker
from keyboards.default.open_market import open_market_kb


router = Router()

@router.message(
    commands=['start'],
)
async def cmd_start(message: Message):
    db.append_user(message.from_user.id)
    await message.answer_sticker(include_sticker, reply_markup=open_market_kb())
