#  Biologia Computacional 2019/2 - Lista de Exercícios 1

#  Aluno: Leonardo Oliveira Wellausen

#  Questão 1d

cromo = open('sequence.fasta','r').read().replace('\n', '')

possible_nucs = list('CATG')
nucleotideos = {}

for i in range(len(cromo)):
    try:
        nucleotideos[cromo[i]] += 1
    except:
        nucleotideos[cromo[i]] = 1


for nuc in possible_nucs:
    print('Número de ocorrências do nucleotídeo ', nuc, ': ', nucleotideos[nuc], '.')


for char in [c for c in list(nucleotideos.keys()) if c not in possible_nucs]:
    print('Caracter diferente encontrado: ', char, ' . Sua contagem:', nucleotideos[char], '.')

