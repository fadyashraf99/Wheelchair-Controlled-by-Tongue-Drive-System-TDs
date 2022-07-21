import cv2
import ultrasonic as ult
import motor as mot
import RPi.GPIO as GPIO  # enable GPIO pins
import time  # enable time delay library
import board  # enable I2C library
import busio  # enable adafruit_blinka library
import adafruit_ads1x15.ads1115 as ADS  # enable ADC component library
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)  # Create an I2C device
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)  # determine the input channel (A0)


frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# pin configuration
sensor_1 = 27
sensor_2 = 22
sensor_3 = 23
sensor_4 = 24

# pin input output configuration
GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor_1, GPIO.IN)
GPIO.setup(sensor_2, GPIO.IN)
GPIO.setup(sensor_3, GPIO.IN)
GPIO.setup(sensor_4, GPIO.IN)

while True:  # main loop

    success, img = cap.read()  # camera window
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

    time.sleep(0.05)
    dist = ult.distance()  # ultrasonic call back function
    print(dist)  # distance indication
    if dist >= 100:  # distance cheack
        print(chan.value)  # light indication
        if chan.value <= 200:  # light check
            if GPIO.input(sensor_1) == GPIO.LOW:  # forward
                mot.forward()

            elif GPIO.input(sensor_2) == GPIO.LOW:  # backword
                mot.backward()

            elif GPIO.input(sensor_3) == GPIO.LOW:  # right
                mot.right()

            elif GPIO.input(sensor_4) == GPIO.LOW:  # left
                mot.left()

            else:  # stop
                mot.stop()
        else:
            mot.stop()

    else:  # stop when obstacle detected
        mot.stop()

        if chan.value <= 200:  # at short distance
            if GPIO.input(sensor_2) == GPIO.LOW:  # backword
                mot.backward()

GPIO.cleanup()
