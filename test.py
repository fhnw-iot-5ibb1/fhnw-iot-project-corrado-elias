import time

import grovepi

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 5

if __name__ == '__main__':
    for i in range(0, 20):
        print(i, i ** 2)
        grovepi.pinMode(i, "OUTPUT")
        grovepi.digitalWrite(buzzer, 1)
        print('start')
        time.sleep(1)
        # Stop buzzing for 1 second and repeat
        grovepi.digitalWrite(buzzer, 0)
        print('stop')
        time.sleep(1)
