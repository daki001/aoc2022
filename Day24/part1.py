import datetime
import re


def read_file(path):
	storms = list()
	storms.append(list())
	storms.append(list())
	storms.append(list())
	storms.append(list())
	endcounter = 0
	with open(path) as f:
		line_counter = 0
		for line in f:
			line = line.strip()

			for element in range(len(line)):
				if line[element] == '>':
					storms[2].append([line_counter, element])
				elif line[element] == '<':
					storms[3].append([line_counter, element])
				elif line[element] == '^':
					storms[1].append([line_counter, element])
				elif line[element] == 'v':
					storms[0].append([line_counter, element])
				endcounter = element
			line_counter += 1
	return [storms, [line_counter - 1, endcounter - 1]]


def move_storms(storms, goal):
	for direction in range(len(storms)):
		for pos in storms[direction]:
			if direction == 0:
				pos[0] += 1
				if pos[0] == goal[0]:
					pos[0] = 1
			elif direction == 1:
				pos[0] -= 1
				if pos[0] == 0:
					pos[0] = goal[0] - 1
			elif direction == 2:
				pos[1] += 1
				if pos[1] > goal[1]:
					pos[1] = 1
			elif direction == 3:
				pos[1] -= 1
				if pos[1] == 0:
					pos[1] = goal[1]

def round(current_pos, storms, goal):
	new_positions = list()
	flat_storm = list()
	for s in storms:
		flat_storm.extend(s)
	if current_pos not in flat_storm:
		new_positions.append(current_pos.copy())

	for i in [-1, 1]:
		if [current_pos[0], current_pos[1] + i] not in flat_storm and 0 < current_pos[1] + i <= goal[1] and 0 < current_pos[0] <= goal[0]:
			new_positions.append([current_pos[0], current_pos[1] + i])
		if [current_pos[0] + i, current_pos[1]] not in flat_storm and 0 < current_pos[0] + i <= goal[0] and 0 < current_pos[1] <= goal[1]:
			new_positions.append([current_pos[0] + i, current_pos[1]])
	return new_positions


def go_through_map(storms, goal):
	print(goal)
	next_round = [[0, 1]]
	counter = 0
	while True:
		#print(storms)
		move_storms(storms, goal)

		new_next_round = list()
		counter += 1
		for element in next_round:
			new_next_round.extend(round(element, storms, goal))
		#print(new_next_round)
		if goal in new_next_round:
			return counter

		next_round = list()

		for i in new_next_round:
			if i not in next_round:
				next_round.append(i)


if __name__ == '__main__':
	start_time = datetime.datetime.now()
	file = read_file('resources/testInput.txt')
	# print(file)
	print(go_through_map(file[0], file[1]))
	file = read_file('resources/input.txt')
	# print(file)
	print(go_through_map(file[0], file[1]))
	print(datetime.datetime.now() - start_time)
