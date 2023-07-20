from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def kb_menu():
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Меню', callback_data='menu')
    ]])

    return kb


def get_kb_menu():
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Послуги', callback_data="service"),
        InlineKeyboardButton('Про мене', callback_data="about"),
        InlineKeyboardButton('Питання', callback_data="questions")
    ],

     [
        InlineKeyboardButton('Замовити консультацію', callback_data="consultasion")
    ], [
        InlineKeyboardButton('Контакти', callback_data="contact")
    ]

    ])

    return kb


def get_back():
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Назад у головне меню', callback_data='back_menu')
    ]])

    return kb
