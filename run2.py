from __future__ import print_function

import threading
import time

import requests
from flask import Flask
from grove.gpio import GPIO

app = Flask(__name__)
# Connect the button to D5
button = GPIO(5, GPIO.IN)
# Connect the buzzer to digital port 6
buzzer = GPIO(6, GPIO.OUT)
# Connect led to D16
led = GPIO(16, GPIO.OUT)

# variable states
alarmActive = False
buzzerActive = 0
testColor = 0

delay = 0.1


def triggerAlarm():
    global buzzerActive, testColor

    # whee u whee u
    buzzerActive = (buzzerActive + 1) % 2
    testColor = (testColor + 1) % 2
    # buzzer.write(buzzerActive)
    led.write(testColor)


def clear():
    buzzer.write(0)
    led.write(0)


def loop():
    while True:
        try:
            if alarmActive:
                triggerAlarm()
                print(button.read())
            if button.read():
                kill_alarm()
            time.sleep(delay)
        finally:
            clear()


@app.route("/trigger_alarm")
def trigger_alarm():
    global alarmActive
    alarmActive = True
    return "trigger_alarm"


def kill_alarm():
    global alarmActive
    alarmActive = False
    print("kill_alarm")
    clear()
    requests.get('http://raspi1:5000/kill_alarm')


if __name__ == "__main__":
    print('Started runner')
    thread = threading.Thread(target=loop)
    thread.start()
    app.run(host="0.0.0.0")
