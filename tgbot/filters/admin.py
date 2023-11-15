from aiogram.filters import Filter
from aiogram.types import Message

from tgbot.config import ADMIN_IDS


class AdminFilter(Filter):

    async def __call__(self, message: Message) -> bool:
        if message.from_user.id in ADMIN_IDS:
            return True
        return False
