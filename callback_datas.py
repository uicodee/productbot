from aiogram.filters.callback_data import CallbackData


class CallbackDataProduct(CallbackData, prefix="product"):
    product_id: int
