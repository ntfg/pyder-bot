from aiogram import executor
from misc import dp 
import handlers

executor.start_polling(dp, skip_updates=True)