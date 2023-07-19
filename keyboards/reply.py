from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def kb_menu():
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Меню', callback_data='menu')
    ]])

    return kb


def get_kb_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Послуги')
    ], [
        KeyboardButton('Про мене')
    ], [
        KeyboardButton('Питання')
    ], [
        KeyboardButton('Замовити консультацію')
    ], [
        KeyboardButton('Контакти')
    ]

    ])

    return kb


def get_back():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Назад в главное меню')
    ]])

    return kb
