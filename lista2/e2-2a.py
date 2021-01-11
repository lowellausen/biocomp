import numpy as np
import sys

hemos = {}

hemos['human'] =   'VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKY'
hemos['horse'] =   'VLSAADKTNVKAAWSKVGGHAGEYGAEALERMFLGFPTTKTYFPHFDLSHGSAQVKAHGKKVGDALTLAVGHLDDLPGALSNLSDLHAHKLRVDPVNFKLLSHCLLSTLAVHLPNDFTPAVHASLDKFLSSVSTVLTSKYR'
hemos['deer'] =    'VLSAANKSNVKAAWGKVGGNAPAYGAQALQRMFLSFPTTKTYFPHFDLSHGSAQQKAHGQKVANALTKAQGHLNDLPGTLSNLSNLHAHKLRVNPVNFKLLSHSLLVTLASHLPTNFTPAVHANLNKFLANDSTVLTSKYR'
hemos['cow'] =     'VLSAADKGNVKAAWGKVGGHAAEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGAKVAAALTKAVEHLDDLPGALSELSDLHAHKLRVDPVNFKLLSHSLLVTLASHLPSDFTPAVHASLDKFLANVSTVLTSKYR'
hemos['pig'] =     'VLSAADKANVKAAWGKVGGQAGAHGAEALERMFLGFPTTKTYFPHFNLSHGSDQVKAHGQKVADALTKAVGHLDDLPGALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHHPDDFNPSVHASLDKFLANVSTVLTSKYR'
hemos['wolf'] =    'VLSPADKTNIKSTWDKIGGHAGDYGGEALDRTFQSFPTTKTYFPHFDLSPGSAQVKAHGKKVADALTTAVAHLDDLPGALSALSDLHAYKLRVDPVNFKLLSHCLLVTLACHHPTEFTPAVHASLDKFFTAVSTVLTSKYR'
hemos['chicken'] = 'MLTAEDKKLIQQAWEKAASHQEEFGAEALTRMFTTYPQTKTYFPHFDLSPGSDQVRGHGKKVLGALGNAVKNVDNLSQAMAELSNLHAYNLRVDPVNFKLLSQCIQVVLAVHMGKDYTPEVHAAFDKFLSAVSAVLAEKYR'
hemos['trout'] =   'MSLTAKDKSVVKAFWGKISGKADVVGAEALGRMLTAYPQTKTYFSHWADLSPGSGPVKKHGGIIMGAIGKAVGLMDDLVGGMSALSDLHAFKLRVDPGNFKILSHNILVTLAIHFPSDFTPEVHIAVDKFLAAVSAALADKYR'


blos = {
frozenset(['A','A']):4,
frozenset(['A','R']):-1,
frozenset(['R','R']):5,
frozenset(['N','A']):-2,
frozenset(['N','R']):0,
frozenset(['N','N']):6,
frozenset(['D','A']):-2,
frozenset(['D','R']):-2,
frozenset(['D','N']):1,
frozenset(['D', 'D']):6,
frozenset(['C','A']):0,
frozenset(['C','R']):-3,
frozenset(['C','N']):-3,
frozenset(['C', 'D']):-3,
frozenset(['C','C']):9,
frozenset(['Q','A']):-1,
frozenset(['Q','R']):1,
frozenset(['Q','N']):0,
frozenset(['Q', 'D']):0,
frozenset(['Q','C']):-3,
frozenset(['Q','Q']):5,
frozenset(['E','A']):-1,
frozenset(['E','R']):0,
frozenset(['E','N']):0,
frozenset(['E', 'D']):2,
frozenset(['E','C']):-4,
frozenset(['E','Q']):2,
frozenset(['E','E']):5,
frozenset(['G','A']):0,
frozenset(['G','R']):-2,
frozenset(['G','N']):0,
frozenset(['G', 'D']):-1,
frozenset(['G','C']):-3,
frozenset(['G','Q']):-2,
frozenset(['G','E']):-2,
frozenset(['G','G']):6,
frozenset(['H','A']):-2,
frozenset(['H','R']):0,
frozenset(['H','N']):1,
frozenset(['H', 'D']):-1,
frozenset(['H','C']):-3,
frozenset(['H','Q']):0,
frozenset(['H','E']):0,
frozenset(['H','G']):-2,
frozenset(['H','H']):8,
frozenset(['I','A']):-1,
frozenset(['I','R']):-3,
frozenset(['I','N']):-3,
frozenset(['I', 'D']):-3,
frozenset(['I','C']):-1,
frozenset(['I','Q']):-3,
frozenset(['I','E']):-3,
frozenset(['I','G']):-4,
frozenset(['I','H']):-3,
frozenset(['I','I']):4,
frozenset(['L','A']):-1,
frozenset(['L','R']):-2,
frozenset(['L','N']):-3,
frozenset(['L', 'D']):-4,
frozenset(['L','C']):-1,
frozenset(['L','Q']):-2,
frozenset(['L','E']):-3,
frozenset(['L','G']):-4,
frozenset(['L','H']):-3,
frozenset(['L','I']):2,
frozenset(['L','L']):4,
frozenset(['K','A']):-1,
frozenset(['K','R']):2,
frozenset(['K','N']):0,
frozenset(['K', 'D']):-1,
frozenset(['K','C']):-3,
frozenset(['K','Q']):1,
frozenset(['K','E']):1,
frozenset(['K','G']):-2,
frozenset(['K','H']):-1,
frozenset(['K','I']):-3,
frozenset(['K','L']):-2,
frozenset(['K','K']):5,
frozenset(['M', 'A']): -1,
frozenset(['M', 'R']): -1,
frozenset(['M', 'N']): -2,
frozenset(['M', 'D']): -3,
frozenset(['M', 'C']): -1,
frozenset(['M', 'Q']): 0,
frozenset(['M', 'E']): -2,
frozenset(['M', 'G']): -3,
frozenset(['M', 'H']): -2,
frozenset(['M', 'I']): 1,
frozenset(['M', 'L']): 2,
frozenset(['M', 'K']): -1,
frozenset(['M', 'M']): 5,
frozenset(['F', 'A']): -2,
frozenset(['F', 'R']): -3,
frozenset(['F', 'N']): -3,
frozenset(['F', 'D']): -3,
frozenset(['F', 'C']): -2,
frozenset(['F', 'Q']): -3,
frozenset(['F', 'E']): -3,
frozenset(['F', 'G']): -3,
frozenset(['F', 'H']): -1,
frozenset(['F', 'I']): 0,
frozenset(['F', 'L']): 0,
frozenset(['F', 'K']): -3,
frozenset(['F', 'M']): 0,
frozenset(['F', 'F']): 6,
frozenset(['P', 'A']): -1,
frozenset(['P', 'R']): -2,
frozenset(['P', 'N']): -2,
frozenset(['P', 'D']): -1,
frozenset(['P', 'C']): -3,
frozenset(['P', 'Q']): -1,
frozenset(['P', 'E']): -1,
frozenset(['P', 'G']): -2,
frozenset(['P', 'H']): -2,
frozenset(['P', 'I']): -3,
frozenset(['P', 'L']): -3,
frozenset(['P', 'K']): -1,
frozenset(['P', 'M']): -2,
frozenset(['P', 'F']): -4,
frozenset(['P', 'P']): 7,
frozenset(['S', 'A']):  1,
frozenset(['S', 'R']): -1,
frozenset(['S', 'N']):  1,
frozenset(['S', 'D']):  0,
frozenset(['S', 'C']): -1,
frozenset(['S', 'Q']): 0,
frozenset(['S', 'E']): 0,
frozenset(['S', 'G']): 0,
frozenset(['S', 'H']): -1,
frozenset(['S', 'I']): -2,
frozenset(['S', 'L']): -2,
frozenset(['S', 'K']): 0,
frozenset(['S', 'M']): -1,
frozenset(['S', 'F']): -2,
frozenset(['S', 'P']): -1,
frozenset(['S', 'S']): 4,
frozenset(['T', 'A']): 0,
frozenset(['T', 'R']): -1,
frozenset(['T', 'N']): 0,
frozenset(['T', 'D']): -1,
frozenset(['T', 'C']): -1,
frozenset(['T', 'Q']): -1,
frozenset(['T', 'E']): -1,
frozenset(['T', 'G']): -2,
frozenset(['T', 'H']): -2,
frozenset(['T', 'I']): -1,
frozenset(['T', 'L']): -1,
frozenset(['T', 'K']): -1,
frozenset(['T', 'M']): -1,
frozenset(['T', 'F']): -2,
frozenset(['T', 'P']): -1,
frozenset(['T', 'S']): 1,
frozenset(['T', 'T']): 5,
frozenset(['W', 'A']): -3,
frozenset(['W', 'R']): -3,
frozenset(['W', 'N']): -4,
frozenset(['W', 'D']): -4,
frozenset(['W', 'C']): -2,
frozenset(['W', 'Q']): -2,
frozenset(['W', 'E']): -3,
frozenset(['W', 'G']): -2,
frozenset(['W', 'H']): -2,
frozenset(['W', 'I']): -3,
frozenset(['W', 'L']): -2,
frozenset(['W', 'K']): -3,
frozenset(['W', 'M']): -1,
frozenset(['W', 'F']): 1,
frozenset(['W', 'P']): -4,
frozenset(['W', 'S']): -3,
frozenset(['W', 'T']): -2,
frozenset(['W', 'W']): 11,
frozenset(['Y', 'A']): -2,
frozenset(['Y', 'R']): -2,
frozenset(['Y', 'N']): -2,
frozenset(['Y', 'D']): -3,
frozenset(['Y', 'C']): -2,
frozenset(['Y', 'Q']): -1,
frozenset(['Y', 'E']): -2,
frozenset(['Y', 'G']): -3,
frozenset(['Y', 'H']): 2,
frozenset(['Y', 'I']): -1,
frozenset(['Y', 'L']): -1,
frozenset(['Y', 'K']): -2,
frozenset(['Y', 'M']): -1,
frozenset(['Y', 'F']): 3,
frozenset(['Y', 'P']): -3,
frozenset(['Y', 'S']): -2,
frozenset(['Y', 'T']): -2,
frozenset(['Y', 'W']): 2,
frozenset(['Y', 'Y']): 7,
frozenset(['V','A']):0,
frozenset(['V','R']):-3,
frozenset(['V','N']): -3,
frozenset(['V','D']): -3,
frozenset(['V','C']): -1,
frozenset(['V','Q']): -2,
frozenset(['V','E']): -2,
frozenset(['V','G']): -3,
frozenset(['V','H']): -3,
frozenset(['V', 'I']): 3,
frozenset(['V', 'L']): 1,
frozenset(['V', 'K']): -2,
frozenset(['V', 'M']): 1,
frozenset(['V', 'F']): -1,
frozenset(['V', 'P']): -2,
frozenset(['V', 'S']): -2,
frozenset(['V', 'T']): 0,
frozenset(['V', 'W']): -3,
frozenset(['V', 'Y']): -1,
frozenset(['V', 'V']): 4
        }

print('Opções de entrada: human, horse, deer, cow, pig, wolf, chicken, trout')
word1 = input("Entre uma espécie: ")
word2 = input("Entre outra espécie: ")

word1 = list(hemos[word1])
word2 = list(hemos[word2])

size1 = len(word1)
size2 = len(word2)

gap = -4

matrix = np.zeros((size1 + 1, size2 + 1))

def blos_matching(a, b):
    return blos[frozenset([a, b])]


for i in range(size1 + 1):
    matrix[i][0] = gap*i

for i in range(size2 + 1):
    matrix[0][i] = gap*i

for i in range(1, size1 + 1):
    for j in range(1, size2 + 1):
        matrix[i][j] = max(blos_matching(word2[j-1], word1[i-1]) + matrix[i-1][j-1], gap + matrix[i-1][j], gap + matrix[i][j-1])

res1 = ''
res2 = ''

i = size1
j = size2

matches = 0

while i!=0 and j!=0:
    up = matrix[i-1][j]
    left = matrix[i][j-1]
    diag = matrix[i-1][j-1]

    if diag >= up and diag >= left:
        res1 += word1[i-1]
        res2 += word2[j-1]
        i -= 1
        j -= 1
        if word1[i] == word2[j]:
            matches += 1
    elif up >= diag and up >= left:
        res1 += word1[i-1]
        res2 += '-'
        i -= 1
    else:
        res1 += '-'
        res2 += word2[j-1]
        j -= 1

res1 = res1[::-1]
res2 = res2[::-1]

print('\n\nTabela de alinhamento:')
print(matrix)


print('\n\nCadeias alinhadas:')
print(res1)
print(res2)

print('\nIdentidade do alinhamento: %2.2f' % (matches/size2*100) + '%')
print('\nScore do alinhamento: %d' % (matrix[size1][size2]))


