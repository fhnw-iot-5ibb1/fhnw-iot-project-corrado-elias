import time

import grovepi

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 5

grovepi.pinMode(buzzer, "OUTPUT")

if __name__ == '__main__':
    # Buzz for 1 second
    grovepi.digitalWrite(buzzer, 1)
    print('start')
    time.sleep(2)

    # Stop buzzing for 1 second and repeat
    grovepi.digitalWrite(buzzer, 0)
    print('stop')
    time.sleep(2)

    # Buzz for 1 second
    grovepi.digitalWrite(buzzer, 1)
    print('start')
    time.sleep(2)

    # Stop buzzing for 1 second and repeat
    grovepi.digitalWrite(buzzer, 0)
    print('stop')
    time.sleep(2)
