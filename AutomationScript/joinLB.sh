#!/bin/bash
ip=$(sudo ifconfig eth0 | awk '/inet addr/ {gsub("addr:", "", $2); print $2}')
sudo ssh -o "StrictHostKeyChecking no" -i ~/nuage.pem ubuntu@10.0.0.13 ~/replace.sh $ip
