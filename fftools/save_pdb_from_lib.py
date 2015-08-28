#!/usr/bin/env python

import sys
import parmed as pmd
fname, resname = sys.argv[1:]

pmd.load_file(fname)[resname].to_structure().save('test.pdb', overwrite=True)
