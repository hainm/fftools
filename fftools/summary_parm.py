#!/usr/bin/env python
import sys
import parmed as pmd
import pytraj as pt
from collections import Counter, OrderedDict

fname = sys.argv[1]
_parm  = pmd.load_file(fname, structure=True)

if isinstance(_parm, OrderedDict):
    parmlist = [_parm[key].to_structure() for key in _parm] 
else:
    parmlist = [_parm, ]

for parm in parmlist:
    print('resname set', set(res.name for res in parm.residues)) 
    print('total charge : ', sum(atom.charge for atom in parm.atoms))
    
    print(pmd.tools.summary(parm))
    print(pt.load_topology(fname))
    
    print(Counter(res.name for res in parm.residues))
