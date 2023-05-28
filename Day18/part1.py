import re



def read_file(path):
    grid = list()

    with open(path) as f:
        for line in f:
            line = line.strip()
            line = line.split(',')
            coords = list()
            for l in line:
                coords.append(int(l))
            grid.append(coords)

    return grid

def see_neighbors(grid):

    count = 6 * len(grid)
    for square in grid:
        for square2 in grid:
            if check_neighbor(square, square2):
                    count -= 1

    return count


def check_neighbor(square1, square2):
    if square1[0] in [square2[0] - 1, square2[0] + 1] and square1[1] == square2[1] and square1[2] == square2[2]:
        return True
    if square1[1] in [square2[1] - 1, square2[1] + 1] and square1[0] == square2[0] and square1[2] == square2[2]:
        return True
    if square1[2] in [square2[2] - 1, square2[2] + 1] and square1[1] == square2[1] and square1[0] == square2[0]:
        return True
    return False

def print_list(field):
    erg = []
    print(max([x[0] for x in field]))
    for i in range(max([x[0] for x in field]) + 1):
        erg.append(list())
        for _ in range(7):
            erg[i].append('.')
    for i in field:
        print(i)
        erg[i[0]][i[1]] = '#'

    for i in erg[::-1]:
        print(i)



def copy_list(old_list):
    new_list = list()
    for element in old_list:
        new_list.append(element.copy())

    return new_list

if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    print(file)
    print(see_neighbors(file))

    file = read_file('resources/input.txt')
    print(file)
    print(see_neighbors(file))
    #print(round(file, 2022))

    #print(go_through_instructions(file))
