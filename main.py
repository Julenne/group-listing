import logging
from telegram.ext import Updater, CommandHandler

updater = Updater(token='1600211792:AAFdWPT9-Gspu2U_dpsAkjYSyVifhyTVIv4', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
            text="Bot funcionando")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
