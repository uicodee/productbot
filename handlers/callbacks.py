from aiogram import Router, types , F
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hide_link
from aiogram.utils.text_decorations import html_decoration as hd
from keyboards import products_menu
from api.api import get_products
from api.api import get_single_product
from callback_datas import CallbackDataProduct
from keyboards import back

router = Router()


@router.callback_query(CallbackDataProduct.filter())
async def on_product(callback: types.CallbackQuery, callback_data: CallbackDataProduct) -> None:
    data = await get_single_product(product_id=callback_data.product_id)
    await callback.message.edit_text(
        text=f"Name: {data.get('title')}\n"
             f"Price: ${data.get('price')}\n"
             f"{hide_link(data.get('thumbnail'))}",
        reply_markup=back()
    )


@router.callback_query(F.data == "back")
async def on_back(callback: types.CallbackQuery) -> None:
    products = await get_products()
    await callback.message.edit_text(
        text="Salom",
        reply_markup=products_menu(products=products)
    )


@router.callback_query(F.data == "plus")
async def on_plus(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    first_number = int(data.get('first_number'))
    second_number = int(data.get('second_number'))
    await callback.message.edit_text(
        text=f"{first_number} + {second_number} = {first_number + second_number}"
    )
