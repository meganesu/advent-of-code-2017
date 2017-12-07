file = open("input.txt", "r")
input = int(file.read())

# Decide what the next direction will be
def updateDir(xdir, ydir):
  if xdir == 1 and ydir == 0:
    return (0, 1)
  elif xdir == 0 and ydir == 1:
    return (-1, 0)
  elif xdir == -1 and ydir == 0:
    return (0, -1)
  elif xdir == 0 and ydir == -1:
    return (1, 0)
  else:
    return None

n = 1 # How many steps have we taken?
x = 0 # Current position along x axis (assume n=1 is at (0,0))
y = 0 # Current position along y axis
dir = (1, 0) # What direction are we walking in?
width = 1 # How wide should this leg of the spiral be?
steps = 0 # How many steps into the current leg are we?
numlegs = 1 # How many legs have we turned in the spiral?

while n < input:
  n += 1
  x += dir[0]
  y += dir[1]
  steps += 1

  #print("n: " + str(n))
  #print("x: " + str(x) + " y: " + str(y))

  # Do we need to turn?
  if steps == width:
    # Change directions (turn)
    dir = updateDir(dir[0], dir[1])
    numlegs += 1
    steps = 0
    #print("Turning...")

    # If we're on an odd leg now, the width has to get increased
    if numlegs % 2 == 1:
      width += 1
      #print("Increasing width to " + str(width))

print(abs(x)+abs(y))

