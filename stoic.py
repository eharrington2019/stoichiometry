import random
symbol = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
"Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y",
"Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr",
"Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au",
"Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es",
"Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

def main():
    printHeader
    leftSide = buildSide()
    # rightSide = buildSide()
    print(leftSide)
# print(leftSide + "->" + rightSide)
def buildside():
    print("Type left side")
    getAnswer("Type Element: ", symbol)
    print("Type right side")
    getAnswer("Type Element: ", symbol)

def getAnswer(questionString, confirmList):
    if input(confirmList) == "Stop":
         
    elif keep going
    # print(leftSide + "->" + rightSide)


class Compound:
  def __init__(self, element1, element2, count):
      self.elements = [element1, element2]

class Element:
  def __init__(self, symbol, count):
      self.symbol = symbol
      self.count = count

elements = [
    Element("H", 1),
    Element("Li", 2)
    ]


def printHeader():
    print("Stiochiometry")

def getAnswer(questionString, confirmList):
    answer = input(questionString)
    if answer not in confirmList:
        print("NOPE")
    if answer == "STOP":

def getAnswer2(questionString, confirmList):
    while(True):
        answer = input(questionString)
        if answer in confirmList:
            return answer

main()
