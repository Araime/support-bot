import logging
import os

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from dialog import detect_intent_texts
from logs_handler import configure_handler

logger = logging.getLogger('tg_bot')


def start(update, context: CallbackContext):
    """Sending a message when the command /start is issued."""
    update.message.reply_text('Добрый день! Бот поддержки рад приветствовать вас!')


def reply_to_message(update, context: CallbackContext):
    """Responding to user messages using dialogflow."""
    project_id = os.getenv('PROJECT_ID')

    # noinspection PyBroadException
    try:
        answer = detect_intent_texts(
            project_id,
            update.message.chat_id,
            update.message.text,
            'ru-RU')
        update.message.reply_text(answer['answer_text'])
    except Exception:
        logger.exception('tg_bot поймал ошибку при сообщения')


def main():
    load_dotenv()

    configure_handler(logger, os.getenv('TG_SERVICE_BOT'), os.getenv('TG_CHAT_ID'))

    # noinspection PyBroadException
    try:
        logger.info('tg_bot запущен!')
        updater = Updater(os.getenv('TG_DIALOG_BOT'))
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(MessageHandler(Filters.text, reply_to_message))
        updater.start_polling()
        updater.idle()
    except Exception:
        logger.exception('tg_bot поймал ошибку: ')


if __name__ == '__main__':
    main()
