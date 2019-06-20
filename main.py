import telebot
from telebot import types

import config
from BotUpdates import BotHandler

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['nomer1'])
def joke_1(message):
    bot.send_message(message.chat.id, "")


@bot.message_handler(commands=['nomer2'])
def joke_2(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer3'])
def joke_3(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer4'])
def joke_4(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer5'])
def joke_5(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer6'])
def joke_6(message):
    bot.send_message(message.chat.id, '')

#работает только для личного чата
@bot.message_handler(commands=["geophone"])
def geophone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением!", reply_markup=keyboard)


@bot.message_handler(commands=['nomer7'])
def joke_7(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer8'])
def joke_8(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer9'])
def joke_9(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer10'])
def joke_10(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer11'])
def joke_11(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer12'])
def joke_12(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer13'])
def joke_13(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer14'])
def joke_14(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['nomer15'])
def joke_15(message):
    bot.send_message(message.chat.id, '')


bot.polling(none_stop=True)
