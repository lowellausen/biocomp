from random import choices
import numpy as np
from copy import deepcopy


def different_cs(cs1, cs2):
    for i in range(len(cs1)):
        for j in range(1, len(cs1[0])):
            if cs1[i][j] != cs2[i][j]:
                return True
    return False


def dist(sample, c):
    return np.linalg.norm(np.subtract(sample[1:], c[1:]))


def eval_group(group):
    labels = {'AML': 0, 'ALL': 0}
    for sample in group:
        labels[sample[0]] += 1

    return labels


def evalprint_group(group):
    labels = {'AML': 0, 'ALL': 0}
    for sample in group:
        labels[sample[0]] += 1

    print('Número de indivíduos no grupo: ', len(group), '. Sendo ', labels['ALL'], ' ALL e ', labels['AML'],  ' AML.')


def kmeans(samples, k):
    cs = list(choices(samples, k=k))
    prev_cs = [[np.inf for i in range(len(samples[0]))] for j in range(k)]
    gs = [[] for i in range(k)]
    while different_cs(cs, prev_cs):
        gs = [[] for i in range(k)]
        sums = [[0 for j in range(len(samples[0]) - 1)] for i in range(k)]
        counts = [0 for i in range(k)]

        for sample in samples:
            dists = [dist(sample, c) for c in cs]
            mindist = dists.index(min(dists))

            gs[mindist].append(sample)
            sums[mindist] = np.add(sums[mindist], sample[1:])
            counts[mindist] += 1

        prev_cs = deepcopy(cs)

        for i in range(k):
            cs[i][1:] = np.divide(sums[i], counts[i])

    return gs


lines = open('leukemia_big.csv', 'r').read().splitlines()
n_samples = len(lines[0].split(','))

labels = lines.pop(0).split(',')

samples = []

for i in range(n_samples):
    this_line = [labels[i]]
    for line in lines:
        l = line.split(',')
        this_line.append(float(l[i]))
    samples.append(this_line)


leuks = {'AML': 0, 'ALL': 0}
for label in labels:
    leuks[label] += 1

print('Rodando para 2 grupos:')

best_score = np.inf
best_model = None
for i in range(1):
    groups = kmeans(samples, 2)

    e0 = eval_group(groups[0])
    e1 = eval_group(groups[1])

    erro = 0

    if e0['ALL'] >= e0['AML']:
        erro += e0['AML']
        erro += e1['ALL']
    else:
        erro += e1['AML']
        erro += e0['ALL']

    if erro <= best_score:
        best_score = erro
        best_model = groups

print('Número real de ALL: ', leuks['ALL'], '. Número real de AML: ', leuks['AML'])
for i, group in enumerate(best_model):
    print('Grupo ', i+1, ':')
    evalprint_group(group)


print('Rodando para 3 grupos: ')
for i in range(1):
    groups = kmeans(samples, 3)


    print('Número real de ALL: ', leuks['ALL'], '. Número real de AML: ', leuks['AML'])
    for i, group in enumerate(groups):
        print('Grupo ', i+1, ':')
        evalprint_group(group)

