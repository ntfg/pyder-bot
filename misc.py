import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()
token = os.getenv("BOT_TOKEN")

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)