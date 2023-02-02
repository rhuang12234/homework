# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library
n= 10
sum = 0
fact = 1
for num  in range(1, n+1, 1):
	sum += num
	fact *= num
print(n, sum, fact)


"""
python3 22sumfac.py
5 15 120
"""
