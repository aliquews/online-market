from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery

from marketdb.database import db
from callbacks.delete_callback import DelCallback
from keyboards.inline.inline_list import inline_list_kb


router = Router()


@router.callback_query(text="delete_product")
async def selecting_prod(callback: CallbackQuery, bot: Bot):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer("<b>выбери удаляемый пак из списка</b>",reply_markup=inline_list_kb(), parse_mode="HTML")

@router.callback_query(DelCallback.filter())
async def delete_product(callback: CallbackQuery, callback_data: DelCallback, bot: Bot):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    match callback_data.action:
        case "delete":
            db.del_product(callback_data.title)
            await callback.message.answer("пак удален")
