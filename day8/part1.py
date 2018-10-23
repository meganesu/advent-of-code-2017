import operator

class Condition:
    def __init__(self, register_name, comparison_operator, amount):
        self.register = register_name
        self.comparison_operator = comparison_operator
        self.amount = amount

    # def evaluate(self, registers):
    #     pass


class Instruction:
    def __init__(self, register_name, should_increase, amount, condition):
        self.register_name = register_name
        multiplier = 1 if should_increase else -1
        self.amount = multiplier * amount
        self.condition = condition


def load_input_from_file(filename):
    file = open(filename)
    return file.readlines()


def parse_instruction(line):
    '''
    :param line:
    :return: an object representing the instruction in the given line
    '''
    # Example line: x dec -715 if kjn == 0
    words = line.split()

    register_name = words[0]
    should_increase = True if words[1] == 'inc' else False
    amount = int(words[2])

    condition_register = words[4]
    operators = {
        '==': operator.eq,
        '!=': operator.ne,
        '<': operator.lt,
        '<=': operator.le,
        '>': operator.gt,
        '>=': operator.ge
    }
    condition_operator = operators[words[5]]
    condition_amount = int(words[6])
    condition = Condition(condition_register, condition_operator, condition_amount)

    instruction = Instruction(register_name, should_increase, amount, condition)

    return instruction

def should_execute_instruction(condition, registers):
    '''
    :param condition: condition object to evaluate
    :return: boolean, whether instruction should be evaluated
    '''
    '''
    evaluate condition:
        ... look up value of register
        ... use operator to evaluate condition
    '''
    '''
    import operator
    add = {"+": operator.add}
    add["+"](3,1)
    '''
    return True


def get_value_of_register(register):
    '''
    :param register: register whose value to look up

    if register is not in dictionary of registers:
    ... add it to dictionary with value of 0

    :return: value of register stored in dictionary

    '''
    '''
    if should_execute_instruction is true:
    ... get value of parsed_instruction.register
    ... inc/dec value of register in dict
    '''
    pass

def update_value_of_register(parsed_instruction, registers):
    pass


def get_largest_register_value(registers):
    pass


def main():
    input_from_file = load_input_from_file('input.txt')
    registers = {}
    for line in input_from_file:
        parsed_instruction = parse_instruction(line)
        # print(parsed_instruction.register_name,
        #       parsed_instruction.amount,
        #       parsed_instruction.condition.register,
        #       parsed_instruction.condition.comparison_operator,
        #       parsed_instruction.condition.amount)
    #     if should_execute_instruction(parsed_instruction.condition, registers):
    #         update_value_of_register(parsed_instruction, registers)
    # print(get_largest_register_value(registers))

if __name__ == '__main__':
    main()
