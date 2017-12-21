import math

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


# STEP 1: Create the initial empty grid

l = math.ceil(math.sqrt(input)) # How many rows/columns will the grid have?
# Make the length odd, so that the origin is in the middle
if (l % 2 == 0):
  l += 1
mid = int(math.floor(l/2)) # What is the index of the "origin"?
origin = (mid, mid) # The coordinates of the point (0,0) in the 2D grid

# Initialize the empty grid
grid = []
for i in range(l):
  row = []
  for j in range(l):
    row.append(0)
  grid.append(row)


# STEP 2: Fill in the spiral
n = 1 # How many steps have we taken?
val = 1 # What is the value we're writing in the cell?
x = 0 # Current position along x axis (assume n=1 is at (0,0))
y = 0 # Current position along y axis
grid[origin[0]+x][origin[1]+y] = val # Set up first square
dir = (1, 0) # What direction are we walking in?
width = 1 # How wide should this leg of the spiral be?
steps = 0 # How many steps into the current leg are we?
numlegs = 1 # How many legs have we turned in the spiral?

while n < input:
  n += 1
  x += dir[0]
  y += dir[1]
  steps += 1

  # Calculate next value and store it in the grid
  val = 0
  for i in range(-1,2): # i = [-1, 0, 1]
    for j in range(-1,2):
      val += grid[origin[0]+x+i][origin[1]+y+j]

  # print(val)

  grid[origin[0]+x][origin[1]+y] = val

  if val > input:
    break

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

print(val)

