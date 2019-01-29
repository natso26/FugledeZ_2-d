'''This file reads multiple files containing matrices of
a given size from Neil Sloane's webpage.

For example, if the dimension is 24 x 24 and the number
of matrices is 60, the program will read the files:

had.24.1.txt, had.24.2.txt, ..., had.24.60.txt.
'''

import urllib.request
from matrix_rank import get_rank_from_file
import matrix_rank

matrix_rank.quiet = True

neil_sloane_url = 'http://neilsloane.com/hadamard/{}.txt'

while True:
    size = int(input('\n\nInput matrix size: '))
    number = int(input('Input number of matrices: '))

    print()

    rank_dict = {}
    
    for i in range(1, number+1):
        file_name = 'had.{}.{}'.format(size, i)
        s = neil_sloane_url.format(file_name)

        print('Looking at {}'.format(file_name))
        
        with urllib.request.urlopen(s) as response:
            contents = response.read().decode('ascii')

        dim, rank = get_rank_from_file(contents)

        if dim != size:
            raise ValueError('The matrix does not have the correct dimensions.')

        print('Rank: {}'.format(rank))
        
        if rank not in rank_dict:
            rank_dict[rank] = 1
        else:
            rank_dict[rank] += 1

    print('\nResults')
    print('Rank Number')
    for rank in sorted(rank_dict):
        print('{:<4} {}'.format(rank, rank_dict[rank]))
