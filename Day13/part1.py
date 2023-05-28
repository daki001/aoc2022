def read_file(path):
	pairs = list()
	with open(path) as f:
		pair = list()
		for line in f:
			line = line.strip()
			if len(line) > 0:
				pair.append(line)
				if len(pair) == 2:
					pairs.append(pair.copy())
					pair = list()

	return pairs


def create_list(input):
	result = list()
	list_level = 0
	number = ''
	is_number = False
	appending_list = result
	for char_index in range(len(input[1:])):
		character = input[1:][char_index]
		if character == '[':
			appending_list = result
			for i in range(list_level):
				appending_list = appending_list[len(appending_list) - 1]
			appending_list.append(list())
			appending_list = appending_list[len(appending_list) - 1]
			list_level += 1
		if character == ']':
			if is_number:
				appending_list.append(int(number))
				is_number = False
				number = ''
			list_level -= 1
			appending_list = result
			for i in range(list_level):
				appending_list = appending_list[len(appending_list) - 1]
		if character.isdigit():
			number += character
			is_number = True
		if character == ',':
			if is_number:
				is_number = False
				appending_list.append(int(number))
				number = ''
	return result


def compare_pairs(left, right):
	final_return = -1
	if len(left) > len(right):
		final_return = 0
	elif len(left) < len(right):
		final_return = 1
	for i in range(len(left)):
		if i >= len(right):
			break
		if type(left[i]) == int and type(right[i]) == int:
			if left[i] < right[i]:
				return 1
			elif left[i] > right[i]:
				return 0
		elif type(left[i]) == int or type(right[i]) == int:
			l = left[i]
			r = right[i]
			if type(l) == int:
				l = [l]
			else:
				r = [r]
			under = compare_pairs(l, r)
			if under != -1:
				return under
		else:
			under = compare_pairs(left[i], right[i])
			if under != -1:
				return under

	return final_return


def calculate_results(pairs):
	result = 0
	counter = 1
	for pair in pairs:
		left = create_list(pair[0])
		right = create_list(pair[1])
		r = compare_pairs(left, right)
		if r == 1:
			result += counter
		counter += 1
	return result

if __name__ == '__main__':
	file = read_file('resources/testInput.txt')
	print(file)
	print(calculate_results(file))





	file = read_file('resources/input.txt')
	print(file)
	print(calculate_results(file))

