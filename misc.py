import os
import aioredis
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.redis import RedisStorage2

load_dotenv()
token = os.getenv("BOT_TOKEN")

redis = aioredis.Redis()
storage= RedisStorage2()

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)
