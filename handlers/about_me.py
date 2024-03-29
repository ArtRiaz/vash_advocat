from aiogram import types, Dispatcher
import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from keyboards.reply import get_back

async def about(call: types.CallbackQuery):
    with open('about_me.jpg', 'rb') as photo1:
        await call.bot.send_photo(chat_id=call.from_user.id,
                                  photo=photo1,
                                  caption=f"<b>Давайте знайомитись!\n"
                                          "\n"
                                          "Мене звати Реу Руслан Васильович, і я є практикуючим адвокатом у місті "
                                          "Одесі та "
                                          "Одеській області з понад 6-річним "
                                          "досвідом роботи в даній професії.\n "
                                          "У моїй практиці я використовую індивідуальний підхід до кожного клієнта та "
                                          "не"
                                          "обмежуюсь застосуванням практичного досвіду, але використовую креативність "
                                          "для "
                                          "вирішення правових проблем.\n "
                                          "Мій досвід роботи в правоохоронних органах дає мені можливість оцінити "
                                          "ситуацію "
                                          "клієнта у кримінальному процесі 'зсередини', прогнозувати можливий розвиток "
                                          "подій та вибудовувати стратегію та тактику захист</b>"
                                  )
        await asyncio.sleep(0.33)
        await call.bot.send_message(chat_id=call.from_user.id,
                                    text="<b>Я отримав освіту в Ізмаїльському інституті Водного транспорту та Одеському"
                                         "національному університеті ім. І.І. Мечникова, де здобув кваліфікацію "
                                         "бакалавра"
                                         "та спеціаліста з правознавства. Моя дипломна робота була присвячена 'Злочинам "
                                         "проти власності'.\n "
                                         "З 2017 року я займаюсь індивідуальною адвокатською діяльністю та маю "
                                         "свідоцтво"
                                         "про право на заняття адвокатською діяльністю. Моя "
                                         "спеціалізація включає кримінальне право, "
                                         "цивільне право, адміністративне право, справи про "
                                         "адміністративні правопорушення та господарське "
                                         "право.</b>", reply_markup=get_back())


def register_handlers_about(dp: Dispatcher):
    dp.register_callback_query_handler(about, text="about")
