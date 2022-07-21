import RPi.GPIO as GPIO #enable GPIO pins

H_1 = 5
H_2 = 6
H_3 = 19
H_4 = 26
honk = 17

pwm = 13
GPIO.setmode(GPIO.BCM)

GPIO.setup(pwm, GPIO.OUT)
GPIO.setup(H_1, GPIO.OUT)
GPIO.setup(H_2, GPIO.OUT)
GPIO.setup(H_3, GPIO.OUT)
GPIO.setup(H_4, GPIO.OUT)
GPIO.setup(honk, GPIO.OUT)

pwm_speed = GPIO.PWM(pwm, 100)
pwm_speed.start(0)
pwm_speed.ChangeDutyCycle(75)

s = 20

def forward():
    pwm_speed.ChangeDutyCycle(s)
    GPIO.output(H_1, GPIO.HIGH)
    GPIO.output(H_2, GPIO.LOW)
    GPIO.output(H_3, GPIO.HIGH)
    GPIO.output(H_4, GPIO.LOW)
    GPIO.output(honk, GPIO.LOW)
    print ('forward')

def backward():
    pwm_speed.ChangeDutyCycle(s)
    GPIO.output(H_1, GPIO.LOW)
    GPIO.output(H_2, GPIO.HIGH)
    GPIO.output(H_3, GPIO.LOW)
    GPIO.output(H_4, GPIO.HIGH)
    GPIO.output(honk, GPIO.LOW)
    print ('backward')

def right():
    pwm_speed.ChangeDutyCycle(s)
    GPIO.output(H_1, GPIO.LOW)
    GPIO.output(H_2, GPIO.HIGH)
    GPIO.output(H_3, GPIO.HIGH)
    GPIO.output(H_4, GPIO.LOW)
    GPIO.output(honk, GPIO.LOW)
    print ('right')

def left():
    pwm_speed.ChangeDutyCycle(s)
    GPIO.output(H_1, GPIO.HIGH)
    GPIO.output(H_2, GPIO.LOW)
    GPIO.output(H_3, GPIO.LOW)
    GPIO.output(H_4, GPIO.HIGH)
    GPIO.output(honk, GPIO.LOW)
    print ('left')

def stop():
    GPIO.output(H_1, GPIO.LOW)
    GPIO.output(H_2, GPIO.LOW)
    GPIO.output(H_3, GPIO.LOW)
    GPIO.output(H_4, GPIO.LOW)
    GPIO.output(honk, GPIO.LOW)

def honky():
    GPIO.output(honk, GPIO.HIGH)