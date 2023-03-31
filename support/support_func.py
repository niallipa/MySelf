#  Функции, которые помогают основным функциям бота
import requests
import time
# config
from config import url_check_proxy


def proxy_check():

    """f = open("support/proxy/raw_proxy.txt", 'r')
      for i in f:
        #  print(i, end='')
        proxies = {'http': '176.9.119.170:3128'}
        response = requests.get(url=url, proxies=proxies)
        response.close()
        print(response.status_code)
    f.close()
    """

    url = 'https://www.google.com/'
    url2 = 'https://www.anilibria.tv/'
    i = '209.97.150.167:8080'
    try:
        proxies = {'http': f'http://{i}',
                   'https': f'https://{i}'}
        response = requests.get(url=url2, proxies=proxies, timeout=2)
        print(response.text)
    except requests.exceptions.ConnectionError:
        print('Падла')
    except:
        print('Не валид')
    return
