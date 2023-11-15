from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


async def user_start(message: Message):
    await message.reply("Hello, user!")


def register_user(dp: Dispatcher):
    dp.message.register(user_start, Command(commands=['start']))
