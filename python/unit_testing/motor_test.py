import argparse
import numpy as np
import sys

# Custom constants script
sys.path.append( '..' )
import constants

# Code from Freenove robot kit
sys.path.insert( 1, '../freenove' )
from Servo import *


def motor_test(leg, motor, angle):

    leg = int(leg)
    motor = int(motor)
    angle = int(angle)
    
    # Init servo and hardware classes
    hrd = constants.hardware()
    servo = Servo()

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


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--angle', help='Angle for motor to move' )
    parser.add_argument('-l', '--leg', help='Leg number to move (0-5)')
    parser.add_argument('-m', '--motor', help='Motor to move (0,1,2)')

    args = parser.parse_args()

    # Sort through arguments
    if args.angle:
        angle = int( args.angle )
    else:
        angle = int( 0 )

    if args.leg:
        leg = int( args.leg )
    else:
        leg = 0

    if args.motor:
        motor = int( args.motor )
    else:
        motor = 0


    motor_test(leg, motor, angle)
