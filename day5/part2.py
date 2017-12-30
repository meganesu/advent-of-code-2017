f = open('input.txt')
input = f.readlines()

# Create the maze - an array of ints,
#  where each element is the offset to jump to the next instruction
maze = []

for line in input:
  maze.append(int(line))

current = 0 # Index of the current instruction
numSteps = 0

# Keep iterating until you jump out of bounds of the maze array
while current < len(maze):
  numSteps += 1

  # Read the element at the current instruction
  offset = maze[current]

  # Update the offset in the current instruction
  if offset >= 3:
    maze[current] -= 1
  else:
    maze[current] += 1

  # Update the current instruction
  current = current + offset

print(numSteps)