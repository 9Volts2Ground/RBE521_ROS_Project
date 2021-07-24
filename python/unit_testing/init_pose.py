import sys
import time

# Custom files
sys.path.append( '..' )
from motor_test import motor_test

sys.path.insert( 1, '../freenove' )
from Servo import *

def init_pose():

    servo = Servo()

    # Move anlkes
    angle = 45
    for leg in range( 6 ):
        print(leg)
        motor_test( servo, leg, 2, angle )
        # time.sleep( 0.5 )

    time.sleep( 1.0 )

    # Move shoulders
    angle = 10
    for leg in range( 6 ):
        print(leg)
        motor_test( servo, leg, 0, angle )
        # time.sleep( 0.5 )

    time.sleep( 1.0 )

    # Move knees
    angle = 45
    for leg in range( 6 ):
        print(leg)
        motor_test( servo, leg, 1, angle )
        # time.sleep( 0.5 )
             
    


if __name__ == "__main__":
    init_pose()