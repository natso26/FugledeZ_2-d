'''This file checks Fuglede's conjecture for all subsets of Z_2^d
of a given size n, which do not lie in any hyperplane.

Beware that this task might not be computationally feasible
if the number of possible subsets is too large.
By invariance under affine transformations, we can fix the first
d+1 elements as
(0,0,...,0), (1,0,...,0), (0,1,...,0), ..., (0,0,...,1).
So the number of subsets to check is (2^d-d-1)C(n-d-1).
'''

import sys
from itertools import combinations

from prelim import dim, N, fixed_elts
import spectral_tile
from spectral_tile import is_spectral, is_tile
import clique

spectral_tile.quiet = True
clique.quiet = True

if len(sys.argv) > 2:
    size = int(sys.argv[2])
else:
    size = int(input('Input size of sets: '))

if len(sys.argv) > 3:
    limit = int(sys.argv[3])
else:
    limit = None
    
pool = [x for x in range(N) if x not in fixed_elts]

ans = {}
for x in [True, False]:
    for y in [True, False]:
        ans[(x, y)] = 0

counter_found = False
cnt = 0

for comb in combinations(pool, size-len(fixed_elts)):
    cnt += 1

    if limit is not None and cnt > limit:
        print('\nStopping at case {}'.format(limit))
        break
        
    if cnt % 100 == 0:
        print('\nChecking case {}'.format(cnt))
    
    E = fixed_elts + list(comb)
    spec_ans = is_spectral(E)
    tile_ans = is_tile(E)
    ans[(spec_ans, tile_ans)] += 1

    if spec_ans != tile_ans:
        print('\nCounterexample found:')
        print(' '.join(format(x, '0'+str(dim)+'b') for x in E))
        if spec_ans:
            print('\nIt IS a spectral set.')
        else:
            print('\nIt IS NOT a spectral set.')
        if tile_ans:
            print('It IS a tile.')
        else:
            print('It IS NOT a tile.')
        counter_found = True

print('\nResults')
print('IS  spectral & IS  Tile:', ans[(True, True)])
print('IS  spectral & NOT Tile:', ans[(True, False)])
print('NOT spectral & IS  Tile:', ans[(False, True)])
print('NOT spectral & NOT Tile:', ans[(False, False)])

if limit is None:
    print(('\nFuglede\'s conjecture is {} for sets of size {} in Z_2^{}' +
           '\nwhich do not lie in any hyperplane') \
          .format(str(not counter_found).upper(), size, dim))
