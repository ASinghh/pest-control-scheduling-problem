# pest-control-scheduling-problem

This a an example of simulative solution to a schedulling problem. Instead of formulating the problem as a CONSTRAINT PROGRAMMING or a SEARCH problem, I model it as a CURSOR in a uni-directional, finite horizon problem with optamility constraints beign applied to each descrete movement in time.

The constraints are defined in the Problem Statement, defined in the PDF file.

Each Discrete step is one day long.

This method is not the most computationally efficient one, but is the most general one. It is independent of any optimization process that 

might be required for solving the problem formulated using CONSTRAINT PROGRAMMING.

This Method converges to optimal strategy every single time, and in my limited testing, has proven to be equally efficient to CONSTRAINT PROGRAMMING .
