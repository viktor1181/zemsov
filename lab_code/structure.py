import properties

Lij = [1000] * 10
L = {}
bindings = {}
ring_structure = [[] for _ in range(properties.n_edge)]
ring = [[] for _ in range(properties.n_edge+properties.n_vertex)]
# список связей
connections = [i+properties.n_vertex for i in range(properties.n_vertex)]

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

# добавим пути в структуру


# длинна связей вершин графа
for i, el in enumerate(Lij):
    L[str(ring_structure[i])] = el
    bindings[connections[i]] = ring_structure[i]

if __name__ == "__main__":
	print(L)
	print("\n")
	print(bindings)
