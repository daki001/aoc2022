import re


def read_file(path):
    commands = list()
    with open(path) as f:
        for line in f:
            line = line.strip()

            commands.append(line.split(' '))

    return commands


def execute_command(grid, command):
    new_state = False
    if command[0] == 'on':
        new_state = True

    coords = re.match('x=(-?\\d+)\\.\\.(-?\\d+),y=(-?\\d+)\\.\\.(-?\\d+),z=(-?\\d+)\\.\\.(-?\\d+)', command[1])
    if coords:
        coords = [[max(int(coords.group(1)), -50), min(int(coords.group(2)), 50)],
                  [max(int(coords.group(3)), -50), min(int(coords.group(4)), 50)],
                  [max(int(coords.group(5)), -50), min(int(coords.group(6)), 50)]]

    for x in range(max(coords[0][0], -50), min(coords[0][1] + 1, 51)):

        for y in range(max(coords[1][0], -50), min(coords[1][1] + 1, 51)):

            for z in range(max(coords[2][0], -50), min(coords[2][1] + 1, 51)):

                if [x, y, z] not in grid[0] and [x, y, z] not in grid[1]:
                    if new_state:

                        grid[0].append([x, y, z])
                    else:
                        grid[1].append([x, y, z])

    return grid


def execute_command(grid, command):
    new_state = False
    if command[0] == 'on':
        new_state = True

    coords = re.match('x=(-?\\d+)\\.\\.(-?\\d+),y=(-?\\d+)\\.\\.(-?\\d+),z=(-?\\d+)\\.\\.(-?\\d+)', command[1])
    if coords:
        coords = [[max(int(coords.group(1)), -50), min(int(coords.group(2)), 50)],
                  [max(int(coords.group(3)), -50), min(int(coords.group(4)), 50)],
                  [max(int(coords.group(5)), -50), min(int(coords.group(6)), 50)]]

        if new_state:
            for c in grid[1]:
                if not coords[0][0] > c[0][1] and not coords[0][1] < c[0][0]:
                    if not coords[1][0] > c[1][1] and not coords[1][1] < c[1][0]:
                        if not coords[2][0] > c[2][1] and not coords[2][1] < c[2][0]:
                            pass
            grid[0].append(coords)
        else:
            grid[1].append(coords)


    return grid


def execute_all_commands(commands):
    grid = [[], []]
    for command in commands[::-1]:
        grid = execute_command(grid, command)

    return len(grid[0])


if __name__ == '__main__':
    file = read_file('resources/testInput.txt')
    characters = execute_all_commands(file)
    print(characters)
