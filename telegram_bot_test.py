

import requests 
from sentences import search_sentence, bot_sentences

TOKEN = "5796909930:AAEGeNbUQk4OBtJTNjpHaDaMgn99gKXaOX4"
ROOT_URL = "https://api.telegram.org/bot"
last_updated_id = 0

def get_updates(token, root_url):
    url = f'{root_url}{token}/getUpdates'
    res = requests.get(url)
    return res.json()

def send_message(token, chat_id, message, root_url):
    url = f'{root_url}{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    req = requests.post(url=url, data=data)
    print(req, chat_id, last_updated_id)



while True:
    updates = get_updates(TOKEN, ROOT_URL)
    messages = updates['result']
    
    for message in messages:
        chat_id = message['message']['chat']['id']
        message_text = message['message']['text']
        if message['update_id'] > last_updated_id:
           result_message = search_sentence(message=message_text, sentences=bot_sentences)
           send_message(TOKEN, chat_id, result_message, ROOT_URL) 
           last_updated_id = message['update_id']
           

  

