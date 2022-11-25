from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.fsm.context import FSMContext

from filters.is_digit import IsDigit
from states.set_product import SetProduct
from marketdb.database import db

router = Router()


@router.callback_query(text="append_product")
async def update_products(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer("Напиши мне описание продукта\nПример:<i>ПАКИ titlename 50пикч</i>", parse_mode="HTML")
    await state.set_state(SetProduct.title)

@router.message(SetProduct.title)
async def setting_title(message: Message, state: FSMContext):
    await state.update_data(title=message.html_text)
    await message.answer(
        text = "Теперь укажи цену в рублях",
    )
    await state.set_state(SetProduct.price)

@router.message(
    IsDigit(),
    SetProduct.price,
)
async def setting_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer(
        text="Ссылку на пак",
    )
    await state.set_state(SetProduct.content)

@router.message(
    SetProduct.price,
)
async def setting_price_incorrectly(message: Message):
    await message.answer(
        "<b>Цена должна быть числом</b>",
        parse_mode="HTML"
    )

@router.message(SetProduct.content)
async def setting_content(message: Message, state: FSMContext):
    await state.update_data(content=message.text)
    data = await state.get_data()
    db.append_product(data)
    await message.answer(
        text="Продукт добавлен",
    )
    await state.clear()
