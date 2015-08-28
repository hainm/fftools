#!/usr/bin/env python

import parmed as pmd

orig_pdb = '../3p4d.pdb'
new_name = '3p4d.onlynu.pdb'

p = pmd.load_file(orig_pdb)
p0 = p['!:HOH,MG']
print(set(res.name for res in p0.residues))
p0.save(new_name)
