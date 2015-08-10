'''print unique residue names from all mol2 files in current folder
python ./residues_from_mol2.py
'''
import parmed as pmd
from glob import glob
from pytraj.tools import flatten

plist = [pmd.load_file(fname, structure=True) for fname in glob('*.mol2')]

reslist = flatten([[res.name for res in p.residues] for p in plist])

print(set(reslist))
