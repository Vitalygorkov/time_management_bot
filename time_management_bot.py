import telebot
from config import api_key
import time


bot = telebot.TeleBot(api_key)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('баланс', 'банк')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == 'баланс':
        bot.send_message(message.from_user.id, 'Баланс', reply_markup=keyboard1)

        print('Баланс')



    #
    #
    # elif message.text.lower() == 'банк':
    #     bot.send_message(message.from_user.id, "В банке: ")
    #
    # elif message.text.lower().split(' ')[0] == 'займ':
    #     bot.send_message(message.from_user.id, "Вы занимаете у банка: " + str(message.text.lower().split(' ')[1]))
    #     try:
    #         bank = 'bank - int(message.text.lower().split(' ')[1])'
    #
    #     except Exception as e:
    #         print(e)
    #         bot.send_message(message.from_user.id, "Ошибка: " + str(e))
    #



    else:
        print(message.text)

        bot.send_message(message.from_user.id, 'Задача пробел минуты', reply_markup=keyboard1)


bot.polling(none_stop=True, interval=0)