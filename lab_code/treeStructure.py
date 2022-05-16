import properties
from BFC import findpaths

Lij = [1000] * 10
L = {}
bindings = {}
sigma_svyzi = 0.2
tree_structure = [[] for _ in range(properties.n_edge+properties.n_vertex + 1)]
# список связей
connections = [i+properties.n_vertex for i in range(properties.n_vertex)]

# интенсивность отказа вершин и связей
int_otk_el = [7, 2, 8, 5, 4, 11, 12, 9, 8, 3]

int_otk_line = [l*sigma_svyzi for l in Lij]

# Construct a graph
tree_structure[0].append(1)
tree_structure[0].append(2)
tree_structure[1].append(0)
tree_structure[1].append(6)
tree_structure[2].append(0)
tree_structure[2].append(3)
tree_structure[3].append(2)
tree_structure[3].append(4)
tree_structure[4].append(3)
tree_structure[4].append(5)
tree_structure[5].append(4)
tree_structure[5].append(5)
tree_structure[6].append(1)
tree_structure[6].append(7)
tree_structure[6].append(8)
tree_structure[7].append(6)
tree_structure[7].append(9)
tree_structure[8].append(6)
tree_structure[8].append(14)
tree_structure[9].append(7)
tree_structure[9].append(10)
tree_structure[9].append(11)
tree_structure[10].append(9)
tree_structure[10].append(12)
tree_structure[11].append(9)
tree_structure[11].append(13)
tree_structure[12].append(10)
tree_structure[12].append(12)
tree_structure[13].append(11)
tree_structure[13].append(13)
tree_structure[14].append(8)
tree_structure[14].append(15)
tree_structure[14].append(16)
tree_structure[15].append(14)
tree_structure[15].append(17)
tree_structure[16].append(14)
tree_structure[16].append(18)
tree_structure[17].append(15)
tree_structure[17].append(17)
tree_structure[18].append(16)
tree_structure[18].append(19)
tree_structure[19].append(18)
tree_structure[19].append(20)
tree_structure[20].append(19)
tree_structure[20].append(20)
# добавлениеновых путей
#ring_structure[0].append(3)
#ring_structure[2].append(8)
#ring_structure[5].append(9)
#ring_structure[7].append(4)

# добавим пути в структуру


# длинна связей вершин графа
for i, el in enumerate(Lij):
    L[str(tree_structure[i])] = el
    bindings[connections[i]] = tree_structure[i]

if __name__ == "__main__":
	src = 2
	dst = 20
	paths = findpaths(tree_structure, src, dst, properties.n_vertex)
	print(L)
	print("\n ring_structure ")
	print(tree_structure)
	print("\n bindings ")
	print(bindings)
	print("\n paths ")
	print(paths)
	for path in paths:
		pass
"""
ring_structure это двумерный список (список смежноси графа) то есть ендукс это вершина,
а значения это список вершин, которые соединены с вершиной(индексом) 
"""