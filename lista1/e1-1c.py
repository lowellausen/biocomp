#  Biologia Computacional 2019/2 - Lista de Exercícios 1

#  Aluno: Leonardo Oliveira Wellausen

#  Questão 1c

cromo = open('sequence.fasta','r').read().replace('\n', '')

subseqs = {}

subseq_size = 37

for i in range(len(cromo) - subseq_size):
    try:
        subseqs[cromo[i:i + subseq_size]] += 1
    except:
        subseqs[cromo[i:i + subseq_size]] = 1


print('Número de subsequências diferentes de tamanho 37 encontradas: ', len(subseqs), '. Listagem completa de cada subsequência se seu número de ocorrências no arquivo e1-1c.txt.')

print('Começando gravação de arquivo. Processo demorado e arquivo gigante!')
with open('e1-1c.txt', 'w') as file:
    print('Número de subsequências diferentes de tamanho 37 encontradas: ', len(subseqs), '. Listagem completa de cada subsequência se seu número de ocorrências:', file=file)
    for k in subseqs.keys():
        print(k, ':', subseqs[k], file=file)

print('Fim gravação de arquivo')

