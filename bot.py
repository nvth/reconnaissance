from telegram.ext import Updater, CommandHandler
from data import *
TOKEN = get_bot_token()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am your bot.")

def main():
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("scan", scan_nuclei))
    
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()