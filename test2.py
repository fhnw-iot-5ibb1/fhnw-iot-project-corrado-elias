import time

from grove.gpio import GPIO

led = GPIO(12, GPIO.OUT)
button = GPIO(22, GPIO.IN)

if __name__ == '__main__':
    for i in range(0, 30):
        print(i)
        grovepi = led = GPIO(i, GPIO.OUT)
        grovepi.write(1)
        print('start')
        time.sleep(1)
        # Stop buzzing for 1 second and repeat
        grovepi.write(0)
        print('stop')
        time.sleep(1)
