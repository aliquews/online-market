import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import setup_routers
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    routers = setup_routers()
    dp.include_router(routers)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
