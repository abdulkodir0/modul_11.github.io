from aiogram import Dispatcher, types, F
from aiogram.filters import CommandStart

from t_bot.keyboards import app_kb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("qalesa", reply_markup=app_kb)


@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_btn(msg: types.Message):
    print(msg)
    await msg.answer(msg.web_app_data.data)