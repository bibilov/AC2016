from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
# Библиотека python-telegram-bot

updater = Updater(token='261792627:AAGhxxvgZomBzNlpioa5D0ldDTv9m_fGQJc')
dispatcher = updater.dispatcher

def calc(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=eval(update.message.text))

calc_handler = MessageHandler([Filters.text], calc)
dispatcher.add_handler(calc_handler)

updater.start_polling()
