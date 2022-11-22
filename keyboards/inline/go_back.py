from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def go_back_to_market_kb():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Вернуться назад",
        callback_data="go_back",
    ))
    return kb.as_markup()
