from __future__ import print_function

import datetime
import threading
import time

import paho.mqtt.publish as publish
import requests
from flask import Flask
from grove.gpio import GPIO
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

# Connect the GroveUltrasonicRanger to D5 & D16
ultrasonic_ranger_1 = GroveUltrasonicRanger(5)
ultrasonic_ranger_2 = GroveUltrasonicRanger(16)
# Connect the buzzer to digital port 6
buzzer = GPIO(6, GPIO.OUT)
# Connect led to digital port 17
led = GPIO(17, GPIO.OUT)

# variable states
alarmActive = False
buzzerActive = 0
testColor = 0
last_ultrasonic_ranger_1 = False
last_ultrasonic_ranger_2 = False
trigger_distance = 120

time_a = datetime.time(6, 0)
time_b = datetime.time(5, 00)
delay = 0.1

app = Flask(__name__)


def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else:
        return nowTime >= startTime or nowTime <= endTime


def isBadTime():
    return isNowInTimePeriod(time_a, time_b, datetime.datetime.now().time())


def triggerAlarm():
    global buzzerActive, testColor

    # whee u whee u
    buzzerActive = (buzzerActive + 1) % 2
    testColor = (testColor + 1) % 2
    # buzzer.write(buzzerActive)
    led.write(testColor)


def entry():
    global alarmActive
    publish.single(topic, payload="field1=1", hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
    print("entry")
    if (isBadTime()):
        requests.get('http://raspi2:5000/trigger_alarm')
        alarmActive = True


def exit():
    publish.single(topic, payload="field2=1", hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
    print("exit")


def clear():
    buzzer.write(0)
    led.write(0)


def loop():
    global last_ultrasonic_ranger_1, last_ultrasonic_ranger_2
    while True:
        try:
            new_ultrasonic_ranger_1 = (ultrasonic_ranger_1.get_distance()) < 120
            new_ultrasonic_ranger_2 = (ultrasonic_ranger_2.get_distance()) < 120
            if last_ultrasonic_ranger_1 and new_ultrasonic_ranger_2 and not last_ultrasonic_ranger_2:
                entry()
            elif last_ultrasonic_ranger_2 and new_ultrasonic_ranger_1 and not last_ultrasonic_ranger_1:
                exit()
            last_ultrasonic_ranger_1 = new_ultrasonic_ranger_1
            last_ultrasonic_ranger_2 = new_ultrasonic_ranger_2

            if alarmActive:
                triggerAlarm()
            time.sleep(delay)
        finally:
            clear()


@app.route("/kill_alarm")
def kill_alarm():
    global alarmActive
    alarmActive = False
    clear()
    print("kill_alarm")
    publish.single(topic, payload="field3=1", hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
    return "kill_alarm"


def setupMqtt():
    global topic, mqttHost, tPort, tTLS, tTransport
    channelID = "931380"
    apiKey = "PCLULCAKPMI6IU1J"
    mqttHost = "mqtt.thingspeak.com"
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs': "/etc/ssl/certs/ca-certificates.crt", 'tls_version': ssl.PROTOCOL_TLSv1}
    tPort = 443
    topic = "channels/" + channelID + "/publish/" + apiKey


if __name__ == '__main__':
    setupMqtt()
    print('Started runner')
    thread = threading.Thread(target=loop)
    thread.start()
    app.run(host="0.0.0.0")
    loop()
