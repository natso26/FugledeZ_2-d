'''This file provides the function get_rank_from_file, which reads
contents from a file, extracts a square matrix, dephases the matrix,
and computes its rank in Z_2.

Input
contents: the string containing the contents of a file

Output
The tuple (dim, rank), where the matrix read is of dimensions
dim x dim, and, after being dephased, has rank rank in Z_2.

Running this file directly brings up test mode.


The implmentation details are as follows.

1. Extracting the square matrix from the file.

   First, we parse a '+' as 0 and a '-' as 1. A line in the
   file is read as a row of a matrix. Any line which is empty or
   which contains any character other than '+' and '-' is ignored.
   Finally, we check that the matrix is nonempty and is square.
   If this is true, we return the matrix.

   Otherwise, we repeat the process but parse a '0' as 0 and a
   '1' as 1. (Some files are encoded using '+' and '-', and some
   files '0' and '1', so we must try to parse the file both ways.)

   If both ways fail, then an error is raised.

   This is implemented in the function parse_file.
   
2. Dephasing the matrix just read.

   This means the following. For a matrix of 0's and 1's, the
   operation of flipping a row or a column is to change a 0 to a 1
   and a 1 to a 0 within that row or column.
   
   To dephase a matrix is to apply the flipping operations to
   rows and columns to make all entries in the first row and the
   first column zero.

   This is implemented in the function dephase_matrix.

3. Computing the rank of the dephased matrix in Z_2.

   This is done using MATLAB's function gfrank.
'''

if __name__ == "__main__":
    test_mode = True
else:
    test_mode = False

if not test_mode:    
    print('Starting MATLAB engine. Please wait...')
    import matlab.engine
    eng = matlab.engine.start_matlab()

quiet = False

def print_matrix(m):
    '''
    >>> print_matrix([[0,1,0],[1,1,0],[1,0,1]])
    0 1 0
    1 1 0
    1 0 1
    '''
    print('\n'.join(' '.join(str(x) for x in row) for row in m))

def dephase_matrix(m):
    '''
    >>> print_matrix(dephase_matrix([[0,1,0],[1,1,0],[1,0,0]]))
    0 0 0
    0 1 1
    0 0 1
    '''
    for i in range(len(m)):
        if m[i][0] == 1:
            for j in range(len(m)):
                m[i][j] = 1 - m[i][j]

    for j in range(len(m)):
        if m[0][j] == 1:
            for i in range(len(m)):
                m[i][j] = 1 - m[i][j]
    return m

def parse_file(contents):
    '''
    >>> print_matrix(parse_file('+-+\\n---\\n-++'))
    0 1 0
    1 1 1
    1 0 0
    >>> print_matrix(parse_file('+-+\\n---\\n\\n\\n--a\\n-++'))
    0 1 0
    1 1 1
    1 0 0
    >>> print_matrix(parse_file('001\\n110\\n010'))
    0 0 1
    1 1 0
    0 1 0
    >>> print_matrix(parse_file('001\\n110\\n--\\n010\\n\\n+'))
    0 0 1
    1 1 0
    0 1 0
    >>> print_matrix(parse_file('001\\n110\\n--\\n010\\n\\n+-'))
    1 1
    0 1
    >>> print_matrix(parse_file('--\\n-'))
    Traceback (most recent call last):
    ...
    ValueError: The file cannnot be parsed as a matrix.
    >>> print_matrix(parse_file('--\\n-+\\n++'))
    Traceback (most recent call last):
    ...
    ValueError: The file cannnot be parsed as a matrix.
    '''
    for symbols in [['+', '-'], ['0', '1']]:
        matrix = []
        
        for line in contents.split('\n'):
            if len(line) == 0 or any(x not in symbols for x in line):
                continue

            row = [symbols.index(x) for x in line]
            matrix.append(row)
        
        N = len(matrix)
        if N == 0 or any(len(row) != N for row in matrix):
            continue

        return matrix

    raise ValueError('The file cannnot be parsed as a matrix.')

def get_rank_from_file(contents):
    matrix = parse_file(contents)

    if not quiet:
        print('Parsed file as:\n')
        print_matrix(matrix)

    dephase_matrix(matrix)

    if not quiet:
        print('\nThe matrix can be dephased as:\n')
        print_matrix(matrix)

    rank = int(eng.gfrank(matlab.double(matrix), 2.0))

    if not quiet:
        print('\nMATLAB computes that this matrix has rank: ' + str(rank))

    return len(matrix), rank

if test_mode:
    import doctest
    doctest.testmod(verbose=True)

    print('Starting MATLAB engine. Please wait...')
    import matlab.engine
    eng = matlab.engine.start_matlab()

    assert get_rank_from_file('010\n110\n100') == (3, 2)
