# Pythagorean Triple Finder

Given a lower bound  *l* and an upper bound *u*, find all pythagorean triples (*a*, *b*, *c*) where *a* &lt; *b* &lt; *c* that satisfy *c*<sup>2</sup> = *a*<sup>2</sup> + *b*<sup>2</sup> for *a*, *b*, *c* positive, non-zero integers with *l* &lt; *c* &lt; *u*.

## Mathematical basis

Given the equation

*(1)* *c*<sup>2</sup> = *a*<sup>2</sup> + *b*<sup>2</sup>

for non-zero, positive integers *a*, *b*, and *c*, we can take the positive square root of both sides to solve for *c* in terms of *a* and *b* to get

*(2)* *c* = +&radic;(*a*<sup>2</sup> + *b*<sup>2</sup>).

Now, assuming that *a* &gt; *c* gives that *a*<sup>2</sup> &gt; *c*<sup>2</sup>, which implies that *a*<sup>2</sup> = *c*<sup>2</sup> + *D* where *D* is some unknown constant greater than zero. But this implies that *c*<sup>2</sup> = *a*<sup>2</sup> - *D*, or that *b*<sup>2</sup> = -*D* from *(1)*. But we know that *b* is a positive, non-zero integer which gives a contradiction.

Next, assuming *a* = *c* gives *a*<sup>2</sup> = *c*<sup>2</sup>, which implies from *(1)* that *b*<sup>2</sup> = 0. But *b*<sup>2</sup> can only be zero if *b* = 0 which leads to another contradiction. Thus *a* is strictly less than *c*. The same argument can be made for *b*; therefore *c* > *a*, and *c* > *b*.
      
Also, because *a* and *b* are positive and non-zero, they must be bounded below by 0.

So,
* 0 &lt; *a* &lt; c,
* 0 &lt; *b* &lt; *c*, and
* *l* &lt; *c* &lt; *u*, where *l* < *u*, and
* *a*, *b*, *c*, *u* are positive, non-zero integers;
* *l* is a non-negative integer.

Then, the set of pythagorean triples *P<sub>y</sub>* bounded by *l* and *u* is the set of all tuples (*a*,*b*,*c*) such that *c*<sup>2</sup> = *a*<sup>2</sup> + *b*<sup>2</sup>  with *a*, *b*, *c*, *l*, and *u* as defined above. (e.g. for *l* = 0, *u* = 5: *P<sub>y</sub>* = {}, and for *l* = 4, *u* = 6: *P<sub>y</sub>* = {(3,4,5), (4,3,5)})

Finally, because *c*<sup>2</sup> = *a*<sup>2</sup> + *b*<sup>2</sup> = *b*<sup>2</sup> + *a*<sup>2</sup>; it suffices to find the set of solutions (*a*,*b*,*c*) with *a* &lt; *b* &lt; *c* because the other set of solutions (*b*,*a*,*c*) can be obtained by simply swapping *a* and *b*, without requiring computation. Thus, for this program, only solutions where *a* &lt; *b* &lt; *c* should be returned.

## Program outline

1. ~~Launch: Clear the screen, introduce the user to the program, and explain how it functions~~
2. Ask the user for an upper and lower bound
3. Find all the pythagorean triples between the upper and lower bound
4. Return a list of the pythagorean triples with *a* &lt; *b* &lt; *c*, or return none if none were found.

## Future development

1. Make the program function in a loop so you don't have to launch it each time
2. Set up the environment for the program and provide commands for modifying the environment (e.g. start over, quit, clear screen, change bounds, etc.)
3. Display the results graphically (on a scatter-plot?), or some 2-D image of the results to help with visualization
4. Develop unit tests for each piece of the code
