import datetime
import re


def read_file(path):
	elves = list()
	with open(path) as f:
		line_counter = 0
		for line in f:
			line = line.strip()

			for element in range(len(line)):
				if line[element] == '#':
					elves.append([line_counter, element])
			line_counter += 1
	return elves


def decide_move(position, elves, start):
	counter = 0
	has_neighbor = False
	for element in range(-1, 2):
		for element2 in range(-1, 2):
			if [position[0] + element, position[1] + element2] in elves and [position[0] + element, position[1] + element2] != position:
				has_neighbor = True
	#print(has_neighbor)
	if not has_neighbor:
		return position
	while counter < 4:
		if start % 4 == 0:
			is_in_elves = False
			for i in range(-1, 2):
				if [position[0] - 1, position[1] + i] in elves:
					is_in_elves = True
			if not is_in_elves:
				return [position[0] - 1, position[1]]
		if start % 4 == 1:
			is_in_elves = False
			for i in range(-1, 2):
				if [position[0] + 1, position[1] + i] in elves:
					is_in_elves = True
			if not is_in_elves:
				return [position[0] + 1, position[1]]
		if start % 4 == 2:
			is_in_elves = False
			for i in range(-1, 2):
				if [position[0] + i, position[1] - 1] in elves:
					is_in_elves = True
			if not is_in_elves:
				return [position[0], position[1] - 1]
		if start % 4 == 3:
			is_in_elves = False
			for i in range(-1, 2):
				if [position[0] + i, position[1] + 1] in elves:
					is_in_elves = True
			if not is_in_elves:
				return [position[0], position[1] + 1]
		start += 1
		counter += 1
	return position


def plan_moves(elves, start):
	new_positions = list()
	for elf in elves:
		pos = decide_move(elf, elves, start)
		#print(elf)
		#print(pos)
		#print('')
		new_positions.append(pos)

	for element in range(len(new_positions)):
		if new_positions.count(new_positions[element]) > 1:
			pos = new_positions[element].copy()
			try:
				while True:
					indexes = new_positions.index(pos)
					new_positions[indexes] = elves[indexes]
			except ValueError:
				pass

	return new_positions


def print_elves(elves):
	x_min = min([x[0] for x in elves])
	x_max = max([x[0] for x in elves])
	y_min = min([x[1] for x in elves])
	y_max = max([x[1] for x in elves])
	square = list()
	for element in range(x_max - x_min + 1):
		square.append(list())
		for element2 in range(y_max-y_min + 1):
			square[element].append('.')

	for elf in elves:
		square[elf[0] - x_min][elf[1] - y_min] = '#'

	for line in square:
		print(line)

def compare_lists(old, new):
	for element in old:
		if element not in new:
			return False
	return True


def go_through_all_moves(elves):
	count = 0
	while True:
		new_elves = plan_moves(elves, count)
		count += 1
		if compare_lists(elves, new_elves):
			break
		elves = new_elves
	print_elves(elves)
	return count


def calculate_square(elves):
	elves = go_through_all_moves(elves)

	return elves


if __name__ == '__main__':
	start_time = datetime.datetime.now()
	file = read_file('resources/testInput.txt')
	# print(file)
	print(calculate_square(file))

	file = read_file('resources/input.txt')
	# print(file)
	print(calculate_square(file))
	#print(go_through_monkeys(file))
	print(datetime.datetime.now() - start_time)
