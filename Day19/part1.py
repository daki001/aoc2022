import datetime
import re


class Robots:
	def __init__(self, ore):
		self.ore_needed = ore

	def __str__(self):
		return 'Robot needs ' + str(self.ore_needed) + ' ores'


class ClayRobots(Robots):
	def __init__(self, ore):
		super().__init__(ore)

	def __str__(self):
		return 'ClayRobot needs ' + str(self.ore_needed) + ' ores'


class OreRobots(Robots):
	def __init__(self, ore):
		super().__init__(ore)

	def __str__(self):
		return 'OreRobot needs ' + str(self.ore_needed) + ' ores'


class ObsidianRobots(Robots):

	def __init__(self, ore, clay):
		super().__init__(ore)
		self.clay_needed = clay

	def __str__(self):
		return 'ObsidianRobot needs ' + str(self.ore_needed) + ' ores and ' + str(self.clay_needed) + ' clays'


class GeodeRobots(Robots):
	def __init__(self, ore, obsidian):
		super().__init__(ore)
		self.obsidian_needed = obsidian

	def __str__(self):
		return 'GeodeRobot needs ' + str(self.ore_needed) + ' ores and ' + str(self.obsidian_needed) + ' obsidian'


def read_file(path):
	blueprints = dict()
	with open(path) as f:
		for line in f:
			line = line.strip()
			matcher = re.match(
				'Blueprint (\\d+): Each ore robot costs (\\d+) ore\\. Each clay robot costs (\\d+) ore\\. Each obsidian robot costs (\\d+) ore and (\\d+) clay\\. Each geode robot costs (\\d+) ore and (\\d+) obsidian\\.',
				line)
			if matcher:
				ore_robot = OreRobots(int(matcher.group(2)))
				clay_robot = ClayRobots(int(matcher.group(3)))
				obsidian_robot = ObsidianRobots(int(matcher.group(4)), int(matcher.group(5)))
				geode_robot = GeodeRobots(int(matcher.group(6)), int(matcher.group(7)))
				blueprints[int(matcher.group(1))] = [ore_robot, clay_robot, obsidian_robot, geode_robot]

	return blueprints


def check_is_stock_possible(robot, stock):
	result = stock[0] >= robot.ore_needed
	if type(robot) == ObsidianRobots:
		result = result and stock[1] >= robot.clay_needed
	if type(robot) == GeodeRobots:
		result = result and stock[2] >= robot.obsidian_needed

	return result


def mine_robots(stock, robots):
	for r in range(len(robots)):
		stock[r] += robots[r]
	return stock


def find_best_way(minutes, blueprint, stock, robots, next_product):
	if minutes == 0:
		return stock[3]
	max_result = 0
	if next_product is None:
		#print(minutes)
		for element in blueprint:
			if type(element) is ObsidianRobots and robots[1] == 0:
				continue
			if type(element) is GeodeRobots and robots[2] == 0:
				continue
			next_product = element

			new_stock = stock.copy()
			if check_is_stock_possible(next_product, stock):
				new_robots = robots.copy()
				new_stock[0] -= next_product.ore_needed

				if type(next_product) == ObsidianRobots:
					new_stock[1] -= next_product.clay_needed
				if type(next_product) == GeodeRobots:
					new_stock[2] -= next_product.obsidian_needed

				mine_robots(new_stock, robots)

				if type(next_product) == OreRobots:
					new_robots[0] += 1
				if type(next_product) == ClayRobots:
					new_robots[1] += 1
				if type(next_product) == ObsidianRobots:
					new_robots[2] += 1
				if type(next_product) == GeodeRobots:
					new_robots[3] += 1
				max_result = max(max_result, find_best_way(minutes - 1, blueprint, new_stock, new_robots, None))
			else:
				mine_robots(new_stock, robots)
				max_result = max(max_result, find_best_way(minutes - 1, blueprint, new_stock, robots, next_product))
	else:
		if check_is_stock_possible(next_product, stock):
			stock[0] -= next_product.ore_needed

			if type(next_product) == ObsidianRobots:
				stock[1] -= next_product.clay_needed
			if type(next_product) == GeodeRobots:
				stock[2] -= next_product.obsidian_needed

			mine_robots(stock, robots)

			if type(next_product) == OreRobots:
				robots[0] += 1
			if type(next_product) == ClayRobots:
				robots[1] += 1
			if type(next_product) == ObsidianRobots:
				robots[2] += 1
			if type(next_product) == GeodeRobots:
				robots[3] += 1
			return find_best_way(minutes - 1, blueprint, stock, robots, None)
		else:
			mine_robots(stock, robots)
			return find_best_way(minutes - 1, blueprint, stock, robots, next_product)
	return max_result


def print_blueprint(all_blueprints):
	for blueprint in all_blueprints.keys():
		print('Blueprint ' + str(blueprint))
		for element in all_blueprints[blueprint]:
			print(str(element))
		print()


if __name__ == '__main__':

	start_time = datetime.datetime.now()
	file = read_file('resources/testInput.txt')
	print_blueprint(file)
	for f in file.values():
		print(find_best_way(24, f, [0, 0, 0, 0], [1, 0, 0, 0], None))

	file = read_file('resources/input.txt')
	print(file)
	print(datetime.datetime.now() - start_time)
