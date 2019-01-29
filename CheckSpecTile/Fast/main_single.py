'''There is no significant change to this file.'''

from prelim import dim, N, fixed_elts
from spectral_tile import is_spectral, is_tile

def parse_input(inp):
    return [int(x, base=2) for x in inp.split()]

while True:
    try:
        inp = parse_input(input('\n\nInput set:\n'))
    except:
        print('Cannot parse input. Please try again.')
        continue

    if any(x < 0 or x >= N for x in inp):
        print('Some elements are out of range. Please try again.')
        continue
    
    E = fixed_elts + inp
    
    print('\nThe set E consists of:')
    print(' '.join(format(x, '0'+str(dim)+'b') for x in E))

    if len(set(E)) != len(E):
        print('There are some duplicate elements. Please try again.')
        continue
    
    print('It has size {}.'.format(len(E)))

    print('\nChecking whether E is a spectral set...')
    spec_ans = is_spectral(E)
    if spec_ans:
        print('\nE IS a spectral set.')
    else:
        print('\nE IS NOT a spectral set.')
    
    print('\nChecking whether E is a tile...')
    tile_ans = is_tile(E)
    if tile_ans:
        print('\nE IS a tile.')
    else:
        print('\nE IS NOT a tile.')
    
    if spec_ans == tile_ans:
        print('\nFuglede\'s conjecture is TRUE for E.')
    else:
        print('\nFuglede\'s conjecture is FALSE for E.')
