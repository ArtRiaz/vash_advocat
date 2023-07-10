from create_bot import dp, bot
from handlers import start, services, back_menu, about_me, question, contact, registr
from utils.set_command_default import set_commands
from aiogram import types, executor


async def on_startup(_):
    print("Бот запущен")
    await set_commands(bot=bot)


start.register_handlers_start(dp)
services.register_service(dp)
back_menu.register_handler_back(dp)
about_me.register_handlers_about(dp)
question.question_menu(dp)
contact.register_handler_contact(dp)
registr.handlers_form(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
