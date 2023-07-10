from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN_API = '6330955424:AAHGU6hlgJXemKSYUOd3YKX8CS6mMWDFxZY'
storage = MemoryStorage()
bot = Bot(TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)

support_ids = [
    1064938479
]