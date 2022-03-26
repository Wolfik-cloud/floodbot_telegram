import telebot
import config
import colorama
import threading
import requests
from colorama import init
init()

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет</b> ✌️', parse_mode='html')
    bot.send_message(message.chat.id, '', parse_mode='html')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'ulHegPqOPUYVGJ':
        bot.send_message(message.chat.id, 'Промокод <b>активирован</b> ✅', parse_mode='html')

    if message.text == 'dCxDgYqVFCUTPd':
        bot.send_message(message.chat.id, 'Промокод <b>активирован</b> ✅', parse_mode='html')

    if message.text == 'MlwGlGNkMNpTkf':
        bot.send_message(message.chat.id, 'Промокод <b>активирован</b>! ✅', parse_mode='html')

    if message.text == 'OfmPaXrEjWMPOH':
        bot.send_message(message.chat.id, 'Промокод <b>активирован</b>! ✅', parse_mode='html')

    if message.text == 'snIbEJnZVkAjTS':
        bot.send_message(message.chat.id, 'Промокод <b>активирован</b>! ✅', parse_mode='html')

bot.polling(none_stop=True)


