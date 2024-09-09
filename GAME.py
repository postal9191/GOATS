import time

import requests
import json

stavka = 10
token = ''
def runGame():
    url = "https://api-dice.goatsbot.xyz/dice/action"

    payload = json.dumps({
        "point_milestone": 75,
        "is_upper": False,
        "bet_amount": stavka
    })
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {token}',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://dev.goatsbot.xyz',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://dev.goatsbot.xyz/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    is_win = response["dice"]["is_win"]
    # print(is_win)
    return is_win


while True:
    # Предположим, что runGame — это функция, которая возвращает результат игры (True или False)
    is_win = runGame()

    # Проверяем результат игры
    if is_win:
        print(f"Вы выиграли {stavka} !")
        if stavka != 10:
            stavka = 10
    # elif stavka >= 1041:
    #     print(f"Снижаем порог ставки: до минимума.")
    #     stavka = 30
    else:
        print(f"Проиграли. Ставка была: {stavka}. Удваиваем ставку и пробуем снова.")
        stavka *= 1  # Удваиваем ставку

    # Ожидание 5 секунд перед следующей попыткой
    # time.sleep(1)