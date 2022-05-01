# Python3 program to print all paths of
# source to destination in given graph
from typing import List
from collections import deque


# Utility function for printing
# the found path in graph
def printpath(path: List[int]) -> None:
    size = len(path)
    for i in range(size):
        print(path[i], end=" ")

    print()


# Utility function to check if current
# vertex is already present in path
def isNotVisited(x: int, path: List[int]) -> int:
    size = len(path)
    for i in range(size):
        if (path[i] == x):
            return 0

    return 1


# Utility function for finding paths in graph
# from source to destination
def findpaths(g: List[List[int]], src: int,
              dst: int, v: int) -> None:
    # Create a queue which stores
    # the paths
    q = deque()
    listAll = []

    # Path vector to store the current path
    path = []
    path.append(src)
    q.append(path.copy())

    while q:
        path = q.popleft()
        last = path[len(path) - 1]

        # If last vertex is the desired destination
        # then print the path
        if (last == dst):
            #printpath(path)
            listAll.append(path)

        # Traverse to all the nodes connected to
        # current vertex and push new path to queue
        for i in range(len(g[last])):
            if (isNotVisited(g[last][i], path)):
                newpath = path.copy()
                newpath.append(g[last][i])
                q.append(newpath)
    return listAll


