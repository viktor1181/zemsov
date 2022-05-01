import itertools


#for L in range(0, len(stuff)+1):
def comb(arr, r):
	combin = [list(subset) for subset in itertools.combinations(arr, r)]
	return combin

if __name__ == "__main__":
	stuff = [1, 2, 3, 4, 5]
	r = 1
	arr = comb(stuff, r)
	print(arr)
# This code is contributed
# by ChitraNayal
