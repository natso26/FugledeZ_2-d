'''This file has been changed in the following ways.

1. The functions is_spectral and is_tile now call clique_exists_helper
   directly instead of clique_exists. Moreover, the "graph" input
   of that function is now a list of N integers instead of an NxN
   matrix of integers.

   See the file clique.py for more information on these changes.

2. It was found that the computations of which nodes are adjacent
   to node 0 are major bottlenecks. Therefore, the corresponding
   pieces of code have been extensively rewritten. (They still are
   major bottlenecks, as the percentages below show.)
   
   Details on these implementations are in the comments below.

In this fast version, the functions is_spectral and is_tile,
excluding calls to clique_exists_helper, account for 48% and 26%
of the total runtime, respectively.
'''

from prelim import dim, N, eval_matrix, sum_rows_fixed_elts
from clique import clique_exists_helper
import clique

quiet = False
    
def is_spectral(E):
    if len(E) % 2 != 0:
        return False

    if not quiet:
        print()

    '''This part computes which nodes are adjacent to node 0.

    First, node i is adjacent to node 0 if and only if the sum
    of entries of the evaluation matrix in column i and rows x
    for all elements x of E is zero.

    Thus, we go through every column and sum up entries in the
    relevant rows. To make the computation faster, we notice that
    E consists of 7 fixed elements and 9 other elements. So we
    precompute the sum of the rows corresponding to the fixed
    elements and only iterate over the remaining 9 elements.

    This increases the efficiency because the two lines of the
    inner loop that sum these elements, indicated below, take
    up most of the computation time for this block of code.
    '''
    Erest = E[dim+1:]
    
    is_ortho_to_0 = [0] * N
    for i in range(N):
        row = eval_matrix[i]
        cnt = sum_rows_fixed_elts[i]
        '''These two lines take up most of the computation time.'''
        for x in Erest:
            cnt += row[x]
        '''End of two lines'''
        if cnt == 0:
            is_ortho_to_0[i] = 1
 
    candidates = [x for x in range(N) if is_ortho_to_0[x]]
    '''End of part'''
    
    clique.cnt = 0
    
    return clique_exists_helper(is_ortho_to_0, len(E)-1, candidates)

def is_tile(E):
    if N % len(E) != 0:
        return False

    if not quiet:
        print()

    '''This part computes which nodes are adjacent to node 0.
    That is, we want to know which translates of E do not overlap
    with E.

    It was found that the most efficient way is to iterate over
    pairs of elements of E, instead of interating over the translates.
    For each x, y in E, the translate of E by x-y must overlap with E,
    and can be marked as such. The remaining translates that are
    not marked do not overlap with E.

    This is efficient because iterating over pairs of elements
    of E means 16C2 = 120 inner loops to go through, while iterating
    over translates of E and checking whether each of their elements
    is in E take 64*16 = 1024 inner loops.
    '''
    is_nonoverlap_with_0 = [0] + [1] * (N-1)

    n = len(E)
    for i in range(n-1):
        for j in range(i+1, n):
            is_nonoverlap_with_0[E[i] ^ E[j]] = 0

    candidates = [x for x in range(N) if is_nonoverlap_with_0[x]]
    '''End of part'''
    
    clique.cnt = 0
    
    return clique_exists_helper(is_nonoverlap_with_0, (N // len(E))-1, candidates)
