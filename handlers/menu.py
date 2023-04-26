from misc import dp, bot 
from data import dataworks
from .apps import AppsView, next_app, appsview_kb
from .my_app import MyApp, myapp_kb
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
    await next_app(message)
    
    
@dp.message_handler(Text(equals="Вернуться в меню↩️"), state=[AppsView.view, MyApp.view])
async def return_to_menu(message: types.Message):
    await message.answer("Не задерживайся в меню и скорее возвращайся смотреть анкеты!",
                         reply_markup=menu_kb)
    await MainMenu.menu.set()
    

@dp.message_handler(Text(equals="Моя анкета🤓"), state=MainMenu)
async def my_app(message: types.Message):
    application = dataworks.get_user_app(message.from_id)
    
    await bot.send_photo(message.from_id, application[4],
                             caption=("Вот твоя анкета:\n\n"
                                      f"{application[2]}, {application[3]}\n\n"
                                      f"{application[5]}"),
                             reply_markup=myapp_kb)

    await MyApp.view.set()