# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list
import sys
import math
box = []
for stuff in sys.argv[1:]:
	box.append(int(stuff))

days = box[0]
people = box[1]

probability = 1
for sims in range (people):
	probability *= (days - sims) / days
probability = 1 - probability
print('{:.4}'.format(probability))
"""
python3 33birthday.py 365 23
0.571
"""

