from misc import dp 
from data import dataworks
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State


# Состояние, вокруг которого построен этот хендлер
class Start(StatesGroup):
    name = State()
    age = State()
    photo = State()
    description = State()



@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if dataworks.is_exist(message["from"]["id"]):
        pass

    
@dp.message_handler(state=Start.age)
async def name(message: types.Message):
    await message.answer("OOOOOOOOOOOOO")
    