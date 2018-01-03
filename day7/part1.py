f = open('input.txt')
input = f.readlines()

# Build data structure for program
#  name, weight, heldBy
class Program:
  def __init__(self, name):
    self.name = name
    self.weight = -1
    self.children = []
    self.parent = None

  def setWeight(self, weight):
    self.weight = weight

  def addChild(self, child):
    self.children.append(child)

  def setParent(self, parent):
    self.parent = parent

programs = {} # key: name of program; val: (weight, heldBy)

# Parse input lines
for line in input:
  words = line.split()

  # Lines have one of the two following formats:
  #  pName (pWeight)
  #  pName (pWeight) -> holdingName [, holdingName2] ...

  # Build a program object as the line is parsed
  pName = words[0] # Name of program
  p = Program(words[0])

  # Get weight
  pWeight = int(words[1][1:-1]) # Get the value between the parentheses in words[1]
  p.setWeight = pWeight

  # If the program is already in programs, copy its parent into the new object
  if pName in programs.keys():
    p.setParent(programs[pName].parent)

  # Get names of programs this program is holding
  if '->' in words:
    pChildren = [] # A list of the names of programs being held by this program

    for i in range(3, len(words)):
      child = words[i].strip(',')
      pChildren.append(child)
      p.addChild(child)

    # For each program this program is holding, update its val in programs
    for c in pChildren:
      # If child is in programs, use the weight already stored
      if c in programs.keys():
        programs[c].setParent(pName)
      # Else, add child to programs, with a dummy weight (-1)
      else:
        newProgram = Program(c)
        newProgram.setParent(pName)
        programs[c] = newProgram

  programs[pName] = p

# Find the bottom program by tracing through heldBy
#  until someone isn't held by anyone
for k in programs.keys():
  #print(k, programs[k].weight, programs[k].parent, programs[k].children)
  if programs[k].parent == None:
    print(k)
