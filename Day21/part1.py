import datetime
import re


class Monkey:
	def __init__(self, name, number=None, neighbor1=None, neighbor2=None, operation=None):
		self.name = name
		if number is None:
			self.is_number = False
			self.neigh1 = neighbor1
			self.neigh2 = neighbor2
			self.operation = operation
		else:
			self.is_number = True
			self.number = number





def read_file(path):
	monkeys = list()
	with open(path) as f:
		for line in f:
			line = line.strip()
			matcher = re.match('([a-z]+): (\\d+)', line)
			if matcher:

				monkeys.append(Monkey(matcher.group(1), number=int(matcher.group(2))))
			else:
				matcher = re.match('([a-z]+): ([a-z]+) ([\\-*/+]) ([a-z]+)', line)
				if matcher:
					monkeys.append(Monkey(matcher.group(1), neighbor1=matcher.group(2), neighbor2=matcher.group(4), operation=matcher.group(3)))

	return monkeys


def get_monkey_by_name(monkeys,name):
	for element in monkeys:
		if element.name == name:
			return element

def go_through_monkeys(monkeys):
	start_name = 'root'
	start = ''
	for element in monkeys:
		#print(element.name)
		if element.name == start_name:
			start = element
	#print(start)
	return recursive(start, monkeys)

def recursive(monkey, monkeys):
	if monkey.is_number:
		return monkey.number
	else:
		neighbor1 = get_monkey_by_name(monkeys, monkey.neigh1)
		neighbor2 = get_monkey_by_name(monkeys, monkey.neigh2)
		element1 = recursive(neighbor1, monkeys)
		element2 = recursive(neighbor2, monkeys)
		if monkey.operation == '+':
			return element1 + element2
		if monkey.operation == '*':
			return element1 * element2
		if monkey.operation == '-':
			return element1 - element2
		if monkey.operation == '/':
			return element1 // element2


if __name__ == '__main__':

	start_time = datetime.datetime.now()
	file = read_file('resources/testInput.txt')
	#print(file)
	print(go_through_monkeys(file))

	file = read_file('resources/input.txt')
	#print(file)
	print(go_through_monkeys(file))
	print(datetime.datetime.now() - start_time)
