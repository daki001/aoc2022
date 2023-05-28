def read_file(path):
	paths = list()
	with open(path) as f:
		path = list()
		for line in f:
			line = line.strip()
			if len(line) > 0:
				for element in line.split('->'):
					path.append(element.strip())
				paths.append(path.copy())
			path = list()

	return paths


def calculate_all_rock_positions(paths):
	all_rocks = list()
	for path in paths:
		start = path[0].split(',')
		start = [int(start[0]), int(start[1])]
		for element in path[1:]:
			end = element.split(',')
			end = [int(end[0]), int(end[1])]
			if end[0] == start[0]:
				for i in range(min(end[1], start[1]), max(end[1] + 1, start[1] + 1)):
					if [end[0], i] not in all_rocks:
						all_rocks.append([end[0], i])
			else:

				for i in range(min(end[0], start[0]), max(end[0] + 1, start[0] + 1)):
					if [i, end[1]] not in all_rocks:
						all_rocks.append([i, end[1]])
			start = end.copy()
	return all_rocks


def falling_sand(x_cord, y_cord, rocks, end_line):
	while True:
		if y_cord + 1 == end_line:
			rocks.append([x_cord, y_cord])
			return [x_cord, y_cord]
		if [x_cord, y_cord + 1] not in rocks:
			y_cord += 1
		elif [x_cord - 1, y_cord + 1] not in rocks:
			y_cord += 1
			x_cord -= 1
		elif [x_cord + 1, y_cord + 1] not in rocks:
			y_cord += 1
			x_cord += 1
		else:
			rocks.append([x_cord, y_cord])
			return [x_cord, y_cord]




def manage_sand(rocks_input):
	max_rocks = 0
	rocks = calculate_all_rock_positions(rocks_input)
	for r in rocks:
		max_rocks = max(max_rocks, r[1])
	#print(max_rocks)
	start_len = len(rocks)
	count = 0
	while True:
		count += 1
		if [500, 0] in rocks:
			print_field(rocks, [])
			return len(rocks) - start_len
		#dropping_list = list()
		falling_sand(500, 0, rocks, max_rocks + 2)
		if count % 1000 == 0:
			print_field(rocks, [])
		#for element in dropping_list:
		#	all_sands.pop(all_sands.index(element))


def recursive(x_cord, y_cord, rocks, end_line):
	rocks.append([x_cord, y_cord])
	erg = 1
	if y_cord + 1 == end_line:
		return 1
	if [x_cord, y_cord + 1] not in rocks:
		erg += recursive(x_cord, y_cord + 1, rocks, end_line)
	if [x_cord - 1, y_cord + 1] not in rocks:
		erg += recursive(x_cord - 1, y_cord + 1, rocks, end_line)
	if [x_cord + 1, y_cord + 1] not in rocks:
		erg += recursive(x_cord + 1, y_cord + 1, rocks, end_line)

	return erg


def calculate_shadow(rocks_input):
	max_rocks = 0
	rocks = calculate_all_rock_positions(rocks_input)
	for r in rocks:
		max_rocks = max(max_rocks, r[1])
	whole_cave = 1
	row = 1
	for i in range(max_rocks + 2):
		row += 2
		whole_cave += row

	whole_cave -= len(rocks)



def print_field(rocks, sand):
	min_y = 0
	max_y = 0
	min_x = 1000
	max_x = 0
	for element in rocks:
		max_y = max(max_y, element[1])
		min_y = min(min_y, element[1])
		max_x = max(max_x, element[0])
		min_x = min(min_x, element[0])
	for element in sand:
		max_y = max(max_y, element[1])
		min_y = min(min_y, element[1])
		max_x = max(max_x, element[0])
		min_x = min(min_x, element[0])

	for y in range(min_y, max_y + 1):
		line = ''
		for x in range(min_x, max_x + 1):
			if [x, y] in sand:
				line += 'o'

			elif [x,y] in rocks:
				line += '#'
			else:
				line += '.'
		print(line)

if __name__ == '__main__':
	file = read_file('resources/testInput.txt')
	print(file)
	max_rocks = 0
	rocks = calculate_all_rock_positions(file)
	for r in rocks:
		max_rocks = max(max_rocks, r[1])
	print(recursive(500, 0, rocks, max_rocks + 2))





	file = read_file('resources/input.txt')
	print(file)
	max_rocks = 0
	rocks = calculate_all_rock_positions(file)
	for r in rocks:
		max_rocks = max(max_rocks, r[1])
	print(recursive(500, 0, rocks, max_rocks + 2))

