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
def FIFO_Vost(diaposon, paths, all_intensiv, mu):
    otk_elements = set()
    tmp_paths = paths.copy()
    ksi_set = []
    vostanov = []
    all_index = []
    time_otk = []
    time_vost = []
    cond = set()
    ksi = []
    for i in range(len(paths)):
        cond.add(i)
    set_index = set()
    while set_index != cond:
        if vostanov:
            all_index.extend(vostanov)
            for i,j in zip(ksi,vostanov):  # не забудь почистить массивы
                time_otk.append(time_from_ksi(ksi=[i], intensivnost=all_intensiv, otk_el=list(otk_elements)))
                time_vost.append(time_vostanov([i],mu))
                otk_elements.remove(j)
            vostanov.clear()
            ksi.clear()
        numb_otk = random.randint(1,2)
        for i in range(numb_otk):
            ksi.append(random.uniform(0, 1))
        for i in ksi:# не забудь почистить массивы
            ind_otk_ela = find_index_of_diaposon(diaposon, i)
            for el in find_index(tmp_paths, ind_otk_ela):
                set_index.add(el[0])
                if ind_otk_ela not in otk_elements:
                    otk_elements.add(ind_otk_ela)
                    ksi_set.append(i)
                    vostanov.append(ind_otk_ela)
        if set_index == cond:
            all_index.extend(vostanov)
            for i, j in zip(ksi, vostanov):
                time_otk.append(time_from_ksi(ksi=[i], intensivnost=all_intensiv, otk_el=list(otk_elements)))
                time_vost.append(time_vostanov([i], mu))

    return (time_otk, time_vost, all_index)
def MIN_Vost(diaposon, paths, all_intensiv, mu):
    otk_elements = set()
    tmp_paths = paths.copy()
    ksi_set = []
    vostanov = []
    all_index = []
    time_otk = []
    time_vost = []
    cond = set()
    ksi = []
    for i in range(len(paths)):
        cond.add(i)
    set_index = set()
    while set_index != cond:
        if vostanov:
            all_index.extend(vostanov)
            vostanov.sort(reverse=True)
            for i,j in zip(ksi,vostanov):
                time_otk.append(time_from_ksi(ksi=[i], intensivnost=all_intensiv, otk_el=list(otk_elements)))
                time_vost.append(time_vostanov([i],mu))
                otk_elements.remove(j)
            vostanov.clear()
            ksi.clear()
        numb_otk = random.randint(1,2)
        for i in range(numb_otk):
            ksi.append(random.uniform(0, 1))
        for i in ksi:# не забудь почистить массивы
            ind_otk_ela = find_index_of_diaposon(diaposon, i)
            for el in find_index(tmp_paths, ind_otk_ela):
                set_index.add(el[0])
                if ind_otk_ela not in otk_elements:
                    otk_elements.add(ind_otk_ela)
                    ksi_set.append(i)
                    vostanov.append(ind_otk_ela)
        if set_index == cond:
            all_index.extend(vostanov)
            vostanov.sort(reverse=True)
            for i, j in zip(ksi, vostanov):
                time_otk.append(time_from_ksi(ksi=[i], intensivnost=all_intensiv, otk_el=list(otk_elements)))
                time_vost.append(time_vostanov([i], mu))

    return (time_otk, time_vost, all_index)
def MAX_Vost(diaposon, paths, all_intensiv, mu):
    otk_elements = set()
    tmp_paths = paths.copy()
    ksi_set = []
    vostanov = []
    all_index = []
    time_otk = []
    time_vost = []
    cond = set()
    ksi = []
    for i in range(len(paths)):
        cond.add(i)
    set_index = set()
    while set_index != cond:
        if vostanov:
            all_index.extend(vostanov)
            vostanov.sort()
            for i,j in zip(ksi,vostanov):
                time_otk.append(time_from_ksi(ksi=[i], intensivnost=all_intensiv, otk_el=list(otk_elements)))
                time_vost.append(time_vostanov([i],mu))
                otk_elements.remove(j)
            vostanov.clear()
            ksi.clear()
        numb_otk = random.randint(1,2)
        for i in range(numb_otk):
            ksi.append(random.uniform(0, 1))
        for i in ksi:# не забудь почистить массивы
            ind_otk_ela = find_index_of_diaposon(diaposon, i)
            for el in find_index(tmp_paths, ind_otk_ela):
                set_index.add(el[0])
                if ind_otk_ela not in otk_elements:
                    otk_elements.add(ind_otk_ela)
                    ksi_set.append(i)
                    vostanov.append(ind_otk_ela)
        if set_index == cond:
            all_index.extend(vostanov)
            vostanov.sort()
            for i, j in zip(ksi, vostanov):
                time_otk.append(time_from_ksi(ksi=[i], intensivnost=all_intensiv, otk_el=list(otk_elements)))
                time_vost.append(time_vostanov([i], mu))

    return (time_otk, time_vost, all_index)
def ESSENT_Vost(diaposon, paths, all_intensiv, mu):
    otk_elements = set()
    tmp_paths = paths.copy()
    ksi_set = []
    vostanov = []
    all_index = []
    time_otk = []
    time_vost = []
    cond = set()
    ksi = []
    for i in range(len(paths)):
        cond.add(i)
    set_index = set()
    while set_index != cond:
        if vostanov:
            all_index.extend(vostanov)
            for i,j in zip(ksi,vostanov):
                time_otk.append(time_from_ksi(ksi=[i], intensivnost=all_intensiv, otk_el=list(otk_elements)))
                time_vost.append(time_vostanov([i],mu))
                otk_elements.remove(j)
            vostanov.clear()
            ksi.clear()
        numb_otk = random.randint(1,2)
        for i in range(numb_otk):
            ksi.append(random.uniform(0, 1))
        for i in ksi:# не забудь почистить массивы
            ind_otk_ela = find_index_of_diaposon(diaposon, i)
            for el in find_index(tmp_paths, ind_otk_ela):
                set_index.add(el[0])
                if ind_otk_ela not in otk_elements:
                    otk_elements.add(ind_otk_ela)
                    ksi_set.append(i)
                if ind_otk_ela in paths:
                    vostanov.append(ind_otk_ela)
        if set_index == cond:
            all_index.extend(vostanov)
            for i, j in zip(ksi, vostanov):
                time_otk.append(time_from_ksi(ksi=[i], intensivnost=all_intensiv, otk_el=list(otk_elements)))
                time_vost.append(time_vostanov([i], mu))

    return (time_otk, time_vost, all_index)
def time_from_ksi(ksi, intensivnost=[], otk_el=[]): # Время отказа элемента
    time = []
    for count,i in enumerate(ksi):
        time.append(-1/intensivnost[otk_el[count]] * np.log(i)*1000000)
    return sum(time)
def time_vostanov(ksi, mu):
    time = []
    for count, i in enumerate(ksi):
        time.append(-1 / mu * np.log(i))
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
            p_lam *= math.pow(math.e, -intensiv[el]*t/(k[el]*1000000))
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
    diagramma = dict()
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
    mu = 0.01
    method = 3
    dic_d = dict()
    dic_s = dict()

    if method == 0:
        paths = findpaths(tree_structure, src, dst, properties.n_vertex)
        for i in range(N):
            (ksi,otk_elements) = find_otk_elements(diaposon, paths)
            time_otkaza = time_from_ksi(ksi=ksi, intensivnost=all_intensiv, otk_el=otk_elements)
            gistagramma.append(time_otkaza)
            #print(otk_elements)
            #print(time_otkaza)
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
        for t in range(20000):
            tim.append(t)
            P_CH.append(P(t,paths,all_intensiv))
        plt.figure(1)
        plt.plot(tim, P_CH)
        plt.figure(2)
        plt.hist(gistagramma, bins=100)
        plt.show()
    elif method == 1:
        suma = []
        av_time_otk = []
        av_time_vost = []
        large_diag = 0
        large_otkaz = []
        large_vost = []
        large_ind = []
        paths = findpaths(tree_structure, src, dst, properties.n_vertex)
        for i in range(N):
            (time_otkaza, time_vosta, indexes) = FIFO_Vost(diaposon, paths, all_intensiv, mu)
            av_time_otk.append(sum(time_otkaza))
            av_time_vost.append(sum(time_vosta))
            for i,j in zip(time_otkaza, time_vosta):
                suma.append(i+j)
            gistagramma.append(sum(suma))
        P_SYS = 1 - sum(gistagramma) / len(gistagramma)
        tmp_otk = sum(av_time_otk) / len(av_time_otk)
        tmp_vost = sum(time_vosta) / len(time_vosta)
        Koeff_Gotov = (tmp_otk)/(tmp_otk+tmp_vost)
        sred_narabotka_na_otkaz = sum(gistagramma) / len(gistagramma)
        min_time = min(gistagramma)
        max_time = max(gistagramma)
        print(paths)
        print(P_SYS)
        print(sred_narabotka_na_otkaz)
        print(min_time)
        print(max_time)
        print(Koeff_Gotov)
        # gistagramma = [int(i*1000) for i in gistagramma]
        # print(gistagramma)
        # выведим гистограмму времен отказов сети связи
        P_CH = []
        tim = []
        for t in range(20000):
            tim.append(t)
            P_CH.append(P(t, paths, all_intensiv))
        plt.figure(1)
        plt.plot(tim, P_CH)
        plt.figure(2)
        plt.hist(gistagramma, bins=100)
        plt.show()
    elif method == 2:
        suma = []
        large_diag = 0
        large_otkaz = []
        large_vost = []
        large_ind = []
        av_time_otk = []
        av_time_vost = []
        paths = findpaths(tree_structure, src, dst, properties.n_vertex)
        for i in range(N):
            (time_otkaza, time_vosta, indexes) = MIN_Vost(diaposon, paths, all_intensiv, mu)
            av_time_otk.append(sum(time_otkaza))
            av_time_vost.append(sum(time_vosta))
            for i, j in zip(time_otkaza, time_vosta):
                suma.append(i + j)
            gistagramma.append(sum(suma))
        P_SYS = 1 - sum(gistagramma) / len(gistagramma)
        tmp_otk = sum(av_time_otk) / len(av_time_otk)
        tmp_vost = sum(time_vosta) / len(time_vosta)
        Koeff_Gotov = (tmp_otk) / (tmp_otk + tmp_vost)
        sred_narabotka_na_otkaz = sum(gistagramma) / len(gistagramma)
        min_time = min(gistagramma)
        max_time = max(gistagramma)
        print(paths)
        print(P_SYS)
        print(sred_narabotka_na_otkaz)
        print(min_time)
        print(max_time)
        print(Koeff_Gotov)
        # выведим гистограмму времен отказов сети связи
        P_CH = []
        tim = []
        for t in range(20000):
            tim.append(t)
            P_CH.append(P(t, paths, all_intensiv))
        plt.figure(1)
        plt.plot(tim, P_CH)
        plt.figure(2)
        plt.hist(gistagramma, bins=100)
        plt.show()
    elif method == 3:
        suma = []
        large_diag = 0
        large_otkaz = []
        large_vost = []
        large_ind = []
        av_time_otk = []
        av_time_vost = []
        paths = findpaths(tree_structure, src, dst, properties.n_vertex)
        for i in range(N):
            (time_otkaza, time_vosta, indexes) = MAX_Vost(diaposon, paths, all_intensiv, mu)
            av_time_otk.append(sum(time_otkaza))
            av_time_vost.append(sum(time_vosta))
            for i, j in zip(time_otkaza, time_vosta):
                suma.append(i + j)
            gistagramma.append(sum(suma))
        P_SYS = 1 - sum(gistagramma) / len(gistagramma)
        tmp_otk = sum(av_time_otk) / len(av_time_otk)
        tmp_vost = sum(time_vosta) / len(time_vosta)
        Koeff_Gotov = (tmp_otk) / (tmp_otk + tmp_vost)
        sred_narabotka_na_otkaz = sum(gistagramma) / len(gistagramma)
        min_time = min(gistagramma)
        max_time = max(gistagramma)
        print(paths)
        print(P_SYS)
        print(sred_narabotka_na_otkaz)
        print(min_time)
        print(max_time)
        print(Koeff_Gotov)
        # выведим гистограмму времен отказов сети связи
        P_CH = []
        tim = []
        for t in range(20000):
            tim.append(t)
            P_CH.append(P(t, paths, all_intensiv))
        plt.figure(1)
        plt.plot(tim, P_CH)
        plt.figure(2)
        plt.hist(gistagramma, bins=100)
        plt.show()
    elif method == 4:
        suma = []
        large_diag = 0
        large_otkaz = []
        large_vost = []
        large_ind = []
        av_time_otk = []
        av_time_vost = []
        paths = findpaths(ring_structure, src, dst, properties.n_vertex)
        for i in range(N):
            (time_otkaza, time_vosta, indexes) = ESSENT_Vost(diaposon, paths, all_intensiv, mu)
            av_time_otk.append(sum(time_otkaza))
            av_time_vost.append(sum(time_vosta))
            for i, j in zip(time_otkaza, time_vosta):
                suma.append(i + j)
            gistagramma.append(sum(suma))
        P_SYS = 1 - sum(gistagramma) / len(gistagramma)
        tmp_otk = sum(av_time_otk) / len(av_time_otk)
        tmp_vost = sum(av_time_vost) / len(av_time_vost)
        #Koeff_Gotov = (tmp_otk) / (tmp_otk + tmp_vost)
        sred_narabotka_na_otkaz = sum(gistagramma) / len(gistagramma)
        min_time = min(gistagramma)
        max_time = max(gistagramma)
        print(paths)
        print(P_SYS)
        print(sred_narabotka_na_otkaz)
        print(min_time)
        print(max_time)
        #print(Koeff_Gotov)
        # выведим гистограмму времен отказов сети связи
        P_CH = []
        tim = []
        for t in range(20000):
            tim.append(t)
            P_CH.append(P(t, paths, all_intensiv))
        plt.figure(1)
        plt.plot(tim, P_CH)
        plt.figure(2)
        plt.hist(gistagramma, bins=100)
        plt.show()
    #print(ysl_el)
    #print("\n")
    #print(ysl_line)