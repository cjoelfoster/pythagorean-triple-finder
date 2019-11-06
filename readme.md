# Pythagorean Triple Finder

Given a lower bound  (l) and an upper bound (u), find all pythagorean triples c^2 = a^2 + b^2 for a, b, c positive, non-zero integers with l < c < u.

## Mathematical basis

Given the equation
(1) c^2 = a^2 + b^2
for non-zero, positive integers a, b, and c, we can take the positive square root of both sides to solve for c in terms of a and b to get
(2) c = +sqrt(a^2 + b^2).
Now, assuming that a > c gives that a^2 > c^2 which implies that a^2 = c^2 + D where D is some unknown constant greater than zero. But this implies that c^2 = a^2 - D, or that b^2 = -D from (1). But we know that b is positive and non-zero which gives a contradiction. Next, assuming a = c gives a^2 = c^2, which implies from (1) that b^2 = 0. But b^2 can only be zero if b = 0 which leads to another contradiction. Thus a is strictly less than c. The same argument can be made for b; thus
(3) {c > a, and
    {c > b.
Also, because a and b are positive and non-zero, they must be bounded below by 0 exclusive (i.e. 0 < a < c < u, and 0 < b < c < u).
So, the range of a is (0:c), the range of b is (0:c), and the range of c is (l:u), where l < u; a, b, c, u are positive, non-zero integers; l is a non-negative integer.

Then, the set of pythagorean triples 'Py' bounded by l and u is the set of all tuples a,b,c such that a^2 + b^2 = c^2 with a, b, c, l, and u as defined above.

e.g. for l = 0, u = 5: Py = {}, and for l = 4, u = 6: Py = {(3,4,5), (4,3,5)}

Finally, because c^2 = a^2 + b^2 = b^2 + a^2; it suffices to find the set of solutions a < b < c because the other set of solutions b < a < c can be obtained by simply swapping a and b, without requiring computation. And for clarity, these should be the only solutions returned.

## Program outline

1. Launch: Clear the screen, introduce the user to the program, and explain how it functions
2. Ask the user for an upper and lower bound
3. Find all the pythagorean triples between the upper and lower bound
4. Display (graphically?) all the triples found for the user, or none if none were found
