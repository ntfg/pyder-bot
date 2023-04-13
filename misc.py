import os
import aioredis
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

load_dotenv()
token = os.getenv("BOT_TOKEN")

redis = aioredis.Redis()

bot = Bot(token=token)
dp = Dispatcher(bot, storage=RedisStorage2())