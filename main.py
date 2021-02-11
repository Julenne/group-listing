import logging
import configparser
from telegram.ext import Updater, CommandHandler

text_newlist = ""
array = []
config = configparser.ConfigParser()
config.read('config.ini')
updater = Updater(token=config['DEFAULT']['token'], use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
            text="Olá, seja bem vindo(a) ao Group Listing Bot.\nEste bot cria uma lista com o que os participantes do grupo adicionarem nela.\nPara começar, adicione este bot à um grupo. ")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def newlist(update, context):
        global text_newlist
        text_newlist = ' '.join(context.args).upper()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Nome da lista: " + text_newlist)
newlist_handler = CommandHandler('newlist', newlist)
dispatcher.add_handler(newlist_handler)

def listing(update, context):
    text_listing = ' '.join(context.args)
    array.append(text_listing)    
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_newlist + "\n" + str(array))
listing_handler = CommandHandler('listing', listing)
dispatcher.add_handler(listing_handler)

updater.start_polling()
