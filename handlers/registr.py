import asyncio
import pytz

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentType
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.reply import kb_menu, get_kb_menu, get_back
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from create_bot import load_config
from data.database import RegisterUser
import datetime
config = load_config()


class RoomOrder(StatesGroup):
    name = State()
    phone = State()
    email = State()
    comentariy = State()

async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Ви відмінили регістрацію")
    await state.reset_state()

async def order_start(call: types.CallbackQuery):
    await RoomOrder.name.set()
    await call.message.answer(
        '<b>Залиште свої контакти і я звʼяжуся з Вами найближчим часом для обговорення всіх питань чи '
        'призначення зустрічі</b>')
    await call.message.answer(f"Введить своє ім'я або нажміть /cancel")


async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    register = RegisterUser()
    register.name = name
    await RoomOrder.next()
    await state.update_data(register=register)
    await message.reply("Введіть свій контактний номер телефону або нажміть /cancel")


async def get_phone(message: types.Message, state: FSMContext):
    if all(c.isdigit() or c == "+" for c in message.text):  # проверка на цифры и символ +
        phone = message.text
        data = await state.get_data()
        register: RegisterUser = data.get("register")
        register.phone = phone
        await state.update_data(register=register)
        await RoomOrder.next()
        await message.answer("Введиіть свій e-mail:\n"
                             "Якщо ви немаєте email напишить @ або нажміть /cancel")
    else:
        await message.answer("Введить вірний номер")


async def get_email(message: types.Message, state: FSMContext):
    if "@" in message.text:
        email = message.text
        data = await state.get_data()
        register: RegisterUser = data.get("register")
        register.email = email
        await state.update_data(register=register)
        await RoomOrder.next()
        await message.answer("Короткий коментар або нажміть /cancel ")
    else:
        await message.answer("Введить вірний email, чи напишить @ ")


async def get_coment(message: types.Message, state: FSMContext):
    coment = message.text
    data = await state.get_data()
    register: RegisterUser = data.get("register")
    register.coment = coment
    await state.update_data(register=register)
    await register.create()

    await message.bot.send_message(chat_id=message.from_user.id,
                                   text=f"Ваша запис пройшов успішно! Я з вами зв'яжусь "
                                        f"найблищим часом\n"
                                        f" Ваше ім'я: {register.name}\n"
                                        f" Ваш номер телефону: {register.phone}\n"
                                        f"Ваш e-mail: {register.email}\n"
                                        f"Коментар: {register.coment}")

    await message.bot.send_message(chat_id=message.from_user.id,
                                   text="Оплатити консультацію, чи внести передоплату,\n"
                                        " ви зможите за реквізитами картки: <b>PrivatBank: 5168745611616886</b>",
                                   reply_markup=get_back())

    await message.bot.send_message(chat_id=config.tg_bot.admin_ids,
                                   text=f"Сьогодні {datetime.datetime.now(tz=pytz.timezone('Europe/Kiev'))}\n"
                                        f"Прийшов запит на консультацію\n"
                                        f"Ім'я: {register.name}\n"
                                        f"Номер телефону: {register.phone}\n"
                                        f"E-mail: {register.email}\n"
                                        f"Коментар: {register.coment}")

    await state.finish()


def handlers_form(dp: Dispatcher):
    dp.register_message_handler(cancel, commands=["cancel"], state=RoomOrder)
    dp.register_callback_query_handler(order_start, text='consultasion', state=None)
    dp.register_message_handler(get_name, state=RoomOrder.name)
    dp.register_message_handler(get_phone, state=RoomOrder.phone)
    dp.register_message_handler(get_email, state=RoomOrder.email)
    dp.register_message_handler(get_coment, state=RoomOrder.comentariy)
