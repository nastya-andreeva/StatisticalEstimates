import math
import numpy as np
import matplotlib.pyplot as plt


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

n = int(round((1.96 ** 2 * sko ** 2) / (delta ** 2), 0))

n_selection = 36
lst_mean = []

for _ in range(n_selection):
    selection = list(np.random.choice(data, size=n, replace=True))
    lst_mean += [find_mean(selection, n)]

min_ind = math.floor(min(lst_mean))
max_ind = math.ceil(max(lst_mean))

bins = np.arange(min_ind, max_ind + 1, 1)

hist = [0] * (len(bins) - 1)
for mean_v in lst_mean:
    for i in range(1, len(bins)):
        if bins[i - 1] <= mean_v < bins[i]:
            hist[i - 1] += 1
            break
print(hist)

rel_freq = [h / len(lst_mean) for h in hist]

print(rel_freq)

plt.hist(lst_mean, bins=bins, edgecolor='black')
plt.show()
