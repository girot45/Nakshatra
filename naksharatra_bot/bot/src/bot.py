import asyncio
import os

from googletrans import Translator

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from naksharatra_bot.bot.src.naksharatra.src.nakshatra_calculations import calc_nakshatra_tithi

load_dotenv()


translator = Translator()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart())
async def hello(message: types.Message):
    await message.answer('Hello')


@dp.message()
async def get_nakha(message: types.Message):
    items = message.text.split(",")
    res = []
    for i in items:
        res.append(translator.translate(i, dest='en').text)
    location = ", ".join(res[:2])
    date_ = " ".join(res[2:4])
    calc_nakshatra_tithi(location, date_)
    await message.answer(translator.translate(message.text,
                                              dest='en').text)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())