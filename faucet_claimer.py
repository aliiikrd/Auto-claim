import requests
import json
import time
import os
from datetime import datetime

# إعدادات الألوان
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
B = '\x1b[38;5;208m' 
C = '\x1b[1;36m'
W = '\x1b[1;37m'
F = '\x1b[2;32m'
E = '\x1b[1;31m'

class FaucetClaimer:
    def __init__(self):
        self.total_money = 0
        self.good_claims = 0
        self.bad_claims = 0
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'Accept-Language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'X-Requested-With': 'XMLHttpRequest'
        })
        
    def print_banner(self):
        print(f'''{B} 
{Y}         Auto Faucet Claimer
{E}=============================={B}
|{F} By  : {B} Anonymous Algeria |
|{F} Tool  : {B} Money $$ |
{E}==============================''')
        
    def login(self):
        email = os.getenv('FAUCET_EMAIL', 'Aliiikrdforbus@gmail.com')
        password = os.getenv('FAUCET_PASSWORD', 'Zxcvv121221122&&')
        
        params = {'act': 'login'}
        json_data = {'email': email, 'password': password}
        
        try:
            response = self.session.post(
                'https://faucetearner.org/api.php',
                params=params,
                json=json_data
            )
            
            if "Login successful" in response.text:
                print(f'{F}Good Login')
                print(f'{Y}_' * 60)
                return True
            elif "wrong username or password" in response.text:
                print(f'{E}Bad Login')
            else:
                print(f'{Y}Error: {response.text}')
        except Exception as e:
            print(f'{E}Login Error: {str(e)}')
        
        return False
    
    def claim_money(self):
        params = {'act': 'faucet'}
        
        try:
            response = self.session.post(
                'https://faucetearner.org/api.php',
                params=params
            )
            
            if 'Congratulations on receiving' in response.text:
                self.good_claims += 1
                json_data = json.loads(response.text)
                message = json_data["message"]
                
                # استخراج المبلغ من الرسالة
                start_index = message.find(">") + 1
                end_index = message.find(" ", start_index)
                balance = message[start_index:end_index]
                
                self.total_money += float(balance)
                print(f"[{self.good_claims}]{F}Done {balance} XRP£. Total money: {self.total_money}")
                print(f'{Y}_' * 60)
                return True
            elif 'You have already claimed, please wait for the next wave!' in response.text:
                self.bad_claims += 1
                print(f'[{self.bad_claims}]{E}Bad Claim Wait please')
                print(f'{Y}_' * 60)
            else:
                print(f'{Y}Claim Error: {response.text}')
        except Exception as e:
            print(f'{E}Claim Error: {str(e)}')
        
        return False
    
    def run(self):
        self.print_banner()
        
        if not self.login():
            return
        
        # حلقة التشغيل الرئيسية مع إدارة الأخطاء
        while True:
            try:
                # جلب المال مع إعادة المحاولة عند الفشل
                for _ in range(3):
                    if self.claim_money():
                        break
                    time.sleep(10)
                
                # انتظر 60 ثانية قبل المحاولة التالية
                time.sleep(60)
                
            except KeyboardInterrupt:
                print(f"\n{E}Stopped by user")
                break
            except Exception as e:
                print(f"{E}Critical Error: {str(e)}")
                print(f"{Y}Restarting in 30 seconds...")
                time.sleep(30)
                # إعادة تهيئة الجلسة بعد الخطأ
                self.session = requests.Session()
                self.login()

if __name__ == '__main__':
    claimer = FaucetClaimer()
    claimer.run()
