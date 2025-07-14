import os
import json
import time
import random
from datetime import datetime

# إعدادات الألوان
class Colors:
    R = '\033[1;31m'
    G = '\033[1;32m'
    Y = '\033[1;33m'
    B = '\033[38;5;208m'
    W = '\033[1;37m'

def print_banner():
    print(f'''{Colors.B}
{Colors.Y}         Auto Faucet Claimer
{Colors.R}=============================={Colors.B}
|{Colors.G} By  : {Colors.B} Anonymous Algeria |
|{Colors.G} Mode: {Colors.B} No Proxy       |
{Colors.R}==============================''')

def login(email, password):
    try:
        # إعداد الطلب مع User-Agent عشوائي
        headers = {
            'User-Agent': random.choice([
                'Mozilla/5.0 (Windows NT 10.0)',
                'Mozilla/5.0 (Linux; Android 10)',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0)'
            ]),
            'Accept-Language': 'ar-YE,ar;q=0.9'
        }
        
        # محاكاة عملية الدخول (استبدل بالكود الحقيقي)
        print(f"{Colors.G}Attempting login: {email[:3]}***{email[-10:]}")
        time.sleep(random.uniform(1, 3))  # تأخير عشوائي
        
        # محاكاة نجاح/فشل الدخول (استبدل بالكود الحقيقي)
        if "error" in email:  # لمحاكاة الحساب المعطّل
            raise Exception("Invalid email format")
            
        return {"status": "success", "cookies": {}}
        
    except Exception as e:
        print(f"{Colors.R}Login failed: {str(e)}")
        return {"status": "failed", "error": str(e)}

def process_accounts():
    accounts = json.loads(os.getenv('FAUCET_ACCOUNTS', '[]'))
    working = []
    failed = []
    
    for acc in accounts:
        result = login(acc['email'], acc['password'])
        
        if result['status'] == 'success':
            working.append(acc)
            # أضف هنا كود المطالبة بعد نجاح الدخول
            print(f"{Colors.G}✓ Success: {acc['email'][:3]}***")
        else:
            failed.append(acc)
            print(f"{Colors.R}✗ Failed: {acc['email'][:3]}***")
        
        time.sleep(random.uniform(5, 10))  # تأخير بين الحسابات
    
    # تسجيل النتائج
    print(f"\n{Colors.Y}=== Summary ===")
    print(f"{Colors.G}Working accounts: {len(working)}")
    print(f"{Colors.R}Failed accounts: {len(failed)}")
    
    # إعادة المحاولة للحسابات الفاشلة بعد 3 ساعات
    if failed:
        print(f"{Colors.Y}Will retry failed accounts in 3 hours...")
        time.sleep(10800)  # 3 ساعات
        process_accounts(failed)

if __name__ == "__main__":
    print_banner()
    process_accounts()
