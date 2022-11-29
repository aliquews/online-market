from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def market_panel_kb():
    inline_kb = InlineKeyboardBuilder()
    inline_kb.add(
        InlineKeyboardButton(
            text="Добавить пак",
            callback_data="append_product",

        )
    )
    inline_kb.add(
        InlineKeyboardButton(
            text="Удалить пак",
            callback_data="delete_product",

        )
    )
    inline_kb.add(
        InlineKeyboardButton(
            text="Закрыть панель",
            callback_data="back",
        )
    )
    inline_kb.adjust(2)
    return inline_kb.as_markup()
