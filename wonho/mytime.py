import time
from datetime import datetime

current_time = datetime.now().time # hour(시간), minute(분)
week_day = datetime.today().weekday() # 월(0), 화(1), 수(2) ~ 일(6)

while(True):
    current_time = datetime.now().time # hour(시간), minute(분)
    week_day = datetime.today().weekday() # 월(0), 화(1), 수(2) ~ 일(6)
    
    if week_day != 6:
        if current_time.hour == 18:
            print("sms 보내기")
            
    time.sleep(1) 

# SMS를 보내는 함수
def send_sms():
    # SMS Key.
    client = CoolsmsClient("NCS2ZNEFHD9SUSBR", "0RFT6GZVXZFWNQSSCT0Q35CZOJNBIONL")

    # 메시지를 생성.
    message = "오후 6시"

    # SMS를 보내기.
    client.send_sms("01054172944", message)

# 메시지를 보내기 시작.
while(True):
    send_sms()
    time.sleep(60)

