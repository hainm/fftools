#!/usr/bin/env python
import sys
from matplotlib import pyplot as plt
import parmed as pmd

res0 = pmd.load_file(sys.argv[1])
c0 = [a.charge for a in res0.atoms]
#print(res0, c0, sum(c0))
print(res0, sum(c0))
