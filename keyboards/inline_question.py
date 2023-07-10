from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ikb_contact():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Мій сайт', url='https://www.advokat-reu.com/')
    ], [InlineKeyboardButton('ryslanrey76@gmail.com', url='ryslanrey76@gmail.com')], [
        InlineKeyboardButton('Геолокація', callback_data='Геолокация')
    ], [
        InlineKeyboardButton('Контактний номер', callback_data='Вызов')
     ]])

    return ikb


def ikb_question():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Як визначається гонорар адвоката?', callback_data="1")
    ], [InlineKeyboardButton('Чи інформуватимуть мене про хід справи?', callback_data="2")], [
        InlineKeyboardButton('Що таке конфлікт інтересів?', callback_data="3")
    ], [
        InlineKeyboardButton("Що виконувати адвокат у процесі співпраці?", callback_data="4")
    ], [
        InlineKeyboardButton("Чи можливе абонентське обслуговування?", callback_data="5")
    ]])

    return ikb


def back_quest():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Назад', callback_data="cancel")
    ]])

    return ikb
