f = open('input.txt')
input = f.read()

# Set up an array to model the memory banks,
#  where each element is the number of blocks in that bank
banks = input.split()
numBanks = len(banks)
for i in range(numBanks):
  banks[i] = int(banks[i])

# Store the different states we've seen after reallocation
states = {}

numReallocations = 0

while True:
  # Find the bank with the max number of blocks
  maxBlocks = -1
  iChosen = -1
  for i in range(numBanks):
    if banks[i] > maxBlocks:
      iChosen = i
      maxBlocks = banks[i]

  # Redistribute the blocks from that bank
  banks[iChosen] = 0
  for i in range(maxBlocks):
    banks[(iChosen + 1 + i) % numBanks] += 1
  numReallocations += 1

  # Build a string based on this state
  state = ''
  for b in range(numBanks):
    state += str(banks[b])
    state += ' '

  # Have we seen this state before?
  #  If yes, we're done
  #  If not, add this state to states and keep going
  if state in states.keys():
    break
  else:
    states[state] = numReallocations

print(numReallocations)