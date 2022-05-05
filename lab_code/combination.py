import itertools

import properties
from BFC import findpaths
from structure import ring_structure

#for L in range(0, len(stuff)+1):
def comb(arr, r):
	combin = [list(subset) for subset in itertools.combinations(arr, r)]
	return combin

def falureCombination(*paths):
	out = []
	common = {}
	d = {}
	for i, el in enumerate(paths):
		d[i] = el
	if len(paths[0]) <= 2:
		common = set.intersection(*(set(v) for k, v in d.items()))
		out = [list(set(v) - common) for k, v in d.items()]
		out[0] = [i for i in common]
		combination = [list(i) for i in itertools.product(*out)]
	else:
		common = set.intersection(*(set(v) for k, v in d.items()))
		out = [list(set(v) - common) for k, v in d.items()]
		combination = [list(i) for i in itertools.product(*out)]
		for i in common:
			combination.append([i])
	return combination

if __name__ == "__main__":
	src = 2
	dst = 3
	paths = findpaths(ring_structure, src, dst, properties.n_vertex)
	arr = falureCombination(*paths)

	print(paths)
	print('\n')
	print(arr)
# This code is contributed
# by ChitraNayal
"""
нам нет необходимости искать больше одного элемента пути в комбинации,
так как если на одном пути вышел из строя второй элемент, то сеть из строя не выйдет и 
следовательно продолжит работу и это НЕ повлияет на время работы сети

если в одном из путей всего два элемента то этот массив не трогаем, 
а из остальных массивов удалим эти элементы

в остальных случаях одинаковые элементы удаляем из всех путей получаем комбинации 
и удаленные элементы вставляем в комбинации
"""