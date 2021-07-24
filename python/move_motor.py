import argparse
import numpy as np
import sys


import constants

# Code from Freenove robot kit
sys.path.insert( 1, './freenove' )
from Servo import *


def move_motor(servo, leg, motor, angle):

    leg = int(leg)
    motor = int(motor)
    angle = int(angle)
    
    # Init servo and hardware classes
    hrd = constants.hardware()
    # servo = Servo()

    # Translate angle command from robot coordinate frames to calibrated motor commands
    angle_command = hrd.motorCenter[leg,motor] + hrd.motorOrientation[leg,motor] * angle

    # Saturate the motor commands to min/max values
    if angle_command > hrd.motorMax[leg,motor]:
        angle_command = hrd.motorMax[leg,motor]
    elif angle_command < hrd.motorMin[leg,motor]:
        angle_command = hrd.motorMin[leg,motor]

    # Ensure angle is an int to pass into setServoAngle()
    angle_command = int( angle_command )

    # servo.setServoAngle( hrd.legChannel[leg,motor], angle )
    servo.setServoAngle( hrd.legChannel[leg,motor], angle_command )