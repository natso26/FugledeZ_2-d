'''This is a new file for this fast version of the program.


== Overview ==

This file enumerates subsets of Z_2^d of a given size n
that contain the d+1 fixed elements
(0,0,...,0), (1,0,...,0), (0,1,...,0), (0,0,...,1),
up to permutation of coordinates.

What this means is the following.
Suppose d = 6 and we switch coordinates 2 and 6, then
(0,1,0,0,1,0) = 18 will become (0,0,0,0,1,1) = 3,
where we identify elements in Z_2^d with integers via
binary expansion as usual.
A subset E of Z_2^d can then be transformed by a
permutation of coordinates by applying this transformation
to each element of E in the above way.
Notice that the set of fixed elements is invariant under
a permutation of coordinates.

Let N=2^d. There are (N-d-1)C(n-d-1) subsets satisfying
our criteria. This file may not enumerate all of them.
However, for each subset E that it does not enumerate,
there is a subset E' which it enumerates such that E
can be transformed into E' by a permutation of coordinates.

It is clear that the properties of being a spectral
set and a tile are invariant under a permutation of
coordinates, so this strategy does not affect the
correctness of the program.


== Effectiveness ==

This file uses a set of heuristics to deduce that a set
E can be transformed via a permutation of coordinates
to a set that has already been enumerated. These heuristics
are not perfect (there can be sets that can be transformed
in the way mentioned that are not detected by the heuristics),
but they are good enough for our purposes.

From the almost 9 billion subsets of size 16 in Z_2^6,
these heuristics reduce the number of subsets to check to
less than 300 million, or a reduction by a factor of 30.

We do not know what the number would be if we were to
perform a perfect detection. (Obviously we cannot get
a reduction by a factor of more than 6! = 720. But the
actual reduction factor may or may not be close to this.)

Notice that performing a perfect detection may be
computationally expensive. So even if we were to implement
a perfect detection, it would need to tested to see
if it actually helps reduce runtime.


== How to use ==

The function generate_sets_reduced is used in main_all.py
to enumerate subsets as explained above.

Input
size: The size n of subsets of Z_2^d that we want to enumerate.
      The prerequisite is that n must be at least d+4.

Running this file directly brings up test mode,
which enumerates subsets of size 16 in Z_2^6.

For checking Fuglede's conjecture for subsets of size 16
in Z_2^6, the function generate_sets_reduced accounts for
about 2.5% of the total runtime.


== Implemented heuristics ==

Assume that n >= d+4. We order subsets of size n of Z_2^d
as follows. Excluding the d+1 fixed elements, there are n-d-1
other elements.
Arrange these elements in increasing order according to
their values as integers (equivalently, according to the
lexicographic ordering).
We now obtain a vector of length n-d-1. Order these vectors
by lexicographic ordering. This gives an ordering of the
subsets of size n.

We now present heuristics to detect when a given subset E
can be transformed by a permutation of coordinates into
a subset E' that comes before it in this ordering.
If this is the case, then we can safely skip the checking
of E as explained above.

Below, assume that elements of E are arranged in increasing
order. So the first element of E is its smallest element, etc.


=== The first element ===

Denote the first element of E by fst. For E to be worthy of
checking, fst must be of the form (0,...,0,1,...,1), that is,
the coordinate values are arranged in increasing order.
If not, then for example, suppose that fst = (0,1,0,1,1,0).
We can switch coordinates 2 and 6 to get fst = (0,0,0,1,1,1).
Notice that fst may no longer be the smallest element, but the
smallest element must be at most (0,0,0,1,1,1), which is
smaller than the original fst. Hence, after permuting
the coordinates, we obtain a subset that comes before E
in the ordering.

This is implemented in the list ok_as_fst.


=== The second element ===

Denote the second element of E by snd. Given fst, in order
for E to be worthy of checking, snd must satisfy the following.

1. Obviously snd > fst.

2. The number of coordinates of snd that are 1 must be at
   least the number of coordinates of fst that are 1.
   Otherwise, we can permute coordinates so that snd becomes
   some (0,...,0,1,...,1) which is smaller than the original fst.

3. Restricting to the coordinates for which fst is 0,
   the coordinate values of snd are nondecreasing. Likewise,
   restricting to the coordinates for which fst is 1, the
   coordinate values of snd are nondecreasing.

   For example, if fst = (0,0,0,1,1,1), then snd must look
   something like (0,1,1,0,0,1), where the first three and
   the last three coordinate values are nondecreasing.

   The proof of this is the following. Suppose not.
   For example, let fst = (0,0,0,1,1,1) and snd = (1,0,1,0,0,1).
   Then we can switch coordinates 1 and 2 to make fst
   stay the same but snd decreases to (0,1,1,0,0,1).
   The resutling subset will come before E in the ordering.

This is implemented in the function ok_as_snd.


=== The third element ===

Denote the third element of E by thd. Given fst and snd, in
order for E to be worthy of checking, thd must satisfy the
following.

1. Obviously thd > snd.

2. As in 2. of snd, the number of coordinates of thd that are 1
   must be at least the number of coordinates of fst that are 1.

3. Restricting to the coordinates for which fst is 0, the
   number of coordinates of thd that are 1 must be at least the
   number of coordinates of snd that are 1.

   Otherwise, we can permute coordinates so that fst is fixed
   and thd becomes smaller than the original snd.

4. For two consecutive coordinates such that the values of fst
   on these coordinates are the same, and likewise for snd,
   the coordinate values of thd are nondecreasing.

   In other words, we cannot have something like
   fst = (...,a,a,...), snd = (...,b,b,...), and thd = (...,1,0,...).
   The proof is that in that case, we can switch these two
   coordinates to fix fst and snd and make thd smaller.

This is implemented in the function ok_as_thd.


=== The rest of the elements ===

Denote by x any element of E that is not one of the first three.
Given fst, snd, and thd, in order for E to be worthy of checking,
x must satisfy the following.

1. Obviously x > thd.

2. As in 2. of snd, the number of coordinates of x that are 1
   must be at least the number of coordinates of fst that are 1.

3. As in 3. of thd, restricting to the coordinates for which fst
   is 0, the number of coordinates of x that are 1 must be at
   least the number of coordinates of snd that are 1.

4. Let the first k coordinates of snd be 0. Then restricting to
   the first k coordinates, the number of coordinates of x that
   are 1 must be at least the number of coordinates of thd that
   are 1.

   To prove this, we first observe that the first k coordinates
   of fst are 0. If not, then fst > snd, a contradiction.
   Then if this condition is not satisfied, then we can permute
   coordinates so that fst and snd are fixed and x becomes
   smaller than thd.
   
This is implemented in the function ok_as_rest.
'''

import sys
if __name__ == "__main__":
    sys.argv.extend([6])
    test_mode = True
else:
    test_mode = False

from itertools import combinations

from prelim import dim, N, fixed_elts

# Transform an integer to the corresponding element of Z_2^d.
def int_to_bits(x):
    '''
    >>> int_to_bits(18)
    (0, 1, 0, 0, 1, 0)'''
    return tuple(int(c) for c in format(x, '0'+str(dim)+'b'))

# Transform an element of Z_2^d to the corresponding integer.
bits_to_int = {}

for x in range(N):
    bits_to_int[int_to_bits(x)]= x

def _():
    '''
    >>> bits_to_int[(1,0,1,1,0,0)]
    44'''

pool = [int_to_bits(x) for x in range(N) if x not in fixed_elts]

ok_as_fst = list(map(int_to_bits, [pow(2,i)-1 for i in range(2, dim+1)]))

def __():
    '''
    >>> ok_as_fst[0] == (0,0,0,0,1,1)
    True
    >>> ok_as_fst[-1] == (1,1,1,1,1,1)
    True'''
    
def ok_as_snd(fst):
    '''
    >>> (0,0,0,0,1,1) in ok_as_snd((0,0,0,1,1,1))
    False
    >>> (0,1,1,0,0,0) in ok_as_snd((0,0,0,1,1,1))
    False
    >>> (0,0,1,1,1,0) in ok_as_snd((0,0,0,1,1,1))
    False
    >>> (0,0,1,0,1,1) in ok_as_snd((0,0,0,1,1,1))
    True
    >>> (0,1,1,1,1,1) in ok_as_snd((0,0,0,1,1,1))
    True'''
    def ok(snd):
        if snd <= fst:
            return False
        if snd.count(1) < fst.count(1):
            return False
        for i in range(dim-1):
            if fst[i] == fst[i+1] and snd[i] > snd[i+1]:
                return False
        return True
    
    return [snd for snd in pool if ok(snd)]

def ok_as_thd(fst, snd):
    '''
    >>> (0,0,0,1,1,1) in ok_as_thd((0,0,0,0,1,1),(0,0,1,1,0,0))
    False
    >>> (0,0,1,1,0,0) in ok_as_thd((0,0,0,1,1,1),(0,0,1,0,1,1))
    False
    >>> (0,1,0,0,1,1) in ok_as_thd((0,0,0,0,1,1),(0,0,1,1,0,1))
    False
    >>> (0,1,0,0,1,1) in ok_as_thd((0,0,0,0,1,1),(0,0,0,1,0,1))
    False
    >>> (1,1,1,1,1,0) in ok_as_thd((0,0,0,1,1,1),(0,0,1,0,1,1))
    False
    >>> (1,1,1,1,0,1) in ok_as_thd((0,0,0,1,1,1),(0,0,1,0,1,1))
    True
    >>> (1,1,0,0,0,1) in ok_as_thd((0,0,0,1,1,1),(0,0,1,0,1,1))
    True
    >>> (1,1,1,0,0,0) in ok_as_thd((0,0,0,1,1,1),(0,1,1,1,1,1))
    True
    '''
    fst1 = fst.index(1)
    
    def ok(thd):
        if thd <= snd:
            return False
        if thd.count(1) < fst.count(1):
            return False
        if thd[:fst1].count(1) < snd[:fst1].count(1):
            return False
        for i in range(dim-1):
            if fst[i] == fst[i+1] and snd[i] == snd[i+1] and thd[i] > thd[i+1]:
                return False
        return True
    
    return [x for x in pool if ok(x)]

def ok_as_rest(fst, snd, thd):
    '''
    >>> (0,1,1,1,1,1) in ok_as_rest((0,0,0,0,1,1),(0,0,1,1,0,0),(1,1,0,0,0,0))
    False
    >>> (0,1,0,0,0,0) in ok_as_rest((0,0,0,1,1,1),(0,0,1,0,1,1),(0,0,1,1,1,1))
    False
    >>> (1,1,0,0,0,0) in ok_as_rest((0,0,0,0,1,1),(0,1,1,1,0,0),(1,0,1,1,0,0))
    False
    >>> (1,0,0,1,1,1) in ok_as_rest((0,0,0,0,1,1),(0,0,0,1,0,1),(0,1,1,0,0,0))
    False
    >>> (1,1,0,1,1,1) in ok_as_rest((0,0,0,0,1,1),(0,0,0,1,0,1),(0,1,1,0,0,0))
    True
    >>> (0,1,0,1,1,0) in ok_as_rest((0,0,0,1,1,1),(0,0,1,0,1,1),(0,0,1,1,1,1))
    True
    >>> (1,1,1,0,0,0) in ok_as_rest((0,0,0,0,1,1),(0,1,1,1,0,0),(1,0,1,1,0,0))
    True
    >>> (1,1,0,1,0,0) in ok_as_rest((0,0,0,0,1,1),(0,1,1,1,0,0),(1,0,1,1,0,0))
    True
    >>> (1,1,1,1,0,0) in ok_as_rest((0,0,0,0,1,1),(0,1,1,1,0,0),(1,0,1,1,0,0))
    True
    '''
    fst1 = fst.index(1)
    snd1 = snd.index(1)
    
    def ok(x):
        if x <= thd:
            return False
        if x.count(1) < fst.count(1):
            return False
        if x[:fst1].count(1) < snd[:fst1].count(1):
            return False
        if x[:snd1].count(1) < thd[:snd1].count(1):
            return False
        return True
    
    return [x for x in pool if ok(x)]

def generate_sets_reduced(size):
    cnt = 0

    for fst in ok_as_fst:
        for snd in ok_as_snd(fst):
            for thd in ok_as_thd(fst, snd):
                first3 = [bits_to_int[x] for x in [fst, snd, thd]]
                new_pool = [bits_to_int[x] for x in ok_as_rest(fst, snd, thd)]
                new_size = size-len(fixed_elts)-3
                for comb in combinations(new_pool, new_size):
                    cnt += 1
                    if test_mode:
                        if cnt % 10000000 == 0:
                            print('\ncnt =', cnt)
                            item = first3 + list(comb)
                            print('item =', item)
                    else:
                        item = first3 + list(comb)
                        yield item

    if test_mode:
        print('\ncnt =', cnt)

if test_mode:
    print('Begin testing...\n')
    
    import doctest
    doctest.testmod(verbose=True)

    print('\nBegin generating sets...')
    
    for s in generate_sets_reduced(16):
        pass
