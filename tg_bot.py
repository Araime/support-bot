import logging
import os
import time

from dotenv import load_dotenv
from telegram.chataction import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from dialog import detect_intent_texts
from logs_handler import configure_handler

logger = logging.getLogger('tg_bot')


def start(update, context: CallbackContext):
    """Sending a message when the command /start is issued."""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    time.sleep(1)
    update.message.reply_text('Добрый день! Бот поддержки рад приветствовать вас!')


def error_callback(update, error):
    """Handling all errors."""
    logger.exception('Update "%s" caused error "%s"', update, error)


def reply_to_message(update, context: CallbackContext):
    """Responding to user messages using dialogflow."""
    project_id = os.getenv('PROJECT_ID')

    answer = detect_intent_texts(
        project_id,
        update.message.chat_id,
        update.message.text,
        'ru-RU')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    time.sleep(1)
    update.message.reply_text(answer['answer_text'])


def main():
    load_dotenv()

    configure_handler(logger, os.getenv('TG_SERVICE_BOT'), os.getenv('TG_CHAT_ID'))

    logger.info('tg_bot запущен!')
    updater = Updater(os.getenv('TG_DIALOG_BOT'))
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, reply_to_message))
    dispatcher.add_error_handler(error_callback)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
