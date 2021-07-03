import numpy as np 
import constants

def ikine_hexapod(P):
    # P = numpy array
    # P[0:3] = desired linear position
    # P[3:6] = desired orientation

    # Unpack given desired pose
    o = P[0:3]
    a = P[3]
    b = P[4]
    c = P[5]

    # Unpack hardware parameters
    hrd = constants.hardware()
    Rm = hrd.Rm
    Rf = hrd.Rf
    alpha = hrd.alpha
    beta = hrd.beta


    # Calculate rotation matrix. Currently uses ZYZ Euler angles
    Rza = np.array( [ [np.cos(a), -np.sin(a), 0.0],
                      [np.sin(a), np.cos(a), 0.0],
                      [0.0, 0.0, 1.0] ] )

    Ryb = np.array( [ [np.cos(b), 0.0, np.sin(b)],
                      [0.0, 1.0, 0.0],
                      [-np.sin(b), 0.0, np.cos(b)] ] )

    Rzc = np.array( [ [np.cos(c), -np.sin(c), 0.0],
                      [np.sin(c), np.cos(c), 0.0],
                      [0.0, 0.0, 1.0] ] )

    R = Rza @ Ryb @ Rzc

    s = np.transpose( np.array( [ [Rm*np.cos(beta/2.0), Rm*np.sin(beta/2.0), 0.0],
                                  [-Rm*np.sin(np.pi/6.0 - beta/2.0), Rm*np.cos(np.pi/6.0 - beta/2.0), 0.0],
                                  [-Rm*np.sin(np.pi/6.0 + beta/2.0), Rm*np.cos(np.pi/6.0 + beta/2.0), 0.0],
                                  [-Rm*np.cos(np.pi/3.0 - beta/2.0), -Rm * np.sin(np.pi/3.0 - beta/2.0), 0.0],
                                  [-Rm*np.cos(np.pi/3.0 + beta/2.0), -Rm*np.sin(np.pi/3.0 + beta/2.0), 0.0],
                                  [Rm*np.cos(beta/2.0), -Rm*np.sin(beta/2.0), 0.0] ] ) )

    u = np.transpose( np.array( [ [Rf*np.cos(alpha/2.0), Rf*np.sin(alpha/2.0), 0.0],
                                  [-Rf*np.sin(np.pi/6 - alpha/2.0), Rf*np.cos(np.pi/6.0 - alpha/2.0), 0.0],
                                  [-Rf*np.sin(np.pi/6.0 + alpha/2.0), Rf*np.cos(np.pi/6.0 + alpha/2.0), 0.0],
                                  [-Rf*np.cos(np.pi/3.0 - alpha/2.0), -Rf*np.sin(np.pi/3.0 - alpha/2.0), 0.0],
                                  [-Rf*np.cos(np.pi/3.0 + alpha/2.0), -Rf*np.sin(np.pi/3.0 + alpha/2.0), 0.0],
                                  [Rf*np.cos(alpha/2.0), -Rf*np.sin(alpha/2.0), 0.0] ] ) )


    # Init arrays
    Leng = np.array( [] )
    n = np.empty( (3,0) )

    # Loop through each leg to calculate leg info
    for i in range(6):

        # L = desired full leg vectors
        L = np.array( [ o + R @ s[0:3,i] - u[0:3,i] ] ).T


        # Leng = desired length of each leg
        Leng = np.hstack( (Leng, np.linalg.norm(L[:,0]) ) )


        # n = leg unit vector
        N = np.array( [ L[:,0]/Leng[i] ] ).T
        n = np.hstack( ( n, N ) )


    return Leng, n, R, s