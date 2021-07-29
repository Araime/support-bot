import logging
import os
import random

import vk_api as vk
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from dialog import detect_intent_texts
from logs_handler import configure_handler

logger = logging.getLogger('vk_bot')


def echo(event, vk_api):
    """Responding to user messages using dialogflow."""
    project_id = os.getenv('PROJECT_ID')

    answer = detect_intent_texts(
        project_id,
        event.user_id,
        event.text,
        'ru-RU')

    if not answer['is_fallback']:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer['answer_text'],
            random_id=random.randint(0, 100000))


def main():
    load_dotenv()

    configure_handler(logger, os.getenv('TG_SERVICE_BOT'), os.getenv('TG_CHAT_ID'))

    # noinspection PyBroadException
    try:
        logger.info('vk_bot запущен!')
        vk_session = vk.VkApi(token=os.getenv('VK_GROUP_TOKEN'))
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                echo(event, vk_api)
    except Exception:
        logger.exception('vk_bot поймал ошибку: ')


if __name__ == '__main__':
    main()
