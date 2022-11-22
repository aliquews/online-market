from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from marketdb.database import db

def select_product_kb():
    kb = ReplyKeyboardBuilder()
    for button in db.show_products().split("\n\n"):
        kb.add(KeyboardButton(text=button))
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
