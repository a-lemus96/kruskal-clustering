# Max-spacing $k$-clustering using Kruskal's Algorithm

This repository contains an implementation of the Kruskal's algorithm for solving the max-spacing $k$-clustering problem. Cycle detection within Kruskal's algorithm is implemented using the weighted quick-union algorithm, which has been shown to run in $O(\log_2 n)$. The script `clustering.py` reads the file `data.txt` which contains the following set of 2-dimensional points:

![points](https://github.com/a-lemus96/kruskal-clustering/assets/95151624/7f247842-d8b8-46f9-8bd1-22bcb3f94ffb)

The script computes the distances between all possible pairs of nodes and builds a weighted and connected graph $G$ using networkX library. Then it runs Kruskal's algorithm with a termination condition on the desired number of connected components $k$, which is provided by the user.

### Running the script
---
The script 

![k2](https://github.com/a-lemus96/kruskal-clustering/assets/95151624/11e26e4a-c9fa-4804-986d-e67d86f33784)

![k3](https://github.com/a-lemus96/kruskal-clustering/assets/95151624/95a94143-8dd8-4d5a-bfc9-b1858c3bb246)

![k4](https://github.com/a-lemus96/kruskal-clustering/assets/95151624/dc4947b0-1356-4e95-88b6-6bf93d43878c)
