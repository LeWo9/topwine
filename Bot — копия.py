import telebot
import random
from telebot import types

# Загружаем список интересных фактов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()


# Создаем экземпляр бота
bot = telebot.TeleBot('5568215227:AAGrFuJIBykFk43s96zjesZ_2_I-KxgZpOU')



# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        markup.add(item1)
        bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт' :
            answer = random.choice(facts)
    else:
            answer = ('Вы написали: ' + message.text)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
