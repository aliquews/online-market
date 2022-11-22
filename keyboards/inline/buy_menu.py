from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def buy_menu_kb(url:str):
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Совершить платеж",
            url=url,
        )
    )
    kb.add(
        InlineKeyboardButton(
            text="Проверка платежа",
            callback_data="check",
        )
    )
    kb.add(
        InlineKeyboardButton(
            text="Отменить платеж",
            callback_data="cancel",
        )
    )
    kb.adjust(1)
    return kb.as_markup()
