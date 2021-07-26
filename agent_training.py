import json
import logging
import os

from dotenv import load_dotenv
from google.cloud import dialogflow_v2 as dialogflow

from logs_handler import create_handler

os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
logger = logging.getLogger('agent_training')


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []

    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[message_texts])
    message = dialogflow.Intent.Message(text=text)
    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])
    intents_client.create_intent(request={'parent': parent, 'intent': intent})


def get_intents_sheet(project_id):
    """Get a list of all intents."""
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    intents = intents_client.list_intents(request={"parent": parent})
    return intents


def delete_intent(project_id, intent_id):
    """Delete intent with the given intent type and intent value."""
    intents_client = dialogflow.IntentsClient()
    intent_path = intents_client.intent_path(project_id, intent_id)
    intents_client.delete_intent(name=intent_path)


def main():
    load_dotenv()
    project_id = os.getenv('PROJECT_ID')

    create_handler(logger, os.getenv('TG_SERVICE_BOT'), os.getenv('TG_CHAT_ID'))
    logger.info('agent_training запущен!')

    with open('questions.json', 'r', encoding='utf-8') as file:
        training_phrases = json.load(file)

    intents_sheet = get_intents_sheet(project_id)
    for theme_name in training_phrases:
        display_name = theme_name
        training_phrases_parts = training_phrases[theme_name]['questions']
        message_texts = training_phrases[theme_name]['answer']
        for intent in intents_sheet:
            if intent.display_name == display_name:
                intent_id = intent.name.split('/')[-1]
                delete_intent(project_id, intent_id)
        create_intent(project_id, display_name, training_phrases_parts, message_texts)

    logger.info('agent_training загрузил новые фразы!')


if __name__ == '__main__':
    main()
