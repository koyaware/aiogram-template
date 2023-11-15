from pathlib import Path

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aioredis import from_url
from environs import Env

from tgbot.db import Database

BASE_DIR = (Path(__file__).resolve()).parent


env = Env()
env.read_env('.env')

BOT_TOKEN = env.str('BOT_TOKEN')
USE_REDIS = env.bool("USE_REDIS")

ADMIN_IDS = [12345678, ]

db = Database('database.db')
storage = RedisStorage(redis=from_url('redis://127.0.0.1:6379')) if USE_REDIS else MemoryStorage()