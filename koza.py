import time

import requests
import refreshToken

token = ''

def claimReklama(token):


    url = "https://dev-api.goatsbot.xyz/missions/action/66db47e2ff88e4527783327e"

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {token}',
        'cache-control': 'no-cache',
        'content-length': '0',
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

    response = requests.request("POST", url, headers=headers, data=payload)
    return response



while True:
    response = claimReklama(token)

    if response.status_code == 401:  # Если код ошибки 401
        print("Токен истек, обновление токена...")
        # Обновление токена
        token = refreshToken.refreshToken()
        continue

    print('Ждем 5 мин забираем монетки')
    time.sleep(60*5+5)
