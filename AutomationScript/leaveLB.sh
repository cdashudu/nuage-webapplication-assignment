#!/bin/bash
ip=$(sudo ifconfig eth0 | awk '/inet addr/ {gsub("addr:", "", $2); print $2}')
sudo ssh -o "StrictHostKeyChecking no" -i /home/ubuntu/nuage.pem ubuntu@10.0.0.13 /home/ubuntu/revReplace.sh $ip
