from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from marketdb import db
from callbacks.delete_callback import DelCallback

def inline_list_kb():
    builder = InlineKeyboardBuilder()
    for titles in db.get_title_list():
        builder.button(
            text=titles,
            callback_data=DelCallback(action="delete", title=titles)
        )
    builder.adjust(1)
    return builder.as_markup()
