import re

def read_file(path):
	with open(path) as f:
		for line in f:
			return line

	return None


def find_start_sequence(input):
	for start_letter in range(len(input)):
		characters = ''
		for i in range(start_letter, start_letter + 14):
			if i < len(input) and input[i] not in characters:
				characters += input[i]
		if len(characters) == 14:
			return input.index(characters) + 14
	return None

if __name__ == '__main__':
	file = read_file('resources/testInput.txt')
	print(file)
	print(find_start_sequence(file))

	file = read_file('resources/input.txt')
	print(file)
	print(find_start_sequence(file))
