import datetime

from grove.gpio import GPIO
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

# Connect the Grove Ultrasonic Ranger to digital port D5 and D16
ultrasonic_ranger_1 = GroveUltrasonicRanger(5)
ultrasonic_ranger_2 = GroveUltrasonicRanger(16)
# Connect the Grove Buzzer to digital port 6
buzzer = grovepi = GPIO(6, GPIO.OUT)
# Connect first LED in Chainable RGB LED chain to digital port 17
led = GPIO(17, GPIO.OUT)

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
    return isNowInTimePeriod(datetime.time(23, 0), datetime.time(5, 00), datetime.datetime.now().time())


def triggerAlarm():
    global buzzerActive, testColor
    # whee u whee u
    buzzerActive = (buzzerActive + 1) % 2
    buzzer.write(buzzerActive)
    # switch test colors used in grovepi.chainableRgbLed_test()
    testColor = (testColor + 1) % 2
    led.write(testColor)


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


def clear():
    buzzer.write(0)
    led.write(0)


def loop():
    global last_ultrasonic_ranger_1, last_ultrasonic_ranger_2
    while True:
        try:
            # Read distance value from Ultrasonic
            print(ultrasonic_ranger_1.get_distance())
            print(ultrasonic_ranger_2.get_distance())

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
            # TODO test time to sleep
            time.sleep(1)
        finally:
            clear()


if __name__ == '__main__':
    loop()
