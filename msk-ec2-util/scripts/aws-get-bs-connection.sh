#!/bin/bash

if [[ -z $1 ]]; then 
  echo "Must pass argument for MSK Cluster ARN"
  exit 1
fi

if [[ -z $2 ]]; then
  aws kafka get-bootstrap-brokers --cluster-arn $1

elif [[ $2 == 'text' ]]; then 
  aws kafka get-bootstrap-brokers --cluster-arn $1 --query BootstrapBrokerString --output text
elif [[ $2 == 'tls' ]]; then
  aws kafka get-bootstrap-brokers --cluster-arn $1 --query BootstrapBrokerStringTls --output text
else
  echo "Unknown 2nd parameter. Allowed values [all, text, tls]"
fi



