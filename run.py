from __future__ import print_function

import datetime
import paho.mqtt.publish as publish
import time
from grove.gpio import GPIO
from grove.grove_led import GroveLed
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

# Connect the Grove Ultrasonic Ranger to digital port D5 and D16
ultrasonic_ranger_1 = GroveUltrasonicRanger(5)
ultrasonic_ranger_2 = GroveUltrasonicRanger(16)
# Connect the Grove Buzzer to digital port 6
buzzer = grovepi = GPIO(6, GPIO.OUT)
# Connect first LED in Chainable RGB LED chain to digital port 17
led = GroveLed(17)

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


def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else:  # Over midnight
        return nowTime >= startTime or nowTime <= endTime


def isBadTime():
    # Test case when range crosses midnight
    return isNowInTimePeriod(time_a, time_b, datetime.datetime.now().time())


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


def entry():
    global alarmActive
    # attempt to publish this data to the topic
    publish.single(topic, payload="field1=1", hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
    print("entry")
    if (isBadTime()):
        alarmActive = True


def exit():
    global alarmActive
    # attempt to publish this data to the topic
    publish.single(topic, payload="field2=1", hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
    print("exit")
    alarmActive = False


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


def setupMqtt():
    global topic, mqttHost, tPort, tTLS, tTransport
    # The ThingSpeak Channel ID
    # Replace this with your Channel ID
    channelID = "931380"

    # The Write API Key for the channel
    # Replace this with your Write API key
    apiKey = "PCLULCAKPMI6IU1J"

    #  MQTT Connection Methods

    # Set useUnsecuredTCP to True to use the default MQTT port of 1883
    # This type of unsecured MQTT connection uses the least amount of system resources.
    useUnsecuredTCP = False

    # Set useUnsecuredWebSockets to True to use MQTT over an unsecured websocket on port 80.
    # Try this if port 1883 is blocked on your network.
    useUnsecuredWebsockets = False

    # Set useSSLWebsockets to True to use MQTT over a secure websocket on port 443.
    # This type of connection will use slightly more system resources, but the connection
    # will be secured by SSL.
    useSSLWebsockets = True

    # The Hostname of the ThinSpeak MQTT service
    mqttHost = "mqtt.thingspeak.com"

    # Set up the connection parameters based on the connection type
    if useUnsecuredTCP:
        tTransport = "tcp"
        tPort = 1883
        tTLS = None

    if useUnsecuredWebsockets:
        tTransport = "websockets"
        tPort = 80
        tTLS = None

    if useSSLWebsockets:
        import ssl

        tTransport = "websockets"
        tTLS = {'ca_certs': "/etc/ssl/certs/ca-certificates.crt", 'tls_version': ssl.PROTOCOL_TLSv1}
        tPort = 443

    # Create the topic string
    topic = "channels/" + channelID + "/publish/" + apiKey


if __name__ == '__main__':
    setupMqtt()
    loop()
