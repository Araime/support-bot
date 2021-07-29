import logging
import telegram


class TelegramBotHandler(logging.Handler):

    def __init__(self, service_bot_token, chat_id):
        """Adding service-message-bot params."""
        super().__init__()
        self.tg_bot_token = service_bot_token
        self.chat_id = chat_id

    def emit(self, record):
        """Initialization service-message-bot."""
        log_entry = self.format(record)
        service_bot = telegram.Bot(self.tg_bot_token)
        service_bot.send_message(chat_id=self.chat_id, text=log_entry)


def configure_handler(logger, service_bot_token, chat_id):
    """Adding a handler for the logger."""
    logger.setLevel(logging.INFO)
    handler = TelegramBotHandler(service_bot_token, chat_id)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
