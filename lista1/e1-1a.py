#  Biologia Computacional 2019/2 - Lista de Exercícios 1

#  Aluno: Leonardo Oliveira Wellausen

#  Questão 1a


cromo = open('sequence.fasta','r').read().replace('\n', '')

target_subseq = 'CAATTGAATAATTG'
possible_nucs = 'CATG'

trg_len = len(target_subseq)

mutated_subseq = []

for i in range(trg_len):
	for nuc in possible_nucs:
		if target_subseq[i] == nuc:
			continue
		mutated_subseq = list(target_subseq)
		mutated_subseq[i] = nuc
		occ = cromo.count(''.join(mutated_subseq))
		if occ == 1:
			print('Subsequência não mutada: ', ''.join(mutated_subseq), '. Encontrada com início na posição ', cromo.find(''.join(mutated_subseq)), ' do cromossomo. Mutação realizada: nucleotídeo', target_subseq[i],
						  ' pelo nucleotídeo ', nuc,' na posição ', i, ' da subsequência.')

		#cromo.replace(target_subseq, ''.join(mutated_subseq))
		#with open('e1-1a.txt', 'w') as file:
		#	print(cromo, file=file)
		#exit()

		#print('Mutando a posição ' + str(i) + ' gene ' + target_subseq[i] + ' pelo gene ' + gene + ' gerando ' + str(cromo.count(''.join(mutated_subseq))) + ' correspondências para a subsequência ' + ''.join(mutated_subseq))
		#for j in range(len(cromo) - trg_len):
			#if ''.join(mutated_subseq) == cromo[j:j + trg_len]:
			#	print ('Correspondencia encontrada com a subsequencia ' + ''.join(mutated_subseq))
		#for line in cromo:
		#	for j in range(len(line) - len(target_subseq)):
		#		if ''.join(mutated_subseq) == line[i:i + len(target_subseq)]:
		#			print(line)
			#if ''.join(mutated_subseq) in line:
			#	print (line)
		#if ''.join(mutated_subseq) in cromo:
		#		print ('Correspondencia encontrada com a subsequencia ' + ''.join(mutated_subseq))


