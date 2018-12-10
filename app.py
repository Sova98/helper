import os
from flask import Flask
from flask import render_template
from flask import Flask, request
import telepot
import urllib3
app = Flask(__name__)
proxy_url = "14.160.23.139:4145"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "bddad84a-f6a3-445b-8f1d-31f9e3b4697b"
bot = telepot.Bot('658605557:AAGQrDKPH3dqtPbDjvEK_I9BcW4VSr-A5yk')
bot.setWebhook("https://sovervo98.scalingo.io/{}".format(secret), max_connections=1)

@app.route('/{}'.format(secret), methods=["POST"])
def hello():
    update = request.get_json()
    print("updates", update)
    if "message" in update:
        global users
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        if chat_id not in users:
            users.append(chat_id)
        bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
