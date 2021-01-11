import numpy as np

hemos = {}

hemos['human'] =   'VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKY'
hemos['horse'] =   'VLSAADKTNVKAAWSKVGGHAGEYGAEALERMFLGFPTTKTYFPHFDLSHGSAQVKAHGKKVGDALTLAVGHLDDLPGALSNLSDLHAHKLRVDPVNFKLLSHCLLSTLAVHLPNDFTPAVHASLDKFLSSVSTVLTSKYR'
hemos['deer'] =    'VLSAANKSNVKAAWGKVGGNAPAYGAQALQRMFLSFPTTKTYFPHFDLSHGSAQQKAHGQKVANALTKAQGHLNDLPGTLSNLSNLHAHKLRVNPVNFKLLSHSLLVTLASHLPTNFTPAVHANLNKFLANDSTVLTSKYR'
hemos['cow'] =     'VLSAADKGNVKAAWGKVGGHAAEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGAKVAAALTKAVEHLDDLPGALSELSDLHAHKLRVDPVNFKLLSHSLLVTLASHLPSDFTPAVHASLDKFLANVSTVLTSKYR'
hemos['pig'] =     'VLSAADKANVKAAWGKVGGQAGAHGAEALERMFLGFPTTKTYFPHFNLSHGSDQVKAHGQKVADALTKAVGHLDDLPGALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHHPDDFNPSVHASLDKFLANVSTVLTSKYR'
hemos['wolf'] =    'VLSPADKTNIKSTWDKIGGHAGDYGGEALDRTFQSFPTTKTYFPHFDLSPGSAQVKAHGKKVADALTTAVAHLDDLPGALSALSDLHAYKLRVDPVNFKLLSHCLLVTLACHHPTEFTPAVHASLDKFFTAVSTVLTSKYR'
hemos['chicken'] = 'MLTAEDKKLIQQAWEKAASHQEEFGAEALTRMFTTYPQTKTYFPHFDLSPGSDQVRGHGKKVLGALGNAVKNVDNLSQAMAELSNLHAYNLRVDPVNFKLLSQCIQVVLAVHMGKDYTPEVHAAFDKFLSAVSAVLAEKYR'
hemos['trout'] =   'XSLTAKDKSVVKAFWGKISGKADVVGAEALGRMLTAYPQTKTYFSHWADLSPGSGPVKKHGGIIMGAIGKAVGLMDDLVGGMSALSDLHAFKLRVDPGNFKILSHNILVTLAIHFPSDFTPEVHIAVDKFLAAVSAALADKYR'

print('Opções de entrada: human, horse, deer, cow, pig, wolf, chicken, trout')
word1 = input("Entre uma espécie: ")
word2 = input("Entre outra espécie: ")

word1 = list(hemos[word1])
word2 = list(hemos[word2])

size1 = len(word1)
size2 = len(word2)

gap = -4
match = 5
mismatch = -3

matrix = np.zeros((size1 + 1, size2 + 1))

def matching(a, b):
    if a == b:
        return match
    else:
        return mismatch


for i in range(size1 + 1):
    matrix[i][0] = gap*i

for i in range(size2 + 1):
    matrix[0][i] = gap*i

for i in range(1, size1 + 1):
    for j in range(1, size2 + 1):
        matrix[i][j] = max(matching(word2[j-1], word1[i-1]) + matrix[i-1][j-1], gap + matrix[i-1][j], gap + matrix[i][j-1])

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

matches = 0
for i in range(len(res1)):
    if res1[i] == res2[i]:
        matches +=1
print(matches/len(word2))
