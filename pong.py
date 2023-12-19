import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from playsound import playsound

# Token deines Telegram-Bots hier einfügen
TELEGRAM_BOT_TOKEN = 'Api key'

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hallo! Schreibe /ping, um ein Pong zu hören.')

def ping(update: Update, context: CallbackContext):
    mp3_file = 'pong.mp3'
    playsound(mp3_file)
    update.message.reply_text('Ja!')

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Handler für /start und /ping Befehle
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ping", ping))

    # Starte den Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
