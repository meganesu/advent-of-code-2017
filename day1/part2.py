# Open the input file and load the input
file = open('input.txt', 'r')

input = file.readline() # type(input) -> str

sum = 0
numdigits = len(input)
jump = int(numdigits / 2) # How far around circle to compare next digit

# Check each of the characters against the next one
for i in range(numdigits):
  inext = (i + jump) % numdigits
  if int(input[i]) == int(input[inext]):
    print('i=' + str(i) + ': ' + input[i] + ' matches ' + input[inext])
    sum += int(input[i])

print(sum)

