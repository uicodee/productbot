from aiogram.fsm.state import StatesGroup, State


class NumberForm(StatesGroup):

    first_number = State()
    second_number = State()
