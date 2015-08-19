import pytraj as pt
pt.set_error_silent(True)

for pdbidb in '3P4A   3P4B   3P4C   3P4D'.split():
    t = pt.load_pdb_rcsb(pdbidb)
    print(pdbidb, ': ', set(res.name.rstrip() for res in t.top.residues))
