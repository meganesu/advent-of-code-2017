def load_input_from_file(filename):
    file = open(filename)
    return file.readlines()


def calculate_score(input):
    index = 0
    ignoring_input = False
    while index < len(input):
        char = input[index]
        if char == '!':
            index += 2
            continue
        elif char == '<':
            ignoring_input = True
        index += 1

    # for each character:
    # ... if char == '!', skip the next char
    # ... if char == '<', ignore everything until the next '>'
    # ... if char == '{', start a new group, increase group score by 1, add group score to total score
    # ... if char == '}', end a group, decrease group score by 1


def main():
    input = load_input_from_file('input.txt')
    print(calculate_score(input))

if __name__ == '__main__':
    main()