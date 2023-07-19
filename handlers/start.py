from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from keyboards.reply import kb_menu, get_kb_menu, get_back


async def cmd_start(message: types.Message):
    with open('start_adv.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption=f'<b> Вітаю Вас, {message.from_user.full_name}!\n </b>'
                                     f'Юридична допомога та розробка шляхів вирішення проблеми\n'
                                     f'Я ставлю клієнта на перше місце на шляху до справедливості.\n'
                                     f'Ви отримуєте необхідну підтримку в якої зацікавлені в боротьбі за свої права.'
                             , reply_markup=kb_menu())


async def cmd_menu(call: types.CallbackQuery):
    await call.message.answer('Управління меню', reply_markup=get_kb_menu())


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_callback_query_handler(cmd_menu, Text(equals='Меню'))
