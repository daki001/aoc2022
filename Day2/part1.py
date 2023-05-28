def read_file(path):
	moves = [[],[]]
	my_moves = ' XYZ'
	opponent_moves = ' ABC'
	with open(path) as f:

		for line in f:
			mov = line.strip().split(' ')

			moves[0].append(opponent_moves.index(mov[0]))
			moves[1].append(my_moves.index(mov[1]))
	return moves


def calculate_outcome(moves):
	outcome = 0
	for i in range(len(moves[0])):
		outcome += moves[1][i]
		if moves[0][i] == moves[1][i]:
			outcome += 3
		else:
			if moves[0][i] - moves[1][i] == -1 or moves[0][i] - moves[1][i] == 2:
				outcome += 6
	return outcome

if __name__ == '__main__':
	file = read_file('resources/testInput.txt')
	print(calculate_outcome(file))
	file = read_file('resources/input.txt')
	print(calculate_outcome(file))