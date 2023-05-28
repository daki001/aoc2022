import re


class Monkey:

    def __init__(self):
        self._items = list()
        self._operation = ''
        self._operator = 0
        self._condition = 0
        self._false_monkey = ''
        self._true_monkey = ''
        self._counter = 0

    def set_operation(self, operation):
        matcher = re.match('Operation: new = old ([*+]) (\\d+|(old))', operation)
        if matcher:
            if matcher.group(2) == 'old':
                if matcher.group(1) == '*':
                    self._operation = lambda old: old * old
                else:
                    self._operation = lambda old: old + old
            else:

                if matcher.group(1) == '*':
                    self._operation = lambda old: old * int(matcher.group(2))
                else:
                    self._operation = lambda old: old + int(matcher.group(2))

    def set_condition(self, cond):
        matcher = re.match('Test: divisible by (\\d+)', cond)
        if matcher:
            self._condition = int(matcher.group(1))

    def initial_list(self, items):
        i = items.split(':')[1].strip().split(',')
        for element in i:
            self._items.append(int(element.strip()))

    def turn(self):
        # print(self._items)
        for element in self._items:
            self._counter += 1
            new_element = self._operation(element)
            new_element //= 3
            if new_element % self._condition == 0:
                self._true_monkey._items.append(new_element)
            else:
                self._false_monkey._items.append(new_element)
        self._items = list()


    def set_monkeys_true(self, true):
        self._true_monkey = true

    def set_monkeys_false(self, false):
        self._false_monkey = false


def read_file(path):
    instructions = list()
    with open(path) as f:
        for line in f:
            line = line.strip()
            instructions.append(line)

    return instructions


def create_monkeys(instruction):
    monkeys = dict()
    for line in instruction:
        line = line.strip()
        if line.startswith('Monkey'):
            monkeys[int(line.split(' ')[1][:-1])] = Monkey()
    return monkeys


def initialize_monkeys(monkeys, instructions):
    current_monkey = 0
    for line in instructions:
        line = line.strip()
        if line.startswith('Monkey'):
            current_monkey = int(line.split(' ')[1][:-1])
        elif line.startswith('Starting items:'):
            monkeys[current_monkey].initial_list(line)
        elif line.startswith('Operation:'):
            monkeys[current_monkey].set_operation(line)
        elif line.startswith('Test:'):
            monkeys[current_monkey].set_condition(line)
        elif line.startswith('If true:'):
            new_monkey = line.split(' ')
            new_monkey = int(new_monkey[len(new_monkey) - 1])
            monkeys[current_monkey].set_monkeys_true(monkeys[new_monkey])
        elif line.startswith('If false:'):
            new_monkey = line.split(' ')
            new_monkey = int(new_monkey[len(new_monkey) - 1])
            monkeys[current_monkey].set_monkeys_false(monkeys[new_monkey])

def rounds(number, monkeys):
    for i in range(number):
        for monkey in monkeys.keys():
            monkeys[monkey].turn()

    most_counter = list()
    for monkey in monkeys.values():
        most_counter.append(monkey._counter)
        #print(monkey._items)
    most_counter.sort(reverse=True)
    #print(most_counter)
    return most_counter[0] * most_counter[1]

if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    print(file)
    monkeys = create_monkeys(file)
    initialize_monkeys(monkeys, file)
    print(rounds(10000, monkeys))
    file = read_file('resources/input.txt')
    print(file)
    monkeys = create_monkeys(file)
    initialize_monkeys(monkeys, file)
    print(rounds(20, monkeys))
    #print(go_through_instructions(file))
