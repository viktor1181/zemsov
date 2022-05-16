import properties
from BFC import findpaths

Lij = [1000] * 10
L = {}
bindings = {}
sigma_svyzi = 0.2
ring_structure = [[] for _ in range(properties.n_edge+properties.n_vertex)]
ring = [[] for _ in range(properties.n_edge+properties.n_vertex)]
# список связей
connections = [i+properties.n_vertex for i in range(properties.n_vertex)]

# интенсивность отказа вершин и связей
int_otk_el = [7, 2, 8, 5, 4, 11, 12, 9, 8, 3]

int_otk_line = [l*sigma_svyzi for l in Lij]

# Construct a graph
ring_structure[0].append(1)
ring_structure[0].append(19)
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
ring_structure[9].append(10)
ring_structure[10].append(9)
ring_structure[10].append(11)
ring_structure[11].append(10)
ring_structure[11].append(12)
ring_structure[12].append(11)
ring_structure[12].append(13)
ring_structure[13].append(12)
ring_structure[13].append(14)
ring_structure[14].append(13)
ring_structure[14].append(15)
ring_structure[15].append(14)
ring_structure[15].append(16)
ring_structure[16].append(15)
ring_structure[16].append(17)
ring_structure[17].append(16)
ring_structure[17].append(18)
ring_structure[18].append(17)
ring_structure[18].append(19)
ring_structure[19].append(18)
ring_structure[19].append(0)
# добавлениеновых путей
#ring_structure[0].append(3)
#ring_structure[2].append(8)
#ring_structure[5].append(9)
#ring_structure[7].append(4)

# добавим пути в структуру


# длинна связей вершин графа
for i, el in enumerate(Lij):
    L[str(ring_structure[i])] = el
    bindings[connections[i]] = ring_structure[i]

if __name__ == "__main__":
	src = 2
	dst = 3
	paths = findpaths(ring_structure, src, dst, properties.n_vertex)
	print(L)
	print("\n ring_structure ")
	print(ring_structure)
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