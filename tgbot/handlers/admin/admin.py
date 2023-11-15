from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


def register_admin(dp: Dispatcher):
    dp.message.register(admin_start, AdminFilter(), Command(commands=['start']))