import numpy as np
import sys
#sys.path.append("..")
from ikine_hexapod import ikine_hexapod
from ikine2angles import ikine2angles
import constants

hrd = constants.hardware()
Rf = hrd.Rf
Alph = hrd.alpha

P = np.array([0.0, 0.0, 30.0, 0.0, 0.0, 0.0])

u = np.transpose( np.array( [ [ -Rf*np.sin(Alph/2.0), Rf*np.cos(Alph/2.0), 0.0 ],
                              [ Rf*np.sin(Alph/2.0), Rf*np.cos(Alph/2.0), 0.0 ],
                              [ Rf*np.sin(-3.0*Alph/2.0), Rf*np.cos(3.0*Alph/2.0), 0.0 ],
                              [ Rf*np.sin(3.0*Alph/2.0), Rf*np.cos(3.0*Alph/2.0), 0.0 ],
                              [ Rf*np.sin(-5.0*Alph/2.0), Rf*np.cos(-5.0*Alph/2.0), 0.0 ],
                              [ Rf*np.sin(5.0*Alph/2.0), Rf*np.cos(5.0*Alph/2.0), 0.0 ] ] ) )


# Calculate overall leg vectors
Leng, n, R = ikine_hexapod( P, u )

# Find individual servo angles
alpha, beta, gamma = ikine2angles( P, Leng, n, R, u )


print( "Alph" )
print(alpha)

print( "beta" )
print(beta)

print( "gamma" )
print(gamma)

