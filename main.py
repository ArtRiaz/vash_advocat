import asyncio
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage

import create_bot
from create_bot import load_config
from aiogram import Bot, Dispatcher
from middleware.anti_time import Anti_time
from handlers import start, services, back_menu, about_me, question, contact, registr
from utils.set_command_default import set_commands
from utils.admin_panel import register_handlers_admin
from aiogram import types
from utils.mailing import register_handler_mailing
logger = logging.getLogger(__name__)

config = load_config()

def register_all_middleware(dp):
    dp.setup_middleware(Anti_time())


# def register_all_fillters(dp):
#     dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    start.register_handlers_start(dp)
    services.register_service(dp)
    back_menu.register_handler_back(dp)
    about_me.register_handlers_about(dp)
    question.question_menu(dp)
    contact.register_handler_contact(dp)
    registr.handlers_form(dp)
    register_handlers_admin(dp)
    register_handler_mailing(dp)


async def startup(bot: Bot):
    await set_commands(bot)
    await bot.send_message(chat_id=config.tg_bot.admin_ids, text='Бот запущен')

async def main():
    logging.basicConfig(
            level=logging.INFO,
            format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s'
        )

    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config  # доставать config из переменной bot, если в handler я хочу достать что то из Config
    # я делаю => bot.get("config")

    register_all_middleware(dp)
    #    register_all_fillters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await dp.bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stop")
