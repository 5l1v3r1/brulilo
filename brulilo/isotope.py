"""
An Isotope is a container holding a species mass, atomic number, etc.
"""

# periodic table, somewhat broken up appropriately
isotope_lut = ['H', 'He',
               'Li', 'Be',
               'B', 'C', 'O', 'F', 'Ne',
               'Na', 'Mg',
               'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
               'K', 'Ca',
               'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co',  # break
               'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
               'Rb', 'Sr',
               'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh',  # break
               'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
               'Cs', 'Ba',
               # Lanthanide Series
               'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu',  # break
               'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
               'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt',  # break
               'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
               'Fr', 'Ra',
               # Actinide Series
               'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am',  # break
               'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
               'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',  # break
               'Rg', 'Cn', 'Uut', 'Fl', 'Uup', 'Lv', 'Uus', 'Uuo']


class Isotope(object):
    def __init__(self, mass, number, ebin):
        self.A = mass
        self.Z = number
        self.B = ebin
        self.symbol = isotope_lut[self.Z + 1]