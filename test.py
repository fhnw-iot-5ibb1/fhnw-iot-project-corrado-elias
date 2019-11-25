import time

import grovepi

if __name__ == '__main__':
    for i in range(0, 20):
        print(i)
        grovepi.pinMode(i, "OUTPUT")
        grovepi.digitalWrite(i, 1)
        time.sleep(1)
        grovepi.analogWrite(i, 1)
        print('start')
        time.sleep(1)
        # Stop buzzing for 1 second and repeat
        grovepi.digitalWrite(i, 0)
        time.sleep(1)
        grovepi.analogWrite(i, 0)
        print('stop')
        time.sleep(1)
