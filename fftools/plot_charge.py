#!/usr/bin/env python
import sys
from matplotlib import pyplot as plt
import parmed as pmd

orig_lib, new_lib, resname0, resname1 = sys.argv[1:]

res0 = pmd.load_file(orig_lib)[resname0]
res1 = pmd.load_file(new_lib)[resname1]

c0 = [a.charge for a in res0.atoms if a.type != 'F']
c1 = [a.charge for a in res1.atoms if a.type != 'F']

plt.plot(c0, c1, 'ro')
plt.show()
