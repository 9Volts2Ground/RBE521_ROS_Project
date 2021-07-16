import sys
import time

# Custom files
import constants
from motor_test import motor_test

def init_pose():

    # Move anlkes
    angle = 90
    for leg in range( 6 ):
        motor_test( leg, 2, angle )
        time.sleep( 0.001 )

    time.sleep( 1.0 )

    # Move shoulders
    angle = 0
    for leg in range( 6 ):
        motor_test( leg, 0, angle )
        time.sleep( 0.001 )

    time.sleep( 1.0 )

    # Move knees
    angle = 90
    for leg in range( 6 ):
        motor_test( leg, 1, angle )
             
    


if __name__ == "__main__":
    init_pose()