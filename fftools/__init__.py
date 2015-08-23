'''
inherit ParmEd' Structure class
'''
from parmed import Structure as _Structure
import parmed as pmd
import numpy as np

def load_file(*args, **kwd):
    p_struct = pmd.load_file(*args, **kwd)

    new_struct = Structure2()
    new_struct.atoms = p_struct.atoms
    new_struct.residues = p_struct.residues
    new_struct.bonds = p_struct.bonds
    new_struct.angles = p_struct.angles
    new_struct.dihedrals = p_struct.dihedrals 
    new_struct.rb_torsions = p_struct.rb_torsions
    new_struct.urey_bradleys = p_struct.urey_bradleys
    new_struct.impropers = p_struct.impropers
    new_struct.cmaps = p_struct.cmaps
    new_struct.trigonal_angles = p_struct.trigonal_angles
    #new_struct.out_of_plane_bends = []
    #new_struct.pi_torsions = []
    #new_struct.stretch_bends = []
    #new_struct.torsion_torsions = []
    #new_struct.chiral_frames = []
    #new_struct.multipole_frames = []
    #new_struct.adjusts = []
    new_struct.acceptors = p_struct.acceptors
    new_struct.donors = p_struct.donors

    return new_struct

class Structure(_Structure):

    @property
    def charge(self):
        return np.array([atom.charge for atom in self.atoms])

    @charge.setter
    def charge(self, values):
        for atom, c in zip(self.atoms, values):
            atom.charge = c

    @property
    def mass(self):
        return np.array([atom.mass for atom in self.atoms])

    @charge.setter
    def mass(self, values):
        for atom, m in zip(self.atoms, values):
            atom.mass = m
