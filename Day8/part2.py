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


def scenic_score(square, coordinates):
    value = square[coordinates[0]][coordinates[1]]
    left = square[coordinates[0]][:coordinates[1]][::-1]
    #print(left)
    result = 1
    count = 0
    for l in left:
        count += 1
        if l >= value:
            break

    result *= count
    count = 0

    right = square[coordinates[0]][coordinates[1] + 1:]
    #print(right)

    for l in right:
        count += 1
        if l >= value:
            break

    result *= count
    count = 0

    vertical_list = list()
    for element in range(len(square)):
        vertical_list.append(square[element][coordinates[1]])

    up = vertical_list[:coordinates[0]][::-1]
    #print(up)
    for l in up:
        count += 1
        if l >= value:
            break

    result *= count
    count = 0
    down = vertical_list[coordinates[0] + 1:]
    #print(down)
    for l in down:
        count += 1
        if l >= value:
            break

    result *= count
    return result


def find_all_visible(square):
    current_score = 0
    for i in range(1, len(square) - 1):
        for j in range(1, len(square[0]) - 1):
            score = scenic_score(square, [i, j])
            if score > current_score:
                current_score = score
    return current_score


if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    print(file)
    #print(scenic_score(file,[3,2]))
    print(find_all_visible(file))

    file = read_file('resources/input.txt')

    print(file)
    print(find_all_visible(file))
