import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask
from threading import Thread
import os

# --- 1. WEB SERVER FOR 24/7 HOSTING ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Money Go Professional Bot is Online!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# --- 2. BOT SETTINGS (IAO DINGTANGATBO) ---
API_TOKEN = '8665660702:AAHoN_Fv98uPalH-xRPp9l43Ss5RpXvs3Mg'  # BotFather Token
BLOGGER_URL = 'https://moneygo24.blogspot.com'  # Blogger URL

bot = telebot.TeleBot(API_TOKEN)

# --- 3. PROFESSIONAL DASHBOARD ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id

    # Design Keyboard
    markup = InlineKeyboardMarkup(row_width=2)
    
    # Buttons
    btn_app = InlineKeyboardButton("🚀 Open Money Go App", web_app=WebAppInfo(url=BLOGGER_URL))
    btn_profile = InlineKeyboardButton("👤 My Profile", callback_data="profile")
    btn_refer = InlineKeyboardButton("👥 Refer & Earn", callback_data="refer")
    btn_support = InlineKeyboardButton("🛡️ Support Group", url="https://t.me/dailymoneyfree")
    
    # Button Layout
    markup.add(btn_app)
    markup.add(btn_profile, btn_refer)
    markup.add(btn_support)

    # Professional Welcome Message
    welcome_msg = (
        f"<b>💎 Welcome to Money Go, {user_name}!</b>\n\n"
        f"India's most trusted earning platform. Start completing tasks and earn real cash daily.\n\n"
        f"🆔 <b>Your ID:</b> <code>{user_id}</code>\n"
        f"📊 <b>Status:</b> Active\n\n"
        f"<i>Click the Start Earning button below to make money 💰!</i>"
    )

    bot.send_message(
        message.chat.id, 
        welcome_msg, 
        reply_markup=markup, 
        parse_mode="HTML"
    )

# --- 4. CALLBACK HANDLERS (BUTTON ACTIONS) ---
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "profile":
        profile_text = (
            "<b>👤 YOUR ACCOUNT PROFILE</b>\n\n"
            f"🏷️ Name: {call.from_user.first_name}\n"
            f"💰 Balance: ₹0.00\n"
            f"📥 Total Withdrawn: ₹0.00\n\n"
            "<i>Work hard to increase your balance!</i>"
        )
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, profile_text, parse_mode="HTML")

    elif call.data == "refer":
        refer_text = (
            "<b>👥 REFER AND EARN</b>\n\n"
            "Invite your friends and earn ₹5 for every active user!\n\n"
            f"🔗 <b>Your Referral Link:</b>\n"
            f"https://t.me/{bot.get_me().username}?start={call.from_user.id}"
        )
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, refer_text, parse_mode="HTML")

# --- 5. STARTING THE BOT ---
if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    print("Money Go Pro Bot is polling...")
    bot.infinity_polling()
