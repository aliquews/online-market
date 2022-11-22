from typing import Union

from aiogram.dispatcher.filters import BaseFilter
from aiogram.types import Message

class IsDigit(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text.isdigit()
