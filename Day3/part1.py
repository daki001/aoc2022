def read_file(path):
    rucksacks = list()
    with open(path) as f:
        for line in f:
            line = line.strip()

            rucksacks.append([line[:len(line) // 2], line[len(line) // 2:]])

    return rucksacks


def find_character(rucksacks):
    letters = list()
    for r in rucksacks:
        for c in r[0]:
            if c in r[1]:
                letters.append(c)
                break
    return letters


def calculate_priority(letters):
    priority = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for l in letters:
        priority += alphabet.index(l) + 1
    return priority


if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    characters = find_character(file)
    print(characters)
    print(calculate_priority(characters))

    file = read_file('resources/input.txt')
    characters = find_character(file)
    print(characters)
    print(calculate_priority(characters))
