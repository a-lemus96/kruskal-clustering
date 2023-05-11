# 3rd-party modules
import networkx as nx

def weighted_quick_union(A, p, q):
    """Weighted quick-union algorithm.
    ----------------------------------------------------------------------------"""
    i = p
    rank_i = 0
    # find root for p
    while A[i] != i:
       i = A[i]
       rank_i += 1
    
    j = q
    rank_j = 0
    # find root for q
    while A[j] != j:
        j = A[j]
        rank_j += 1

    # check if both roots are the same or not
    if i != j:
        if rank_i <= rank_j: 
            A[i] = j
            old_root = i
        else:
            A[j] = i
            old_root = j
        return True, old_root
    else:
        return False, i

def kruskal_modified(G, k=2):
    """Kruskal's algorithm with termination condition. User provides the number
    of desired unconnected components to terminate algorithm.
    ----------------------------------------------------------------------------
    Parameters:
    -----------
        G: networkx weighted connected graph.
        k: integer value representing the desired number of components
    Returns:
    ---------
        """
    edges = G.edges.data() # retrieve edges and their weights
    edges = list(edges)
    edges.sort(key=lambda x: x[-1]['weight']) # sort edges by increasing weight
    edges = iter(edges)
    T = []
    # initialize array to implement union-find algorithm
    n = G.number_of_nodes()
    A = list(range(n))
    roots = n * [True] # True if i-th node is a root of a group
    while sum(roots) > k:
        e = next(edges)
        added, rm_idx = weighted_quick_union(A, e[0], e[1])
        if added:
            T.append(e) # add edge to MST solution
            roots[rm_idx] = False # remove node from root nodes
    return T
