import numpy as np
import sys
#sys.path.append("..")
from ikine_hexapod import ikine_hexapod

P = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])

Leng, n, R, s = ikine_hexapod(P)

print('Printing Leng...')
print(Leng)

print('Printing n...')
print(n)

print('Printing R...')
print(R)

print('Printing s...')
print(s)