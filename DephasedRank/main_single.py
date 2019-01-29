'''This file reads a single file from Neil Sloane's webpage.

Input file names without .txt. For example,
to read http://neilsloane.com/hadamard/had.16.4.txt, type:

had.16.4
'''

import urllib.request
from matrix_rank import get_rank_from_file

neil_sloane_url = 'http://neilsloane.com/hadamard/{}.txt'

while True:
    try:
        name = input('\n\nInput file name (without .txt): ')
        s = neil_sloane_url.format(name)
        with urllib.request.urlopen(s) as response:
            contents = response.read().decode('ascii')
    except:
        print('\nSomething is wrong. Maybe the file name is misspelled.')
        continue

    print('\nFetched file as:\n')
    print(contents)
    
    get_rank_from_file(contents)
    

