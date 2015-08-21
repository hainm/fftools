import parmed as pmd

lib_file = 'GF2.lib'
mol2_red = '/home/haichit/research/rna_project/resp_fit/GF2/download_RED/P25049/Data-R.E.D.Server/Mol_MM/INTER/CT-A_m1-c1_m2-c1.mol2'
resname = 'GF2'
output = 'GF2_RED_update.lib'

# load off file and get 1st residue
res0 = pmd.load_file(lib_file)[resname]
res1 = pmd.load_file(mol2_red)

# mapping atom names to be replaced
atom_map = [
  ("O1P", "OP1"),
  ("O2P", "OP2"),
  ("F2'", "F"),
  ("H5'1", "H5'"),
  ("H5'2", "H5''"),
]

adict = dict(atom_map)
# print(adict)

# match atom name for mol2 file from R.E.D to tleap
# todo: idiom
for atom in res1:
    if atom.name in adict:
        atom.name = adict[atom.name]

# print (set(a.name for a in res0) ^ set(a.name for a in res1))

# update charge for off file

for atom0 in res0:
    for atom1 in res1:
        if atom1.name == atom0.name:
            atom0.charge = atom1.charge

res0.save(output)
