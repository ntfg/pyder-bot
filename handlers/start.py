from misc import dp, bot
from data import dataworks
from .menu import MainMenu, menu_kb
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Состояние, вокруг которого построен этот хендлер
class Start(StatesGroup):
    data = []
    
    name = State()
    age = State()
    photo = State()
    description = State()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if dataworks.is_exist(message["from"]["id"]):
        await message.answer("Привет! Рады снова видеть тебя в Pyder",
                             reply_markup=menu_kb)
        await MainMenu.menu.set()
    else:
        await message.answer("Привет! Добро пожаловать в Pyder\n"
                             "Здесь ты можешь найти единомышленников, используя не лицо,а код.\n\n"
                             "Но для начала надо пройти регистрацию\n"
                             "Введи своё имя:")
        await Start.name.set()


@dp.message_handler(state=Start.name)
async def name(message: types.Message):
    name: list[str] = message["text"].split()
    
    if len(name) == 1 and name[0][0].isupper():
        await message.answer("Славно! А сколько тебе лет?")
        await Start.age.set()
        Start.data.append(message.from_id)
        Start.data.append(name[0])
    else:
        await message.answer("Хм, я ожидаю что твоё имя состоит из одного слова и начинается с заглавной буквы") 
        

@dp.message_handler(state=Start.age)
async def age(message: types.Message):
    """
        Функция int одновременно проверяет и на .isdigit(), и на длину
    """
    try:
        age = int(message["text"])
        if age < 0 or age > 120:
            await message.answer("Кажется, вы перепутали свой возраст😉")
        else:
            await message.answer("Прекрасно! А теперь пришлите свою фотокарточку")
            await Start.photo.set()
            Start.data.append(age)
    except:
        await message.answer("Вы указали возраст в неправильном формате")
    

@dp.message_handler(state=Start.photo, content_types=["photo"])
async def photo(message: types.Message):
    file_id: str = message["photo"][0]["file_id"]
    await message.answer("Отлично! Осталось только написать описание\n"
                         "Требование: не более 500 символов")
    await Start.description.set()
    Start.data.append(file_id)
    

@dp.message_handler(state=Start.description)
async def description(message: types.Message):
    if len(message.text) > 500:
        await message.answer("Ой, ваш текст слишком большой! Нужно уместиться в 500 символов")
    else:
        await message.answer("Отлично, регистрация завершена!")
        Start.data.append(message.text) 
        Start.data.append(message["from"]["username"]) 
        dataworks.new_user(Start.data)
        await bot.send_photo(message.from_id, Start.data[3],
                             caption=("Вот твоя анкета:\n\n"
                                      f"{Start.data[1]}, {Start.data[2]}\n"
                                      f"{Start.data[4]}"),
                             reply_markup=menu_kb)
        
        Start.data = []
        await MainMenu.menu.set()
        