'''Check whether a k-clique exists in a graph.

The function to use is clique_exists. clique_exists_helper
is a helper function.

Inputs
1. graph: The input graph. It should be given by a list of lists,
   where graph[x][y] is 1 if there is an edge (x,y), and 0 otherwise.
   The graph should be undirected with no self-loop.
2. k: The size of the clique. A nonnegative integer.
3. must_contain: A list of nodes (nonnegative integers) that the clique
   must contain. This is an optional argument with default value [].
'''

quiet = False

# Test case. The largest clique is of size 4.
g = \
[[0,1,0,0,1,1,0],
 [1,0,0,0,1,0,1],
 [0,0,0,1,1,1,1],
 [0,0,1,0,0,1,1],
 [1,1,1,0,0,0,1],
 [1,0,1,1,0,0,1],
 [0,1,1,1,1,1,0]];

'''Helper function. It checks whether there is a k-clique in graph
whose nodes are in candidates.

The algorithm proceeds as follows.
1. Do the trivial check that the size of candidates is at least k.
2. The cases k <= 2 are simple enough to be handled directly.
3. Filter out candidates that are adjacent to less than k-1
   other candidates.
   If there are fewer than k candidates left, return False.
4. For each possible candidate c, define new_candidates to be those
   candidates that are adjacent to c. Then recurse to check whether
   there is a (k-1)-clique in graph whose nodes are in new_candidates.
   If the answer is False, then remove c from the list of candidates.
   If there are fewer than k candidates left, return False.
'''
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
                if graph[x][y]:
                    return True
        return False

    candidates = [x for x in candidates if sum(graph[x][y] for y in candidates) >= k-1]

    if not quiet and cnt < 30:
        print('After filtering: nodes =', candidates)
    
    if len(candidates) < k:
        return False

    for candidate in candidates:
        new_candidates = [x for x in candidates if graph[x][candidate]]
        if clique_exists_helper(graph, k-1, new_candidates):
            return True

        candidates.remove(candidate)
        if len(candidates) < k:
            return False

    return False

'''Main function. Usage is as above.

It performs the following tasks.
1. Check that the size of must_contain is more than k and that
   nodes in must_contain indeed form a clique.
2. Compute candidates, which consists of nodes that are adjacent
   to all nodes in must_contain.
3. Call the helper function to check whether there is a
   (k-len(must_contain))-clique whose nodes are in candidates.
'''
def clique_exists(graph, k, must_contain=[]):
    global cnt
    cnt = 0
    
    if len(must_contain) > k:
        return False
    
    for x in must_contain:
        for y in must_contain:
            if y > x and not graph[x][y]:
                return False

    candidates = [x for x in range(len(graph)) if all(graph[x][y] for y in must_contain)]

    return clique_exists_helper(graph, k-len(must_contain), candidates)
