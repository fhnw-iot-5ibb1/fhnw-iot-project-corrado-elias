# IoT Engineering
## Project Access Barrier
* code is based on: 
   - https://github.com/Seeed-Studio/grove.py
   - https://community.thingspeak.com/tutorials/update-a-thingspeak-channel-using-mqtt-on-a-raspberry-pi/

## Installation
1. `sudo apt install fish`
1. `chsch`
1. `sudo apt install python3-paho-mqtt python3-flask python3-pip python-pip python3-grove-py`
1. `curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -`
1. connect headers (pins) as specified

## Run Pi 1
1. ssh pi@raspi1
1. run `systemctl enable run1.service && systemctl start run1.service`
## Run Pi 2 
1. ssh pi@raspi2
1. run `systemctl enable run2.service && systemctl start run2.service`

