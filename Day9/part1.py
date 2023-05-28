def read_file(path):
	all_lines = list()
	with open(path) as f:
		for line in f:
			all_lines.append(line.strip().split(' '))

	return all_lines


def is_next_to_head(tail_position, head_position):
	if head_position[0] in range(tail_position[0] - 1, tail_position[0] + 2) and head_position[1] in range(tail_position[1] - 1, tail_position[1] + 2):
		return []
	else:
		if head_position[0] == tail_position[0]:
			return [0, (head_position[1] - tail_position[1])//abs(head_position[1] - tail_position[1])]
		elif tail_position[1] == head_position[1]:
			return [(head_position[0] - tail_position[0]) // abs(head_position[0] - tail_position[0]), 0]
	return [(head_position[0] - tail_position[0]) // abs(head_position[0] - tail_position[0]), (head_position[1] - tail_position[1]) // abs(head_position[1] - tail_position[1])]


def find_next_move(tail_position, head_position, next_move):
	if next_move == 'R':
		head_position[1] += 1
	elif next_move == 'L':
		head_position[1] -= 1
	elif next_move == 'U':
		head_position[0] -= 1
	elif next_move == 'D':
		head_position[0] += 1
	new_tail = is_next_to_head(tail_position, head_position)
	for i in range(len(new_tail)):
		tail_position[i] += new_tail[i]



def go_through_all_moves(moves):
	head_position = [0,0]
	tail_position = [0,0]
	visited_positions = list()


	for move in moves:
		for count in range(int(move[1])):
			if tail_position not in visited_positions:
				visited_positions.append(tail_position.copy())
			find_next_move(tail_position, head_position, move[0])

	if tail_position not in visited_positions:
		visited_positions.append(tail_position.copy())

	return len(visited_positions)





if __name__ == '__main__':

	file = read_file('resources/testInput.txt')
	print(go_through_all_moves(file))

	file = read_file('resources/input.txt')
	print(go_through_all_moves(file))
