import sys
import time

# Custom files
sys.path.append( '..' )
from motor_test import motor_test

def init_pose():

    # Move anlkes
    angle = 45
    for leg in range( 6 ):
        print(leg)
        motor_test( leg, 2, angle )
        time.sleep( 0.5 )

    time.sleep( 1.0 )

    # Move shoulders
    angle = 10
    for leg in range( 6 ):
        print(leg)
        motor_test( leg, 0, angle )
        time.sleep( 0.5 )

    time.sleep( 1.0 )

    # Move knees
    angle = 45
    for leg in range( 6 ):
        print(leg)
        motor_test( leg, 1, angle )
        time.sleep( 0.5 )
             
    


if __name__ == "__main__":
    init_pose()