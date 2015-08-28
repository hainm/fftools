#!/bin/env python

import parmed as pmd
import sys

lib, res_old, res_new = sys.argv[1:]

res = pmd.load_file(lib)[res_old]
res.name = res_new
res.save(res_new + '.lib')
