'''Check whether a subset of Z_2^d is a spectral set or a tile.

Input
E: The subset in question. It should be given by a list of nonnegative
integers, whose binary expansions correspond to elements of Z_2^d
in the natural way.
'''

from prelim import N, eval_matrix
from clique import clique_exists

quiet = False
    
'''Check whether a set E is a spectral set.

This works as follows.
A set E is a spectral set if and only if the evaluation matrix,
with rows restricted to elements of E, has |E| orthogonal columns.
Now construct a graph G with columns of the evaluation matrix as nodes
and two nodes are adjacent if they are orthogonal in the above sense.
Then, E is spectral if and only if G has an |E|-clique.

To reduce the amount of work, by translational invariance, we can assume
that column 0 is in the clique.
(In fact, by this argument, G is always a regular graph.)

The algorithm is as follows.
1. Construct the graph G as above, represented by its adjacency matrix.
2. Check whether there is an |E|-clique in G that contains 0.
'''
def is_spectral(E):
    def is_col_ortho(m, n):
        return int(sum(eval_matrix[x][m] * eval_matrix[x][n] for x in E) == 0)
    
    adj_matrix = [[is_col_ortho(i, j) for j in range(N)] for i in range(N)]
    
    return clique_exists(adj_matrix, len(E), [0])

'''Check whether a set E is a tile.

This works as follows.
First, in order for E to be a tile, its size must divide N=2^d.
Given that this is true, E is a tile if and only if there are N/|E|
nonoverlapping translational copies of E. Now construct a graph G
whose nodes are translational copies of E and two nodes are adjacent
if they are nonoverlapping. Then, E is a tile if and only if G
has an (N/|E|)-clique.

As in the above function, we can assume that the original copy is in
the clique.

The algorithm is as follows.
1. If the size of E does not divide N, return False.
2. Construct the graph G as above, represented by its adjacency matrix.
   Notice that in Z_2^d, where elements are represented by integers
   as mentioned, translation can be achieved by using bitwise XOR (^).
3. Check whether there is an (N/|E|)-clique in G that contains 0.
'''
def is_tile(E):
    if N % len(E) != 0:
        return False

    if not quiet:
        print()
    
    def is_nonoverlap(m, n):
        return int(not bool(set(x ^ m for x in E) & set(x ^ n for x in E)))

    adj_matrix = [[is_nonoverlap(i, j) for j in range(N)] for i in range(N)]
    
    return clique_exists(adj_matrix, N // len(E), [0])
