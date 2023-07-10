from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
import asyncio
from keyboards.reply import get_back
from keyboards.inline_question import order


async def service(messsage: types.Message):
    with open('reu.jpg', 'rb') as photo:
        markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[
            InlineKeyboardButton(text='Для людей', callback_data='people'),
            InlineKeyboardButton(text='Для юридичних осіб', callback_data='phis')
        ]])
        await bot.send_photo(chat_id=messsage.from_user.id, photo=photo,
                             caption=f'<b>Мої послуги</b>\n'
                                     '\n'
                                     f'Працюю за всіма юридичними напрямками незалежно від складності',
                             reply_markup=markup)



async def for_people(callback: CallbackQuery):
    await callback.message.answer("<b>Трудові суперечки</b>\n"
                                  "\n"
                                  "Допоможу вам отримати компетентну юридичну консультацію з питань трудового права.", reply_markup=get_back())
    await asyncio.sleep(2)
    await callback.message.answer("<b>Захист прав споживачів</b>\n"
                                  "\n"
                                  "Я готовий допомогти вам у судовому представництві, в тому числі у справах про "
                                  "неналежну якість товарів та послуг, "
                                  "порушення правил продажу, шахрайства тощо.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Складання заяви, скасування судового наказу</b>\n"
                                  "\n"
                                  f"Забезпечу допомогу в складанні заяви та скасуванні судового наказу, а також буду "
                                  "вашим представником у суді та "
                                  "допоможу з необхідними документами.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Сімейні суперечки</b>\n"
                                  "\n"
                                  "Якщо вам потрібна допомога у питаннях розірвання шлюбу, поділу майна, стягненні "
                                  "аліментів або укладанні шлюбного "
                                  "договору, я надаю повний спектр послуг у сімейних правових питаннях, щоб захистити"
                                  " ваші права та інтереси.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Адміністративне судочинство</b>\n"
                                  "\n"
                                  "Захищаю ваші інтереси в адміністративному суді, надаю допомогу з захисту порушених "
                                  "прав та підготую заперечення на "
                                  "складені протоколи та постанови.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Адвокат у кримінальних справах</b>\n"
                                  "\n"
                                  "Маю величезний досвід у роботі з найскладнішими справами та готовий допомогти вам "
                                  "захищати ваші інтереси на "
                                  "досудовому слідстві та у суді.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Право на спадщину</b>\n"
                                  "\n"
                                  "Допомагаю вирішити різні питання, пов'язані зі спадщиною, включаючи складні "
                                  "ситуації з поділом майна між "
                                  "спадкоємцями, суперечки між ними, визнання дійсності заповіту або його оскарження, "
                                  "а також питання, пов'язані з правом на отримання спадщини.",
                                  reply_markup=order())


"""for phisic"""


async def for_phisic(callback: CallbackQuery):
    await callback.message.answer("<b>Бухгалтерське обслуговування</b>\n"
                                  "\n"
                                  "Надаю послуги з бухгалтерського обліку та податкового консультування. Організую "
                                  "незалежний внутрішній контроль "
                                  "фінансової інформації.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Економічна безпека</b>\n"
                                  "\n"
                                  "Надаю послуги з економічної безпеки, які включають захист ваших інтересів на досудовому слідстві та у суді. Маю "
                                  "великий досвід у складних справах та готовий допомогти вирішити будь-які проблеми, "
                                  "пов'язані з економічною безпекою вашого бізнесу.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Налогові консультації</b>\n"
                                  "\n"
                                  "Готовий надати вам професійні послуги з налогових консультацій та допомогти вирішити будь-які питання, пов'язані з "
                                  "оподаткуванням.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Абонентське обслуговування</b>\n"
                                  "\n"
                                  "Я можу запропонувати послугу абонентського обслуговування, що включає супровід "
                                  "господарської діяльності вашого "
                                  "підприємства з усіх правових питань.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Складання договорів</b>\n"
                                  "\n"
                                  "Надаю послуги складання договорів. Це необхідно для правильного ведення бізнесу та "
                                  "успішного укладення угод.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Представництво в судах</b>\n"
                                  "\n"
                                  "Надаю послуги представництва в судах будь-якого рівня та напрямку: від підготовки "
                                  "документів та розробки стратегії "
                                  "захисту до представництва у суді та захисту ваших інтересів.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Документи для підприємців</b>\n"
                                  "\n"
                                  "Допомагаю у складанні необхідних документів для вашого бізнесу. Включає в себе "
                                  "документи для розвитку фірми, "
                                  "участі в тендерах.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Приватне підприємство</b>\n"
                                  "\n"
                                  "Розглядаю питання, пов'язані з реєстрацієй, змінами, ліквідацієй та банкрутством "
                                  "приватних підприємств. Звертайтесь "
                                  "для отримання професійної консультації та підтримки.", reply_markup=order())


def register_service(dp: Dispatcher):
    dp.register_message_handler(service, Text(equals="Послуги"))
    dp.register_callback_query_handler(for_people, text='people')
    dp.register_callback_query_handler(for_phisic, text='phis')
