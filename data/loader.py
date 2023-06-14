from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database.database import DataBase


bot = Bot('5483050351:AAHjUJ26xuZ0tsG2VG_7DuTSaQruc8sHJls', parse_mode='HTML')
storage = MemoryStorage()
db = DataBase()
dp = Dispatcher(bot, storage=storage)