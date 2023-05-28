def read_file(path):
	moves = [[],[]]
	my_moves = {'X': 0, 'Y': 3, 'Z': 6}
	opponent_moves = ' ABC'
	with open(path) as f:

		for line in f:
			mov = line.strip().split(' ')

			moves[0].append(opponent_moves.index(mov[0]))
			moves[1].append(my_moves[mov[1]])
	return moves


def calculate_outcome(moves):
	outcome = 0
	for i in range(len(moves[0])):
		outcome += moves[1][i]
		if moves[1][i] == 3:
			print(moves[0][i])
			outcome += moves[0][i]
		else:
			if moves[1][i] == 0:
				my_move = moves[0][i] - 1
				if my_move <= 0:
					my_move += 3
				print(my_move)
				outcome += my_move
			else:
				my_move = moves[0][i] + 1
				if my_move > 3:
					my_move -= 3
				print(my_move)
				outcome += my_move
	return outcome

if __name__ == '__main__':
	file = read_file('resources/testInput.txt')
	print(calculate_outcome(file))
	file = read_file('resources/input.txt')
	print(calculate_outcome(file))