import itertools
import random

import lineStructure
import properties
import ringStructure
import treeStructure
from BFC import findpaths
from ringStructure import int_otk_el, int_otk_line, ring_structure
from lineStructure import int_otk_el, int_otk_line, line_structure
from treeStructure import int_otk_el, int_otk_line, tree_structure
import matplotlib.pyplot as plt

import numpy as np
import collections
import math
import operator
import functools
import decimal


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
    for el, line in zip(ysl_el, ysl_line):
        ysl_all.append(el)
        ysl_all.append(line)
    #ysl_all.extend(ysl_el)
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
    ksi_set = []
    cond = set()
    for i in range(len(paths)):
        cond.add(i)
    set_index = set()
    while set_index != cond:
        ksi = random.uniform(0, 1)
        ind_otk_ela = find_index_of_diaposon(diaposon,ksi)
        for el in find_index(tmp_paths, ind_otk_ela):
            set_index.add(el[0])
            if ind_otk_ela not in otk_elements:
                otk_elements.add(ind_otk_ela)
                ksi_set.append(ksi)

    return (ksi_set, list(otk_elements))

def time_from_ksi(ksi, method=0, intensivnost=[], otk_el=[]):
    time = []
    for count,i in enumerate(ksi):
        time.append(-1/intensivnost[otk_el[count]] * np.log(i)*1000000)
    return sum(time)
def P(t, paths, intensiv):
    P_C = 1
    p_lam = 1
    p = []
    k = dict()
    no_of_lists_per_name = collections.Counter(itertools.chain.from_iterable(map(set, paths)))

    for name, no_of_lists in no_of_lists_per_name.most_common():
        k[name] = no_of_lists
    for path in paths:
        for el in path:
            p_lam *= math.pow(math.e, intensiv[el]*t/(k[el]*1000000))
        p.append(1 - p_lam)

        mul = functools.reduce(operator.mul, p)
    P_C = 1 - mul
    return P_C
#def Modeling(diaposon, paths, N):
#    # генерируем случайную величину
#    for i in range(10000):
#        ksi = random.uniform(0,1)
#
#    return ksi
if __name__ == "__main__":
    P_SYS = 0
    min_time = 0
    max_time = 0
    sred_narabotka_na_otkaz = 0
    all_intensiv=[]
    gistagramma = list()
    otk_elem_failure = list()
    diaposon = Diaposon(treeStructure.int_otk_el, treeStructure.int_otk_line)
    for el, line in zip(treeStructure.int_otk_el, treeStructure.int_otk_line):
        all_intensiv.append(el)
        all_intensiv.append(line)
    #all_intensiv.extend(ringStructure.int_otk_el)
    #all_intensiv.extend(ringStructure.int_otk_line)
    src = 2
    dst = 4
    N = 10000
    paths = findpaths(tree_structure, src, dst, properties.n_vertex)
    for i in range(N):
        (ksi,otk_elements) = find_otk_elements(diaposon, paths)
        time_otkaza = time_from_ksi(ksi=ksi, intensivnost=all_intensiv, otk_el=otk_elements)
        gistagramma.append(time_otkaza)
        #print(otk_elements)
        #print(time_otkaza)
    print(len(gistagramma))
    P_SYS = 1 - sum(gistagramma)/len(gistagramma)
    sred_narabotka_na_otkaz = sum(gistagramma)/len(gistagramma)
    min_time = min(gistagramma)
    max_time = max(gistagramma)
    print(paths)
    print(P_SYS)
    print(sred_narabotka_na_otkaz)
    print(min_time)
    print(max_time)
    #gistagramma = [int(i*1000) for i in gistagramma]
    #print(gistagramma)
    # выведим гистограмму времен отказов сети связи
    P_CH = []
    tim = []
    for t in range(700):
        tim.append(t)
        P_CH.append(P(t,paths,all_intensiv))
    plt.figure(1)
    plt.plot(tim, P_CH)
    plt.figure(2)
    plt.hist(gistagramma, bins=100)
    plt.show()

    #print(ysl_el)
    #print("\n")
    #print(ysl_line)