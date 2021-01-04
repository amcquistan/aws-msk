import os
import sys
import traceback

from flask import request, jsonify
from flask_lambda import FlaskLambda

from kafka import KafkaProducer


app = FlaskLambda(__name__)

KAFKA = os.environ['MSK_BOOTSTRAP_SERVERS']
TOPIC = os.environ['MSK_TOPIC']

@app.route('/send-message/', methods=('POST',))
def produce_message():
    print("KAFKA: " + KAFKA)
    print("Topic: " + TOPIC)
    try:
        producer = KafkaProducer(bootstrap_servers=KAFKA)

        req_data = request.get_json()

        msg_bytes = bytes(req_data['message'], encoding='utf-8')

        producer.send(TOPIC, msg_bytes)
        producer.flush()

        return jsonify({'status': 'Sent'})
    except Exception as e:
        print("Exception in code")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print(str(e))
        print("-"*60)

    return jsonify({'status': 'Failed'})
