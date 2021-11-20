#!/usr/bin/env python3
# Pi-camera-robot
# Author: eldraco@gmail.com
import RPi.GPIO as GPIO
from time import sleep
import argparse

def init_rpi():
    """
    Initialize the rpi io
    """
    # this sets the names to board mode, which just names the pins according to the numbers in the middle of the diagram above.
    GPIO.setmode(GPIO.BOARD)

def stop_rpi():
    """
    Stop the rpi
    """
    GPIO.cleanup()

class Servo():
    """
    A Class to deal with a servo
    """

    def __init__(self, gpio):
        self.io_pin = gpio
        GPIO.setup(self.io_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.io_pin, 50)
        self.pwm.start(0)

    def stop(self):
        self.pwm.stop()

    def set_angle(self, angle):
        """
        Set the angle on servo
        """
        duty = int(angle) / 18 + 2
        GPIO.output(self.io_pin, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(0.5)
        GPIO.output(self.io_pin, False)
        self.pwm.ChangeDutyCycle(0)

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

    # Servo horisontal
    servo_horiz = Servo(3)
    # Servo Vertical
    servo_vert = Servo(5)

    # Move servo 1
    for angle in range(0,180,10):
        servo_horiz.set_angle(angle)

    stop_rpi()

