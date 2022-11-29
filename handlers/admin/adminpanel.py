from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery

from filters.is_admin import IsAdmin
from keyboards.default.open_market import open_market_kb
from keyboards.inline.market_panel import market_panel_kb

router = Router()
@router.message(
    IsAdmin(user_id=[416493063, 407108391]),
    commands=['market'],
)
async def show_products(message: Message):
    await message.answer("<b>management market panel</b>", reply_markup=market_panel_kb(), parse_mode="HTML")

@router.callback_query(text="back")
async def close_panel(callback: CallbackQuery, bot: Bot):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer("Панель закрыта",reply_markup=open_market_kb())
