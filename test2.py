import time

from grove.gpio import GPIO
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

print('Detecting distance...')
while True:
    print('{} cm'.format(sonar.get_distance()))
    time.sleep(1)
led = GPIO(12, GPIO.OUT)
button = GPIO(22, GPIO.IN)


def doIt(i: int):
    doItV1(i)


def doItV1(i: int):
    print(i)
    grovepi = GPIO(i, GPIO.OUT)
    grovepi.write(1)
    print('start')
    time.sleep(1)
    # Stop buzzing for 1 second and repeat
    grovepi.write(0)
    print('stop')
    time.sleep(1)


def doItV2(i: int):
    print(i)
    grovepi = GPIO(i, GPIO.OUT)
    print(grovepi.read())
    time.sleep(1)


def doItV3(i: int):
    sonar = GroveUltrasonicRanger(i)  # pin12, slot D12
    print('{} cm'.format(sonar.get_distance()))
    time.sleep(1)


if __name__ == '__main__':
    doIt(16)
    doIt(5)
    doIt(0)
    doIt(2)
    doIt(4)
