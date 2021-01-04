import telebot
from config import api_key

bot = telebot.TeleBot(api_key)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('баланс', 'банк')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == 'баланс':
        bot.send_message(message.from_user.id, 'Баланс', reply_markup=keyboard1)

        print('Баланс')

    else:
        print(message.text)

        bot.send_message(message.from_user.id, 'Задача пробел минуты', reply_markup=keyboard1)


bot.polling(none_stop=True, interval=0)
