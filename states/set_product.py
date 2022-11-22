from aiogram.dispatcher.fsm.state import StatesGroup, State

class SetProduct(StatesGroup):
    title = State()
    price = State()
    content = State()
