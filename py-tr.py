#! /usr/bin/env python3.6

## Find all pythagorean triples within a specified range of values
# setup
import sys
import subprocess
import time

# verify import
print(sys.version_info)
time.sleep(0.5)

# initialize screen
subprocess.call("clear")
print("Pythagorean Triple Finder")

# get bounds
lower = int(input("Please enter an non-negative integer for a lower bound: "))
upper = int(input("Please enter a positive, non-zero integer for an upper bound: "))

Py = []

# find triples
for c in range(lower, upper):
    for b in range(1, c):
        for a in range(1, b):
            if(c^2 == (a^2 + b^2)):
                Py.append((a,b,c))
                print(a, b, c)
            else:
                print(".")


print(Py)
