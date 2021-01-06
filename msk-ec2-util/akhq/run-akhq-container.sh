#!/bin/bash

set -e


docker run -d -p 8080:8080 -v akhq-config.yaml:/app/application.yaml tchiotludo/akhq
