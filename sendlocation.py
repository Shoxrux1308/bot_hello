import requests
import os
TOKEN = os.environ['TOKEN'] 
url = f"https://api.telegram.org/bot{TOKEN}/sendLocation"

def send_location(chat_id,latitude,longitude):
    params = {
        'chat_id':chat_id,
        'latitude': latitude,
        'longitude': longitude
    }
    response = requests.get(url,params = params)
    return (response.text)
print(send_location(chat_id=6824726862,latitude= 41.502636,longitude=64.494987))
    