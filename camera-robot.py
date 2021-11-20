#!/usr/bin/env python3
import network
import os
import RPi.GPIO as GPIO
from time import sleep

# this sets the names to board mode, which just names the pins according to the numbers in the middle of the diagram above.
GPIO.setmode(GPIO.BOARD)


GPIO.setup(3, GPIO.OUT)

# Now setup PWM on pin #3 at 50Hz
pwm = GPIO.PWM(3, 50)

#Then start it with 0 duty cycle so it doesn't set any angles on startup
pwm.start(0)

# to set the angle of the servo, we need to send a specific signal to it. This can differ from servo to servo, as normally it's from 2.5-12.5%, and on the ones I'm using it's 2-12%. Regardless, it will be a 10% window, so to calculate the duty cycle for your desired angle, divide by 18, then add the lowest available value, in this case 2


def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(3, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3, False)
    pwm.ChangeDutyCycle(0)


SetAngle(90) 

pwm.stop()
GPIO.cleanup()

