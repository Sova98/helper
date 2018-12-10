from flask import Flask, request
import telebot
from telebot import types
import time

secret = "n1hz7waCT9"
bot = telebot.TeleBot('658605557:AAGQrDKPH3dqtPbDjvEK_I9BcW4VSr-A5yk', threaded=False)

bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url="https://sovervo98.scalingo.io/{}".format(secret))

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200


@bot.message_handler(commands=['start', 'help'])
def startCommand(message):
    bot.send_message(message.chat.id, 'Hi *' + message.chat.first_name + '*!' , parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
