import numpy as np
import sys
#sys.path.append("..")
from ikine_hexapod import ikine_hexapod
from ikine2angles import ikine2angles
import constants
import time

sys.path.insert( 1, "../unit_testing")
from move_motor import move_motor

sys.path.insert( 1, '../freenove' )
from Servo import *


# Set this flag if testing in Wanda or Vision
Wanda = True
# Wanda = False

if Wanda:
    servo = Servo()


hrd = constants.hardware()
Rf = hrd.Rf
Alph = hrd.alpha

P = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

u = np.transpose( np.array( [ [ -Rf*np.sin(Alph/2.0), Rf*np.cos(Alph/2.0), 0.0 ],
                              [ Rf*np.sin(Alph/2.0), Rf*np.cos(Alph/2.0), 0.0 ],
                              [ Rf*np.sin(-3.0*Alph/2.0), Rf*np.cos(3.0*Alph/2.0), 0.0 ],
                              [ Rf*np.sin(3.0*Alph/2.0), Rf*np.cos(3.0*Alph/2.0), 0.0 ],
                              [ Rf*np.sin(-5.0*Alph/2.0), Rf*np.cos(-5.0*Alph/2.0), 0.0 ],
                              [ Rf*np.sin(5.0*Alph/2.0), Rf*np.cos(5.0*Alph/2.0), 0.0 ] ] ) )


for z in range(100):

    P[2] = z


    # Calculate overall leg vectors
    Leng, n, R = ikine_hexapod( P, u )

    # Find individual servo angles
    alpha, beta, gamma = ikine2angles( P, Leng, n, R, u )

    print("================================")

    print(P)

    print("alpha: " + str(alpha[0]) + str(alpha[1]) + str(alpha[2]) + str(alpha[3]) + str(alpha[4]) + str(alpha[5]) )

    print("beta: " + str(beta[0]) + str(beta[1]) + str(beta[2]) + str(beta[3]) + str(beta[4]) + str(beta[5]) )

    print("gamma: " + str(gamma[0]) + str(gamma[1]) + str(gamma[2]) + str(gamma[3]) + str(gamma[4]) + str(gamma[5]) )




    if Wanda:

        for leg, alph in enumerate( alpha ):
            move_motor( servo, leg, 0, alph )

        for leg, bet in enumerate( beta ):
            move_motor( servo, leg, 1, bet )

        for leg, gam in enumerate( gamma ):
            move_motor( servo, leg, 2, gam )

        time.sleep( .01  )



