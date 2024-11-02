from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.env import API_TOKEN

import logging

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

bot = Bot(token=API_TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=storage)