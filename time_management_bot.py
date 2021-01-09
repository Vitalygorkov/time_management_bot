import telebot
from config import api_key
import models

bot = telebot.TeleBot(api_key)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('задача', 'банк')
print('start')
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == 'Go':
        bot.send_message(message.from_user.id, 'начинаем эффективную работу', reply_markup=keyboard1)
        print('Баланс')
    elif message.text.lower().split()[0] == '1':
        the_task = message.text.split()
        print(the_task)
        the_task.remove('1')
        print(the_task)
        the_task = ' '.join(the_task)
        bot.send_message(message.from_user.id, 'Добавлена задача на 10 лет: ' + the_task)

    elif message.text.lower().split()[0] == '2':
        the_task = message.text.split()
        print(the_task)
        the_task.remove('2')
        print(the_task)
        the_task = ' '.join(the_task)
        bot.send_message(message.from_user.id, 'Добавлена задача на год: ' + the_task)

    elif message.text.lower().split()[0] == '3':
        the_task = message.text.split()
        print(the_task)
        the_task.remove('3')
        print(the_task)
        the_task = ' '.join(the_task)
        bot.send_message(message.from_user.id, 'Добавлена задача на месяц: ' + the_task)

    elif message.text.lower().split()[0] == '4':
        the_task = message.text.split()
        print(the_task)
        the_task.remove('4')
        print(the_task)
        the_task = ' '.join(the_task)
        task_4 = models.TaskObject(the_task,0,4)
        bot.send_message(message.from_user.id, 'Добавлена задача на день: ' + the_task)

    elif message.text.lower().split()[0].isdigit() == True:
        bot.send_message(message.from_user.id, 'задание '+ message.text, reply_markup=keyboard1)
        print('задание')
    elif message.text.lower().split()[0] == 'задача':
        the_task = message.text.lower().split()
        print(the_task)
        the_task.remove('задача')
        print(the_task)
        the_task = ' '.join(the_task)
        bot.send_message(message.from_user.id, 'Добавлена задача: ' + the_task)
    else:
        print(message.text)
        bot.send_message(message.from_user.id, '1-4(тип задачи) пробел задача. Задачи на один день: ', reply_markup=keyboard1)
        tasks = ' '
        for i in models.task_read():
            tasks += i[0] + '\n'
        bot.send_message(message.from_user.id, tasks, reply_markup=keyboard1)


bot.polling(none_stop=True, interval=0)
