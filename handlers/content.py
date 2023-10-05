from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from keyboards import actions
from state import NumberForm

router = Router()


@router.message(NumberForm.first_number)
async def on_first_number(message: types.Message, state: FSMContext) -> None:
    number = message.text
    # {'number': 1000}
    await message.answer(
        text="Ikkinchi sonni kiriting"
    )
    await state.update_data(first_number=number)
    await state.set_state(NumberForm.second_number)


@router.message(NumberForm.second_number)
async def on_second_number(message: types.Message, state: FSMContext) -> None:
    number = message.text
    await message.answer(
        text="Amallarni tanlang",
        reply_markup=actions()
    )
    await state.update_data(second_number=number)
