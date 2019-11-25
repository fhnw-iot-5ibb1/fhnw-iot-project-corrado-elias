import time

from grove.gpio import GPIO

led = GPIO(12, GPIO.OUT)
button = GPIO(22, GPIO.IN)


def doIt(i: int):
    print(i)
    grovepi = led = GPIO(i, GPIO.OUT)
    grovepi.write(1)
    print('start')
    time.sleep(1)
    # Stop buzzing for 1 second and repeat
    grovepi.write(0)
    print('stop')
    time.sleep(1)


if __name__ == '__main__':
    doIt(16)
    doIt(5)
    doIt(0)
    doIt(2)
    doIt(4)
