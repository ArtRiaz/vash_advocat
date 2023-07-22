import asyncio

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentType
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.reply import kb_menu, get_kb_menu, get_back
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from create_bot import load_config


config = load_config()
class RoomOrder(StatesGroup):
    name = State()
    phone = State()
    email = State()
    comentariy = State()


async def order_start(call: types.CallbackQuery):
    await RoomOrder.name.set()
    await call.message.answer(
        '<b>Залиште свої контакти і я звʼяжуся з Вами найближчим часом для обговорення всіх питань чи '
        'призначення зустрічі</b>')
    await call.message.answer(f"Введить своє ім'я: ")


async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await RoomOrder.next()
    await message.reply("Введіть свій контактний номер телефону: ")


async def get_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone"] = message.text
    await RoomOrder.next()
    await message.answer("Введиіть свій e-mail: ")


async def get_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["email"] = message.text
    await RoomOrder.next()
    await message.answer("Короткий коментар: ")


async def get_coment(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["comentariy"] = message.text
        com = data["comentariy"]
        name = data["name"]
        phone = data["phone"]
        email = data["email"]

        await message.bot.send_message(chat_id=message.from_user.id,
                                       text=f"Ваша запис пройшов успішно! Я з вами зв'яжусь "
                                            f"найблищим часом\n"
                                            f" Ваше ім'я: {name}\n"
                                            f" Ваш номер телефону: {phone}\n"
                                            f"Ваш e-mail: {email}\n"
                                            f"Коментар: {com}")


        await message.bot.send_message(chat_id=message.from_user.id,
                                       text="Оплатити консультацію, чи внести передоплату,\n"
                                            " ви зможите за реквізитами картки: 42424242424242",
                                       reply_markup=get_back())

        await message.bot.send_message(chat_id=config.tg_bot.admin_ids,
                                       text=f"Прийшов запит на консультацію\n"
                                            f"Ім'я: {name}\n"
                                            f"Номер телефону: {phone}\n"
                                            f"E-mail: {email}\n"
                                            f"Коментар: {com}")

        await state.finish()


def handlers_form(dp: Dispatcher):
    dp.register_callback_query_handler(order_start, text='consultasion', state=None)
    dp.register_message_handler(get_name, state=RoomOrder.name)
    dp.register_message_handler(get_phone, state=RoomOrder.phone)
    dp.register_message_handler(get_email, state=RoomOrder.email)
    dp.register_message_handler(get_coment, state=RoomOrder.comentariy)
