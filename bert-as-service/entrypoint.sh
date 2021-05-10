#!/bin/sh
bert-serving-start -model_dir=./cased_L-12_H-768_A-12 -num_worker=4 -max_seq_len=64 -cpu -http_port 8125