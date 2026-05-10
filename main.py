import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask
from threading import Thread
import os

# --- WEB SERVER FOR 24/7 HOSTING ---
app = Flask('')

@app.route('/')
def home():
    return "Money Go Bot is Online!"

def run():
    # Render-ni gita port-ko auto-detect ka·gen
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- MONEY GO BOT SETTINGS ---
# BotFather-oni man·gipa Token-ko iano donbo
API_TOKEN = '8665660702:AAHoN_Fv98uPalH-xRPp9l43Ss5RpXvs3Mg' 

# Na·ni Blogger URL-ko iano donbo
BLOGGER_URL = 'https://na·niblog.blogspot.com'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    
    # Keyboard button-rang tariania
    markup = InlineKeyboardMarkup()
    
    # Web App Button (Money Go Mini App)
    earn_button = InlineKeyboardButton(
        text="💰 Start Earning Now", 
        web_app=WebAppInfo(url=BLOGGER_URL)
    )
    
    # Official Channel Button (Link-ko dingtangatbo)
    channel_button = InlineKeyboardButton(
        text="📢 Join Official Channel", 
        url="https://t.me/dailymoneyfree" 
    )
    
    markup.add(earn_button)
    markup.add(channel_button)

    welcome_text = (
        f"Welcome {user_name} to **Money Go**! 💸\n\n"
        "India-ni nambatgipa earning platform-o na·a poisa kamana man·gen.\n\n"
        "👇 Click the button below to open the App."
    )
    
    bot.send_message(
        message.chat.id, 
        welcome_text, 
        reply_markup=markup, 
        parse_mode="Markdown"
    )

# --- BOT-KO START KA·ANI ---
if __name__ == "__main__":
    keep_alive()  # Server start ka·gen
    print("Money Go Bot is running...")
    bot.polling(none_stop=True)
