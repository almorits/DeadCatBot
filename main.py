import random
import telebot
from telebot import types

TOKEN = "8629064923:AAELWnldIa0OrOlhBjU6huqdNFw-jo4p7sw"
bot = telebot.TeleBot(TOKEN)

EXCUSES = [
    "Вчера порезал колесо и всё ушло туда. А сегодня на цветах сделал только 60 шекелей :(",
    "Счёт у меня все ещё в блоке, если бы они провели аудит и разблочили, я бы уже давно отдал",
    "Просто я вчера наебнулся на масле и выключился вечером. А сейчас ползу в мокед",
    "Мне позвонил адвокат. Уточнял как называются части тела, которые получили урон",
    "Уши сели, я в касде, блдт",
    "Я из паровоза пересел в обратную сторону в Биньямине. Я ехал в Хайфу, блядь",
    "Сломался холодильник, в морозилке которого я месяц хранил труп умершей кошки...",
    "Завтра я везу нового котенка в ветеринарку в Бат-Ям. Первая прививка",
    "Вот кот. У пса ворует. На твои деньги"
]

DEADLINES = [
    "Планирую к вечеру послезавтра закрыть",
    "До конца недели планирую. Возможно, раньше. Сегодня точно нет 😢",
    "В течение получаса сделаю",
    "Уже в конце недели"
]

STATUSES = [
    "Спит сладким сном до полудня под напоминания о долге",
    "Трое суток подряд играет в Хомака",
    "Энергично наяривает простыни в Твиттер без держателя телефона",
    "Занят ебущимися медведями"
]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn1 = types.KeyboardButton("🤖 Выдать отмазку")
    btn2 = types.KeyboardButton("📅 Когда деньги?")
    btn3 = types.KeyboardButton("🔍 Где Рома?")
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(
        message.chat.id, 
        "Бот активирован! Выберите действие:", 
        reply_markup=markup
    )

@bot.message_handler(content_types=['text'], func=lambda message: True)
def handle_text(message):
    if message.text == "🤖 Выдать отмазку":
        bot.send_message(message.chat.id, random.choice(EXCUSES))
    elif message.text == "📅 Когда деньги?":
        bot.send_message(message.chat.id, f"Официальный ответ поциента:\n«{random.choice(DEADLINES)}»")
    elif message.text == "🔍 Где Рома?":
        bot.send_message(message.chat.id, f"Текущий статус:\nРоман {random.choice(STATUSES)}.")

bot.polling(none_stop=True)
