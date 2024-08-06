import requests
import os
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
import time

def get_text_from_update(update):
    """
    Get text from update

    Args:
        update (dict): update

    Returns:
        str: text from update
    """
    return update["message"]["text"]

# Get updates
first_update_id=-1
while True:
    response = requests.get(URL)
    data = response.json()
    result=data['result'][-1]
    next_update_id=result
    if first_update_id!=next_update_id["update_id"]:
        print(get_text_from_update(result))
    first_update_id=next_update_id["update_id"]
    