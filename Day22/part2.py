import part1

def read_file(path):
    rucksacks = [[]]
    with open(path) as f:
        group = 0
        for line in f:
            if group == 3:
                group = 0
                rucksacks.append([])
            line = line.strip()

            rucksacks[len(rucksacks) - 1].append(line)
            group += 1
    return rucksacks


def find_character(rucksacks):
    letters = list()
    for r in rucksacks:
        for g in r[0]:
            if g in r[1] and g in r[2]:
                letters.append(g)
                break
    return letters


if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    print(file)
    characters = find_character(file)
    print(characters)
    print(part1.calculate_priority(characters))

    file = read_file('resources/input.txt')
    print(file)
    characters = find_character(file)
    print(characters)
    print(part1.calculate_priority(characters))