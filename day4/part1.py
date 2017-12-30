f = open('input.txt')
input = f.readlines()

numValid = 0

# Process each line in the file
for line in input:
  print(line)
  # Dictionary 
  words = {}
  duplicates = False
  # Process each word in the name
  for word in line.split():
    print(word)
    if word in words.keys():
      duplicates = True
      break
    else:
      words[word] = True

  if duplicates == False:
    numValid += 1

print(numValid)
