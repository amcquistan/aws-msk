import argparse
import logging
import sys

from kafka import KafkaProducer
from kafka.errors import KafkaConfigurationError


logging.basicConfig(
  format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S',
  level=logging.INFO
)


def produce_to_topic(bootstrap_servers, topic, message, acks='1'):
    try:
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

        if not isinstance(message, bytes):
            message = bytes(message, encoding='utf-8')

        producer.send(topic, message)
        producer.flush()


    except KafkaConfigurationError as e:
        logging.error(str(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('kafka', help='Bootstrap servers')
    parser.add_argument('topic')
    parser.add_argument('message')
    parser.add_argument('--allacks', action='store_true', help='Wait for leader and all brokers to acknowledge reciept of message')
    parser.add_argument('--noacks', action='store_true', help='Fire and forget (ie, do not wait for the Cluster to acknowledge the message)')
    parser.add_argument('--leaderacks', action='store_true', help='The default. Only wait for the leader to acknowledge reciept of message')

    args = parser.parse_args()

    if sum([bool(args.allacks), bool(args.noacks), bool(args.leaderacks)]) > 1:
        logging.error('allack, noack, and leaderack are mutually exclusive, please only specify one')
        sys.exit()

    acks = 1
    if args.allacks:
        acks = 'all'
    elif args.noacks:
        acks = 0

    produce_to_topic(args.kafka, args.topic, args.message, acks=acks)

