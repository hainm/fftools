#!/usr/bin/env python

# require: parmed
# python ./add_flourine_to_AG.py you_pdb.pdb

# TODO: change this filename and methods' name

import sys
import parmed as pmd
import pytraj as pt

split_res = pt.tools.split_parmed_by_residues


your_pdb = sys.argv[1]
p = pmd.load_file(your_pdb)


root_name = your_pdb.split('.')[0]

for idx, s in enumerate(split_res(p)):
    s.save("".join((root_name, '_', "res", str(idx + 1), ".pdb")))
