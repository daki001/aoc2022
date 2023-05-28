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


def falling_sand(x_cord, y_cord, rocks):
	if [x_cord, y_cord + 1] not in rocks:
		return [x_cord, y_cord + 1]
	if [x_cord - 1, y_cord + 1] not in rocks:
		return [x_cord - 1, y_cord + 1]
	if [x_cord + 1, y_cord + 1] not in rocks:
		return [x_cord + 1, y_cord + 1]

	rocks.append([x_cord, y_cord])
	return[x_cord, y_cord]


def manage_sand(rocks_input):
	max_rocks = 0
	rocks = calculate_all_rock_positions(rocks_input)
	for r in rocks:
		max_rocks = max(max_rocks, r[1])
	#print(max_rocks)
	start_len = len(rocks)
	all_sands = list()
	max_y = 0
	while True:
		all_sands.append([500, 0])
		dropping_list = list()
		for sand in all_sands:
			new_position = falling_sand(sand[0], sand[1], rocks)
			max_y = max(max_y, new_position[1])
			if new_position == sand:
				dropping_list.append(sand)
			else:
				sand[0] = new_position[0]
				sand[1] = new_position[1]
		for element in dropping_list:
			all_sands.pop(all_sands.index(element))
		#print(max_y)
		if max_y > max_rocks:
			print_field(rocks, all_sands)
			return len(rocks) - start_len



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
	print(manage_sand(file))





	file = read_file('resources/input.txt')
	print(file)
	print(manage_sand(file))

