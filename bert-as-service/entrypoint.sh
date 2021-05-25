#!/bin/sh
apt-get update
apt-get install wget
wget https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip
unzip ./cased_L-12_H-768_A-12.zip
bert-serving-start -model_dir=./cased_L-12_H-768_A-12 -num_worker=4 -max_seq_len=64 -cpu -http_port 8125
