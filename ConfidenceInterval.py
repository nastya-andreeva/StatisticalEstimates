from scipy.stats import t

import math
import numpy as np


def average(data):
    return sum(data)/len(data)


def variance(data):
    av = average(data)
    un_data = set(data)
    ages = []
    freq = []
    for i in un_data:
        ages += [i]
        freq += [data.count(i)]
    var = sum([(ages[i] - av) ** 2 * freq[i] for i in range(len(un_data))]) / sum(freq)
    return var


def quar_mean(data):
    return math.sqrt(variance(data))


def find_mean(selection, n):
    sel_uniq = set(selection)
    lst = list(sel_uniq)
    s = 0
    for i in range(len(sel_uniq)):
        s += lst[i] * selection.count(lst[i])
    return s / n


file_path = "Москва_2021.txt"
with open(file_path, 'r') as file:
    data = file.read().splitlines()
data = list(map(int, data))

gamma = 0.95
delta = 3

sko = quar_mean(data)


def find_mean(selection, n):
    sel_uniq = set(selection)
    lst = list(sel_uniq)
    s = 0
    for i in range(len(sel_uniq)):
        s += lst[i] * selection.count(lst[i])
    return s / n


def find_std(selection, n, mean):
    sel_uniq = set(selection)
    lst = list(sel_uniq)
    s = 0
    for i in range(len(sel_uniq)):
        s += (lst[i] - mean) ** 2 * selection.count(lst[i])
    return math.sqrt(s / (n - 1))


n = int(round((1.96 ** 2 * sko ** 2) / (delta ** 2), 0))

n_selection = 36
lst_mean = []


selection = list(np.random.choice(data, size=n, replace=True))

gamma = 0.95
n = len(selection)
a = 1 - gamma
sel_mean = find_mean(selection, 62)
sel_std = find_std(selection, n, sel_mean)

t_a = t.ppf(1 - a / 2, df=n - 1)
ind1 = sel_mean - t_a * (sel_std / np.sqrt(n))
ind2 = sel_mean + t_a * (sel_std / np.sqrt(n))
delta = t_a * sel_std / math.sqrt(n)

print('выборочное среднее', sel_mean)
print('доверительный интервал', ind1, ind2)
print(delta)

