#!/bin/bash

./ffsclient list history --decoded --format=json > history.json

cat history.json | ./save.py
