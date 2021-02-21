import logging
import configparser
import telepot
from telegram.ext import Updater, CommandHandler, MessageHandler

text_newlist = ""
text_sent = ""
array = []
config = configparser.ConfigParser()
config.read('config.ini')
updater = Updater(token=config['DEFAULT']['token'], use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Olá, seja bem vindo(a) ao Group Listing Bot."
        + "\n Este bot cria uma lista com o que os participantes do grupo adicionarem nela."
        + "\n Para começar, adicione este bot à um grupo. Para utilizar:"
        + "\n /newlist - Para criar uma nova lista "
        + "\n /add - Para adicionar um elemento à lista")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def newlist(update, context):
        global text_newlist
        global text_sent
        text_newlist = ' '.join(context.args).upper()
        text_sent = context.bot.send_message(chat_id=update.effective_chat.id, 
                text="Nome da lista: " + text_newlist)
        
newlist_handler = CommandHandler('newlist', newlist)
dispatcher.add_handler(newlist_handler)


def listing(update, context):
        text_listing = ' '.join(context.args)
        array.append(text_listing)    
        context.bot.edit_message_text(chat_id=update.effective_chat.id, 
                message_id=text_sent.message_id,
                text=text_sent.text + "\n" + '\n'.join(array))
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id = update.message.message_id)
    #context.bot.send_message(chat_id=update.effective_chat.id, text=text_newlist + "\n" + str(array))
listing_handler = CommandHandler('add', listing)
dispatcher.add_handler(listing_handler)



updater.start_polling()
