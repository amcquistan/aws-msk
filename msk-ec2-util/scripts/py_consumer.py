import argparse
import logging

from kafka import KafkaConsumer
from kafka.errors import KafkaConfigurationError


logging.basicConfig(
  format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S',
  level=logging.INFO
)


def consume_from_topic(bootstrap_servers, topic, auto_offset_reset='latest'):
    try:
        consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, auto_offset_reset=auto_offset_reset)
        consumer.subscribe(topic)

        for msg in consumer:
            logging.info("New Message:\n  - %s" % (msg, ))

    except KafkaConfigurationError as e:
        logging.error(str(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('kafka', help='Bootstrap servers')
    parser.add_argument('topic')
    parser.add_argument('--beginning', action='store_true', help='If specified the messages for this topic will be consumed starting at the beginning offset otherwise the current is used.')

    args = parser.parse_args()

    auto_offset_reset = 'earliest' if args.beginning else 'latest'

    consume_from_topic(args.kafka, args.topic, auto_offset_reset=auto_offset_reset)

