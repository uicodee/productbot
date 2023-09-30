from aiogram import Router, types
from aiogram.utils.text_decorations import html_decoration as hd

from api.api import get_single_product
from callback_datas import CallbackDataProduct
from keyboards import back

router = Router()


@router.callback_query(CallbackDataProduct.filter())
async def on_product(callback: types.CallbackQuery, callback_data: CallbackDataProduct) -> None:
    data = get_single_product(product_id=callback_data.product_id)
    await callback.message.edit_text(
        text=f"Name: {data.get('title')}\n"
             f"Price: ${data.get('price')}\n"
             f"Image: {data.get('thumbnail')}",
        reply_markup=back()
    )


