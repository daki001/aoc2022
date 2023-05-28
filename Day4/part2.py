def read_file(path):
    pairs = list()
    with open(path) as f:
        for line in f:
            line = line.strip()

            pairs.append(line.split(','))

    return pairs


def compare_pairs(pairs):
    count = 0
    for p in pairs:
        first_elf = range(int(p[0].split('-')[0]), int(p[0].split('-')[1]) + 1)
        second_elf = range(int(p[1].split('-')[0]), int(p[1].split('-')[1]) + 1)

        for second in second_elf:
            if second in first_elf:
                count += 1
                break


    return count

if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    pairs = compare_pairs(file)
    print(pairs)

    file = read_file('resources/input.txt')
    pairs = compare_pairs(file)
    print(pairs)
