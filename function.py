from pprint import pprint
import requests
# files
from config import random_org_token, phone_qiwi, qiwi_token
from messages import help_command_text


def random_org(text):  # Находит рандомное число(а)
    try:
        x = text.split(' ')
        print(x)
        if len(x) == 3:  # Проверка указано ли кол-во чисел выдачи
            x.append(1)
        print(x)

        random_int = requests.post("https://api.random.org/json-rpc/2/invoke", json={
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": random_org_token,
                "n": x[3],
                "min": x[1],
                "max": x[2],
                "replacement": True,
                "base": 10
            },
            "id": 1
        })
        answer = "Random: " + str(random_int.json()["result"]["random"]["data"])[1:-1] + "\nОсталось: " + str(
            random_int.json()["result"]["requestsLeft"])
        return str(answer)
    except Exception as e:
        print(type(e), e)
        return 'Ошибка!'


def help_command(text):
    try:
        x = text.split(' ')
        if len(x) == 1:
            x[0] = help_command_text['true_help']
            return x[0]
        elif x[1] in help_command_text:
            x[0] = help_command_text[x[1]]
            return x[0]
        else:
            return f'Информации по команде {x[1]} не найдено.'
    except Exception as e:
        print(type(e), e)
        return 'Ошибка!'


def balance():
    s = requests.Session()
    s.headers['Accept'] = 'application/json'
    s.headers['authorization'] = 'Bearer ' + qiwi_token
    b = s.get('https://edge.qiwi.com/funding-sources/v2/persons/' + phone_qiwi + '/accounts')
    c = b.json()['accounts']
    rub_alias = [x for x in c if x['alias'] == 'qw_wallet_rub']
    usd_alias = [x for x in c if x['alias'] == 'qw_wallet_usd']
    rub_balance = rub_alias[0]['balance']['amount']
    usd_balance = usd_alias[0]['balance']['amount']
    total = "RUB: " + str(rub_balance) + "\nUSD: " + str(usd_balance)
    return total


def bbb():
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + qiwi_token
    parameters = {'rows': 2}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + phone_qiwi + '/payments', params=parameters)
    pprint(h.json()["data"][0]["comment"])
    pprint(h.json()["data"][1]["comment"])
    return h.json()["data"]
    #  ?operation=IN&rows=3
