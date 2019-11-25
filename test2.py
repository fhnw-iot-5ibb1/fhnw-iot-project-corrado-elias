import time

from grove.gpio import GPIO

led = GPIO(12, GPIO.OUT)
button = GPIO(22, GPIO.IN)

while True:
    if button.read():
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)

if __name__ == '__main__':
    for i in range(0, 20):
        print(i)
        grovepi= led = GPIO(i, GPIO.OUT)
        grovepi.write(i, 1)
        print('start')
        time.sleep(1)
        # Stop buzzing for 1 second and repeat
        grovepi.write(i, 0)
        print('stop')
        time.sleep(1)
