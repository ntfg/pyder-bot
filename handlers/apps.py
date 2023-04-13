from misc import dp, bot 
from data import dataworks
from aiogram import types 
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# Состояние просмотра анкет
class AppsView(StatesGroup):
    view = State()
    # Состояние просмотра совпадений
    matches = State()
    

# Клавиатура просмотра анкет
appsview_kb = ReplyKeyboardMarkup()
appsview_kb.add(KeyboardButton("Оценить❤"))
appsview_kb.add(KeyboardButton("Следующий➡"))
appsview_kb.add(KeyboardButton("Вернуться в меню↩️"))


@dp.message_handler(Text(equals="Оценить❤"), state=AppsView.view)
async def like(message: types.Message):
    application = dataworks.get_app(message.from_id)
    dataworks.make_match(message.from_id, application[1])
    await message.answer("Лайк отправлен! Ждём ответа")
    await next(message)
        
        
@dp.message_handler(Text(equals="Следующий➡"), state=AppsView.view)
async def next(message: types.Message):
    if dataworks.load_match(message.from_id):
        await AppsView.matches.set()
    else:   
        application = dataworks.get_app(message.from_id)
        await bot.send_photo(message.from_id, application[4],
                             caption=(f"{application[2]}, {application[3]}\n\n"
                                      f"{application[5]}"),
                             reply_markup=appsview_kb)