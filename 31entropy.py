# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input
import sys
import math

box = []
for stuff in sys.argv[1:]:
	box.append(float(stuff))

assert(math.isclose(sum(box), 1.0))

summ = 0
for freq in box:
	summ += -(freq * math.log2(freq))
print('{:.4}'.format(summ))

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
