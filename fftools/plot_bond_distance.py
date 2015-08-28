usage = '''python ./plot_bond_distance.py input.parm7 input.rst7
'''

import sys
import pytraj as pt

top, crd = sys.argv[1:]

traj = pt.iterload(crd, top)
indices = traj.top.bond_indices

distances = pt.distance(traj, indices)

from matplotlib import pyplot as plt
try:
    import seaborn as snb
    snb.set()
except ImportError:
    pass

plt.plot(distances, 'bo')
pt.show()
