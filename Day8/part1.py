def read_file(path):
    square = list()
    with open(path) as f:
        count = 0
        for line in f:
            line = line.strip()
            square.append(list())
            for character in line:
                square[count].append(int(character))
            count += 1

    return square


def is_visible(square, coordinates):
    value = square[coordinates[0]][coordinates[1]]
    if value > max(square[coordinates[0]][:coordinates[1]]) or value > max(square[coordinates[0]][coordinates[1] + 1:]):
        return True
    vertical_list = list()
    for element in range(len(square)):
        vertical_list.append(square[element][coordinates[1]])

    if value > max(vertical_list[:coordinates[0]]) or value > max(vertical_list[coordinates[0] + 1:]):
        return True


    return False


def find_all_visible(square):
    count = len(square) * 2 + len(square[0]) * 2 - 4
    for i in range(1,len(square) - 1):
        for j in range(1, len(square[0]) - 1):
            if is_visible(square, [i,j]):
                count += 1
    return count


if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    print(file)
    print(find_all_visible(file))

    file = read_file('resources/input.txt')

    print(file)
    print(find_all_visible(file))
