import RPi.GPIO as GPIO  # enable GPIO pins
import time  # enable time delay library
import motor as mot

# pin configuration
line_left = 17
line_right = 25

# pin input output configuration
GPIO.setmode(GPIO.BCM)

GPIO.setup(line_left, GPIO.IN)
GPIO.setup(line_right, GPIO.IN)

while True:  # main loop
    time.sleep(0.05)
    if (GPIO.input(line_left) == GPIO.LOW and GPIO.input(line_right) == GPIO.LOW):
        mot.forward()

    elif (GPIO.input(line_left) == GPIO.LOW and GPIO.input(line_right) == GPIO.HIGH):
        mot.right()

    elif (GPIO.input(line_left) == GPIO.HIGH and GPIO.input(line_right) == GPIO.LOW):
        mot.left()

    else:
        mot.stop()

GPIO.cleanup()
