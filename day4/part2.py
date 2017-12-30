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
    # Split the word into an array of characters, then sort alphabetically
    chars = []
    for char in word:
      chars.append(char)
    chars.sort()

    # Build a new string with characters from the word in alphabetical order
    wordSorted = ''
    for char in chars:
      wordSorted += char

    if wordSorted in words.keys():
      duplicates = True
      break
    else:
      words[wordSorted] = True

  if duplicates == False:
    numValid += 1

print(numValid)
