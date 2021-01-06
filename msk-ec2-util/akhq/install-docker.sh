#!/bin/bash

# This script is meant to be ran on an Amazon Linux 2 EC2 instance
# reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html

set -e 

user=$(whoami)

if [[ $user != "root" ]]; then
  echo "You are executing commands as user $user. Please run as root user or with sudo"
  exit 1
fi

amazon-linux-extras install docker

systemctl start docker

usermod -a -G docker ec2-user


