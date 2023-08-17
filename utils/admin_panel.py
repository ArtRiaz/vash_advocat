from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.reply import kb_menu, get_kb_menu, get_back
from data.database import DBCommands, create_db, User
from create_bot import load_config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
from keyboards.inline_question import back_admin_panel

db = DBCommands()
config = load_config()


def menu_admin():
    markup = InlineKeyboardMarkup(inline_keyboard=True).add(
        InlineKeyboardButton('Розсилання', callback_data='send')).add(
        InlineKeyboardButton('Список вхідних користувачів',
                             callback_data='list_users')).add(
        InlineKeyboardButton("Список заявок на консультацию", callback_data='list_contacts')).add(
        InlineKeyboardButton("Інструкція для адміна", callback_data="instr_admin")
    )
    return markup


async def admin(message: types.Message):
    await message.answer(text="Вітаю тебе адміністратор!\n"
                              "Це панель управління та статистики.\n"
                              "Виберить потрибну кнопку нище 👇",
                         reply_markup=menu_admin())
    await message.edit_reply_markup()


async def show_list(call: types.CallbackQuery):
    all_users = await db.show_users()
    for users in all_users:
        text = "Ім'я: {full_name} Никнєйм: {username}"
        await call.message.answer(
            text=text.format(
                full_name=users.full_name,
                username=users.username
            ))
    await call.message.answer("Щоб повернутись нажміть назад", reply_markup=back_admin_panel())


async def show_contacts(call: types.CallbackQuery):
    all_contacts = await db.show_registr_users()
    for contact in all_contacts:
        text = "Ім'я: {name}\n" \
               "Номер телефону: {phone}\n" \
               "Email: {email}\n" \
               "Дата регистрації: {register_time}"
        await call.message.answer(
            text=text.format(
                name=contact.name,
                phone=contact.phone,
                email=contact.email,
                register_time=datetime.now()
            ))
    await call.message.answer("Щоб повернутись нажміть назад", reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton("Очистити список", callback_data="empty_list")
    ], [
        InlineKeyboardButton('Назад', callback_data="cancel_admin_menu")
    ]]))


async def empty_my_list(call: types.CallbackQuery):
    await db.empty_cart()
    await call.message.answer("Список видаленний")


async def cancel_admin_panel(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Відміна", reply_markup=menu_admin())


async def instruct_menu(call: types.CallbackQuery):
    await call.message.answer("Виберіть категорію для інструкцій: ",
                              reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
                                  InlineKeyboardButton("Інструкція розсилання", callback_data="inst_mail")
                              ], [
                                  InlineKeyboardButton("Інструкція Список вхідних користувачів",
                                                       callback_data="inst_users")
                              ], [
                                  InlineKeyboardButton("Інструкція Список заявок на консультацию",
                                                       callback_data="inst_contact")
                              ], [
                                  InlineKeyboardButton('Назад', callback_data="cancel_admin_menu")
                              ]]))




def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin, Text(equals='Admin'), user_id=config.tg_bot.admin_ids)
    dp.register_callback_query_handler(show_list, text='list_users', user_id=config.tg_bot.admin_ids)
    dp.register_callback_query_handler(show_contacts, text='list_contacts', user_id=config.tg_bot.admin_ids)
    dp.register_callback_query_handler(cancel_admin_panel, text="cancel_admin_menu", user_id=config.tg_bot.admin_ids)
    dp.register_callback_query_handler(empty_my_list, text="empty_list", user_id=config.tg_bot.admin_ids)
    dp.register_callback_query_handler(instruct_menu, text="instr_admin", user_id=config.tg_bot.admin_ids)

