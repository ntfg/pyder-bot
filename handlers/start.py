from misc import dp, bot
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
        await message.answer("Привет! Рады снова видеть тебя в Pyder")
    else:
        await message.answer("Привет! Добро пожаловать в Pyder\n"
                             "Здесь ты можешь найти единомышленников, используя не лицо,а код.\n\n"
                             "Но для начала надо пройти регистрацию")
        await Start.name.set()

    
@dp.message_handler(state=Start.age)
async def name(message: types.Message):
    await message.answer("OOOOOOOOOOOOO")
    
    
@dp.message_handler(content_types=["photo"])
async def any(message: types.Message):
    print(message)
    await bot.send_photo(chat_id=message["from"]["id"],
                         photo=message["photo"][0]["file_id"])
    
