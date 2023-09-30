from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_datas import CallbackDataProduct


def products_menu(products: list[dict]) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for product in products:
        builder.button(
            text=product['title'],
            callback_data=CallbackDataProduct(product_id=product['id'])
        )
    builder.adjust(2)
    return builder.as_markup()


def back() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="Back", callback_data="back")
    )
    return builder.as_markup()
