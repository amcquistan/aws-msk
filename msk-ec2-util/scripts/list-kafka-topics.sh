#!/bin/bash

# !!! Attention !!!
# Must enable TCP 9092 traffic in security group for MSK cluster from 
# machine running these commands.

# Can retrieve bootstrap server(s) like so:
# Get Cluster ARN
#  ./aws-list-clusters-arn.sh
# Get Bootstrap Server(s) URL
#  KAFKA=$(./aws-get-bs-connection.sh $ARN text)
# Use list-kafka-topics.sh as like so
#  ./list-kafka-topics.sh $KAFKA

if [[ -z $1 ]]; then 
  echo "Missing required parameter for bootstrap servers connection URL(s)"
  exit 1
fi

kafka-topics --bootstrap-server $1 --list
