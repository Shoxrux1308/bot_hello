import requests
from send_message import send_message
import os
import time
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'


def get_text_from_update(update):
    """
    Get text from update

    Args:
        update (dict): update

    Returns:
        str: text from update
    """
    return update['message']['text'] 




# Loop get updates
chat_id=6824726862
while True:
    # Get updates
    response = requests.get(URL)
    data = response.json()

    # Get results
    result = data['result']

    # Get last update
    last_update = result[-1]

    # Get last text from update
    text = get_text_from_update(last_update)
    send_message(chat_id,text)
    # Print text
    print(text)
    time.sleep(2)
