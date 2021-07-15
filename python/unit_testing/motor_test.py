import numpy as np
import sys

sys.path.append( '..' )
import constants

sys.path.insert( 1, '../freenove' )
from Servo import *

# Need to figure out how to add Servo.py to path
# Or better yet, just copy over the code and make a fresh script
#from Servo import *

def motor_test():
    
    hrd = constants.hardware()
    servo = Servo()

    servo.setServoAngle(hrd.legChannel[0,2], 0.0)


if __name__ == "__main__":
    motor_test()
