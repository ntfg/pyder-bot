from misc import dp, bot 
from data import dataworks
from aiogram import types 
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# Состояние просмотра анкет
class AppsView(StatesGroup):
    # Просматриваемая анкета
    app: int    

    view = State()
    
    # Состояние просмотра совпадений
    matches = State()
    
    match_id: int
    

# Клавиатура просмотра анкет
appsview_kb = ReplyKeyboardMarkup(resize_keyboard=True)
appsview_kb.add(KeyboardButton("Оценить❤"))
appsview_kb.add(KeyboardButton("Следующий➡"))
appsview_kb.add(KeyboardButton("Вернуться в меню↩️"))

# Клавиатура просмотра совпадений
matchview_kb = ReplyKeyboardMarkup(resize_keyboard=True)
matchview_kb.add(KeyboardButton("Оценить❤"))
matchview_kb.add(KeyboardButton("Пропустить➡"))


@dp.message_handler(Text(equals="Оценить❤"), state=AppsView.view)
async def like(message: types.Message):
    dataworks.make_match(message.from_id, AppsView.app)
    await message.answer("Лайк отправлен! Ждём ответа")
    await next_app(message)
        
        
@dp.message_handler(Text(equals="Следующий➡"), state=AppsView.view)
async def next_app(message: types.Message):
    if dataworks.load_match(message.from_id):
        await AppsView.matches.set()
        await next_match(message)
    else:   
        application = dataworks.get_random_app(message.from_id)
        await bot.send_photo(message.from_id, application[4],
                             caption=(f"{application[2]}, {application[3]}\n\n"
                                      f"{application[5]}"),
                             reply_markup=appsview_kb)
        AppsView.app = application[1]
    
        await AppsView.view.set()
        
        
@dp.message_handler(Text(equals="Пропустить➡"), state=AppsView.matches)
async def next_match(message: types.Message):
    if application := dataworks.load_match(message.from_id):
        AppsView.match_id = application[1]
        await bot.send_photo(message.from_id, application[4],
                             caption=("Ой! Кажется твоя анкета кому то понравилась:\n\n"
                                      f"{application[2]}, {application[3]}\n\n"
                                      f"{application[5]}"),
                             reply_markup=matchview_kb)
    else:
        await next_app(message)
        await AppsView.view.set()
        

@dp.message_handler(Text(equals="Оценить❤"), state=AppsView.matches)
async def like_match(message: types.Message):
    dataworks.remove_match(AppsView.match_id, message.from_id)
    await message.answer(f"Вот контакт: @{dataworks.get_user_app(AppsView.match_id)[6]}")
    await bot.send_message(AppsView.match_id,
                           f"У тебя взаимная симпатия! Вот контакт: @{dataworks.get_user_app(message.from_id)[6]}")
    await next_match(message)
