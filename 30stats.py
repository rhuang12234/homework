# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys
import sys

container = []
for stuff in sys.argv[1:]:
	container.append(float(stuff))

count = len(container)
print('Count:', count)

minimum = container[0]
maximum = container[0]
for numbers in container:
	if numbers < minimum:
		minimum = numbers
	if numbers > maximum:
		maximum = numbers
print('Maximum:', maximum)
print('Minimum', minimum)

sum = 0
for i in container:
	sum += i
	mean = sum / len(container)
print('Mean', '{:.2}'.format(mean))

differenceSquares = []
for values in container:
	differenceSquares.append((values-mean) ** 2)
variance = 0
for differences in differenceSquares:
	variance += differences
variance = variance / len(container)
standardeviation = variance ** 0.5
print('Standard Deviation:','{:.2}'.format(standardeviation))

median = (len(container) + 1) / 2
print('Median:', median)
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
