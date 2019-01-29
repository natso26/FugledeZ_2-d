'''The change in this file is the addition of a new
precomputed list, sum_rows_fixed_elts.

See explanations for its role in the file spectral_tile.py
'''

import sys

if len(sys.argv) > 1:
    dim = int(sys.argv[1])
else:
    dim = int(input('Input dimension: '))
N = pow(2, dim)

def bitget(n, pos):
    return (n >> pos) & 1

def entry(m, n):
    if sum(bitget(m, i) * bitget(n,  i) for i in range(dim)) % 2 == 0:
        return 1
    else:
        return -1

eval_matrix = [[entry(i, j) for j in range(N)] for i in range(N)]

fixed_elts = [0] + [pow(2, i) for i in range(dim)]

# The new precomputed list
sum_rows_fixed_elts = [sum(eval_matrix[x][i] for x in fixed_elts) for i in range(N)]
