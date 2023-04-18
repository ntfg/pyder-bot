from . import start

from misc import dp, bot 
from data import dataworks
from aiogram import types 
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# Состояние просмотра своей анкеты
class MyApp(StatesGroup):
    view = State()
    

# Клиавиатура просмотра своей анкеты
myapp_kb = ReplyKeyboardMarkup(resize_keyboard=True)
myapp_kb.add("Вернуться в меню↩️")
myapp_kb.add("Изменить анкету🔄")


@dp.message_handler(Text(equals="Изменить анкету🔄"), state=MyApp.view)
async def edit_app(message: types.Message):
    await start.Start.name.set()
    
    await message.answer("Хорошо, давай заполним анкету заново\n"
                         "Введи имя:")