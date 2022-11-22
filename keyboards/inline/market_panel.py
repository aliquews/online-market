from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def market_panel_kb():
    inline_kb = InlineKeyboardBuilder()
    inline_kb.add(
        InlineKeyboardButton(
            text="Добавить продукт",
            callback_data="append_product",
        )
    )
    return inline_kb.as_markup()
