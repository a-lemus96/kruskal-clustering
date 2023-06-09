# stdlib modules
import argparse

# 3rd-party modules
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# custom modules
import mst

# create argument parser and add arguments to it
parser = argparse.ArgumentParser(description='Max-spacing k-clustering')
parser.add_argument('k', type=int, default=2, help='number of desired groups')
# parse arguments
args = parser.parse_args()

# load data points from .txt file
points = [] # to hold coordinate pairs and apply post processing
att = [] # to hold coordinate pairs as attributes for a graph node
with open('data.txt', 'r') as f:
    n = int(f.readline()) # number of data points
    for k in range(n):
        pair = f.readline()
        x, y = pair.split(" ")
        points.append((float(x), float(y)))
        att.append({'x': float(x), 'y': float(y)})

points = np.array(points) # cast to numpy array
# plot points
#subax1 = plt.subplot(121)
#plt.scatter(points[:, 0], points[:, 1])

# compute distances among all points
diffs = points.reshape(n, 1, 2) - points.reshape(1, n, 2)
dists = np.sqrt(np.sum(diffs**2, axis=2))
dists = dists.flatten()

# compute edges
edges = np.mgrid[0:n, 0:n]
edges = np.stack((edges[0, ...], edges[1, ...]), axis=-1)
edges = edges.reshape(-1, 2)

# create Graph using networkx
G = nx.Graph()
G.add_nodes_from(zip(range(n), att)) # add nodes
G.add_weighted_edges_from(zip(edges[:, 0], edges[:, 1], dists)) # add edges
G.remove_edges_from(nx.selfloop_edges(G)) # remove self-loops

# compute K-clustering
t = mst.kruskal_modified(G, args.k)
T = nx.Graph(t)
for component in nx.connected_components(T):
    # select points
    p = points[list(component)]
    plt.scatter(p[:, 0], p[:, 1])
#ax.scatter(points[:, 0], points[:, 1])
plt.show()
