import requests
from time import sleep
from config import phone_qiwi, qiwi_token, telegram_token
from pprint import pprint
from aiogram import Bot, Dispatcher

bot = Bot(token=telegram_token)
dp = Dispatcher(bot)


def check(response):
    txnid = response["data"][0]["txnId"]
    with open("last.txt", "r") as f:
        last = f.readline()
        if str(txnid) != str(last):
            return True
        else:
            pass
    return False


async def send():
    await bot.send_message("758042568", h.json()["data"][0]["txnId"])


s = requests.Session()
s.headers['authorization'] = 'Bearer ' + qiwi_token
parameters = {'rows': 1}

while True:
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + phone_qiwi + '/payments', params=parameters)
    # pprint(h.json()["data"][0]["comment"])
    pprint(h.json()["data"][0]["txnId"])
    if check(h.json()):
        pass
    sleep(3)
