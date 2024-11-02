from aiogram.types import Message

from loader import dp
from utils import texts

@dp.message_handler(commands=['start'])
async def start_handler(message: Message):

    first_name = message.from_user.first_name
    user_id = message.from_user.id
    username = message.from_user.username
    is_bot = message.from_user.is_bot
    text = message.text

    await message.answer(texts.user_info(
        first_name=first_name,
        user_id=user_id,
        username=username,
        is_bot=is_bot,
        text=text
    ))