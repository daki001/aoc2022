import re
import datetime
def read_file(path):
	beacons = list()
	sensors = dict()
	with open(path) as f:
		for line in f:
			line = line.strip()
			matcher = re.match('Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)', line)
			if matcher:
				beac = [int(matcher.group(3)), int(matcher.group(4))]
				sensors[matcher.group(1) + ' ' + matcher.group(2)] = beac
				if beac not in beacons:
					beacons.append(beac)
			else:
				print('HAYA')
	return [sensors, beacons]


def calculate_covered_space(sensors, row, max_distance):


	covered = list()
	for key in sensors.keys():
		s = [int(key.split(' ')[0]), int(key.split(' ')[1])]
		if row - max_distance <= s[1] <= row + max_distance:
			manhatten = calculate_manhatten_distance(s, sensors[key], row)
			for i in manhatten:
				if i not in covered:
					covered.append(i)
	coords = list()
	#print('here')
	#print(covered)
	oldlength = len(covered) + 1
	newlength = len(covered)
	covered_copy = covered.copy()
	while oldlength != newlength:
		oldlength = len(covered)
		new_covered = list()
		used = list()
		for element in range(len(covered)):
			for element2 in range(element + 1, len(covered)):
				if element not in used and element2 not in used:
					r = compare_ranges(covered[element], covered[element2])
					if len(r) == 1:
						used.append(element)
						used.append(element2)
						for e in r:
							if e not in new_covered:
								new_covered.append(e)
						break
			if element not in used:
				new_covered.append(covered[element])
		if len(new_covered) == 0:
			new_covered = covered
		covered = new_covered
		newlength = len(covered)
		#print(covered)

	count = 0
	#print(covered)
	if len(covered) > 1:
		print(covered_copy)
		print(covered)
		print(row)
		print(max(covered[0][0], covered[1][0]) - 1)
		print((max(covered[0][0], covered[1][0]) - 1) * 4000000 + row)
		return (max(covered[0][0], covered[1][0]) - 1) * 4000000 + row
	return -1


def compare_ranges(range1, range2):
	#print(range1)
	#print(range2)
	if range1[0] > range2[1] + 1 or range1[1] < range2[0] - 1:
		return [range1, range2]
	return [[min([range1[0], range2[0]]), max(range1[1], range2[1])]]


def calculate_manhatten_distance(sensor, beacon, row):
	distance = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
	x_cord = sensor[0]
	y_cord = sensor[1]
	coords = list()
	if abs(row - sensor[1]) <= distance:
		i = distance - abs(row - sensor[1])
	#for i in range(distance + 1):
		if y_cord + (distance - i) == row:
			if x_cord - i < 4000001 and x_cord + 1 > -1:
				coords.append([max(x_cord - i, 0), min(x_cord + i, 4000000)])
		elif y_cord - (distance - i) == row:
			if x_cord - i < 4000001 and x_cord + 1 > -1:
				coords.append([max(x_cord - i, 0), min(x_cord + i, 4000000)])

	return coords


def calculate_all_rows(file):
	max_distance = 0
	for sens in file[0].keys():
		s = [int(sens.split(' ')[0]), int(sens.split(' ')[1])]
		max_distance = max(max_distance, abs(file[0][sens][0] - s[0]) + abs(file[0][sens][1] - s[1]))
	for i in range(0, 4000001):
		if i % 100000 == 0:
			print(i)
		num = calculate_covered_space(file[0], i, max_distance)
		if num != -1:
			return num


if __name__ == '__main__':
	start = datetime.datetime.now()
	file = read_file('resources/testInput.txt')
	print(file)
	#print(calculate_covered_space(file[0], file[1], 10))





	file = read_file('resources/input.txt')
	print(file)
	print(calculate_all_rows(file))
	print(datetime.datetime.now() - start)
	#print(2423862 + 951857 * 4000000)
	#2423862
#951857
#3807430423862
	#print(calculate_covered_space(file[0], file[1], 2000000))

