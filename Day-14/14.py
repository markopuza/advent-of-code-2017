from knothash import knot
import numpy as np
from scipy.ndimage.measurements import label

key = 'stpzcrnm'

M = np.array([list( '{:0128b}'.format(int(knot(key+'-'+str(i)), 16)) ) for i in range(128)], dtype=int)
print('Part 1: {:d}'.format(np.count_nonzero(M)))
print('Part 2: {:d}'.format(label(M)[1]))
