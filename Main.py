import requests
import json
import time
import os
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
B = '\x1b[38;5;208m' 
C = '\x1b[1;36m'
W = '\x1b[1;37m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[1;97m'
Y = '\x1b[1;90m'
E = '\x1b[1;31m'
C = '\x1b[1;97m'
print(f'''{B} 
{X}         Fuck Crypto
{E}=============================={B}
|{F} By  : {B} Anonymous Algeria |
|{F} Tool  : {B} Money $$ |
{E}==============================''')
total_money = 0
Good = 0
Bad = 0
def Login():
    email = 'Aliiikrdforbus@gmail.com';
    password = 'Zxcvv121221122&&';

    headers = {
        'authority': 'faucetearner.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://faucetearner.org',
        'referer': 'https://faucetearner.org/login.php',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'act': 'login',
    }

    json_data = {
        'email': email,
        'password': password,
    }

    response = requests.post('https://faucetearner.org/api.php', params=params, headers=headers, json=json_data)

    if "Login successful" in response.text:
        Mahos = response.cookies.get_dict()
        print(f'{F}Good Login')
        print(Mahos)
        print(f'{Y}_' *60)   
        Money(Mahos)
    elif "wrong username or password" in response.text:
        print(f'{E}Bad Login')
    else:
        print(f'{X}Error')

def Money(cookies):
    global total_money , Bad , Good
    while True:
        time.sleep(5)
        headers = {
            'authority': 'faucetearner.org',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'origin': 'https://faucetearner.org',
            'referer': 'https://faucetearner.org/faucet.php',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'act': 'faucet',
        }

        json_data = {}

        rr = requests.post('https://faucetearner.org/api.php', params=params, cookies=cookies, headers=headers).text

        if 'Congratulations on receiving' in rr:
            Good += 1
            json_data = json.loads(rr)
            message = json_data["message"]
            start_index = message.find(">") + 1
            end_index = message.find(" ", start_index)
            balance = message[start_index:end_index]
            total_money += float(balance)
            print(f"[{Good}]{F}Done {balance} XRP£. Total money: {total_money}")    
            print(f'{Y}_' *60)   
        elif 'You have already claimed, please wait for the next wave!' in rr:
            Bad += 1
            print(f'[{Bad}]{E}Bad Claim Wait please')
            print(f'{Y}_' *60)   
        else:
            print(f'{X}Erorr')

Login()
