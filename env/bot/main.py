import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

TOKEN = "6452901767:AAEaKcoEpf4M0VbohD_LMuaaDo-VDAeylXk"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
  
#     Most event objects have aliases for API methods that can be called in events' context
#     For example if you want to answer to incoming message you can use `message.answer(...)` alias
#     and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
#     method automatically or call API method directly via
#     Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Assalomu Alleykum🙋‍♂️, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:    
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())