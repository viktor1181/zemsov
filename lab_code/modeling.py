import random

import properties
from BFC import findpaths
from ringStructure import int_otk_el, int_otk_line, ring_structure

import numpy as np


def Diaposon(int_otk_el, int_otk_line):
    # сумарная интенсивность отказа
    treygolinik = sum(int_otk_el) + sum(int_otk_line)

    # условные интенсивности отказов узлов и линий сети
    ysl_line = []
    ysl_el = []
    ysl_all = []

    for el in int_otk_el:
        ysl_el.append(el/treygolinik)

    for l in int_otk_line:
        ysl_line.append(l / treygolinik)
    ysl_all.extend(ysl_el)
    #ysl_all.extend(ysl_line)
    #определим интервал пропорциональный его интенсивности отказа всех элементов сети
    diaposon = [0]
    for i,ysl in enumerate(ysl_all):
        diaposon.append(diaposon[i] + ysl)
    diaposon[-1] = 1
    return diaposon
def find_index(paths, el):
    indexes = [(ix, iy) for ix, row in enumerate(paths) for iy, i in enumerate(row) if i == el]
    return indexes
def find_index_of_diaposon(diaposon,n):
    for i, d in enumerate(diaposon):  # i - 1 является номером отказавшего элемента
        if n < diaposon[i]:
            return i-1
    return None

def find_otk_elements(diaposon, paths):
    otk_elements = set()
    tmp_paths = paths.copy()
    cond = set()
    for i in range(len(paths)):
        cond.add(i)
    set_index = set()
    while set_index != cond:
        ksi = random.uniform(0, 1)
        ind_otk_ela = find_index_of_diaposon(diaposon,ksi)
        for el in find_index(tmp_paths, ind_otk_ela):
            set_index.add(el[0])
            otk_elements.add(ind_otk_ela)
    return otk_elements
#def Modeling(diaposon, paths, N):
#    # генерируем случайную величину
#    for i in range(10000):
#        ksi = random.uniform(0,1)
#
#    return ksi
if __name__ == "__main__":
    diaposon = Diaposon(int_otk_el, int_otk_line)

    src = 2
    dst = 3
    paths = findpaths(ring_structure, src, dst, properties.n_vertex)
    for i in range(10000):
        otk_elements = find_otk_elements(diaposon, paths)
        print(i)
        print(otk_elements)

    #print(ysl_el)
    #print("\n")
    #print(ysl_line)