import datetime
import time

import grovepi

# Connect the Grove Ultrasonic Ranger to digital port D4 SIG,NC,VCC,GND
ultrasonic_ranger_1 = 4
ultrasonic_ranger_2 = 4
# Connect the Grove Buzzer to digital port D8 SIG,NC,VCC,GND
buzzer = 8
# Connect first LED in Chainable RGB LED chain to digital port D7; In: CI,DI,VCC,GND ; Out: CO,DO,VCC,GND
ledPin = 7
# I have 10 LEDs connected in series with the first connected to the GrovePi and the last not connected
# First LED input socket connected to GrovePi, output socket connected to second LED input and so on
numleds = 2  # If you only plug 1 LED, change 10 to 1

grovepi.pinMode(ledPin, "OUTPUT")
grovepi.pinMode(buzzer, "OUTPUT")
grovepi.chainableRgbLed_init(ledPin, numleds)

# variable states
alarmActive = False
buzzerActive = 0
testColor = 0
last_ultrasonic_ranger_1 = False
last_ultrasonic_ranger_2 = False
# TODO test trigger distance
trigger_distance = 120


def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else:  # Over midnight
        return nowTime >= startTime or nowTime <= endTime


def isBadTime():
    # Test case when range crosses midnight
    return isNowInTimePeriod(time(23, 0), time(5, 00), datetime.utcnow().time())


def triggerAlarm():
    global buzzerActive, testColor
    # whee u whee u
    buzzerActive = (buzzerActive + 1) % 2
    grovepi.digitalWrite(buzzer, 1)
    # switch test colors used in grovepi.chainableRgbLed_test()
    testColor = (testColor + 1) % 8
    grovepi.chainableRgbLed_test(ledPin, numleds, testColor)


def entry():
    global alarmActive
    # TODO send to firebase or whatever
    print("entry")
    # TODO only trigger based on time
    if (isBadTime()):
        alarmActive = True


def exit():
    global alarmActive
    # TODO send to firebase or whatever
    print("exit")
    alarmActive = False


def loop():
    global last_ultrasonic_ranger_1, last_ultrasonic_ranger_2
    while True:
        try:
            # Read distance value from Ultrasonic
            print(grovepi.ultrasonicRead(ultrasonic_ranger_1))
            print(grovepi.ultrasonicRead(ultrasonic_ranger_2))

            new_ultrasonic_ranger_1 = grovepi.ultrasonicRead(ultrasonic_ranger_1) < 120
            new_ultrasonic_ranger_2 = grovepi.ultrasonicRead(ultrasonic_ranger_2) < 120
            if last_ultrasonic_ranger_1 and new_ultrasonic_ranger_2 and not last_ultrasonic_ranger_2:
                entry()
            elif last_ultrasonic_ranger_2 and new_ultrasonic_ranger_1 and not last_ultrasonic_ranger_1:
                exit()
            last_ultrasonic_ranger_1 = new_ultrasonic_ranger_1
            last_ultrasonic_ranger_2 = new_ultrasonic_ranger_2

            if alarmActive:
                triggerAlarm()
            # TODO test time to sleep
            time.sleep(.5)

        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            grovepi.digitalWrite(buzzer, 0)
            grovepi.chainableRgbLed_test(ledPin, numleds, 0)
            break
        except TypeError:
            print("TypeError")
            break
        except IOError:
            print("IOError")
            break


if __name__ == '__main__':
    loop()
