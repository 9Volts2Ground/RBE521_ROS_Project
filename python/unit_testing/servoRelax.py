#!/bin/python

import sys

# Code from Freenove robot kit
sys.path.insert( 1, '../freenove' )
from Servo import *

def servoRelax():
    servo = Servo()

    servo.relax()



