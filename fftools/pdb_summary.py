#!/usr/bin/env python

import parmed as pmd
import sys

p = pmd.load_file(sys.argv[1])
pmd.tools.printSummary(p)
