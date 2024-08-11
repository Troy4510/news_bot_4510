import sql_module as sql
import parser_module as parser
import datetime
import configparser
import urllib.request
import telebot
from telebot import types
import requests
import time

settings = configparser.ConfigParser()
settings.read('config.ini')
bot_key = settings['settings']['bot_key']
channel_id = settings['settings']['channel_id']
news_site = settings['settings']['news_site']
db_name = settings['settings']['db_name']
update_time = int(settings['settings']['update_time'])

bot1 = telebot.TeleBot (bot_key)
sql.check_base(db_name)

def read_and_pack(url):
    news = parser.go(url)
    total = len(news)
    print(f'found: {total} raw objects')
    for new in news:
        time = new[0]
        name = new[1]
        link = new[2]
        sql.add_record(db_name, time, name, link)
        
def publicate_today(db_name):
    today = sql.read_today_records(db_name)
    for each in today:
        #print(each)#2,3,4
        msg = f"{each[2]} <a href={each[4]}>{each[3]}</a>."
        bot1.send_message(chat_id=channel_id , text=f'{each[1]} в {each[2]}:')
        bot1.send_message(chat_id=channel_id , text=f'{each[4]}')
        time.sleep(30)

'''
@bot1.message_handler(commands=['start'])
def start(message):
    dt = datetime.datetime.now().strftime('%d.%m.%y/%H:%M')
    bot1.send_message(chat_id=channel_id , text=f'старт бота {dt}')

@bot1.message_handler(commands=['stop'])
def stop(message):
    dt = datetime.datetime.now().strftime('%d.%m.%y/%H:%M')
    bot1.send_message(chat_id=channel_id , text=f'стоп бота {dt}')
    bot1.stop_polling()
'''

def get_updates(offset=0):
    url = 'https://api.telegram.org/bot'
    result = requests.get(f'{url}{bot_key}/getUpdates?offset={offset}').json()
    return result['result']

#read_and_pack(news_site)
publicate_today(db_name)


while True:
    dt = datetime.datetime.now().strftime('%H:%M:%S')
    #bot1.send_message(chat_id=channel_id , text=f'проверка таймера(5) {dt}')
    #time.sleep(update_time * 60)
    x = get_updates()
    last = len(x) - 1
    exp = x[last]['message']['from']['first_name']
    str1 = x[last]['message']['text']
    print(f'{exp} : {str1}')
    time.sleep(10)

'''
while True:
    try:
        bot1.polling(none_stop=True, interval = 5)
    except Exception as e:
        print(e)
        time.sleep(15)
'''