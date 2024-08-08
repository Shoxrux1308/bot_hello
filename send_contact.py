import requests
import os
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/sendContact'
def sendContact(chat_id,phone_number,first_name):
    params={
        "chat_id":chat_id,
        "phone_number":phone_number,
        "first_name":first_name
    }
    response=requests.get(URL,params=params)
    return response.status_code
print(sendContact(chat_id=6824726862,phone_number=+998932837874,first_name="Xodjayev"))
    