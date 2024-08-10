
import requests
import os
from pprint import pprint
from send_message import send_message
from openai import OpenAI
import time

# Get Open AI API key
TOKEN_OPENAI = os.environ['TOKEN_OPENAI']
# Get Telegram API key
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
def get_file(file_id: str):
    """
    Get file

    Args:
        file_id (str): file id

    Returns:
        dict: file
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/getFile'
    response = requests.get(URL, params={'file_id': file_id})
    return response.json()

def download_file(file_path: str):
    """
    Download file

    Args:
        file_path (str): file path

    Returns:
        bytes: file
    """
    URL = f'https://api.telegram.org/file/bot{TOKEN}/{file_path}'
    # Get file
    response = requests.get(URL)
    content = response.content

    
    return content

def speech_to_text(file_content: bytes):
    """
    Speech to text

    Args:
        file_content (bytes): file content

    Returns:
        str: text
    """
    client = OpenAI(api_key=TOKEN_OPENAI,base_url="https://api.lemonfox.ai/v1")
    transcription = client.audio.transcriptions.create(

        model='whisper-1',
        file=file_content
    ) 

    return transcription
next_update_id=0
chat_id=6824726862
while True:
    response = requests.get(URL)
    data = response.json()
    result=data['result'][-1]
    
    first_update_id=len(data['result'])
    if first_update_id!=next_update_id:
        format=list(result["message"])[-1]
        file_id=result['message'][format]['file_id']
        file_path = get_file(file_id)['result']['file_path']
        print(file_path)
        file_content = download_file(file_path)
        text = speech_to_text(file_content).text
        print(text)
        send_message(chat_id,text)
    next_update_id=first_update_id
    time.sleep(0.3)
    
    

# file_id = 'AwACAgIAAxkBAAOdZrb0TmX3vndupmNhtswFnb6-5uMAAhZWAALffblJ0vgSp9hYlcs1BA'


# file_path = get_file(file_id)['result']['file_path']
# print(file_path)

# file_content = download_file(file_path)
# text = speech_to_text(file_content)
# print(text)