file = open("input.txt", "r")

checksum = 0

# For each line
line = file.readline()
while line != '':
  elems = line.split()

  min = 9999999999
  max = -1

  # Check each value against all the other values
  for i1 in range(len(elems)):
    for i2 in range(len(elems)):
      if i1 == i2:
        continue
      if int(elems[i1]) % int(elems[i2]) == 0:
        # If the two values are evenly divisible,
        #  add the result of the division to the checksum
        checksum += int(elems[i1]) / int(elems[i2])
        break

  # Read the next line
  line = file.readline()

# Print the checksum
print(checksum)