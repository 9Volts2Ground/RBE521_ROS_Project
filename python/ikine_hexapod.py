import numpy as np 
import constants

def ikine_hexapod( P, u ):
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


    # Calculate rotation matrix. Currently uses ZYZ Euler angles
    Rxa = np.array( [ [ 1.0, 0.0, 0.0 ],
                      [ 0.0, np.cos(a), -np.sin(a) ],
                      [ 0.0, np.sin(a), np.cos(a) ] ] )


    Ryb = np.array( [ [np.cos(b), 0.0, np.sin(b)],
                      [0.0, 1.0, 0.0],
                      [-np.sin(b), 0.0, np.cos(b)] ] )

    Rzc = np.array( [ [np.cos(c), -np.sin(c), 0.0],
                      [np.sin(c), np.cos(c), 0.0],
                      [0.0, 0.0, 1.0] ] )

    R = Rxa @ Ryb @ Rzc

    s = hrd.s


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


    return Leng, n, R

if __name__ == "__main__":

    hrd = constants.hardware()
    Rf = hrd.Rf
    alpha = hrd.alpha

    P = np.array( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )

    u = np.transpose( np.array( [ [Rf*np.cos(alpha/2.0), Rf*np.sin(alpha/2.0), 0.0],
                                  [-Rf*np.sin(np.pi/6 - alpha/2.0), Rf*np.cos(np.pi/6.0 - alpha/2.0), 0.0],
                                  [-Rf*np.sin(np.pi/6.0 + alpha/2.0), Rf*np.cos(np.pi/6.0 + alpha/2.0), 0.0],
                                  [-Rf*np.cos(np.pi/3.0 - alpha/2.0), -Rf*np.sin(np.pi/3.0 - alpha/2.0), 0.0],
                                  [-Rf*np.cos(np.pi/3.0 + alpha/2.0), -Rf*np.sin(np.pi/3.0 + alpha/2.0), 0.0],
                                  [Rf*np.cos(alpha/2.0), -Rf*np.sin(alpha/2.0), 0.0] ] ) )

    ikine_hexapod( P, u )