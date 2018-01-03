f = open('input.txt')
input = f.readlines()

# Build data structure for program
#  name, weight, heldBy

programs = {} # key: name of program; val: (weight, heldBy)

# Parse input lines
for line in input:
  words = line.split()

  # Lines have one of the two following formats:
  #  pName (pWeight)
  #  pName (pWeight) -> holdingName [, holdingName2] ...

  # Get name of program
  pName = words[0] # Name of program

  # Get weight
  pWeight = int(words[1][1:-1]) # Get the value between the parentheses in words[1]

  # Add weight to programs dictionary
  if pName in programs.keys():
    programs[pName] = (pWeight, programs[pName][1])
  else:
    programs[pName] = (pWeight, '')

  # Get names of programs this program is holding
  if '->' in words:
    pHolding = [] # A list of the names of programs being held by this program

    for i in range(3, len(words)):
      pHolding.append(words[i].strip(','))

    # For each program this program is holding, update its val in programs
    for p in pHolding:
      # If holding is in programs, use the weight already stored
      if p in programs.keys():
        programs[p] = (programs[p][0], pName)
      # Else, add holding to programs, with a dummy weight (-1)
      else:
        programs[p] = (-1, pName)

print(programs)

# Find the bottom program by tracing through heldBy
#  until someone isn't held by anyone
for k in programs.keys():
  if programs[k][1] == '':
    print(k)