#!/bin/bash

# Add route for 10.0.0.0/8
sudo ip route add 10.0.0.0/8 via 10.0.0.1

# Add route for 172.16.0.0/12
sudo ip route add 172.16.0.0/12 via 10.0.0.1

# Add route for 192.168.0.0/16
sudo ip route add 192.168.0.0/16 via 10.0.0.1

