import datetime


def read_file(path):
	number_list = list()
	index_list = list()
	with open(path) as f:
		counter = 0
		for line in f:
			line = line.strip()
			number_list.append(int(line))
			index_list.append(counter)
			counter += 1

	return [number_list, index_list]


def change_positions(numbers, indexes):
	for element in range(len(numbers)):
		#print(create_new_list(numbers, indexes))
		#print(indexes)
		changing_number = numbers[element]
		#print(changing_number)
		current_index = indexes[element]
		if changing_number >= 0:
			indexes[element] += changing_number
			if indexes[element] >= len(indexes):
				if current_index > indexes[element] % len(indexes):
					indexes[element] = (indexes[element] + 1) % len(indexes)
				else:
					indexes[element] %= len(indexes)
				for others in range(len(indexes)):
					if others != element:
						if current_index > indexes[element]:
							if current_index > indexes[others] >= (current_index + changing_number + 1) % len(indexes):
								indexes[others] = (indexes[others] + 1) % len(indexes)
						else:
							if current_index < indexes[others] <= (current_index + changing_number) % len(indexes):
								indexes[others] = (indexes[others] - 1) % len(indexes)
			else:
				for others in range(len(indexes)):
					if others != element:
						if current_index < indexes[others] <= current_index + changing_number:
							indexes[others] = (indexes[others] - 1) % len(indexes)

		else:
			indexes[element] += changing_number
			if indexes[element] < 0:
				if current_index < indexes[element] % len(indexes):
					indexes[element] = (indexes[element] - 1) % len(indexes)
				else:
					indexes[element] %= len(indexes)
				for others in range(len(indexes)):
					if others != element:
						if current_index < indexes[element]:
							if current_index < indexes[others] <= (current_index + changing_number - 1) % len(indexes):
								indexes[others] = (indexes[others] - 1) % len(indexes)
						else:
							if current_index > indexes[others] >= (current_index + changing_number) % len(indexes):
								indexes[others] = (indexes[others] + 1) % len(indexes)
			else:
				for others in range(len(indexes)):
					if others != element:
						if current_index > indexes[others] >= current_index + changing_number:
							indexes[others] = (indexes[others] + 1) % len(indexes)

	#print(indexes)
	new_list = create_new_list(numbers,indexes)
	start = new_list.index(0)
	#print(start)
	result = 0
	result += new_list[(start + 1000) % len(new_list)]
	result += new_list[(start + 2000) % len(new_list)]
	result += new_list[(start + 3000) % len(new_list)]
	return result


def create_new_list(numbers, indexes):
	new_list = numbers.copy()
	for ind in range(len(indexes)):
		new_list[ind] = numbers[indexes.index(ind)]
	return new_list


if __name__ == '__main__':

	start_time = datetime.datetime.now()
	file = read_file('resources/testInput.txt')
	print(file)
	print(change_positions(file[0], file[1]))

	file = read_file('resources/input.txt')
	print(file)
	print(change_positions(file[0], file[1]))
	print(datetime.datetime.now() - start_time)
