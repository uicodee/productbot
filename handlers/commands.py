from datetime import datetime

from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from api.api import get_products
from keyboards import products_menu
import random

from state import NumberForm

router = Router()


@router.message(Command(commands=['start']))
async def on_cmd_start(message: types.Message) -> None:
    products = await get_products()
    await message.answer(
        text="Salom",
        reply_markup=products_menu(products=products)
    )


@router.message(Command(commands=['random']))
async def on_cmd_random(message: types.Message) -> None:
    number = random.randint(1, 1000)
    await message.answer(
        text=f"Tasodifiy son: {number}"
    )


@router.message(Command(commands=['time']))
async def on_cmd_time(message: types.Message) -> None:
    current_date = datetime.now().strftime("%H:%M:%S")
    await message.answer(
        text=current_date
    )


@router.message(Command(commands=['number']))
async def on_cmd_number(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        text="Birinchi raqamni kiriting"
    )
    await state.set_state(NumberForm.first_number)
