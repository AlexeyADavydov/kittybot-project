import requests

from telegram import Bot

bot = Bot(token='6470259487:AAFyJ-E1aMelGuD1AuXqWB_hUs8QHoFonns')
URL = 'https://api.thecatapi.com/v1/images/search'  
chat_id = 51462465


response = requests.get(URL).json()
random_cat_url = response[0].get('url')  
bot.send_photo(chat_id, random_cat_url) 

# print(response)
# print(type(response))
# print(len(response))
# print(type(response[0]))











'''

from telegram import Bot

bot = Bot(token='6470259487:AAFyJ-E1aMelGuD1AuXqWB_hUs8QHoFonns')

URL = 'https://cdn2.thecatapi.com/images/3dl.jpg'

chat_id = 51462465
text = 'Вам телеграмма!'
# Отправка сообщения
bot.send_message(chat_id, text)
# Отправка изображения
bot.send_photo(chat_id, URL)'''