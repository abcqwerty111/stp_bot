import sqlite3
import telebot
from telebot import *

bot = telebot.TeleBot("878479849:AAE6JYUMCYfslkFC_ZOGsh9SQCx3BXL3tTQ", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add('Скинь документ')
	bot.reply_to(message, 'Введите слово или словосочетание для поиска. Для получения документа с вопросами и ответами нажми "Скинь документ"', reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	
	cid = message.chat.id

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add('Скинь документ')

	if message.text == 'Скинь документ':
		doc = open('1-220.docx', 'rb')
		bot.send_document(cid, doc, reply_markup=markup)

	else:
		con = sqlite3.connect('bot_db.sqlite3')
		cur = con.cursor()
		for row in cur.execute('SELECT * FROM answers'):
			if (message.text in str(row[1])) or (message.text.lower() in str(row[1])) or (message.text.upper() in str(row[1])) or (message.text.capitalize() in str(row[1])):
				answer = f'''{row[1]}\n\n{row[2]}'''
				bot.send_message(cid, answer, reply_markup=markup)
				print(answer)

bot.polling()