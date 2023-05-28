def read_file(path):
	all_lines = list()
	with open(path) as f:
		for line in f:
			all_lines.append(line.strip())

	return all_lines


def create_directory_structure(commands):
	tree = dict()
	pwd = ''
	last_index = 0
	for line_index in range(len(commands)):
		if line_index < last_index:
			continue
		line = commands[line_index].strip()
		if line.startswith('$'):
			if line.startswith('$ cd'):
				if line != '$ cd ..':
					if len(pwd) > 0:
						pwd += line.split(' ')[2] + '/'
					else:
						pwd += '/'

				else:
					if '/' in pwd[1:]:
						pwd = pwd[:pwd.rindex('/') - 1]
					else:
						pwd = ''
			else:

				files = get_file_listing(commands, line_index + 1)
				last_index = files[0]
				files = files[1]
				#print(files)
				copy_tree = tree
				if pwd != '/':
					working = pwd.split('/')
					#print(pwd)
					for element in working[1:-1]:
						if element in copy_tree.keys():

							copy_tree = copy_tree[element]
						else:
							copy_tree[element] = dict()
							copy_tree = copy_tree[element]
				for file, content in files.items():
					if content != 'dir':
						copy_tree[file] = content
					else:
						copy_tree[file] = dict()
	return tree

def get_file_listing(commands, index):
	files = dict()
	while not commands[index].startswith('$'):
		line = commands[index].strip()
		#print(line)
		if line.startswith('dir'):
			key = line.split(' ')[1]
			files[key] = 'dir'
		else:
			key = line.split(' ')[1]
			#print(key)
			files[key] = int(line.split(' ')[0])

		index += 1
		if index == len(commands):
			return [index, files]

	return [index, files]


def find_start_sequence(input):
	for start_letter in range(len(input)):
		characters = ''
		for i in range(start_letter, start_letter + 4):
			if i < len(input) and input[i] not in characters:
				characters += input[i]
		if len(characters) == 4:
			return input.index(characters) + 4
	return None


def calculate_sizes(tree):
	sum = 0
	directories = list()
	for key,value in tree.items():
		if not isinstance(value, int):
			#print(value)
			subdirectory = calculate_sizes(value)
			if subdirectory[0] <= 100000:
				directories.append(subdirectory[0])
			directories.extend(subdirectory[1])
			sum += subdirectory[0]
		else:
			#print(value)
			sum += value
	return [sum, directories]



if __name__ == '__main__':
	#test = dict()
	#test['test'] = 1
	#print(test)
	file = read_file('resources/testInput.txt')
	#print(file)
	tree = create_directory_structure(file)
	#print(tree)
	print(sum(calculate_sizes(tree)[1]))

	file = read_file('resources/input.txt')
	# print(file)
	tree = create_directory_structure(file)
	# print(tree)
	print(sum(calculate_sizes(tree)[1]))
