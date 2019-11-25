import time

from grove.gpio import GPIO

led = GPIO(12, GPIO.OUT)
button = GPIO(22, GPIO.IN)


def doIt(i: int):
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


if __name__ == '__main__':
    doItV2(16)
    doItV2(5)
    doItV2(0)
    doItV2(2)
    doItV2(4)
