import re
import part2


stones = [[[0,0],[0,1],[0,2],[0,3]], [[1,0],[0,1],[1,1],[1,2],[2,1]], [[2,2],[1,2],[0,0],[0,1],[0,2]], [[0,0],[1,0],[2,0],[3,0]], [[0,0],[1,0],[0,1],[1,1]]]
def read_file(path):
    instructions = list()
    with open(path) as f:
        for line in f:
            line = line.strip()
            return line

    return instructions

def round(wind, max_value):
    #stone_index = 0
    field = list()
    wind_index = 0
    current_height = 0
    for stone_index in range(max_value):
        part2.delete_old(field)
        current_stone = copy_list(stones[stone_index % 5])
        if len(field) > 0:
            current_height = max([x[0] for x in field])
        #lowest = max([x[0] for x in current_stone])
        for element in range(len(current_stone)):
            current_stone[element][1] = current_stone[element][1] + 2
            current_stone[element][0] = current_stone[element][0] + 4 + current_height
        is_placed = False
        while not is_placed:
            if wind[wind_index % len(wind)] == '<':
                left_most = min([x[1] for x in current_stone])
                if left_most > 0:
                    new_current_stone = current_stone
                    accept = True
                    for element in new_current_stone:
                        if [element[0], element[1] - 1] in field:
                            accept = False
                            break
                    if accept:
                        for element in new_current_stone:
                            element[1] -= 1
                        current_stone = new_current_stone
            else:
                right_most = max([x[1] for x in current_stone])
                #print(right_most)
                if right_most < 6:
                    new_current_stone = current_stone
                    accept = True
                    for element in new_current_stone:
                        if [element[0], element[1] + 1] in field:
                            accept = False
                            break
                    if accept:
                        for element in new_current_stone:
                            element[1] += 1
                        current_stone = new_current_stone

            wind_index += 1
            new_current_stone = current_stone


            accept = True
            for element in new_current_stone:
                if element[0] - 1 == 0 or [element[0] - 1, element[1]] in field:
                    accept = False
                    break
            if accept:
                for element in new_current_stone:
                    element[0] -= 1
                current_stone = new_current_stone
            else:
                for element in current_stone:
                    field.append(element)
                    is_placed = True
    #print(field)
    #print_list(field)
    return max([x[0] for x in field])


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

    file = read_file('resources/input.txt')
    print(file)
    print(round(file, 2022))

    #print(go_through_instructions(file))
