#!/bin/bash
sudo iptables -A INPUT -p tcp -s 54.71.230.219 --dport 22 -j ACCEPT
sudo iptables -A INPUT -p udp -s 54.71.230.219 --dport 53 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 54.71.230.219 --dport 53 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 10.0.0.13 --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 10.0.0.13 --dport 53 -j ACCEPT
sudo iptables -A INPUT -p udp -s 10.0.0.13 --dport 53 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 54.71.230.219 --dport 5000 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 10.0.0.13 --dport 5000 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 5000 -j DROP
sudo iptables -A INPUT -p tcp --dport 80 -j DROP
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
