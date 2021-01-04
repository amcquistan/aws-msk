# MSK Utilities

This directory contains a number of helper scripts for interacting with an AWS MSK cluster.

### Installing EC2 Utility Instance

For the purpose of interacting with an MSK cluster it is useful to utilize an EC2 instance within the same user managed VPC that
the MSK cluster is running in.  The utility scripts here are intended to be used against a Amazon Linux 2 AMI.

Instance Requirements

* EC2 Must have an IAM role for AmazonMSKReadOnlyAccess
* EC2 Must be in the same VPC as the MSK cluster

MSK Requirements

* MSK must allow in bound TCP traffic from EC2 Utility Instance over port 9092


Initial Installs

* See initial-installs.sh and install-kafka.sh

### Listing Topics

A. First get Cluster ARN

```
$ ./aws-list-clusters-arn.sh 
[
    [
        "msk-dev01-cluster", 
        "arn:aws:kafka:us-east-2:574715127331:cluster/msk-dev01-cluster/90a0b109-536a-4051-89cc-9b4290145dc9-2"
    ]
]
```

B. Then get Bootstrap Server URL(s)

```
ARN="arn:aws:kafka:us-east-2:574715127331:cluster/msk-dev01-cluster/90a0b109-536a-4051-89cc-9b4290145dc9-2"
KAFKA=$(./aws-get-bs-connection.sh $ARN text)
```

C. Use the ARN in conjunction with list-kafka-topics.sh to list the Cluster topics associated with the ARN / Bootstrap servers just discovered

```
./list-kafka-topics.sh $KAFKA
```

### Creating Topics with Kafka CLI Utility

Retrieve the ARN and Bootstrap server urls described in A and B of Listing Topics

```
kafka-topics --bootstrap-server $KAFKA --create \
  --replication-factor somenumber \
  --partitions somenumber \
  --topic topicname
```

### Consuming Messages with Kafka CLI Utility

Retrieve the ARN and Bootstrap server urls described in A and B of Listing Topics

```
kafka-console-consumer --bootstrap-server $KAFKA --topic topicname
```

### Producing Messages with Kafka CLI Utility

Retrieve the ARN and Bootstrap server urls described in A and B of Listing Topics

```
kafka-console-producer --bootstrap-server $KAFKA --topic topicname
```

### Python Library

To install the Python based kafka-client library pip install the package like so.

```
pip3 install kafka-python
```

See the following for producing and consuming to/from cluster

* py_producer.py
* py_consumer.py

