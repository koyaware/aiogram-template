import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from tgbot.config import BOT_TOKEN, storage
from tgbot.handlers import register_all_handlers

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    dp = Dispatcher(storage=storage)
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

    register_all_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")