"""
    Version 0.03
    Todo БД user's
    Todo при /start запись ID в БД
    Todo /ban
"""


from aiogram import Bot, types, Dispatcher, executor
# files
from config import telegram_token
from function import random_org, balance, help_command, bbb
from messages import todo_command_text
from db import *

bot = Bot(token=telegram_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет!', reply=False)
    await message.reply('Список команд - /help')  # Сохранять id в БД


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_command(message.text), parse_mode="Markdown")


@dp.message_handler(commands=['ban'])
async def process_ban_command(message: types.Message):
    await message.reply('~~~', reply=False)


@dp.message_handler(commands=['todo'])
async def process_ban_command(message: types.Message):
    await message.reply(todo_command_text, parse_mode="Markdown", reply=False)


@dp.message_handler(commands=['random'])
async def process_random_command(message: types.Message):
    await message.reply(random_org(message.text))


@dp.message_handler(commands=['balance'])
async def process_balance_command(message: types.Message):
    await message.reply(balance(), reply=False)


@dp.message_handler(commands=['bbb'])
async def process_qiwi_notif(message: types.Message):
    await message.reply(bbb(), reply=False)


async def bot_started(dispatcher: Dispatcher):
    await bot.send_message('758042568', 'Bot started')  # Себе
    await bot.send_message('920379538', 'Bot started')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=bot_started, skip_updates=True)
