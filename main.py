import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from API.cats import SmileApi
from config import config
from handlers import common
from keyboards.menu import main_menu_command
from middleware.api import WaifuApiMiddleWare


def register_all_routers(dp: Dispatcher):
    dp.include_router(common.common_router)


def register_all_middlewares(dp: Dispatcher, waifu_api: SmileApi):
    waifu_api_middleware = WaifuApiMiddleWare(waifu_api)
    dp.update.middleware(waifu_api_middleware)


async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher(storage=MemoryStorage())

    register_all_routers(dp)

    waifu_api = SmileApi()

    register_all_middlewares(dp, waifu_api)

    try:
        print('Bot Started')
        await bot.set_my_commands(main_menu_command)
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')