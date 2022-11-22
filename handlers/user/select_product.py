import random
from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery
from pyqiwip2p import QiwiP2P


from marketdb.database import db
from keyboards.inline.buy_menu import buy_menu_kb
from keyboards.default.open_market import open_market_kb
from config import QIWI_TOKEN


router = Router()
p2p = QiwiP2P(auth_key=QIWI_TOKEN)

@router.message()
async def selecting_product(message: Message):
    if message.text in db.show_products().split("\n\n"):
        price = db.select_product_price(message.text)
        bill_id = str(message.from_user.id) + str(random.randint(100000,1000000))
        user_bill = p2p.bill(bill_id=bill_id, amount=price, lifetime=10)
        db.append_bill(message.from_user.id, bill_id, db.select_content(message.text))
        await message.answer("Вы выбрали пак, чтобы оплатить нажмите на кнопку <b>Совершить платеж</b>, после оплаты проверьте статус платежа кнопкой <b>Проверка платежа</b>. Если же вы передумали покупать, нажмите на кнопку <b>Отменить платеж</b>", reply_markup=buy_menu_kb(user_bill.pay_url), parse_mode="HTML")

@router.callback_query(text="check")
async def check_pay(callback: CallbackQuery, bot: Bot):
    # WAITING EXPIRED PAID
    bill_id = db.show_bill(callback.message.chat.id)
    pass
    if p2p.check(bill_id=bill_id).status == "WAITING":
        await callback.message.answer("Платеж ожидает оплаты")
    if p2p.check(bill_id=bill_id).status == "EXPIRED":
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await callback.message.answer("Срок платежа истек", reply_markup=open_market_kb())
    if p2p.check(bill_id=bill_id).status == "PAID":
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await callback.message.answer("Платеж прошел успешно! Спасибо за покупку")
        await callback.message.answer(f"Ссылка на пак:\n{db.show_content(bill_id)}", reply_markup=open_market_kb())
        p2p.reject(bill_id)
        db.del_bill(bill_id)


@router.callback_query(text="cancel")
async def cancel_pay(callback: CallbackQuery, bot: Bot):
    bill_id = db.show_bill(callback.message.chat.id)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer("Платеж отменен", reply_markup=open_market_kb())
    p2p.reject(bill_id)
    db.del_bill(bill_id)
