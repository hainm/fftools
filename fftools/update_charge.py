#!/usr/bin/env python

'''pyton ./update_charge.py offlib_file mol2_file
'''
import sys
import parmed as pmd

resname_final = 'GF25'
lib_file, mol2_red = sys.argv[1:]
resname = 'GF5'
output = '%s_RED_update.lib' % resname_final

# load off file and get 1st residue
res0 = pmd.load_file(lib_file)[resname]
res1 = pmd.load_file(mol2_red)

name0 = [atom.name for atom in res0]
name1 = [atom.name for atom in res1]

print('orig_lib')
print([atom.name for atom in res0 if atom.name not in name1])
print('RED mol2')
print([atom.name for atom in res1 if atom.name not in name0])

# mapping atom names to be replaced
atom_map = [
  ("O1P", "OP1"),
  ("O2P", "OP2"),
  #("H5T'", "HO5'"),
  ("H5T", "HO5'"),
  ("H3T", "HO3'"),
  ("O1", "O3'"),  # used for 5' (GF25.mol2, ...)
  #("O1", "O5'"), # used for 3' (GF23.mol2, ...)
  ("H5'1", "H5'"),
  ("H5'2", "H5''"),
]
print(atom_map)

adict = dict(atom_map)
# print(adict)

# match atom name for mol2 file from R.E.D to tleap
# todo: idiom
for atom in res1:
    if atom.name in adict:
        atom.name = adict[atom.name]

name0 = [atom.name for atom in res0]
name1 = [atom.name for atom in res1]
new_set = set(name0) ^ set(name1)
print(new_set)
assert new_set == set()

# update charge for off file
for atom0 in res0:
    for atom1 in res1:
        if atom1.name == atom0.name:
            atom0.charge = atom1.charge

res0.name = resname
res0.save(output)
