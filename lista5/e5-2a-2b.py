def mut_cmp(str1, str2):
    diffs = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diffs += 1
    return diffs


def find_motif(seqs, l, m):
    seq_trg = seqs[0]
    ret = [-1 for i in range(len(seqs) + 1)]
    for i in range(len(seq_trg) - l + 1):
        candi1 = seq_trg[i:i+l]
        seqs_ok = 0
        ret = [-1 for i in range(len(seqs) + 1)]
        for k, seq in enumerate(seqs):
            for j in range(len(seq_trg) - l + 1):
                candi2 = seq[j:j + l]
                if mut_cmp(candi1, candi2) <= m:
                    seqs_ok += 1
                    ret[k] = j
                    break
        if seqs_ok == len(seqs):
            ret[k + 1] = candi1
            return ret
    return ret


seqs1 = [
    'cccctgatagacgctatctggctatccacgtacataggtcctctgtgcgaatctatgcgtttccaaccat',
    'agtttactggtgtacatttgatacgtacgtacaccggcaacctgaaacaaacgctcagaaccagaagtgc',
    'aaaggagtccgtgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatttt',
    'agcccctccgatgtaagtcatagctgtaactattacctgccacccctattacatcttacgtacgtataca',
    'ctgggttatacaacgcgtcatggcggggtatgcgttttggtcgtcgtacgctcgatcgttaacgtaggtc',
]

seqs2 = [
    'gtcacgcttctgcataccatcctgactactcgtggcgaatacggttcgtctcagaacattgacgagtaggacctccatgtacacgtgagttcgccagtagagggcagaactagaggcccgagctcgttacccagtatatgtactcggcacacactgggatataatactacacgggatactaatagtggcatatcacgccg',
    'atccctctaacaagttgttttgacggaccgtatttccaaatgtgctcggcttcagaaacaacctttctgccctctactggcgacgtcacaacgacgacaacagaccatatggagtggaccctactcatgtaattgagaccgtcgcatgtagttgatttatgtaaacatatggctctagtttcaggcccctgtaaaggtaa',
    'ttacataggttccttcacgtcactccttgtccgcgatatctcctcttacccttactaccaagcgtttcctgaaaggcaatgaaaagttgccatgcgctgtcgccagtagagggcagaataccaaggcgcttcagacaactgtcgctgttcgtgggtgggagggattgtatctataatataggatagttcgtatcgaaaaa',
    'ttatcgaccgccactttctcgccagtagagggcagaaccacaaagtgactccccgagcaatggctgacctactagttatccggcatcacatcggcacatatacgggcgagaccgagccctctccgtaaccaccagtcccactacttcacaggcatatcctgtatcaatgaaatcacaaacgttcgcatgaagataatcgt',
    'gacggcacattttaacggcccaggttggcagacaggaaatctacgatggtgctactgctttcccgagctctgccacgatgccacacagcacaattctgccctctactggcgatcacctcgaataaaaccgaatgcaagaccgagtaacagcggctggtaacatgcgggaggacgcgctttccgcaagtatattaataggt',
    'tgcatcataggttagtaagagttataaatcttcgatccctaagtgtggtgcactactcggtcgacctcgcattgacacaacgcgagagtcgccagtagagggcagaagccggcacttttgacctcttctatagaaggtagaccgtgagatcgcgcccgaaggggcccgacggtctccaaggtggaacgtattaggtaatc',
    'gccgtgtataggcctccgatcgtgcggttctgccctctactggcgaaaggggcatttgctattccaatcgcatagattaccaaataaaaaacgaaagaaggccgtccttgcaaagcttagtccttaaactgagatgcttggcgaccggccataagctccactcgcttgagcacatcaccaagaatcaaagtagcaaaccc',
    'tgtccgctctgcagacgtccgggatctacgttggtgttctctctagtaacagtacggcagttctttttcggtccgaagcgaatcccacccgccaaggttacataagcattatctgaaggcaaccatacgaactctcattggctcgccagtagagggcagaaggacatcgtgtcatagcacatgcccacagaggagattcg',
    'ccggtctcaatagccgaacgaggatcgactggtaggcgtgtcgggtgtgtgtggaccggctttggaagaaccacacttctctggccctcaattggccaaaagtcatcttaaggatcggttggccggcagcccctcgtgactacgataaccccaggttctgccctctactggcgaccttgacagagcacttacccactgta',
    'aaaagagtagtgatgagttagaaagaatttaagggacatcctcttgatttggacggctatccccaggaaatcgtaggcgggggtgcacatggatatctttaggtattaattcccccattccctcttcgttctgccctctactggcgaatgttgctcgcaatactacagcctcctcaatacaggtagggtattttacatat'
]

#####  EXERCÍCIO 2A
motif = find_motif(seqs1, 8, 2)

print('Motivo encontrado para tamanho 8 com 2 mutações: ', motif[-1], 'PARA O CONJUNTO 1')
for i in range(len(seqs1)):
    print('Presente na sequência ', i+1, 'na posição ', motif[i], 'como ', seqs1[i][motif[i]: motif[i] + 8])


motif = find_motif(seqs1, 5, 3)

print(' \nMotivo encontrado para tamanho 5 com 3 mutações: ', motif[-1], 'PARA O CONJUNTO 1')
for i in range(len(seqs1)):
    print('Presente na sequência ', i+1, 'na posição ', motif[i], 'como ', seqs1[i][motif[i]: motif[i] + 5])

motif = find_motif(seqs1, 3, 1)

print(' \nMotivo encontrado para tamanho 3 com 1 mutações: ', motif[-1], 'PARA O CONJUNTO 1')
for i in range(len(seqs1)):
    print('Presente na sequência ', i+1, 'na posição ', motif[i], 'como ', seqs1[i][motif[i]: motif[i] + 3])


### EEXERCÍCIO 2B

motif = find_motif(seqs2, 3, 1)

print('\n\nMotivo encontrado para tamanho 3 com 1 mutações: ', motif[-1], 'PARA O CONJUNTO 2')
for i in range(len(seqs2)):
    print('Presente na sequência ', i+1, 'na posição ', motif[i], 'como ', seqs2[i][motif[i]: motif[i] + 3])


motif = find_motif(seqs2, 5, 2)

print(' \nMotivo encontrado para tamanho 5 com 2 mutações: ', motif[-1], 'PARA O CONJUNTO 2')
for i in range(len(seqs2)):
    print('Presente na sequência ', i+1, 'na posição ', motif[i], 'como ', seqs2[i][motif[i]: motif[i] + 5])
