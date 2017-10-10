import random
symbol = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
"Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y",
"Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr",
"Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au",
"Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es",
"Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

def main():
  elements = [
    Element("H", 1),
    Element("Li", 2)
    ]
  printHeader()
  selection1 = getUserSelection()
  selection2 = getUserSelection2()
  print(selection1, selection2)

class Compound:
  def __init__(self, element1, element2, count):
      self.elements = [element1, element2]

class Element:
  def __init__(self, symbol, count):
      self.symbol = symbol
      self.count = count

def printHeader():
    print("Stiochiometry")

def getUserSelection():
    leftside = input("Type left side: ")
    return(leftside)

def getUserSelection2():
    rightside = input("Type right side: ")
    return(rightside)

main()
