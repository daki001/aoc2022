def read_file(path):
	all_lines = list()
	with open(path) as f:
		for line in f:
			line = line.strip()
			if len(line) > 0:
				all_lines.append(list())
				for character in line:
					all_lines[len(all_lines) - 1].append(character)

	return all_lines


def go_through_positions(map, x_cord, y_cord, end, sum_map, next_round):
	#print(map[x_cord][y_cord])
	if x_cord == end[0] and y_cord == end[1]:
		return sum_map[x_cord][y_cord]
	current_height = map[x_cord][y_cord]
	next_sum_value = sum_map[x_cord][y_cord] + 1


	if x_cord - 1 >= 0 and (map[x_cord - 1][y_cord] in range(0, current_height + 2)):
		if sum_map[x_cord - 1][y_cord] == -1:
			sum_map[x_cord - 1][y_cord] = next_sum_value
			if next_sum_value in next_round.keys():
				next_round[next_sum_value].append([x_cord - 1, y_cord])
			else:
				next_round[next_sum_value] = [[x_cord - 1, y_cord]]
	if x_cord + 1 < len(map) and map[x_cord + 1][y_cord] in range(0, current_height + 2):
		if sum_map[x_cord + 1][y_cord] == -1:
			sum_map[x_cord + 1][y_cord] = next_sum_value
			if next_sum_value in next_round.keys():
				next_round[next_sum_value].append([x_cord + 1, y_cord])
			else:
				next_round[next_sum_value] = [[x_cord + 1, y_cord]]
	if y_cord - 1 >= 0 and map[x_cord][y_cord - 1] in range(0, current_height + 2):
		if sum_map[x_cord][y_cord - 1] == -1:
			sum_map[x_cord][y_cord - 1] = next_sum_value
			if next_sum_value in next_round.keys():
				next_round[next_sum_value].append([x_cord, y_cord - 1])
			else:
				next_round[next_sum_value] = [[x_cord, y_cord - 1]]
	if y_cord + 1 < len(map[x_cord]) and map[x_cord][y_cord + 1] in range(0, current_height + 2):
		if sum_map[x_cord][y_cord + 1] == -1:
			sum_map[x_cord][y_cord + 1] = next_sum_value
			if next_sum_value in next_round.keys():
				next_round[next_sum_value].append([x_cord, y_cord + 1])
			else:
				next_round[next_sum_value] = [[x_cord, y_cord + 1]]

	#print(next_round)

	return -1


def find_start(map):
	starting_points = list()
	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j] == 'S':
				map[i][j] = 'a'
				starting_points.append([i,j])
			elif map[i][j] == 'a':
				starting_points.append([i, j])
	return starting_points

def find_end(map):
	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j] == 'E':
				map[i][j] = 'z'
				return [i, j]


def translate_map(map):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	for i in range(len(map)):
		for j in range(len(map[i])):
			map[i][j] = alphabet.index(map[i][j])


def go_through_all(map, x_cord, y_cord, end):
	sum_map = list()
	for i in range(len(map)):
		sum_map.append(list())
		for j in range(len(map[i])):
			sum_map[i].append(-1)
	sum_map[x_cord][y_cord] = 0
	end_value = -1
	next_round = dict()

	while end_value == -1:
		end_value = go_through_positions(map, x_cord, y_cord, end, sum_map, next_round)
		if end_value != -1:
			return end_value
		else:
			while True:
				#print(list(next_round.keys()))
				if len(list(next_round.keys())) == 0:
					return 100000
				next_key = min(list(next_round.keys()))
				if len(next_round[next_key]) > 0:
					x_cord = next_round[next_key][0][0]
					y_cord = next_round[next_key][0][1]
					next_round[next_key].pop(0)
					break
				else:
					next_round.pop(next_key)


if __name__ == '__main__':
	file = read_file('resources/testInput.txt')
	start = find_start(file)
	end = find_end(file)
	translate_map(file)
	min_path = 100000
	for s in start:
		min_path = min(min_path, go_through_all(file, s[0], s[1], end))
	print(min_path)



	file = read_file('resources/input.txt')
	start = find_start(file)
	end = find_end(file)
	translate_map(file)
	min_path = 100000
	for s in start:
		min_path = min(min_path, go_through_all(file, s[0], s[1], end))
	print(min_path)
