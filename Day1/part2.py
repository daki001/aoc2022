def read_file(path):
	all_elfs = list()
	with open(path) as f:
		elf = 0
		for line in f:
			if len(line.strip()) > 0:
				elf += int(line.strip())
			else:
				all_elfs.append(elf)
				elf = 0
		if elf != 0:
			all_elfs.append(elf)
	return all_elfs



def find_max(elfs):
	print(elfs)
	elfs.sort(reverse=True)
	print(elfs)

	return sum(elfs[:3])


if __name__ == '__main__':
	file = read_file('resources/testInput.txt')
	print(find_max(file))
	file = read_file('resources/input.txt')
	print(find_max(file))