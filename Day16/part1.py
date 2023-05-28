import datetime
import re


class Cave:

	def __init__(self, name: str, pressure: int):
		self.name = name
		self.pressure = pressure
		self.neighbors = list()
		self.neighbor_objects = list()

	def set_neighbors(self, neighbors):
		self.neighbors = neighbors.copy()

	def set_neighbor(self, neighbor):
		self.neighbors.append(neighbor)

	def get_neighbors(self):
		return self.neighbors.copy()

	def set_neighbor_objects(self, all_nodes):
		#print(self.neighbors)
		for element in all_nodes:
			#print(element.name)
			if element.name in self.neighbors:
				self.neighbor_objects.append(element)

	def __str__(self):
		return self.name + ';' + str(self.pressure) + ';' + str(self.neighbors)

	def __eq__(self, other):
		if type(other) == Cave:
			return self.name == other.name
		return False

	def __hash__(self):
		return hash(self.name)

def read_file(path):
	caves = list()
	with open(path) as f:
		for line in f:
			line = line.strip()
			matcher = re.match('Valve ([A-Z]+) has flow rate=(\\d+); tunnels lead to valves(( [A-Z]+,?)+)', line)
			if matcher:
				new_cave = Cave(matcher.group(1), int(matcher.group(2)))
				new_cave.set_neighbors(matcher.group(3)[1:].split(', '))
				caves.append(new_cave)
			else:
				matcher = re.match('Valve ([A-Z]+) has flow rate=(\\d+); tunnel leads to valve(( [A-Z]+,?)+)', line)
				if matcher:
					new_cave = Cave(matcher.group(1), int(matcher.group(2)))
					new_cave.set_neighbors(matcher.group(3)[1:].split(', '))
					caves.append(new_cave)
		for cave in caves:
			cave.set_neighbor_objects(caves)
	return caves

def find_path(cave1: Cave, used):
	next_el = list()
	result = dict()
	next_el.extend(cave1.neighbor_objects)
	step_count = [1 for _ in range(len(next_el))]
	steps = [[cave1] for _ in range(len(next_el))]
	visited = dict()
	visited[cave1] = []
	while True:
		#print([x.name for x in next_el])
		next_step_index = step_count.index(min(step_count))
		next_step_count = step_count[next_step_index]
		next_step_object = next_el[next_step_index]
		next_step_history = steps[next_step_index]
		next_el.pop(next_step_index)
		steps.pop(next_step_index)
		step_count.pop(next_step_index)
		next_step_history.append(next_step_object)
		visited[next_step_object] = next_step_history.copy()
		if next_step_object.pressure > 0 and next_step_object not in used:
			result[next_step_object] = next_step_history.copy()
		for neigh in next_step_object.neighbor_objects:
			if neigh not in visited:
				if neigh in next_el:
					if next_step_count < step_count[next_el.index(neigh)]:
						step_count[next_el.index(neigh)] = next_step_count + 1
						steps[next_el.index(neigh)] = next_step_history.copy()
				else:
					next_el.append(neigh)
					step_count.append(next_step_count + 1)
					steps.append(next_step_history.copy())

		if len(next_el) == 0:
			return result


def bruteforce(minutes, score, round_score, current: Cave, max_value, used, next_cave, path, bs):
	if minutes < 0:
		score -= round_score * abs(minutes)
		minutes = 0
	if minutes == 0:
		return score
	if bs - max_value * minutes > score:
		return 0

	if round_score != max_value:
		best_score = score
		if next_cave is None:
			paths = find_path(current, used)
			for goal, p in paths.items():
				path.append(goal)
				best_score = max(best_score, bruteforce(minutes - len(p) + 1, score + round_score * (len(p) - 1), round_score, goal, max_value, used.copy(), goal, path, best_score))
				path.pop(len(path) - 1)
			return best_score
		else:

			used.append(current)
			score += round_score
			round_score += current.pressure
			minutes -= 1
			return bruteforce(minutes, score, round_score, current, max_value, used.copy(), None, path, bs)


	else:
		return score + round_score * minutes



if __name__ == '__main__':

	start_time = datetime.datetime.now()
	file = read_file('resources/testInput.txt')
	start = ''
	for element in file:
		if element.name == 'AA':
			start = element


	print(bruteforce(30, 0, 0, start, sum([c.pressure for c in file]), [], None, [], 0))
	# print(calculate_covered_space(file[0], file[1], 10))

	file = read_file('resources/input.txt')
	for element in file:
		if element.name == 'AA':
			start = element


	print(bruteforce(30, 0, 0, start, sum([c.pressure for c in file]), [], None, [], 0))
	#print(file)
	# print(calculate_covered_space(file[0], file[1], 2000000))
	print(datetime.datetime.now() - start_time)

"""if current.pressure == 0:
	paths = find_path(current, used)
	for element in paths:
		if len(previous) == 0 or element != previous[len(previous) - 1]:
			previous.append(current)
			best_score = max(best_score,
							 bruteforce(minutes - 1, score, round_score, element, previous, max_value, used))
			previous.pop(previous[len(previous) - 1])
else:
	for element in current.neighbor_objects:
		if element != previous:
			if len(previous) == 0 or element != previous[len(previous) - 1]:
				previous.append(current)
				best_score = max(best_score,
								 bruteforce(minutes - 1, score, round_score, element, previous, max_value, used))
				previous.pop(previous[len(previous) - 1])

	used.append(current)
	score += round_score
	round_score += current.pressure
	minutes -= 1

	for element in current.neighbor_objects:
		previous.append(current)
		best_score = max(best_score,
						 bruteforce(minutes - 1, score, round_score, element, previous, max_value, used))
		previous.pop(previous[len(previous) - 1])
	used.pop(len(used) - 1)
	return best_score"""

