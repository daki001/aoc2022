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
        is_inside = True
        first_elf = range(int(p[0].split('-')[0]), int(p[0].split('-')[1]) + 1)
        second_elf = range(int(p[1].split('-')[0]), int(p[1].split('-')[1]) + 1)
        if len(first_elf) >= len(second_elf):
            for second in second_elf:
                if second not in first_elf:
                    is_inside = False
        else:
            for first in first_elf:
                if first not in second_elf:
                    is_inside = False

        if is_inside:
            count += 1
    return count


if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    pairs = compare_pairs(file)
    print(pairs)


    file = read_file('resources/input.txt')
    pairs = compare_pairs(file)
    print(pairs)