import logging
import configparser
from telegram.ext import Updater, CommandHandler
config = configparser.ConfigParser()
config.read('config.ini')
updater = Updater(token=config['DEFAULT']['token'], use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
            text="Bot funcionando")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
