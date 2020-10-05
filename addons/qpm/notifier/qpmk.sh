#!/bin/sh
cd /var/lib/asterisk/qpmnd
python3 ./qpmk.py $1:$2-$3
