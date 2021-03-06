# импортируем необходимые библиотеки


import telebot
from telebot import types
from dictionary_for_files import storage
from keyboa import keyboa_maker
import random
from PIL import Image
from urllib.request import urlopen
import os

token = os.environ.get('token')

# инициируем бота: обращаемся к библиотеке telebot, к классу, который берет на вход токен
bot = telebot.TeleBot(token)

# смайлики для инлайн клавиатуры для реакции на отправку мемов
smiles = [{'Класс\U0001F44D': 'class'},
          {'Такое себе\U0001F44E': 'nu_takoe'}, ]

# мем в ответ на непонравившийся мем
Nu_takoe_url = 'https://sun9-5.userapi.com/impg/ewevUQOxhDp2VomTkEmvZs_DbzhKXXz79z0fEQ/wnvGMJ7Qn4k.jpg?size=512x443&quality=96&sign=a1dadb47ac24182544a5b793fb8e6f90&type=album'
Kill = Image.open(urlopen(Nu_takoe_url))

# клавиатура с реакцией на мемы
kb_smiles = keyboa_maker(items=smiles, items_in_row=2)


# отправка рандомного мема из массива мемов при нажатии /mem
@bot.message_handler(commands=['mem'])
def mem_message(message):
    mem_links = [
        'https://sun9-73.userapi.com/impg/-n4ZfMst3A5pQ4d3FGDN8VMzCBOeoOYEzuoKHg/Nrvk7E9q8Yk.jpg?size=1500x1206&quality=96&sign=112ec3119e313070084120c7f8bb3b91&type=album',
        'https://sun9-23.userapi.com/impg/Gr-mqJIMlvCltU1kYhGnHRGmETNMP9aFtWwc1w/n9ANM7udTKg.jpg?size=1080x718&quality=96&sign=40709512045a092d55d5bd4eb05fe7cd&type=album',
        'https://sun9-44.userapi.com/impf/c626429/v626429824/1188a/uBTvTjjl6Nw.jpg?size=780x960&quality=96&sign=e6a04fb8ae16f25f83d84958467dce1c&type=album',
    'https://sun9-28.userapi.com/impf/c626924/v626924580/38304/ZDC34aZKYIk.jpg?size=787x960&quality=96&sign=c0467b72469914c745b068df626e9511&type=album',
    'https://sun9-71.userapi.com/impg/3-exnR6ZNPQ0IQ_QzfO_iMDXdfGY9nh17BE71Q/8okrYG8Vyic.jpg?size=1742x1342&quality=96&sign=7bcc9eabbff4d3bfa8a1ef30f4925617&type=album',
    'https://sun9-38.userapi.com/impg/HaQtWZivvW5TUTkF5SzV6P9h3tMQH5u5wNjqqA/rwjtdMyCeqI.jpg?size=1138x1282&quality=96&sign=7b21d8763bb794b275e2da8afcf5fedf&type=album',
    'https://sun9-1.userapi.com/impg/IGyvEEqDaRKKESauBhIhHuoLeEDvxwPA8tlIvQ/GI5GvN3Cedo.jpg?size=640x473&quality=96&sign=4b1b20996076d3cf0cd9b66006c6d0f6&type=album',
    'https://sun9-1.userapi.com/impg/QyuYxZ_bE8RmPAnAg7aU3sKitOlnyjewMZmhrw/qh42iuTiicE.jpg?size=1420x948&quality=96&sign=2c8e8e241a9beec0fefd9a40648374c1&type=album',
    'https://sun9-1.userapi.com/impg/A-x3jlbpZ-N8ftRNwXl3t2jYJTXdB_F-KXEEnA/kC6sxqMwc00.jpg?size=1024x768&quality=96&sign=02c0a02234cf502136738b900ef08818&type=album',
    'https://sun9-33.userapi.com/impg/4O5i9BWafOF7JijmrApjM2CR8r7ogzYK1c48hA/bYxevE7_rAY.jpg?size=1486x1252&quality=96&sign=4f9d974b84eb9b9b7561e54d293cd60a&type=album',
    'https://sun9-26.userapi.com/impg/0PVPY2SoUSPy1_lrCgh6OZ81MHFB1V7zm8iZfA/pfSqa8DWX3w.jpg?size=1170x897&quality=96&sign=196bbc7dc9ca891d5bd5c95ba345441f&type=album',
    'https://sun9-50.userapi.com/impg/lT1Lei2MhD_g4iGW73OL6h5qGrCAYtl4kABDXg/A9fk1vE9gMo.jpg?size=828x810&quality=96&sign=5728c518a54dfd7a119312ef2816990a&type=album',
    'https://sun9-13.userapi.com/impf/c621704/v621704627/8fd88/3Mi-hwIiZLc.jpg?size=720x525&quality=96&sign=b9b3f426f2e4d2b339e45222109bcff2&type=album',
    'https://sun9-28.userapi.com/impf/c834203/v834203658/1953f5/c2OYGmm7Rts.jpg?size=640x526&quality=96&sign=541b3483b5b1a12bb43c7505beb04eaf&type=album']
    choice_mem = random.choice(mem_links)
    img = Image.open(urlopen(choice_mem))
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.from_user.id, 'Как тебе мем?\U0001F609', reply_markup=kb_smiles)
    # вместе с мемом присылает вопрос "Как тебе мем?" и клавиатуру с выбором "Класс" или "Такое себе"
    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == 'class':
            bot.send_message(call.message.chat.id, 'Запомню;)')
        elif call.data == "nu_takoe":
            bot.send_photo(message.chat.id, Kill)


# реакция бота на команду /start с приветствием (сделать обращение по имени??)
@bot.message_handler(commands=['start'])
def start(message):
    line1 = 'Привет!\U0001F44B\n'
    line2 = 'Я лабораторный бот-помощник.\nЯ помогу тебе найти нужный протокол для работы. ' \
            'Можешь воспользоваться поиском по темам или ввести ключевое слово\n\n'
    line3 = 'Нажми /search, чтобы начать поиск'
    msg = line1+line2+line3
    bot.send_message(message.chat.id, msg)


# реакция бота на команду /help
@bot.message_handler(commands=['help'])
def help(message):
    line1 = 'Чтобы начать поиск протоколов, нажми /search и выбери нужный формат поиска. ' \
            'Чтобы посмотреть мемы про жизнь в лабе, нажми /mem'
    bot.send_message(message.chat.id, line1)


# реакция бота на команду /search, клавиатура с выбором метода поиска
@bot.message_handler(commands=['search'])
def first(message):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('По ключевому слову')
    keyboard.row('По теме')
    how = 'Как будем искать?'
    send = bot.send_message(message.chat.id, how, reply_markup=keyboard)
    bot.register_next_step_handler(send, second)


# какая-то магия с register_next_step_handler
# первый аргумент - объект отправленного сообщения (send), второй - что следующее сообщение
# от пользователя будет обработано функцией third и т.п.
def second(message):
    if message.text == 'По теме':
        keyboard = types.ReplyKeyboardMarkup(True, True)
        # клавиатура для выбора темы протокола
        keyboard.row('DNA', 'RNA')
        keyboard.row('Обратная транскрипция')
        keyboard.row('PCR', 'Назад')
        send = bot.send_message(message.chat.id, 'Выбери тему', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == 'По ключевому слову':
        send = bot.send_message(message.chat.id, 'Введи ключевое слово на русском:')
        bot.register_next_step_handler(send, third)
    else:
        bot.send_message(message.chat.id, 'Если тебе нужна помошь, нажми /help')


# выбор конкретной темы и отправка протокола пользователю
def third(message):
    if message.text == 'DNA':
        keyboard = types.ReplyKeyboardMarkup(True, True)
        keyboard.row('По-Хомченски', 'Магнитные частицы')
        keyboard.add('Назад')
        send = bot.send_message(message.chat.id, 'Выбери протокол', reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
    elif message.text == 'RNA':
        keyboard = types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Extract RNA')
        keyboard.add('Назад')
        send = bot.send_message(message.chat.id, 'Выбери протокол', reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
    elif message.text == 'Обратная транскрипция':
        bot.send_message(message.from_user.id, storage['обратная транскрипция'])
        bot.send_message(message.from_user.id, 'Чтобы начать новый поиск, нажми /search. '
                                               'А пока ждешь таймер, можешь развлечь себя мемами /mem')

    elif message.text == 'PCR':
        bot.send_message(message.from_user.id, storage['usual PCR'])
        bot.send_message(message.from_user.id, 'Чтобы начать новый поиск, нажми /search. '
                                               ' пока ждешь таймер, можешь развлечь себя мемами /mem')
    # можно вернуться назад в основное меню
    elif message.text == 'Назад':
        first(message)
    # поиск по ключу, распаковка словаря, ввод текста пользователем, поиск совпадений
    else:
        list = [*storage]
        found_links = []
        for i in list:
            if message.text.lower() in i:
                found_links.append(storage[i])

        if len(found_links) > 0:
            bot.send_message(message.from_user.id, "\n\n".join(found_links))
            bot.send_message(message.from_user.id, 'Чтобы начать новый поиск, нажми /search')
        else:
            bot.send_message(message.from_user.id, 'Совпадений не найдено. Попробуй ввести другое слово, например: ДНК.'
                                                   '\nНажми /search, чтобы начать поиск')


# отправка конкретных протоколов
def fourth(message):
    if message.text == 'По-Хомченски':
         bot.send_message(message.from_user.id, storage['выделение днк хомченко по-хомченко'])
         bot.send_message(message.from_user.id, 'Чтобы начать новый поиск, нажми /search. '
                                                'А пока ждешь таймер, можешь развлечь себя мемами /mem')
    elif message.text == 'Магнитные частицы':
        bot.send_message(message.from_user.id, storage['выделение днк магнитные частицы магниты'])
        bot.send_message(message.from_user.id, 'Чтобы начать новый поиск, нажми /search. '
                                               'А пока ждешь таймер, можешь развлечь себя мемами /mem')
    elif message.text == 'Назад':
        first(message)
    elif message.text == 'Extract RNA':
        bot.send_message(message.from_user.id, storage['выделение рнк'])
        bot.send_message(message.from_user.id, 'Чтобы начать новый поиск, нажми /search. '
                                               'А пока ждешь таймер, можешь развлечь себя мемами /mem')


# почему я просто переставила это вниз, и все заработало...?
@bot.message_handler(content_types=['text'])
def stupid_message(message):
    greet = ['hello','hi','привет', 'приветик', 'прив', 'здарова', 'здравствуй']
    if any(greetings in message.text.lower() for greetings in greet):
        bot.send_message(message.from_user.id, 'Рад тебя видеть! Я скучал по тебе')
# а если напишешь какую-нибудь хрень помимо приветствий, он предложит тебе помочь, хе-хе
    else:
        bot.send_message(message.from_user.id, 'Если тебе нужна помощь, нажми /help')


bot.polling()
