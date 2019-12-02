import time

from grove.gpio import GPIO


def doIt():
    doItV1()


def doItV1():
    while 1 == 1:
        grovepi = GPIO(5, GPIO.OUT)
        grovepi.write(1)
        print('start')
        time.sleep(1)
        # Stop buzzing for 1 second and repeat
        grovepi.write(0)
        print('stop')
        time.sleep(1)


if __name__ == '__main__':
    doIt()
