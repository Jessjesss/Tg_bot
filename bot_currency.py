import telebot
import requests
from cfg import TOKEN

bot = telebot.TeleBot(TOKEN)

def get_usd():
    result = []
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = res['Valute']["USD"]['Name'], res['Valute']["USD"]['Value']
    values_usd = ' '.join(str(i) for i in result)
    return(values_usd)

def get_eur():
    result = []
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = res['Valute']["EUR"]['Name'], res['Valute']["EUR"]['Value']
    values_eur = ' '.join(str(i) for i in result)
    return(values_eur)

def get_cny():
    result = []
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = res['Valute']["CNY"]['Name'], res['Valute']["CNY"]['Value']
    values_cny = ' '.join(str(i) for i in result)
    return(values_cny)

@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(message.chat.id, f'Привет, напиши код валюты и я пришлю тебе актуальный курс!')


@bot.message_handler(commands=['help'])
def start_game(message):
    bot.send_message(message.chat.id, 'Доступен курс на 3 валюты: доллар, евро, китайский юань. \nПример ввода: USD - ответ: Доллар США (курс)')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.strip().upper() == 'USD':
        bot.send_message(message.chat.id, get_usd())
    elif message.text.strip().upper() == 'EUR':
        bot.send_message(message.chat.id, get_eur())
    elif message.text.strip().upper() == 'CNY':
        bot.send_message(message.chat.id, get_cny())
    else:
        bot.send_message(message.chat.id, 'Введите: USD, EUR или CNY!')


bot.infinity_polling()
