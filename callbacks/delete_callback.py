from aiogram.dispatcher.filters.callback_data import CallbackData

class DelCallback(CallbackData, prefix="delete"):
    action: str
    title: str
