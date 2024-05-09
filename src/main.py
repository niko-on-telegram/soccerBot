import asyncio
import logging.config
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.basic_handlers import router as base_router
from handlers.errors_handler import router as errors_router
from middlewares.updates_dumper_middleware import UpdatesDumperMiddleware
from settings import get_logging_config, get_settings


async def main():
    logs_directory = Path("logs")
    logs_directory.mkdir(parents=True, exist_ok=True)
    logging_config = get_logging_config('bot')
    logging.config.dictConfig(logging_config)
    settings = get_settings()
    bot = Bot(token=settings.TOKEN.get_secret_value(), parse_mode=ParseMode.MARKDOWN)
    logging.info("bot started")
    storage = MemoryStorage()
    dispatcher = Dispatcher(storage=storage, target_channel_id=settings.TARGET_CHANNEL_ID)
    dispatcher.update.outer_middleware(UpdatesDumperMiddleware())
    dispatcher.include_routers(base_router, errors_router)
    await dispatcher.start_polling(bot)


def run_main():
    asyncio.run(main())


if __name__ == '__main__':
    run_main()
