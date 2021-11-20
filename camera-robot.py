#!/usr/bin/env python3
# Pi-camera-robot
# Author: eldraco@gmail.com

import RPi.GPIO as GPIO
from time import sleep
import argparse

SERVO_HORIZ_IO = 3
SERVO2_VERT_IO = 5

def init_rpi():
    """
    Initialize the rpi io
    """
    # this sets the names to board mode, which just names the pins according to the numbers in the middle of the diagram above.
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    # Now setup PWM on pin #3 at 50Hz
    pwm = GPIO.PWM(3, 50)
    #Then start it with 0 duty cycle so it doesn't set any angles on startup
    pwm.start(0)

def stop_rpi():
    """
    Stop the rpi
    """
    pwm.stop()
    GPIO.cleanup()

def set_angle(angle, direction='base'):
    """
    Set the angle on servo X
    direction can be 'horizontal' or 'vertical'
    """
    duty = angle / 18 + 2
    if direction == 'horizontal':
        # Move servo horizontal
        GPIO.output(SERVO_HORIZ_IO, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(SERVO_HORIZ_IO, False)
        pwm.ChangeDutyCycle(0)
    elif direction == 'vertical':
        GPIO.output(SERVO2_VERT_IO, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(SERVO2_VERT_IO, False)
        pwm.ChangeDutyCycle(0)


####################
# Main
####################
if __name__ == '__main__':
    print('Pi-camera-robot.')

    # Parse the parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose',metavar='<verbositylevel>',action='store', required=False, type=int, help='amount of verbosity. This shows more info about the results.')

    args = parser.parse_args()

    init_rpi()

    # Move servo 1
    for angle in range(0,100,10):
        set_angle('horizontal', angle) 

    s0top_rpi()
