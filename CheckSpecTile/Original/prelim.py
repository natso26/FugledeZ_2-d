'''Preliminary computation in Z_2^d.

Elments of Z_2^d are represented by nonnegative integers
by putting coordinates in bits in the natural way, as follows.
Suppose d = 5. Then (1,0,0,1,0) is represented by 10010 in
base 2, which is 18.

Let N=2^d. The evaluation matrix is an NxN matrix whose
(m, n) entry is as follows. Suppose m corresponds to the
element (x_1,...,x_d) of Z_2^d and n corresponds to the
element (y_1,...,y_d) of Z_2^d. Define the inner product
of m and n to be <m,n> = x_1*y_1 + ... + x_d*y_d.
Then the (m, n) entry is exp(2*pi*i*<m,n>/2).
In other words, it is 1 if <m,n> is even and -1 otherwise.
'''

import sys

if len(sys.argv) > 1:
    dim = int(sys.argv[1])
else:
    dim = int(input('Input dimension: '))
N = pow(2, dim)

# Get the bit at position pos from the left of an integer n.
def bitget(n, pos):
    return (n >> pos) & 1

# The (m, n) entry of the evaluation matrix.
def entry(m, n):
    if sum(bitget(m, i) * bitget(n,  i) for i in range(dim)) % 2 == 0:
        return 1
    else:
        return -1

# The evaluation matrix.
eval_matrix = [[entry(i, j) for j in range(N)] for i in range(N)]

# The set consisting of d+1 elements
# (0,0,...,0), (1,0,...,0), (0,1,...,0), ... ,(0,0,...,1).
fixed_elts = [0] + [pow(2, i) for i in range(dim)]
