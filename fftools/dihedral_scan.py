import pytraj as pt
import numpy as np

traj = pt.iterload("RAN.rst7", "RAN.parm7")

print(traj.n_atoms, traj.top.n_residues)
print(pt.calc_chin(traj))

t0 = traj[:1]
deg_ene = []

flist = []

for deg in range(-180, 180, 5):
    pt._rotate_dih(t0, dihtype='chin', deg=deg, resid='1')
    flist.append(t0[0].copy())

en = pt.energy_decomposition(flist,
                             top=traj.top,
                             igb=8,
                             parm='./RAN.parm7')['dihedral']

chin = pt.calc_chin(flist, top=traj.top).values
en = en - en.min()

from matplotlib import pyplot as plt
plt.plot(chin, en, '--bo')
plt.show()
