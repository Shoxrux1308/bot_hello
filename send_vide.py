import requests
import os
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/sendVideo'

def send_video(chat_id,file_id):
    params={
        "chat_id":chat_id,
        "video":file_id
    }
    response=requests.get(URL,params=params)
    return response.status_code
print(send_video(chat_id=6824726862,file_id= "BAACAgIAAxkBAAOWZrSm8TZXdqnOVtS38kJ-c9XupRwAAu1RAAJosplJg9GyueFNFKg1BA"))