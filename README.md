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
1. run `python run1.py`
## Run Pi 2 
1. ssh pi@raspi2
1. run `python run2.py`

#IoT Engineering Template

### Presentation
4-slide presentation, PDF format, committed to (this) project repo.

[MY_TEAM_PROJECT_PRESENTATION.pdf](MY_TEAM_PROJECT_PRESENTATION.pdf)

1) Use-case of your project.
2) Reference model of your project.
3) Single slide interface documentation.
4) Issues you faced, how you solved them.

### Live demo
Working end-to-end prototype, "device to cloud", part of your 10' presentation.

[https://MY_TEAM_PROJECT_DEMO_HOST:PORT/](https://MY_TEAM_PROJECT_DEMO_HOST:PORT/)

1) Sensor input on a IoT device triggers an event.
2) The event or measurement shows up online, in an app or Web client.
3) The event triggers actuator output on the same or on a separate IoT device.
