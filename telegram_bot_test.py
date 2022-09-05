

import requests 

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
        if message['update_id'] > last_updated_id:
           send_message(TOKEN, message['message']['chat']['id'], message['message']['text'], ROOT_URL) 
           last_updated_id = message['update_id']
           

  

