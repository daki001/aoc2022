import re
import part1



stones = [[[0,0],[0,1],[0,2],[0,3]], [[1,0],[0,1],[1,1],[1,2],[2,1]], [[2,2],[1,2],[0,0],[0,1],[0,2]], [[0,0],[1,0],[2,0],[3,0]], [[0,0],[1,0],[0,1],[1,1]]]
def read_file(path):
    instructions = list()
    with open(path) as f:
        for line in f:
            line = line.strip()
            return line

    return instructions

def round(wind, max_value, test_new):
    #stone_index = 0
    field = list()
    wind_index = 0
    current_height = 0
    wind_list = list()
    stone_list = [{},{},{},{}, {}]
    for stone_index in range(max_value):
        if test_new and stone_index > len(wind):
            if wind_index % len(wind) in list(stone_list[stone_index % 5].keys()) :
                print(stone_index)
                print(stone_list[stone_index % 5][wind_index % len(wind)])
                print(stone_index + 1 * (stone_index - stone_list[stone_index % 5][wind_index % len(wind)]))
                print(part1.round(wind, stone_list[stone_index % 5][wind_index % len(wind)]))
                print(part1.round(wind, stone_index))
                difference = part1.round(wind, stone_index + 1 * (stone_index - stone_list[stone_index % 5][wind_index % len(wind)])) - part1.round(wind, stone_index)
                return ((max_value - stone_index) // (stone_index - stone_list[stone_index % 5][wind_index % len(wind)])) * difference + part1.round(wind, stone_index + ((max_value - stone_index) % (stone_index - stone_list[stone_index % 5][wind_index % len(wind)])))
                #print(part1.round(wind, stone_index + 2 * (stone_index - stone_list[stone_index % 5][wind_index % len(wind)])))
                #print(part1.round(wind, stone_index + 3 * (stone_index - stone_list[stone_index % 5][wind_index % len(wind)])))
                #return 'test'
            else:
                stone_list[stone_index % 5][wind_index % len(wind)] = stone_index
        if wind_index % len(wind) == 0:
            print(stone_index)
        delete_old(field)
        current_stone = copy_list(stones[stone_index % 5])
        if len(field) > 0:
            current_height = max([x[0] for x in field])
        #lowest = max([x[0] for x in current_stone])
        for element in range(len(current_stone)):
            current_stone[element][1] = current_stone[element][1] + 2
            current_stone[element][0] = current_stone[element][0] + 4 + current_height
        is_placed = False
        while not is_placed:
            if stone_index % 5 == 0 and wind_index % len(wind) == 0:
                print('here')
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
    #test = list()
    #for element in field:
    #    if element[0] < 11:
    #        test.append(element)
    #print_list(test)
    return max([x[0] for x in field])


def delete_old(field):
    highest = [0, 0, 0, 0, 0, 0, 0]
    for f_ind in range(len(field)):
        f = field[f_ind]
        #print(f)
        highest[f[1]] = max(f[0], highest[f[1]])
    drop_point = min(highest)
    for f_ind in range(len(field))[::-1]:
        f = field[f_ind]
        if f[0] < drop_point:
            field.pop(f_ind)

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
    print(round(file, 1000000000000, True))

    file = read_file('resources/input.txt')
    #print(file)
    print(round(file, 1000000000000, True))

    #print(go_through_instructions(file))
