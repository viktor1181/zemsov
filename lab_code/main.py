# Driver code
from BFC import findpaths
import properties
from combination import comb
from timeCombination import DFS

ring_structure = [[] for _ in range(properties.n_edge)]
# Construct a graph
ring_structure[0].append(1)
ring_structure[0].append(9)
ring_structure[1].append(0)
ring_structure[1].append(2)
ring_structure[2].append(1)
ring_structure[2].append(3)
ring_structure[3].append(2)
ring_structure[3].append(4)
ring_structure[4].append(3)
ring_structure[4].append(5)
ring_structure[5].append(4)
ring_structure[5].append(6)
ring_structure[6].append(5)
ring_structure[6].append(7)
ring_structure[7].append(6)
ring_structure[7].append(8)
ring_structure[8].append(7)
ring_structure[8].append(9)
ring_structure[9].append(8)
ring_structure[9].append(1)
# добавлениеновых путей
#ring_structure[0].append(3)
#ring_structure[2].append(8)
#ring_structure[5].append(9)
#ring_structure[7].append(4)

src = 2
dst = 3
timeFaluer = []
if __name__ == "__main__":
    # Number of vertices

    print("path from src {} to dst {} are".format(
        src, dst))

    # Function for finding the paths
    path = findpaths(ring_structure, src, dst, properties.n_vertex)
    #for i in range(2, properties.n_edge+2):
    #    ans = DFS(properties.n_edge+1, i, src, dst)
    #    timeFaluer.append(ans)
    for i in path:
        if len(i) > 2:
            for j in range(len(i)-1):
                arr = comb(i, j+2)
                timeFaluer.append(arr)
        else:
            arr = comb(i, 1)
            timeFaluer.append(arr)

    for i in timeFaluer:
        for j in path:
            pass

    print(timeFaluer)