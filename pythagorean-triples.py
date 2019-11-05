#! /usr/bin/env python3.6

## Find all pythagorean triples within a specified range of values

# 1) input a value, 'z'
# 2) find all pythagorean triples such that x^2 + y^2 = z^2, 0<=x<=z, 0<=y<=z
# 3) return the list of triples in ordered by increasing z, x, y
# 4) future development: include a lower bound for 'z' such that
#    z1<=x<=z2, z1<=y<=z2

# setup
import sys
import subprocess
import time

def get_bounds():
    """Ask user for an upper bound and returns a list containing an upper and lower bound"""
    lower_bound = 0
    upper_bound = input("Please enter a whole number: ")
    domain = [lower_bound, upper_bound]
    return domain


def find_triples(domain):
    """mathematical basis:
        pythagorean triples are tuples of whole numbers, (x, y, z) which satisfy the equation x^2 + y^2 = z^2.
        let z_lower-bound > zero (i.e. ignore trivial solution x = y = z = 0), then z_lower-bound <= z <= z_upper-bound is a set (i.e. list) of all pythagorean triples which satisfy z_lower-bound <= sqrt(x^2 + y^2) <= z_upper-bound.
        This implies that x^2 + y^2 >= (z_lower-bound)^2 AND x^2 + y^2 <= (z_upper-bound)^2. Which further implies that for x, y not equal to zero (further ignoring all trivial solutions of the form a^2 + 0^2 = z^2), we have that x, y > z_lower-bound AND x, y < z_upper-bound.
        Then we can incrementally look at the validity of solutions where we incrementally fix the independent variable (z) and one of the dependent variables while whe increment the other independent variable between the bounds."""
    if(domain.first < domain.last):
        #Obviously this cannot work with x,y restricted to be within the bounds of z because even for the elementary 5,4,3 tuple if you restricted 4<z<6 our tuple would be invalid; so the domains for x and y have to be any whole number between zero and z_upper-bound exclusive.
    
    for z in range(domain.first, domain.last):
        for x in range(domain.first + 1, domain.last - 1):
            for y in range(domain.first + 1, domain.last -1)
# verify import
print(sys.version_info)
time.sleep(0.5)

# initialize screen






# Begin Sandbox
Initialize_sandbox(name)

n = ""
while(n !=':q:'):
	n = input(":: ")
	if(n==':q:'):
		print("Goodbye!")
	elif(n==' '):
		Initialize_sandbox(name)
	else:
		print("   " + n)


#exit
subprocess.call("clear")
