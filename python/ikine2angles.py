import numpy as np
import constants


def ikine2angles( P, Leng, n, R, u ):

    hrd = constants.hardware()
    s = hrd.s

    # Unpack desired pose P
    # o = np.transpose( np.array( P[0:3] ) )
    o = np.array( [ [ P[0] ],
                    [ P[1] ],
                    [ P[2] ] ] )

    # Initialize joint angles
    alpha = np.array( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
    beta =  np.array( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
    gamma = np.array( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )

    # alpha = np.empty( [3,0] )
    # beta = np.empty( [3,0] )
    # gamma = np.empty( [3,0] )

    # Initialize intermediate calculations
    s2 = np.zeros( [3,6] )
    # l_prime = np.empty( [3,0] )
    phi = np.array( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
    rho = np.array( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )


    # Loop through each leg
    for i in range(6):

        # print("index: " + str(i) + "-------------------------------------")

        # Hip joint angle, defined from upper platform +X directoin
        alpha[i] = np.arctan2( -n[1,i], -n[0,i] )

        s2[0,i] = s[0,i] + hrd.L1 * np.cos( alpha[i] )
        s2[1,i] = s[1,i] + hrd.L1 * np.sin( alpha[i] )
        s2[2,i] = s[2,i]

        # Vector from foot to knee joint
        l_prime = np.array( o + R @ np.array( [ s2[:,i] ] ).T - np.array( [ u[:,i] ] ).T )

        # Angle from ground to hip joint vector
        phi[i] = np.arcsin( ( l_prime[2] - Leng[i] * n[2,i] ) / hrd.L1 )

        # Angle from ground to knee joint
        rho[i] = np.arctan2( np.linalg.norm( l_prime[0:2] ), l_prime[2] )

        # Knee joint angle, positive knee up
        beta[i] = np.arccos( ( hrd.L2**2 + np.linalg.norm( l_prime[0:3] )**2 - hrd.L3**2 ) / \
            ( 2 * hrd.L2 * np.linalg.norm( l_prime[0:3] ) ) ) - ( rho[i] + phi[i] )

        # Ankle joint angle, positive foot down
        gamma[i] = np.pi - np.arccos( ( hrd.L2**2 + hrd.L3**2 - np.linalg.norm( l_prime[0:3] )**2 ) / \
            ( 2 * hrd.L2 * hrd.L3 ) )

        # Remove alpha offset, so we can send a motor angle to the servo rather than a global angle
        alpha[i] = alpha[i] - hrd.alpha_offset[i]

        # Convert angles from rad to deg for servo reception
        alpha[i] = alpha[i] * 180.0 / np.pi
        beta[i] = beta[i] * 180.0 / np.pi
        gamma[i] = gamma[i] * 180.0 / np.pi


    return alpha, beta, gamma



