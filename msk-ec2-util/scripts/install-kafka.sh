#!/bin/bash

# This script is meant to be ran on an Amazon Linux 2 EC2 instance

set -e 

user=$(whoami)

if [[ $user != "root" ]]; then
  echo "You are executing commands as user $user. Please run as root user or with sudo"
  exit 1
fi

wget https://archive.apache.org/dist/kafka/2.5.0/kafka_2.13-2.5.0.tgz

tar -xzf kafka_2.13-2.5.0.tgz

mv kafka_2.13-2.5.0 /usr/local/

for i in /usr/local/kafka_2.13-2.5.0/bin/*.sh; do
	mv $i ${i%???}
done;

cp /usr/local/kafka_2.13-2.5.0/bin/kafka-run-class /usr/local/kafka_2.13-2.5.0/bin/kafka-run-class.sh

ln -sfn /usr/local/kafka_2.13-2.5.0 /usr/local/kafka

echo "export PATH=/usr/local/kafka/bin:$PATH" >> /etc/profile
