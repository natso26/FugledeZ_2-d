'''This file has been changed in the following ways.

We enumerate subsets of size n in Z_2^d that contain
the d+1 fixed elements, n >= d+1.

If n >= d+4, then we call generate_sets_reduced from
the file generate.py. This function enumerates fewer
subsets than a naive enumeration but still yields correct
results for the checking of Fuglede's conjecture,
because the omitted subsets will be equivalent to
some subsets that are enumerated.

If n < d+4, then the mentioned function does not apply,
and we resort to naive enumeration. But there are not
very many subsets in this case anyway.
'''

import sys
from itertools import combinations

from prelim import dim, N, fixed_elts
import spectral_tile
from spectral_tile import is_spectral, is_tile
import clique

from generate import generate_sets_reduced

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

ans = {}
for x in [True, False]:
    for y in [True, False]:
        ans[(x, y)] = 0

counter_found = False
cnt = 0

def naive_generator(size):
    pool = [x for x in range(N) if x not in fixed_elts]
    
    for comb in combinations(pool, size-len(fixed_elts)):
        yield list(comb)
        
if size - len(fixed_elts) < 3:
    generator = naive_generator(size)
else:
    generator = generate_sets_reduced(size)
    
for comb in generator:
    cnt += 1

    if limit is not None and cnt > limit:
        print('\nStopping at case {}'.format(limit))
        break

    E = fixed_elts + comb
    
    if cnt % 10000 == 0:
        print('\nChecking case {}'.format(cnt))
        print('E = {}'.format(E))
    
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
