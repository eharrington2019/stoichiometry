import random
elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P",

def main():
    h = Element("h", 2)
    o = Element("O", 1)

    print(h.symbol)
    print(o.symbol)

    compound = Compound(h, o)

class Compound:
  def __init__(self, element1, element2, count):
      self.elements = [element1, element2]

class Element:
  def __init__(self, symbol, count):
      self.symbol = symbol
      self.count = count
