#  Biologia Computacional 2019/2 - Lista de Exercícios 1

#  Aluno: Leonardo Oliveira Wellausen

#  Questão 1b

cromo = open('sequence.fasta','r').read().replace('\n', '')
size1 = 9
size2 = 11
pal1 = {}
pal2 = {}
total1 = 0
total2 = 0
auxseq = ''

for i in range(len(cromo) - 1):  # -1 para não pegar a última letra como um palíndromo (gambi)
    auxseq = cromo[i:i + size1]
    if auxseq == auxseq[::-1]:
        try:
            pal1[auxseq] += 1
        except:
            pal1[auxseq] = 1
        finally:
            total1 += 1
    auxseq = cromo[i:i + size2]
    if auxseq == auxseq[::-1]:
        try:
            pal2[auxseq] += 1
        except:
            pal2[auxseq] = 1
        finally:
            total2 += 1

print('Total de palíndromos de tamanho 9: ', total1, 'sendo ', len(pal1), ' únicos (diferentes entre si).')
print('Total de palíndromos de tamanho 11: ', total2, 'sendo ', len(pal2), ' únicos (diferentes entre si).')
print('Listagem completa de cada palíndromo e seu número de ocorrências no arquivo e1-1b.txt.')

with open('e1-1b.txt', 'w') as file:
    print('Total de palíndromos de tamanho 9: ', total1, 'sendo ', len(pal1), ' únicos (diferentes entre si). Listagem de cada palíndromo e seu número de ocorrências:', file=file)
    for k in pal1.keys():
        print(k, ':', pal1[k], file=file)
    print('Total de palíndromos de tamanho 11: ', total2, 'sendo ', len(pal2), ' únicos (diferentes entre si). Listagem de cada palíndromo e seu número de ocorrências:', file=file)
    for k in pal2.keys():
        print(k, ':', pal2[k], file=file)

