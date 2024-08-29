import os
import telebot

from telebot import types
bot = telebot.TeleBot('7512140873:AAGiIaaU5FB1Ej4ByEIvvKdfJSSlatFGiz8')
category = 'Не указан'
budget = 'Не указан'
@bot.message_handler(commands=['start', 'hello'])
def start(message):
	markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	btn1 = types.KeyboardButton('Лендинги, промостраницы')
	btn2 = types.KeyboardButton('Корпоративные сайты')
	btn3 = types.KeyboardButton('Интернет-магазины')
	btn4 = types.KeyboardButton('Десктопные / мобильные приложения и telegram-боты')
	btn5 = types.KeyboardButton('Редизайн сайта')
	btn6 = types.KeyboardButton('Техническая поддержка')
	markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
	bot.send_message(message.chat.id, "Привет! 👋\nНужна помощь в разработке, дизайне или продвижении сайта? Напишите мне, и я с удовольствием помогу! 💻\nНачнем работу? Выберите интересующую услугу или задайте свой вопрос. Мы сделаем всё возможное, чтобы ваш проект стал успешным!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Лендинги, промостраницы', 'Корпоративные сайты', 'Интернет-магазины', 'Десктопные / мобильные приложения и telegram-боты', 'Редизайн сайта', 'Техническая поддержка'])
def budget(message):
	category = message.text
	markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	btn1 = types.KeyboardButton('100.000 - 200.000 ₽')
	btn2 = types.KeyboardButton('200.000 - 500.000 ₽')
	btn3 = types.KeyboardButton('500.000 - 1 млн ₽')
	btn4 = types.KeyboardButton('от 1 млн ₽')
	markup.add(btn1, btn2, btn3, btn4)
	bot.send_message(message.chat.id, "Какой ожидаемый бюджет?", reply_markup=markup)
                          
	@bot.message_handler(func=lambda message: message.text in ['100.000 - 200.000 ₽', '200.000 - 500.000 ₽', '500.000 - 1 млн ₽', 'от 1 млн ₽'])
	def tasks(message):
		budget = message.text
		markup = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Опишите задачу и предпочтения: ", reply_markup=markup)
		@bot.message_handler(content_types=['text'])
		def get_tasks(message):
			task = 'Выбранная услуга - ' + category + '\n' + 'Бюджет - ' + budget + '\n' + 'О задаче: ' + message.text
			bot.send_message(message.chat.id, 'Загрузите ТЗ: ')
			@bot.message_handler(content_types=['document'])
			def get_tz(message):
				chat_id = message.chat.id
				username = message.from_user.username
				file_info = bot.get_file(message.document.file_id)
				downloaded_file = bot.download_file(file_info.file_path)
				src = f'C:/Users/artem/OneDrive/Desktop/QUASAR/files/{username}/' + message.document.file_name
				if not os.path.exists(os.path.dirname(src)):
					os.makedirs(os.path.dirname(src))
				with open(src, 'wb') as new_file:
					new_file.write(downloaded_file)
				task_file = f'C:/Users/artem/OneDrive/Desktop/QUASAR/files/{username}/task.txt'
				with open(task_file, 'w', encoding='utf-8') as f:
					f.write(task)
				bot.send_message(message.chat.id, 'Ваше ТЗ получено! Ожидайте ответа менеджера.')
bot.infinity_polling()