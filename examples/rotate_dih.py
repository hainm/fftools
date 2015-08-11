#!/usr/bin/env python 
import pytraj as pt

traj = pt.iterload('./RAN.rst7', './RAN.parm7')
t0 = traj[:]

flist = []
for deg in range(-180, 175, 5):
    pt._rotate_dih(t0, resid='1', dihtype='chin', deg=deg)
    flist.append(t0[0].copy())

print(pt.calc_chin(flist, top=t0.top))
pt.write_traj('combined_traj.nc', flist, top=t0.top)
