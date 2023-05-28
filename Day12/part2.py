def read_file(path):
	all_lines = list()
	with open(path) as f:
		for line in f:
			all_lines.append(line.strip().split(' '))

	return all_lines
def go_through_positions(map, x_cord, y_cord, end):
	#print(map[x_cord][y_cord])
	if x_cord == end[0] and y_cord == end[1]:
		return 0
	current_height = map[x_cord][y_cord]
	moves = list()
	map[x_cord][y_cord] = -1



	if x_cord - 1 >= 0 and (map[x_cord - 1][y_cord] in range(0, current_height + 2)):
		path = go_through_positions(map, x_cord - 1, y_cord, end)
		if path != -1:
			moves.append(path + 1)
	if x_cord + 1 < len(map) and map[x_cord + 1][y_cord] in range(0, current_height + 2):
		path = go_through_positions(map, x_cord + 1, y_cord, end)
		if path != -1:
			moves.append(path + 1)
	if y_cord - 1 >= 0 and map[x_cord][y_cord - 1] in range(0, current_height + 2):
		path = go_through_positions(map, x_cord, y_cord - 1, end)
		if path != -1:
			moves.append(path + 1)
	if y_cord + 1 < len(map[x_cord]) and map[x_cord][y_cord + 1] in range(0, current_height + 2):
		path = go_through_positions(map, x_cord, y_cord + 1,end)
		if path != -1:
			moves.append(path + 1)
	map[x_cord][y_cord] = current_height
	if len(moves) > 0:
		return min(moves)
	else:
		return -1


def print_round(tail_position, head_position):
	min_value_x = head_position[0]
	min_value_y = head_position[1]
	max_value_x = head_position[0]
	max_value_y = head_position[1]

	for tail in tail_position:
		min_value_x = min(min_value_x, tail[0])
		min_value_y = min(min_value_y, tail[1])
		max_value_x = max(max_value_x, tail[0])
		max_value_y = max(max_value_y, tail[1])

	square = list()
	for i in range(min_value_x, max_value_x + 1):
		square.append(list())
		for j in range(min_value_y, max_value_y + 1):
			square[i - min_value_x].append('.')
	#print(square)
	square[head_position[0] - min_value_x][head_position[1] - min_value_y] = 'H'
	counter = 1
	for tail in tail_position:
		if square[tail[0] - min_value_x][tail[1] - min_value_y] == '.':
			square[tail[0] - min_value_x][tail[1] - min_value_y] = str(counter)

		counter += 1


	for i in square:
		line = ''
		for j in i:
			line += j
		print(line)


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
	for tail in range(len(tail_position)):
		if tail > 0:
			new_tail = is_next_to_head(tail_position[tail], tail_position[tail - 1])
		else:
			new_tail = is_next_to_head(tail_position[tail], head_position)
		for i in range(len(new_tail)):
			tail_position[tail][i] += new_tail[i]



def go_through_all_moves(moves):
	head_position = [0,0]
	tail_position = []
	for i in range(9):
		tail_position.append([0,0])
	visited_positions = list()


	for move in moves:
		for count in range(int(move[1])):
			if tail_position[8] not in visited_positions:
				visited_positions.append(tail_position[8].copy())
			find_next_move(tail_position, head_position, move[0])
		#print_round(tail_position, head_position)
		#print()
	if tail_position[8] not in visited_positions:
		visited_positions.append(tail_position[8].copy())

	return len(visited_positions)





if __name__ == '__main__':

	file = read_file('resources/testInput.txt')
	print(go_through_all_moves(file))

	file = read_file('resources/input.txt')
	print(go_through_all_moves(file))
