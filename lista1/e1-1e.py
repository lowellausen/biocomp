#  Biologia Computacional 2019/2 - Lista de Exercícios 1

#  Aluno: Leonardo Oliveira Wellausen

#  Questão 1e

cromo = list(open('sequence.fasta','r').read())

for i in range(len(cromo)):
    if cromo[i] == 'A':
        cromo[i] = 'T'
    elif cromo[i] == 'T':
        cromo[i] = 'A'
    elif cromo[i] == 'C':
        cromo[i] = 'G'
    elif cromo[i] == 'G':
        cromo[i] = 'C'

cromo = ''.join(cromo)

print('Gravando sequência complementar no arquivo e1-1e.txt.')
with open('e1-1e.txt', 'w') as file:
    print(cromo, file=file)

print('Processo concluído.')