import re
import sys


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


def see_neighbors2(grid):
    start = [0,0,0]
    max_x = max([x[0] for x in grid])
    max_y = max([x[1] for x in grid])
    max_z = max([x[2] for x in grid])
    used = list()
    return recursive(grid, start, max_x, max_y, max_z, used)

def see_neighbors3(grid):
    start = [0,0,0]
    max_x = max([x[0] for x in grid])
    max_y = max([x[1] for x in grid])
    max_z = max([x[2] for x in grid])
    used = list()
    next_coords = list()
    next_coords.append(start.copy())
    count = 0
    while len(next_coords) > 0:
        current = next_coords[0]
        next_coords.pop(0)
        if current in used:
            continue
        used.append(current)
        for i in [-1, 1]:
            if -1 <= current[0] + i <= max_x + 1:
                current[0] += i
                if current in grid:
                    count += 1
                else:
                    next_coords.append(current.copy())
                current[0] -= i
            if -1 <= current[1] + i <= max_y + 1:
                current[1] += i
                if current in grid:
                    count += 1
                else:
                    next_coords.append(current.copy())
                current[1] -= i
            if -1 <= current[2] + i <= max_z + 1:
                current[2] += i
                if current in grid:
                    count += 1
                else:
                    next_coords.append(current.copy())
                current[2] -= i

    return count


def recursive(grid, coords, max_x, max_y, max_z, used):

    if coords in used:
        return 0
    count = 0
    used.append(coords.copy())
    for i in [-1,1]:
        if 0 <= coords[0] + i <= max_x + 1:
            coords[0] += i
            if coords in grid:
                count += 1
            else:
                count += recursive(grid, coords, max_x, max_y, max_z, used)
            coords[0] -= i

        if 0 <= coords[1] + i <= max_y + 1:
            coords[1] += i
            if coords in grid:
                count += 1
            else:
                count += recursive(grid, coords, max_x, max_y, max_z, used)
            coords[1] -= i

        if 0 <= coords[2] + i <= max_z + 1:
            coords[2] += i
            if coords in grid:
                count += 1
            else:
                count += recursive(grid, coords, max_x, max_y, max_z, used)
            coords[2] -= i
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
    #print_list(file)
    print(see_neighbors3(file))
    #sys.setrecursionlimit(15000)
    file = read_file('resources/input.txt')
    print(file)
    print(see_neighbors3(file))
    #print(see_neighbors(file))
    #print(round(file, 2022))

    #print(go_through_instructions(file))
