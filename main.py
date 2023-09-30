import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN

from handlers.commands import router as command_router
from handlers.callbacks import router as callback_router


dp = Dispatcher()


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp.include_router(command_router)
    dp.include_router(callback_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())