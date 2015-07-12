# require, parmed, pysander, pytraj

# Aim: change "k" for bond and re-evaluate new energy

import parmed as pmd
import sander

traj = pt.iterload("./data/Tc5b.crd", "./data/Tc5b.top")
p = pmd.load_file(traj.top.filename)
inp = sander.gas_input(8)
coords = traj[0].coords

fname = "tmp.parm7"

with pt.utils.context.goto_temp_folder():
    for k in range(20, 100):
        p.bonds[3].type.k = k
        p.save(fname)
        p = pmd.load_file(fname)
        with sander.setup(p, coords, None, inp):
            ene, frc = sander.energy_forces()
            print (ene.bond, ene.dihedral)
