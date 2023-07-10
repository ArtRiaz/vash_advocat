from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.reply import kb_menu, get_kb_menu, get_back
from aiogram.dispatcher.filters import Text
import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

async def about(message: types.Message):
    with open('about_me.jpg', 'rb') as photo1:
        markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[
            InlineKeyboardButton(text='Сертіфікати', callback_data='sertific')
        ]])
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo1,
                             caption=f"<b>Давайте знайомитись!\n"
                                     "\n"
                                     "Мене звати Реу Руслан Васильович, і я є практикуючим адвокатом у місті Одесі та "
                                     "Одеській області з понад 6-річним "
                                     "досвідом роботи в даній професії.\n "
                                     "У моїй практиці я використовую індивідуальний підхід до кожного клієнта та не "
                                     "обмежуюсь застосуванням практичного досвіду, але використовую креативність для "
                                     "вирішення правових проблем.\n "
                                     "Мій досвід роботи в правоохоронних органах дає мені можливість оцінити ситуацію "
                                     "клієнта у кримінальному процесі “зсередини”, прогнозувати можливий розвиток "
                                     "подій та вибудовувати стратегію та тактику захист</b>",
                             reply_markup=get_back())
        await bot.send_message(chat_id=message.from_user.id, text="<b>Я отримав освіту в Ізмаїльському інституті Водного транспорту та Одеському "
                                     "національному університеті ім. І.І. Мечникова, де здобув кваліфікацію бакалавра "
                                     "та спеціаліста з правознавства. Моя дипломна робота була присвячена 'Злочинам "
                                     "проти власності'.\n "
                                     "З 2017 року я займаюсь індивідуальною адвокатською діяльністю та маю свідоцтво "
                                                                 "про право на заняття адвокатською діяльністю. Моя "
                                                                 "спеціалізація включає кримінальне право, "
                                                                 "цивільне право, адміністративне право, справи про "
                                                                 "адміністративні правопорушення та господарське "
                                                                 "право.</b>", reply_markup=markup)


async  def sertificat(callback: CallbackQuery):
    await callback.bot.send_message(chat_id=callback.from_user.id, text='Мої сертифікати:', reply_markup=get_back())
    with open('sert1.jpg', 'rb') as photo1:
        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo1)
        await asyncio.sleep(2)
    with open('sert2.jpg', 'rb') as photo2:
        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo2)
        await asyncio.sleep(2)
    with open('sert3.jpg', 'rb') as photo3:
        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo3)



def register_handlers_about(dp: Dispatcher):
    dp.register_message_handler(about, Text(equals='Про мене'))
    dp.register_callback_query_handler(sertificat, text='sertific')
