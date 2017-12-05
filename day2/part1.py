file = open("input.txt", "r")

checksum = 0

# For each line
line = file.readline()
while line != '':
  elems = line.split()

  min = 9999999999
  max = -1

  # Find the min and max values in the line
  for s in elems:
    if int(s) < min:
      min = int(s)
    if int(s) > max:
      max = int(s)

  print("min: " + str(min))
  print("max: " + str(max))
  # Add the difference between max and min to the checksum
  checksum += max - min

  # Read the next line
  line = file.readline()

# Print the checksum
print(checksum)