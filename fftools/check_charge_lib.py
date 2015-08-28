#!/usr/bin/env python
import sys
import parmed as pmd

d = pmd.load_file(sys.argv[1])

for key in d:
    res0 = d[key]
    c0 = [a.charge for a in res0.atoms]
    #print(res0, c0, sum(c0))
    print(res0, sum(c0))
