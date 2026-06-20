import os
import time
import random
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import telebot
from telebot import types

TOKEN = "8629064923:AAELWnldIa0OrOlhBjU6huqdNFw-jo4p7sw"
bot = telebot.TeleBot(TOKEN)

# (Сюда вставьте ваши массивы EXCUSES, DEADLINES, STATUSES)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn1 = types.KeyboardButton("🤖 Выдать отмазку")
    btn2 = types.KeyboardButton("📅 Когда деньги?")
    btn3 = types.KeyboardButton("🔍 Где Рома?")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Бот активирован!", reply_markup=markup)

@bot.message_handler(content_types=['text'], func=lambda message: True)
def handle_text(message):
    if message.text == "🤖 Выдать отмазку":
        bot.send_message(message.chat.id, random.choice(EXCUSES))
    elif message.text == "📅 Когда деньги?":
        bot.send_message(message.chat.id, f"Официальный ответ поциента:\n«{random.choice(DEADLINES)}»")
    elif message.text == "🔍 Где Рома?":
        bot.send_message(message.chat.id, f"Текущий статус:\nРоман {random.choice(STATUSES)}.")

def run_bot():
    bot.polling(none_stop=True)

# Запуск бота в фоне
threading.Thread(target=run_bot, daemon=True).start()

# Веб-заглушка для Render
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

port = int(os.environ.get("PORT", 10000))
server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
server.serve_forever()
