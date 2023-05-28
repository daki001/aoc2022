def read_file(path):
    instructions = list()
    with open(path) as f:
        count = 0
        for line in f:
            line = line.strip()
            instructions.append(line)

    return instructions


def execute_instruction(cycle, instruction, register):
    if instruction.startswith('addx'):
        cycle += 2
        register += int(instruction.split(' ')[1])
    else:
        cycle += 1

    return [cycle, register]

def go_through_instructions(instructions):
    register = 1
    cycle = 0
    signal_strengths = list()
    for inst in instructions:
        if inst.startswith('addx'):
            if (cycle + 1 - 20) % 40 == 0:

                signal_strengths.append((cycle + 1) * register)
            elif (cycle + 2 - 20) % 40 == 0:

                signal_strengths.append((cycle + 2) * register)
        else:
            if (cycle + 1 - 20) % 40 == 0:

                signal_strengths.append((cycle + 1) * register)
        after_instruction = execute_instruction(cycle, inst, register)
        register = after_instruction[1]
        cycle = after_instruction[0]
    return sum(signal_strengths)

if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    print(file)
    print(go_through_instructions(file))

    file = read_file('resources/input.txt')

    print(go_through_instructions(file))
