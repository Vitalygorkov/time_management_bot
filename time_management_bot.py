import telebot
from config import api_key
import models

bot = telebot.TeleBot(api_key)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('add', 'del', 'complete')
print('start')


# заготовка с менюшками и кнопками

@bot.message_handler(content_types=['text'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Tasks for 10 years', 'Tasks for the day')
    msg = bot.send_message(message.chat.id, text = 'Нажми кнопку в меню', reply_markup = keyboard )
    menu1 = telebot.types.InlineKeyboardMarkup()
    menu1.add(telebot.types.InlineKeyboardButton(text = 'добавить задачу', callback_data ='add_10_years'))
    menu1.add(telebot.types.InlineKeyboardButton(text = 'Вторая кнопка первого меню', callback_data ='second menu1'))
    menu1.add(telebot.types.InlineKeyboardButton(text = 'третья кнопка первого меню', callback_data='тhree menu1'))

    menu2 = telebot.types.InlineKeyboardMarkup()
    menu2.add(telebot.types.InlineKeyboardButton(text = 'Первая кнопка второго меню', callback_data ='first menu2'))
    menu2.add(telebot.types.InlineKeyboardButton(text = 'Вторая кнопка второго меню', callback_data ='second menu2'))
    menu2.add(telebot.types.InlineKeyboardButton(text = 'третья кнопка второго меню', callback_data='тhree menu2'))


    if message.text == 'Tasks for 10 years':
        msg = bot.send_message(message.chat.id, text='задачи на 10 лет', reply_markup=menu1)
        bot.send_message(message.chat.id, models.task_read(1))
    elif message.text == 'Tasks for the day':
        msg = bot.send_message(message.chat.id, text='Нажми первую inline кнопку', reply_markup=menu2)


@bot.callback_query_handler(func=lambda call: True)
def step2(call):
    menu2call = telebot.types.InlineKeyboardMarkup()
    menu2call.add(telebot.types.InlineKeyboardButton(text = 'Третья кнопка', callback_data ='third'))
    menu2call.add(telebot.types.InlineKeyboardButton(text = 'Четвертая кнопка', callback_data ='fourth'))

    menu10Ycall = telebot.types.InlineKeyboardMarkup()
    menu10Ycall.add(telebot.types.InlineKeyboardButton(text='Третья кнопка', callback_data='third'))
    menu10Ycall.add(telebot.types.InlineKeyboardButton(text='Четвертая кнопка', callback_data='fourth'))

    if call.data == 'first':
        msg = bot.send_message(call.message.chat.id, 'Нажми третью кнопку', reply_markup = menu2call)
    elif call.data == 'add_10_years':
        msg = bot.send_message(call.message.chat.id, 'Вы в меню 10 летних задач, добавить, пометить выполненными?', reply_markup=menu10Ycall)




# предыдущий код который переносим в заготовку
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text.lower() == 'add':
#         bot.send_message(message.from_user.id, 'вы хотите добавить задачу, напишите цифру типа задачи нажмите пробел и напишите задачу', reply_markup=keyboard1)
#         print('Баланс')
#         if message.text.lower().split()[0] == '4':
#             the_task = message.text.split()
#             print(the_task)
#             the_task.remove('4')
#             print(the_task)
#             the_task = ' '.join(the_task)
#             models.task_write(the_task,0,4)
#             bot.send_message(message.from_user.id, 'Added daily task: ' + the_task)
#
#     # elif message.text.lower().split()[0] == '1':
#     #     the_task = message.text.split()
#     #     print(the_task)
#     #     the_task.remove('1')
#     #     print(the_task)
#     #     the_task = ' '.join(the_task)
#     #     bot.send_message(message.from_user.id, 'Добавлена задача на 10 лет: ' + the_task)
#     #
#     # elif message.text.lower().split()[0] == '2':
#     #     the_task = message.text.split()
#     #     print(the_task)
#     #     the_task.remove('2')
#     #     print(the_task)
#     #     the_task = ' '.join(the_task)
#     #     bot.send_message(message.from_user.id, 'Added task for a year: ' + the_task)
#     #
#     # elif message.text.lower().split()[0] == '3':
#     #     the_task = message.text.split()
#     #     print(the_task)
#     #     the_task.remove('3')
#     #     print(the_task)
#     #     the_task = ' '.join(the_task)
#     #     bot.send_message(message.from_user.id, 'Added a task for a month: ' + the_task)
#     # # если в начале предложения 4
#     # elif message.text.lower().split()[0] == '4':
#     #     the_task = message.text.split()
#     #     print(the_task)
#     #     the_task.remove('4')
#     #     print(the_task)
#     #     the_task = ' '.join(the_task)
#     #     models.task_write(the_task,0,4)
#     #     bot.send_message(message.from_user.id, 'Added daily task: ' + the_task)
#
#     # elif message.text.lower().split()[0].isdigit() == True:
#     #     bot.send_message(message.from_user.id, 'task '+ message.text, reply_markup=keyboard1)
#     #     print('task')
#     elif message.text.lower().split()[0] == 'task':
#         the_task = message.text.lower().split()
#         print(the_task)
#         the_task.remove('task')
#         print(the_task)
#         the_task = ' '.join(the_task)
#         bot.send_message(message.from_user.id, 'Added task: ' + the_task)
#
#     # выводим задачи на день
#     else:
#         print(message.text)
#         bot.send_message(message.from_user.id, '1-4(task type) space then task). Tasks for one day: ', reply_markup=keyboard1)
#         tasks = ''
#         num = 1
#         for i in models.task_read(4):
#             tasks += str(num) + '. '+ i[0] + '\n'
#             num +=1
#         bot.send_message(message.from_user.id, tasks, reply_markup=keyboard1)
#
#
bot.polling(none_stop=True, interval=0)
