import asyncio

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from data.database import load_config, User, DBCommands
from keyboards.inline_question import back_admin_panel


db = DBCommands()
config = load_config()
bot = Bot(config.tg_bot.token)
dp = Dispatcher(bot)


class Mailing(StatesGroup):
    Text = State()
    state = State()
    photo = State()

async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Ви відмінили введення текста")
    await state.reset_state()

async def send_all(call: types.CallbackQuery):
    await call.message.answer(f'Введіть текст розсилки або натисніть /cancel:')
    await Mailing.Text.set()


async def mailing_text(message: types.Message, state: FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[
        InlineKeyboardButton(text='Додати фото', callback_data='add_photo'),
        InlineKeyboardButton(text='Далі', callback_data='next'),
        InlineKeyboardButton(text='Відмінить', callback_data='quit')
    ]])
    await state.update_data(text=answer)
    await message.answer(text=answer, reply_markup=markup)
    await Mailing.state.set()


async def next_time(callback: CallbackQuery, state: FSMContext):
    all_user_ids = await db.get_all_user_ids()

    data = await state.get_data()
    text = data.get('text')
    await state.finish()

    for user in all_user_ids:
        await dp.bot.send_message(chat_id=user, text=text)
        await asyncio.sleep(0.33)
    await callback.message.answer('Розсилка виконана', reply_markup=back_admin_panel())


async def add_photo(callback: CallbackQuery):
    await callback.message.answer('Прийшліть фото')
    await Mailing.photo.set()


async def mailing_send(message: types.Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[
        InlineKeyboardButton(text='Далі', callback_data='next'),
        InlineKeyboardButton(text='Відмінить', callback_data='quit')
    ]])
    await message.answer_photo(photo=photo, caption=text, reply_markup=markup)


async def start_next(callback: CallbackQuery, state: FSMContext):
    all_user_ids = await db.get_all_user_ids()

    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await state.finish()

    for user in all_user_ids:
        await dp.bot.send_photo(chat_id=user, photo=photo, caption=text)
        await asyncio.sleep(0.33)
    await callback.message.answer('Розсилка виконана', reply_markup=back_admin_panel())


async def no_photo(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[
        InlineKeyboardButton(text='Відмінить', callback_data='quit')
    ]])
    await message.answer('Прийшліть фото', reply_markup=markup)


async def quit_send(callback: CallbackQuery, state: FSMContext):
    await state.finish()
    await callback.message.answer('Розсилка відмінена')


def register_handler_mailing(dp: Dispatcher):
    dp.register_message_handler(cancel, commands=["cancel"], state=Mailing)
    dp.register_callback_query_handler(send_all, text='send')
    dp.register_message_handler(mailing_text, state=Mailing.Text)
    dp.register_callback_query_handler(next_time, text='next', state=Mailing.state)
    dp.register_callback_query_handler(add_photo, text='add_photo', state=Mailing.state)
    dp.register_message_handler(mailing_send, state=Mailing.photo, content_types=types.ContentType.PHOTO)
    dp.register_message_handler(no_photo, state=Mailing.photo)
    dp.register_callback_query_handler(quit_send, text='quit',
                                       state=[Mailing.Text, Mailing.photo, Mailing.state])
    dp.register_callback_query_handler(start_next, text='next', state=Mailing.photo)

