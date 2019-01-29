'''This file has been changed in the following ways.

1. We no longer use the function clique_exists, but directly use
   clique_exists_helper to check whether there is a k-clique whose
   nodes are in candidates.

2. The graph is no longer explicitly computed. It was found that
   computing the 64x64 adjacency matrix is one of the bottlenecks
   of the program.

   We use the symmetry of the graph that node x is adjacent to
   node y if and only if node 0 is adjacent to node x-y
   (as elements of Z_2^d). Then, the "graph" is represented as
   the list of size N such that graph[x] is 1 if node 0 is adjacent
   to node x, and it is 0 otherwise. So node x is adjacent to
   node y if and only if graph[x ^ y] is 1, where ^ is the XOR.
   
   (Recall that, in our representation of elements of Z_2^d using
   integers, x ^ y computes the sum of x and y, which is the same
   as the difference of x and y.)

Further changes are explained in the comments below.

In this fast version, the function clique_exists_helper accounts
for about 21% of the total runtime.
'''

quiet = False
cnt = None

def clique_exists_helper(graph, k, candidates):
    global cnt
    cnt += 1
    
    if not quiet:
        if cnt == 30:
            print('\nSwitching to printing less output.\n')

        if cnt < 30:
            print('Recursion {}: {}-clique, nodes = {}'.format(cnt, k, candidates))
        elif (cnt < 1000 and cnt % 100 == 0) or (cnt < 30000 and cnt % 1000 == 0) \
             or cnt % 5000 == 0:
                print('Recursion {}'.format(cnt))   
    
    if len(candidates) < k:
        return False
    
    if k <= 1:
        return True

    if k == 2:
        for x in candidates:
            for y in candidates:
                if graph[x ^ y]:
                    return True
        return False

    '''The original code for this part reads:

    candidates = [x for x in candidates if sum(graph[x][y] for y in candidates) >= k-1]
    
    and it filters candidates down to those nodes that are adjacent to at least
    k-1 other candidates.

    It was found to be a bottleneck in the computation. Therefore, a lower-level
    but faster version of this line of code has been implemented below.
    
    This implementaion also allows us to return False immediately if there are
    fewer than k candidates left, without having to go through every candidate.
    This consideration also speeds up computation.
    '''
    new_candidates = []
    remaining = len(candidates)
    
    for x in candidates:
        deg = 0
        for y in candidates:
            deg += graph[x ^ y]
        if deg >= k-1:
            new_candidates.append(x)
        else:
            remaining -= 1
            if remaining < k:
                return False

    candidates = new_candidates
    '''End of part'''

    if not quiet and cnt < 30:
        print('After filtering: nodes =', candidates)

    '''This block of code is new and leads to a minor speedup.

    It does the following. If there are exactly k candidates left,
    then there is a k-clique if and only if these nodes form a clique,
    and this can be directly checked.
    '''
    if len(candidates) == k:
        for x in candidates:
            for y in candidates:
                if y > x and not graph[x ^ y]:
                    return False
        return True
    '''End of block of code'''

    for candidate in candidates:
        new_candidates = [x for x in candidates if graph[x ^ candidate]]
        if clique_exists_helper(graph, k-1, new_candidates):
            return True

        candidates.remove(candidate)
        if len(candidates) < k:
            return False

    return False
