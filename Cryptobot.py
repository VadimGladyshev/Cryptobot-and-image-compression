import requests
from bs4 import BeautifulSoup as bs
import telebot
from telebot import types

URL = 'https://myfin.by/crypto-rates'
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
api_key = '5423845526:AAEqW5ax6KYeKfCkZvf0VK7WpDB4TcE_lqk'

def parser(url):

    r = requests.get(url, headers = headers)

    html = bs(r.content, 'html.parser')

    table = html.findAll('tbody', {'class' : 'table-body'}) 

    return [c.text for c in table]

list_of_crypto = parser(URL)

bot = telebot.TeleBot(api_key)

#@bot.message_handler()
#def init(message):
    #bot.send_message(message.chat.id, '<b>Commands list:</b>' '\n' '\n' '/start - launch the bot' '\n' '/show - show the cryptotable' '\n' '/site - go on the website', parse_mode='html')


@bot.message_handler(commands = ['start'])
def hello(message):
    bot.send_message(message.chat.id, '<b>Commands list:</b>' '\n' '\n' '/start - launch the bot' '\n' '/show - show the cryptotable' '\n' '/site - go on the website', parse_mode='html')
    bot.send_message(message.chat.id, 'Hi, go watching?')

@bot.message_handler(commands = ['show'])
def hello(message):
    bot.send_message(message.chat.id, 'Cryptocurrences:')
    bot.send_message(message.chat.id, list_of_crypto[0])
    bot.send_message(message.chat.id, 'Press r button to show it again')

@bot.message_handler(commands = ['site'])
def test(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("view on the website", url = 'https://coinmarketcap.com/'))
    bot.send_message(message.chat.id, 'link:', reply_markup=markup)

@bot.message_handler(content_types = ['text'])

def hi(message):

    if message.text.lower() == 'hi' or message.text.lower() == 'hello' or message.text.lower() == 'привет' or message.text.lower() == 'здарова':
        bot.send_message(message.chat.id, 'Hi, how are doing?')
    elif message.text.lower() == 'fine' or message.text.lower() == 'nice' or message.text.lower() == 'good' or message.text.lower() == 'хорошо' or message.text.lower() == 'нормально':
        bot.send_message(message.chat.id, 'Me too, go looking at crypto!')
        bot.send_message(message.chat.id, 'Cryptocurrences:')
        bot.send_message(message.chat.id, list_of_crypto[0])
        bot.send_message(message.chat.id, 'Press r button to show it again')
    elif message.text.lower() == 'r' or message.text.lower() == 'go': 
        bot.send_message(message.chat.id, 'Cryptocurrences:')
        bot.send_message(message.chat.id, list_of_crypto[0])
        bot.send_message(message.chat.id, 'Press r button to show it again')
    else:
        bot.send_message(message.chat.id, 'One more time:)')


bot.polling(none_stop = True)