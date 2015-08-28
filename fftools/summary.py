#!/usr/bin/env python
import sys
import parmed as pmd
import pytraj as pt
from collections import Counter

fname = '3gx5.14sb.gaff.parm7'
parm  = pmd.load_file(fname)

print('resname set', set(res.name for res in parm.residues)) 
print('total charge : ', sum(atom.charge for atom in parm.atoms))

print(pmd.tools.summary(parm))
print(pt.load_topology(fname))

print(Counter(res.name for res in parm.residues))
