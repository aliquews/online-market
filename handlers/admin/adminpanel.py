from aiogram import Router
from aiogram.types import Message

from filters.is_admin import IsAdmin
from keyboards.inline.market_panel import market_panel_kb

router = Router()
@router.message(
    IsAdmin(user_id=[416493063, 407108391]),
    commands=['market'],
)
async def show_products(message: Message):
    await message.answer("<b>management market panel</b>", reply_markup=market_panel_kb(), parse_mode="HTML")
