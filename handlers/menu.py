from misc import dp, bot 
from data import dataworks
from .apps import AppsView, next
from aiogram import types 
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# Состояние главного меню
class MainMenu(StatesGroup):
    menu = State()
    
    
# Клавиатура главного меню
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.add(KeyboardButton("Смотреть анкеты🔭"))
menu_kb.add(KeyboardButton("Моя анкета🤓"))


@dp.message_handler(Text(equals="Смотреть анкеты🔭") ,state=MainMenu)
async def menu_apps(message: types.Message):
    await next(message)
    await AppsView.view.set()
    
    
@dp.message_handler(Text(equals="Вернуться в меню↩️"), state=AppsView.view)
async def next(message: types.Message):
    await message.answer("Не задерживайтесь в меню и скорее возвращайтесь смотреть анкеты!",
                         reply_markup=menu_kb)
    await MainMenu.menu.set()