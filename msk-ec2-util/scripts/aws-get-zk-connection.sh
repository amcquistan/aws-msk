#!/bin/bash

if [[ -z $1 ]]; then 
  echo "Must pass argument for MSK Cluster ARN"
  exit 1
fi

aws kafka describe-cluster --cluster-arn $1 \
    --query 'ClusterInfo.ZookeeperConnectString'

