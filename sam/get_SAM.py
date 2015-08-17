import parmed as pmd

p = pmd.download_PDB('3gx5')
p[':SAM'].save('SAM.pdb')
