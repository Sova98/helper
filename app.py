from flask import Flask, request
import telepot
import urllib3
from threading import Timer
import os
"""proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
"""
secret = "bddad84a-f6a3-445b-8f1d-31f9e3b4697b"
bot = telepot.Bot('658605557:AAGQrDKPH3dqtPbDjvEK_I9BcW4VSr-A5yk')
bot.setWebhook("https://sova98.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)
"""users = []
def update_data(interval, bot):
    print('CALLED update_data !!!!!!!!!!!!!!')
    global users
    print('USERS ARE : ', users)
    for id in users:
        print('TRY TO SEND msg to ', id)
        bot.sendMessage(id, "each 10 sec")
    Timer(interval, update_data, [interval]).start()

# update data every second
update_data(10, bot)
"""

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    print(update)
    if "message" in update:
        global users
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        if chat_id not in users:
            users.append(chat_id)
        bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 22774))
    app.run(host='0.0.0.0', port=port)


