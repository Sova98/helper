"""import requests  
import datetime
proxies={'https' : '66.66.113.95:3128'}
resp = requests.get("https://api.telegram.org/bot{}/getUpdates".format("658605557:AAGQrDKPH3dqtPbDjvEK_I9BcW4VSr-A5yk"), proxies={'https' : '118.172.201.141:30104'})
print(resp.text)
"""

import requests  
import datetime
import time
import json
proxies={'https' : '66.66.113.95:3128'}
token="658605557:AAGQrDKPH3dqtPbDjvEK_I9BcW4VSr-A5yk"

def get_updates(offset=None, timeout=30):
    params = {'timeout': timeout, 'offset': offset}
    return requests.get("https://api.telegram.org/bot{}/getUpdates".format(token), proxies=proxies, data=params).json()['result']

def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    requests.get("https://api.telegram.org/bot{}/sendMessage".format(token), proxies=proxies, data=params)

now = datetime.datetime.now()
chat_ids = []
chat_ids.append('331856179')
def main():
    new_offset = None
    last_update_id = 0
    today = now.day
    hour = now.hour
    minute = now.minute
    sent_statistics = False
    woke_up = False
    wished_good_night = False
    while True:
        try:
            last_update = get_updates(new_offset)[0]
            last_update_id = last_update['update_id']
            last_chat_id = last_update['message']['chat']['id']
            new_offset = last_update_id + 1
        except:
            pass

        if (hour == 7) and (woke_up == False):
            send_message(chat_ids[0], 'Новый день(по счету {}). Удачи!'.format(now.day - today))
            woke_up = True
        elif (hour == 23) and (wished_good_night == False):
            send_message(chat_ids[0], 'Пора спать!')
            wished_good_night = True

if __name__ == '__main__':  
    main()
