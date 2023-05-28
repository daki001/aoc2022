import re

def read_file(path):
	positions_finished = False
	positions = dict()
	movements = list()
	with open(path) as f:
		for line in f:
			if positions_finished:
				line = line.strip()
				matcher = re.match('move (\\d+) from (\\d+) to (\\d+)', line)
				if matcher:
					movements.append([int(matcher.group(2)), int(matcher.group(3)), int(matcher.group(1))])
			else:
				if len(line.strip()) == 0:
					positions_finished = True
					continue
				for i in range(0,(len(line) + 1), 4):
					if i < len(line) - 4:
						part = line[i:i+4]
					else:
						part = line[i:]

					matcher = re.match('\\[([a-zA-Z]+)\\]', part)
					if matcher:
						if i // 4 + 1 in positions.keys():
							positions[i//4 + 1].append(matcher.group(1))
						else:
							positions[i//4 + 1] = [matcher.group(1)]


	return [positions, movements]


def move_crates(input):
	initial_positions = input[0]
	movements = input[1]
	for element in movements:
		for _ in range(element[2]):
			moved_crate = initial_positions[element[0]][0]
			initial_positions[element[1]].insert(0, moved_crate)
			initial_positions[element[0]].pop(0)
			print(initial_positions)

	keys = list(initial_positions.keys())
	keys.sort()
	result = ''
	for element in keys:
		result += initial_positions[element][0]
	return result


if __name__ == '__main__':
	file = read_file('resources/testInput.txt')
	print(file)
	print(move_crates(file))

	file = read_file('resources/input.txt')
	print(file)
	print(move_crates(file))
