import time

import grovepi

# Connect the Grove Ultrasonic Ranger to digital port D4 SIG,NC,VCC,GND
ultrasonic_ranger = 4
# Connect the Grove Buzzer to digital port D8 SIG,NC,VCC,GND
buzzer = 8
# Connect first LED in Chainable RGB LED chain to digital port D7; In: CI,DI,VCC,GND ; Out: CO,DO,VCC,GND
ledPin = 7
# I have 10 LEDs connected in series with the first connected to the GrovePi and the last not connected
# First LED input socket connected to GrovePi, output socket connected to second LED input and so on
numleds = 2  # If you only plug 1 LED, change 10 to 1

grovepi.pinMode(ledPin, "OUTPUT")
grovepi.pinMode(buzzer, "OUTPUT")
grovepi.chainableRgbLed_init(ledPin, numleds)

# variable states
alarmActive = False
buzzerActive = 0
testColor = 0


def triggerAlarm():
    global buzzerActive, testColor
    # whee u whee u
    buzzerActive = (buzzerActive + 1) % 2
    grovepi.digitalWrite(buzzer, 1)
    # switch test colors used in grovepi.chainableRgbLed_test()
    testColor = (testColor + 1) % 8
    grovepi.chainableRgbLed_test(ledPin, numleds, testColor)


def loop():
    while True:
        try:
            # Read distance value from Ultrasonic
            print(grovepi.ultrasonicRead(ultrasonic_ranger))
            # TODO add if condition if range is less than 1.20m or something like that
            # TODO save the condition -> if first ranger 1 or ranger 2
            # TODO we could cange the logic based on the time e.g. trigger alarm anyway if time is 23:00 - 5:00
            if alarmActive:
                triggerAlarm()
            # and send the data in,out detection anyway
            time.sleep(.5)

        except KeyboardInterrupt:
            grovepi.digitalWrite(buzzer, 0)
            grovepi.chainableRgbLed_test(ledPin, numleds, 0)
            break
        except TypeError:
            print("Error")
            break
        except IOError:
            print("Error")
            break


if __name__ == '__main__':
    loop()
