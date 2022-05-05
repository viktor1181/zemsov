import properties

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