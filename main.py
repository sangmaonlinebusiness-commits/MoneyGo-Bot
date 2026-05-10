import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask
from threading import Thread
import os

# 1. WEB SERVER SETTINGS
app = Flask(__name__)

@app.route('/')
def home():
    return "Money Go Bot is Alive!"

def run():
    # Render needs this port to start properly
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# 2. BOT SETTINGS (IAO DINGTANGATBO)
API_TOKEN = '8665660702:AAHoN_Fv98uPalH-xRPp9l43Ss5RpXvs3Mg' 
BLOGGER_URL = 'https://moneygo24.blogspot.com/'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text="💰 Start Earning", web_app=WebAppInfo(url=BLOGGER_URL))
    markup.add(btn)
    bot.send_message(message.chat.id, "Welcome to Money Go! Click below:", reply_markup=markup)

# 3. STARTING THE BOT & SERVER
if __name__ == "__main__":
    # Flask-ko thread-o start ka·chengbao
    server_thread = Thread(target=run)
    server_thread.start()
    
    print("Bot is polling...")
    # Bot-ko off ong·gija chalaiangbo
    bot.infinity_polling()
