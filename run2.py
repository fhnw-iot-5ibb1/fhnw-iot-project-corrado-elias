from __future__ import print_function

import threading
import time

import requests
from flask import Flask
from grove.gpio import GPIO
from grove.grove_led import GroveLed

app = Flask(__name__)
# Connect the Grove button to digital port 5
# TODO replace with button
button = GPIO(5, GPIO.OUT)
# Connect the Grove Buzzer to digital port 6
buzzer = GPIO(6, GPIO.OUT)
# Connect first LED in Chainable RGB LED chain to D16
led = GroveLed(16)

# variable states
alarmActive = False
buzzerActive = 0
testColor = 0

delay = 0.1


def triggerAlarm():
    global buzzerActive, testColor

    # whee u whee u
    buzzerActive = (buzzerActive + 1) % 2
    buzzer.write(buzzerActive)

    if testColor:
        led.on()
    else:
        led.off()
    testColor = (testColor + 1) % 2


def clear():
    buzzer.write(0)
    led.write(0)


def loop():
    while True:
        try:
            if alarmActive:
                triggerAlarm()
            if button.read():
                kill_alarm()
            time.sleep(delay)
        finally:
            clear()


@app.route("/trigger_alarm")
def trigger_alarm():
    return "trigger_alarm"


def kill_alarm():
    global alarmActive
    alarmActive = False
    clear()
    requests.get('http://raspi1:5000/kill_alarm')


if __name__ == "__main__":
    print('Started runner')
    thread = threading.Thread(target=loop)
    thread.start()
    app.run(host="0.0.0.0")
