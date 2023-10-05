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


def actions() -> types.InlineKeyboardMarkup:
    actions_list = {
        "+": "plus",
        "-": "minus",
        "*": "multiply",
        "/": "divide"
    }
    builder = InlineKeyboardBuilder()
    print(actions_list.values())
    for action, callback_data in actions_list.items():
        builder.row(
            types.InlineKeyboardButton(
                text=action,
                callback_data=callback_data
            )
        )
    builder.adjust(2)
    return builder.as_markup()
