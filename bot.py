import os
from dotenv import load_dotenv

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (
            ReplyKeyboardMarkup,
            KeyboardButton,
            )

from meme_generator import MemeGenerator as meme_generator

load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    random_meme_button = KeyboardButton('🎲 Случайный мем')

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(random_meme_button)

    await message.reply("Hi!\nI'm pr1kols_bot!", reply_markup=keyboard)


@dp.message_handler()
async def echo(message: types.Message):

    if message.text[2:] == 'Случайный мем':
        await bot.send_photo(chat_id=message.from_user.id, photo=meme_generator.return_meme())

    else:
        await message.answer('Я вас не понимаю')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)