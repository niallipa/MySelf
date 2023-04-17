from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from database import WorkWithDatabase

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!")


WorkWithDatabase.create_bd()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
