
# Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.


import telebot
import sys
from cfg import TOKEN
from random import choice
from random import randint

bot = telebot.TeleBot(TOKEN)

candies = 117

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Условие игры: На столе лежит 117 конфет. \nИграют два игрока делая ход друг после друга. \nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход.")

@bot.message_handler(commands=['start'])
def start_game(message):
    global candies
    bot.send_message(message.chat.id, f'На столе лежит: {str(candies)} конфет')
    determing_moves = choice(['User', 'Bot'])
    bot.send_message(message.chat.id, f'Первым ходит:  {determing_moves}')
    if determing_moves == 'Bot':
        rand = randint(1, 29)
        bot.send_message(message.chat.id, f'Бот взял: {rand} конфет')
        candies = int(candies) - rand
        bot.send_message(message.chat.id, f'Осталось: {candies} конфет')
        bot.send_message(message.chat.id, f'User, твой ход!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    global candies
    if int(message.text.lower()) <= 28:
        candies = int(candies) - int(message.text.lower())
        bot.send_message(message.chat.id, f'Осталось: {candies} конфет')
        if candies <= 28:
            bot.send_message(message.chat.id, f'Бот взял: {candies} конфет')
            bot.send_message(message.chat.id, 'Bot победил!')
            sys.exit()
        else:
            rand = randint(1, 29)
            bot.send_message(message.chat.id, f'Бот взял: {rand} конфет')
            candies = int(candies) - rand
            bot.send_message(message.chat.id, f'Осталось: {candies} конфет')
            bot.send_message(message.chat.id, f'User, твой ход!')
    else:
        bot.send_message(message.chat.id, 'Введите допустимое количество конфет!')
    if candies <= 28:
        bot.send_message(message.chat.id, 'User победил!')

    
bot.infinity_polling()

