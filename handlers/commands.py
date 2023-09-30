from aiogram import Router, F, types
from aiogram.filters import Command

from api.api import get_products
from keyboards import products_menu

router = Router()


@router.message(Command(commands=['start']))
async def on_cmd_start(message: types.Message) -> None:
    products = get_products()
    await message.answer(
        text="Salom",
        reply_markup=products_menu(products=products)
    )
