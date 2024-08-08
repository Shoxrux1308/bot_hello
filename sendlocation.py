import requests
import os
TOKEN = os.environ['TOKEN'] 


def send_location(chat_id,latitude,longitude):
    params = {
        'chat_id':chat_id,
        'latitude': latitude,
        'longitude': longitude
    }
    url = f"https://api.telegram.org/bot{TOKEN}/sendLocation"
    response = requests.get(url,params = params)
    return (response.text)
# print(send_location(chat_id=6824726862,latitude= 41.502636,longitude=64.494987))


def send_venue(chat_id,location,title,address):
    params = {
        "chat_id":chat_id,
        "latitude":location['latitude'],
        "longitude":location['longitude'],
        "title":title,
        "address":address
    }
    url = f"https://api.telegram.org/bot{TOKEN}/sendVenue"
    response = requests.get(url,params = params)
    return response
print(send_venue(chat_id=6824726862,location={"latitude": 41.402636,"longitude": 61.494987},title="Codeschool",address="83-uy"))


