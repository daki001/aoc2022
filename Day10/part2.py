def read_file(path):
    instructions = list()
    with open(path) as f:
        count = 0
        for line in f:
            line = line.strip()
            instructions.append(line)

    return instructions


def execute_instruction(cycle, instruction, register):
    is_printed = [False]
    if (cycle % 40) in range(register - 1, register + 2):
        is_printed[0] = True
    if instruction.startswith('addx'):

        if ((cycle % 40) + 1) % 40 in range(register - 1, register + 2):
            is_printed.append(True)
        else:
            is_printed.append(False)
        cycle += 2
        register += int(instruction.split(' ')[1])
    else:
        cycle += 1

    return [cycle, register, is_printed]

def go_through_instructions(instructions):
    register = 1
    cycle = 0
    signal_strengths = []
    count = 0
    for inst in instructions:
        after_instruction = execute_instruction(cycle, inst, register)
        for elements in after_instruction[2]:
            if count % 40 == 0:
                signal_strengths.append('')
            if elements:
                signal_strengths[len(signal_strengths) - 1] += '#'
            else:
                signal_strengths[len(signal_strengths) - 1] += '.'
            count += 1
        register = after_instruction[1]
        cycle = after_instruction[0]
    return signal_strengths

def print_signal_strenghts(input):
    for l in input:
        print(l)


if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    print(file)
    print(print_signal_strenghts(go_through_instructions(file)))

    file = read_file('resources/input.txt')

    print(print_signal_strenghts(go_through_instructions(file)))
