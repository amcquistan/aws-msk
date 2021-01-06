#!/bin/bash

# This script is meant to be ran on an Amazon Linux 2 EC2 instance

set -e

user=$(whoami)

if [[ $user != "root" ]]; then
  echo "You are executing commands as user $user. Please run as root user or with sudo"
  exit 1
fi

yum update -y
yum install -y java-11-amazon-corretto-headless
sudo alternatives --config java
yum install -y python3 git jq maven nc

# aws configure 
# set region us-east-2 
# defaults for all others

