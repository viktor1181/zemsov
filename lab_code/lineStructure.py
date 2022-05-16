import properties
from BFC import findpaths

Lij = [1000] * 10
L = {}
bindings = {}
sigma_svyzi = 0.2
line_structure = [[] for _ in range(properties.n_edge+properties.n_vertex)]
# список связей
connections = [i+properties.n_vertex for i in range(properties.n_vertex)]

# интенсивность отказа вершин и связей
int_otk_el = [7, 2, 8, 5, 4, 11, 12, 9, 8, 3]

int_otk_line = [l*sigma_svyzi for l in Lij]

# Construct a graph
line_structure[0].append(0)
line_structure[0].append(1)
line_structure[1].append(0)
line_structure[1].append(2)
line_structure[2].append(1)
line_structure[2].append(3)
line_structure[3].append(2)
line_structure[3].append(4)
line_structure[4].append(3)
line_structure[4].append(5)
line_structure[5].append(4)
line_structure[5].append(6)
line_structure[6].append(5)
line_structure[6].append(7)
line_structure[7].append(6)
line_structure[7].append(8)
line_structure[8].append(7)
line_structure[8].append(9)
line_structure[9].append(8)
line_structure[9].append(10)
line_structure[10].append(9)
line_structure[10].append(11)
line_structure[11].append(10)
line_structure[11].append(12)
line_structure[12].append(11)
line_structure[12].append(13)
line_structure[13].append(12)
line_structure[13].append(14)
line_structure[14].append(13)
line_structure[14].append(15)
line_structure[15].append(14)
line_structure[15].append(16)
line_structure[16].append(15)
line_structure[16].append(17)
line_structure[17].append(16)
line_structure[17].append(18)
line_structure[18].append(17)
line_structure[18].append(19)
line_structure[19].append(18)
line_structure[19].append(19)
# добавлениеновых путей
#ring_structure[0].append(3)
#ring_structure[2].append(8)
#ring_structure[5].append(9)
#ring_structure[7].append(4)

# добавим пути в структуру


# длинна связей вершин графа
for i, el in enumerate(Lij):
    L[str(line_structure[i])] = el
    bindings[connections[i]] = line_structure[i]

if __name__ == "__main__":
	src = 2
	dst = 4
	paths = findpaths(line_structure, src, dst, properties.n_vertex)
	print(L)
	print("\n line_structure ")
	print(line_structure)
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