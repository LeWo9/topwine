import telebot
import random
from telebot import types

# Загружаем список вина
f = open('data/wine.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

tempr = "Игристое: 6–10 °С.\nБелое: 6–12 °C.\nРозовое: 6–8 °C.\nКрасное: 10–18 °С"

# Создаем экземпляр бота
bot = telebot.TeleBot('5568215227:AAGrFuJIBykFk43s96zjesZ_2_I-KxgZpOU')


# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем кнопку
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Выбери вино")
        markup.add(item1)
        item2=types.KeyboardButton("Температура подачи")
        markup.add(item2)
        bot.send_message(m.chat.id, 'Привет! Могу посоветовать вино на сегодня, для этого нажми: \n-->Выбери вино\nА ещё ты всегда можешь узнать идеальную температуру подачи вина, для этого нажми: \n-->Температура подачи',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему вино
    if message.text.strip() == 'Выбери вино' :
            answer = random.choice(facts)
    elif message.text.strip() == 'Температура подачи' :
            answer = tempr
    else:
            answer = ('Вы написали: ' + message.text + "\nЧтобы узнать, что я могу, нажми: /start")
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
