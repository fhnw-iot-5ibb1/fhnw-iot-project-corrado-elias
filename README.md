# IoT Engineering
## Project Access Barrier
* code is based on: 
   - https://github.com/Seeed-Studio/grove.py
   - https://community.thingspeak.com/tutorials/update-a-thingspeak-channel-using-mqtt-on-a-raspberry-pi/

## Installation
1. `curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -`
1. `sudo apt install sudo apt install python3-paho-mqtt`
## Run
1. connect headers as specified
1. run `python run.py`

#IoT Engineering Template
## Introduction
This project is part of the [IoT Engineering](../../../fhnw-iot) course.

* 2-person teams, building an IoT system.
* 32 hours of work per person, 1 prototype.
* 10' presentation of the project at Demo Day.
* Slides, source code and setup steps on GitHub.
* Both team members are able to explain the project.

### Team members
* @corradoparisi, Corrado Parisi
* @cintoros, Elias Schorr

### Source code
Source code, Arduino C, JS or Python, committed to (this) project repo.

[Arduino/MY_TEAM_PROJECT/MY_TEAM_PROJECT.ino](Arduino/MY_TEAM_PROJECT_FILE.ino)

[Nodejs/MY_TEAM_PROJECT.js](Nodejs/MY_TEAM_PROJECT_FILE.js)

[Python/MY_TEAM_PROJECT.py](Nodejs/MY_TEAM_PROJECT_FILE.py)

... (adapt as required)

1) Embedded code / microcontroller firmware.
2) Glue Code used on the gateway or "in the cloud".
3) App or Web UI code, or IoT platform setup steps.

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
