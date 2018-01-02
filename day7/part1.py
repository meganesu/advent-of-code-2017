# Build data structure for program
#  name, weight, heldBy

programs = {} # key: name of program; val: (weight, heldBy)

# Parse input lines
# Get name of program
# Get weight
# For each program this program is holding, update its val in programs
  # If holding is in programs, use the weight already stored
  # Else, add holding to programs, with a dummy weight (-1)

# Find the bottom program by tracing through heldBy
#  until someone isn't held by anyone