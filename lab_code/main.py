# Driver code
import itertools

from BFC import findpaths
import properties
from combination import comb
from structure import ring_structure
from timeCombination import DFS

src = 2
dst = 3
timeFaluer = []
if __name__ == "__main__":
    # Number of vertices

    print("path from src {} to dst {} are".format(
        src, dst))

    # Function for finding the paths
    paths = findpaths(ring_structure, src, dst, properties.n_vertex)


    combination = [list(i) for i in itertools.product(*paths)]
    print(combination)
