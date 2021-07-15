import argparse
import numpy as np
import sys

# Custom constants script
sys.path.append( '..' )
import constants

# Code from Freenove robot kit
sys.path.insert( 1, '../freenove' )
from Servo import *

# Need to figure out how to add Servo.py to path
# Or better yet, just copy over the code and make a fresh script
#from Servo import *

def motor_test(leg, motor, angle):
    
    hrd = constants.hardware()
    servo = Servo()

    print( hrd.legChannel[leg,motor] )

    servo.setServoAngle( hrd.legChannel[leg,motor], angle )


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--angle', help='Angle for motor to move' )
    parser.add_argument('-l', '--leg', help='Leg number to move (0-5)')
    parser.add_argument('-m', '--motor', help='Motor to move (0,1,2)')

    args = parser.parse_args()

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

    print(leg)
    print(motor)
    print(angle)

    motor_test(leg, motor, angle)
