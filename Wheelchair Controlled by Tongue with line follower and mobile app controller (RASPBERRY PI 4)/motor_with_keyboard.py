import RPi.GPIO as GPIO
import time
import keyboard_controller as keybo
import motor as mot

GPIO.setwarnings(False)

while True: #main loop
    keybo.init()
    time.sleep(0.05)
    if keybo.getKey('UP'):
        mot.forward()
        
    elif keybo.getKey('DOWN'):
        mot.backward()
        
    elif keybo.getKey('RIGHT'):
        mot.right()
        
    elif keybo.getKey('LEFT'):
        mot.left()
        
    else: #stop
        mot.stop()
        
GPIO.cleanup()
