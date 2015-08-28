#!/usr/bin/env python

# require: parmed
# python ./add_flourine_to_AG.py you_pdb.pdb

# TODO: change this filename and methods' name

import sys
import parmed as pmd


your_pdb = sys.argv[1]
p = pmd.load_file(your_pdb)

def add_F_to_AG(p):
    for res in p.residues:
        if res.name in ['A', 'G']:
            res.name = res.name + 'F2'

def replace_O2prime_F2prime(p):
    for atom in p:
        if atom.residue.name in ['AF2', 'GF2'] and atom.name == "O2'":
            atom.name = "F2'"
            atom.atomic_number = 9

add_F_to_AG(p)
replace_O2prime_F2prime(p)

fname = your_pdb.split(".")[0] + "_F2.pdb"
print (p.residues)
p["!:AF2,GF2@HO2'"].save(fname)

#for idx, s in enumerate(pmd.tools.split_by_residues(p["!:AF2,GF2@HO2'"])):
#    s.save("".join(("res", str(idx + 1), ".pdb")))
