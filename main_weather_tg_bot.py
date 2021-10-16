import requests
import datetime
from Get import get_weather as get
from config import token_bot, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=token_bot)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города"
                        " (на английском, пожааалуйста) и я"
                        " пришлю сводку погоды!")

@dp.message_handler(content_types=["text"])
async def get_weather(message: types.Message):
    await message.reply(get(message.text, open_weather_token))


if __name__ == '__main__':
    executor.start_polling(dp)