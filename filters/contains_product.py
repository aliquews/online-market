from aiogram.dispatcher.filters import BaseFilter
from aiogram.types import Message


class ContainsIn(BaseFilter):
    '''
    filter to check the condition whether the product is in the list
    '''
    data: list

    async def __call__(self, message: Message) -> bool:
        return message.text in self.data
