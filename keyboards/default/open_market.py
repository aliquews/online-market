from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def open_market_kb():
    kb = ReplyKeyboardBuilder()
    kb.add(KeyboardButton(text="Открыть магазин"))
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
