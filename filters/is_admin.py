from typing import Union

from aiogram.dispatcher.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    '''
    filter for handling messages from users who are in the admin list
    '''
    user_id: Union[int, list]

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.user_id, int):
            return message.from_user.id == self.user_id
        else:
            return message.from_user.id in self.user_id
