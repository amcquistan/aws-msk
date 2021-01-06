#!/bin/bash

# List the Kafka Clusters filtering output to just ClusterName and ClusterArn

aws kafka list-clusters --query "ClusterInfoList[*].[ClusterName,ClusterArn]"
