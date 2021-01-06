
import base64
import logging

# import requests
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('The function has been invoked')

    records = event.get('records', {})

    for topic_partition, messages in records.items():
        logger.info('Processing topic partition ' + topic_partition)
        for message in messages:
            logger.info('Received message: ' + str(message))
            decoded_value = base64.b64decode(message['value'].encode('utf-8')).decode('utf-8')
            logger.info('Decoded message value: ' + decoded_value)
