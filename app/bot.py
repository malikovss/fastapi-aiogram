from aiogram import Dispatcher, Bot, types

TOKEN = "1945118170:AAH4ZVOXOgEC8F3wDCB-rZ81817fynT7INk"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}")