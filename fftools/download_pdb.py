#!/usr/bin/env python

import sys
import parmed as pmd

pdb_id = sys.argv[1]
fname = pdb_id + '.pdb'

pmd.download_PDB(pdb_id).save(fname, overwrite=True)
