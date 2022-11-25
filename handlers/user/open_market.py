from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery

from marketdb.database import db
from keyboards.default.select_product import select_product_kb
from keyboards.default.open_market import open_market_kb
from keyboards.inline.go_back import go_back_to_market_kb

router = Router()

@router.message(text="Открыть магазин")
async def open_market(message: Message):
    await message.answer("<b>СПИСОК ПАКОВ</b>, используйте кнопки для выбора", reply_markup=select_product_kb(), parse_mode="HTML")
    await message.answer(db.show_products(),reply_markup=go_back_to_market_kb(), parse_mode="HTML")

@router.callback_query(text="go_back")
async def go_back_to_market(callback: CallbackQuery, bot: Bot):
    await callback.message.answer("Вы вернулись на главную страницу",reply_markup=open_market_kb())
