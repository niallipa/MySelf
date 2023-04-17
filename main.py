# TO DO: 234У
# I
# 1. Пустой телеграмм бот с командой /start
# 2. Подключить проект к github
# II
# 1. Сделать развертывание на raspberry, т.е. autoupdate с github
# (Выпустила коммит, запушила - обновление погрузилось на raspberry и развернулось)
# 2. Создание бд как сущность объект-класс
# Table user {id (default инкримент), tg_id, permission}
# Table files {id, key_tg, blob_file, type(webm, mp4, etc}
# III
# 1. Добавить команду /load, после которой включается состояние впитывания файлов, отправка blob в бд (! Не ключей от телеграмма). Команда /end заканчивает состояние впитывания файлов
# IV
# 1. Корутина на отправку файлов, причем в 3 канала, все это тестить на левом канале
# V
# 1. Написать простой html+css+js лендинг jinja2 шаблоном. Сервер - Flask
# 2. Server. Превратить это в localserver, порт придумать, желательно покрасивее и проверить на свободу пора
# 3. На сервере добавить авторизацию по login pass с permission просмотр бд в видео самих файлов (подгружать в браузер файлы для просмотра)
# VI
# 1. Статистика каналов
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
