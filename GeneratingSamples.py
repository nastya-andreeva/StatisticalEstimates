import math
import numpy as np
from scipy.stats import t


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
t_a = 1.96

n = int(round((t_a ** 2 * sko ** 2) / (delta ** 2), 0))
print('объем выборки:', n)

n_selection = 36
lst_mean = []

for _ in range(n_selection):
    selection = list(np.random.choice(data, size=n, replace=True))
    lst_mean += [find_mean(selection, n)]

print(*lst_mean, sep='\n')


