class Graph:
    """Undirected graph class definition.
    A graph stores nodes and edges with optional data, or attributes.
    The graph datatype handles undirected edges.
    Self loops are allowed but multiple edges are not.

    This implementation is based on networkX's Graph base class definition."""

    def __init__(self, nodes=None, edges=None):
        """Initialize a graph with nodes (containing optional attributes) and
        edges. It stores the Graph in the adjacency list format.
        ------------------------------------------------------------------------ 
        Parameters:
        -----------  
            nodes : (n,)-sized List or Tuple containing nodes containing n pairs
                of node IDs (and optional satellite data). Satellite data is
                passed as a python dictionary.
            edges : (n, 2)-sized List or Tuple containing the list of edges."""
        self._adj = {} # adjacency list implementation
        self._attr = {} # attributes
        for node in nodes:
            if type(node) == list or type(node) == tuple:
                self._adj[node[0]] = [] # empty adjacency list
                self._attr[node[0]] = node[1]
            else:
                self._adj[node] = {}
                self._attr[node] = {}
        
        for u, v in edges:
            keys = self._adj.keys()
            # insert edges whose nodes are present as keys in self._adj
            if u in keys and v in keys:
                self._adj[u].append(v)
                self._adj[v].append(u)
            # otherwise raise err msg
            else:
                err_msg = f"At least a node from ({u}, {v}) is not in self._adj"
                raise Exception(err_msg)

