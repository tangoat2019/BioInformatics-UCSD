def compNucleotide(n):
    dics = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return dics[n]

def findComplement(gene):
    comp = ''
    for i in range (len(gene)-1, -1, -1):
        comp += compNucleotide(gene[i])
    return comp

gene = 'AACCCTCGGGAGTTCATCCTTCTCGAAATATGGCGTCCGTTCTAATCGGGGATCGGCAGCACGGCAAAAGACTGAACACTAGCTTCAAACTGGTCCACATACAGTGAGAAAAAAGACGATATCGCTCGCGCATAAGGAACTACTACAAGGAGCCTGTGCTCTTGTCGGCGATCAATTTAAACCTTCAAACAATAAGTAGGGGCGGCGAGCCGCCCCAGGACTTTATATGTTCCAAAGATCGGCTTACGAGTGACGGTATGAAAGCGATTCCCTTACCCATCACCATGTCACCTGGTGGCTGCACGTCCGCGTTCTTTGATTTAACCAATCCCCCAAGTATCAACGGAGCCTGATGCGCCGTAGATTCGCAAGTTTTGCTCATGCCTTGCTATGTATAAGGACGTTTTAGACAGGGTTCTTCGAGGCTTAGGAAGCTTTGATCACACCCGCCCCAATCGATAATTAGGACGGATTGTTCGCCGGATATAAATCAGGAATGCTGCGGTGCGCCTTGGGGAAACTTATTCCCAAGAACGCACGTTCAAGAGGGACCCTAGTTCAACACAAGCCCCGTGTGCTCCATCTGCCAAAAATGCGAGACGCGCTAAGCGTGGCGCCGTTTGACGCAGCAACCCAAGTAAGCTTGCAGAGATACGCATCCTAAATCGTCGACGGACAAGCGCAATACGTCAGACAGTTGTTTTATATACAGCCGCTCAGCGCGCACGTGTCTCAGTCCCTCAATTCTAACCAGTTGACCGAATGATAACTGTTCACCCATGCCAAAGACGTCCAATCAGTATTTATCAGTGACTGGTGTCCTTCTCTTGCCGTTGATCAACCAATTGACAAACTTAGGCTTGAGTCATGATGTAGACATGTCTTGGAAAAACCCGAGGATAGGTTTCTTAACGATAACACGCGCCGCCGCTTGAATTAATCAGAAAAAGACAAGTTGTCAGAATTCTCGATGTTCAAAGTAAACATGTAGGCTCCTGAGGTTCCTCTTGTGTGTTGATGTACACTGGCATCGCCTCTGACATCTTTACTACATGAAAGCCTAGAGCTGCTACAGAAGTCAAGGACTCACGGGCCGGGATCCTATCTGGTAAATCGTGAGACAATCTACAATAGTATGTAACTCGCTGTCGTGGATGTGCATGTATCGAGGTCGATTTTCCTATGCAACTTCCACGAATTAGGCACCCCTATCAGAAGTGGGAGCGGGGCTGCCCCCGATCCCATCCCGACAAACCACTCTCCGCTCGGTGCGTCAGTCTCTCAATTCGTCGGAAGAATGGCTAGAGTGAAGTTTACCTGATCGTAAAAATTAACGTAATTATCTCCCGTGGATAGCTCGAGGGAATAATTGTATCCATCATTAAGCTACTTGGCAATCAGCTGGCACAGCATACTAAGTTGTACCGGCGCGAAAGTGGGTGACGGCTTGCGGACTGCACTCGTTTTTGGGTTGTACCTGGCCTGTAGCCTGGGGGAAATTAGTTTAGCTCGAGAATGAGTAATCCACACTATAGATAAGAAAGTCATCTCTTCCCGGTGTATACTCACTTGTACAGTACTCTCGGGTGAAGATAGGAATCTGGGAGTTCGAGACTGGGCCATCTTCGGTAAAAGGGGCGAAGGCAAAGCCCGTGTCGTGCATACTTACGTCGATACAAGTTTGTGCTTGTTGATACTACCTGCCACCCTAAGCACCTATGTTCTACTGTCTTGAAATCGCAATGCCAAAAATACGACAACATTTTGGTCGGAGCATTGCGTACGTTTGCAATCGTCGGTCCGGGTCGGGTATATGTTGACCAACACGTCTCCAGCGCCAGCTCGTCGTTGCCTTGTAGAGGACTCGGGGCATTGGCCTGGGCAGAACTACACACCCATGGATCGCCTAGGTCATCTCCCAACCCGATGGGGCTTGGCACGCCACTTCCCTTGGATCTCAAATTACCAGCTTTTTGCATTCGGCACGTTCGCAATTTCTTGGCATGACGGCGCCGACATGGGTGGCGGTGTAAGCTAAGTTGTAGCATCAAGGGCGGACTCACGCTTTCACAAAGTTGCACAAAACCCATAAGTTCACACCGCAATTCCGTTAGGGGCACGGGTGGCGTTGCTTATGCACAAGCAGAGCACTGCTGGGTGGTTACATTCATACGCCAGCACGGATAAGACAAGCTCGTGGATATCTGTAGCACGACAGGGTGTGCGAAGATGTCGATAGATAGGCCTGGGTAAGATTCGATTCAAATACACAAGATGAAGTCCTTCCATCGGGACGTACAGGTGCAAAGGTGAGGCTGGCAAGACCCTACTATTATATCGCAAGCTGTTGCCTCTAGTGTGACTAATACCGGGTCGGTGAAGCCGTAAATACAAGTTGCAGCGCGCGGGCGTGCAACCCTTATCACTTCAACAGTATCTAGCAGTGCAAAGAAAAGGGATAAGGGCGCAGTCATAGGTTAACCACTCTGGAGCTACGAAAGATTGCGTGACAAAAGGGGTCCAGGTGCTGTATGACTTTTAGGCCGACTGCTGAATGTAGTTAGAAGACGACGACTTGTGGTGCGTACGGCTGGTGTATACATACACCAATTAGGAGTGTCCGAACTCTAAAACCGAATGCTCCTGCGTGTGAAAGTCGAACCTCCTACAAGACTAGAAGAACACTATGGTGTGCAACGGCAGCTCTATAATACTCCATTTATAGATGTCAAGTATGCCACAGGAAGCAGAGTACGGCACAAGGAATGTTAGCTCTAGTTCGGCTTAGGAACGTGTATCAGTGTTACTCCTTGTCGCAACGATTGCTCTATTGCATCCCCAGGTTGAGCGGACTCCCGCGTGAATGTGACAATCAGTATGGAGCACTCGAAAAGAGCGTGCTTCCCGCACTGTTGGCAGCACAGTGCATTGAGGGATCTTATTCCACGGGTGCGTATCGAATACCACCTGCGCGTTAGACTCACCCTAATGCGGGGGCGATGCACCTTCAGGCCAAGGCACGCGGATCAACGGCCCATGACTGTGACGGTACACGAGAATTACTCCACGGAACCTTCGAAGCGATACGCGAGTGAGATAGTCCCTTCGTCACTAGACCAATGTTTACTACCTGGTATGATGACGGTTGCCTTCTCGCTCCACGCTCGCCAATGCAGACATCACAGTCATGGTTACTTATGGGCATGGTGGGCCTACCACCGAGGGGGAGTTTCTGTACGCCTGGAAAAGTGACTATGCCCCTCCTAGTTCGAACTTGGGTATCGAAAGGTTAGGCCGAAGCCGAACTAGGCCGACGTGCGTGCTCTAAGACGAGATTGCGCTAAAAGATAGCCTTTGCGTCTCTGGGAAGCAAGGTCCTTGTTCGAAACGCCTTAGTAGGGTATCGGATATTCAAGAAGATAAGCGCTGAGCTTTCTGTCCAAATGGCAATGGCTCGCGAAATCTTCCGAGGCGAATGCAGAATAGTACCACTTTGGCTCATCCGCACTTCAGCAGACGGCCTTGCGCTTAAGCATCTAGGTGATGAGCAATGCTGTGCTGAAGCACGGACTTCATATGAATGTATTTGCCTCGTCAATGAGAATGCTAGCATCCCGTTCGCACCGTCCACAGTCTAACCAACAGCAAATTGTAGGGCGACGAACGATATCATGATTGAACCGCTTACGTGGTAACTTATTCCAATGAACAAAGGGGCACTGGTGGATTGCTGCGACGTGTCGTGGCCTAAATGCGACACCTGTCGTCGAATCCACCTGGGATATGGCAGCGCTGTTGTGGTGAGAAGTGACTTCCTTAGGACAGGCTTTTCCCACATACCACGCGTACGTCGACCAAACGTGTTGGTCGCACCCTGCGTGGTTTGCAAGTTGTCGACGAGACACACCCGGAATACAGGAACATCACACCTGGAAAGCGATCACTCAGGGTCTCGTACAAGGCGTGTCCAGTATTATACGCTACTCGATTAGGCAGCGTTGAAATATACCCTGGAGTACGCCACCTTATTTCTTATATTGTCGGTCGGGGTCCAGCGATCTCTCGCGCATTGAGTTCCCAGACGCGTATTAATCAAAGCGAGTTTACGAGGATAATCCACTCGCCACCGCCCGTTCGCTTATAAAATTTTCGACTGCTCAAGCTTATTCAACCACGGACGGATGGTGAATCGCGTTATCCGCCCTAAAGCCAACTCTGTTCTATTAGGGGGTCATCGGCTACTTCACGGACCATGAACTGACTCACCCGTTCACCTCAAACGTATGGTTCATGGAGGGTGTCCTTCTTTATCCTGCAAGTAATCATAGCGTAAAGGCGAACGTAGTCATCATCTACAGTCTCAATGACAAGTAGTTATTAAACCTCAAAGACTAGACCATCCAGCACTCGTCTTCTCCATAGTACTGGACGTGTAAACTGAAAAGAGGATTGTCTCCAGTCCCAATCCAACACGTTCAAGATGATTACGCAACCTAAGTACAACTGACTTGCCCTGGAATGGGTCCTAACTGCCAATCACGAAAATAGAAAACCCTGAGCTACAGTGCCTGGACTGATGGCTACCCTATCCGATGTTCCCAAGAAGGTGCCCTTTCCACGAAAGCGTGTTGAGCGTCGCGTTCCCAGGTAAAGTTAATCCCAGCCATGATCGATACGTCCGTAATTCCAGAATTACGGTCCAGGGCGATTATAACTTGCTGGGTCTAGCTGGTGCCCGTCGTATATTGCCTTGTGCTCGGATGAGTTAGGGGCGGGTCCACATGAGTTTCACTACCAATCGCAGCCCTGGGTTTTATTTGTTCTCCAATTAACTGCCCTTCGGTGTTAGGCGAGATATATCCGCAGGACAGCTTTTGCTATCCGATGCCGTCGCTAGGGATAGGGTAAAAAATGCGGAGTACGCAACGACTGAATTCGAAGAAATGGGTGGGCTGCCCAATAGAAAGGCGAAGGGGCATCTCCTCACACATAGCTCGGTCGCCGTATACCCTTAGAAGTTCTAGGTAATAGGATATGCACCGATGGCACGGAATGGCCCCCCAAGGCTATGATAGTCACGCAAGCGGGAGTATGGGCGGAGGGTTGCTGCGACATCCCCATGTTTGAGTGGTTAGTAGCTTTTGTGTGTGTAATGGTTCTCGTACGGGACCCCTCCATGCCGGGCCACGCGGATAACATTCTCCCTGTCTTGTTAGAAAAAGATGTCACCTATTGCGAGTTATGAGCGTTGTGATGCAGCTTCGTGCTTTGTGCTCTTCCGAAGTAGCGGCCGCCTAATTAGTCGTCTCCACAAGAGGACGCCCTGCCTTGAGCTGTTCGCCATTTAGATGTAATACGTTCACCTCTGACGGACCACTTTGGATTTTAAAAAAGGGTTGAAAGCGGTCAGCTTTATTATGCTGCTTAAAATAATATACTAACGCAACTATGGTACCTACCCAACCAGTGCACCGACCATGCACTCGCCGTGTCGCAAAAAGGCGGGGCAGTCCAGCCGCTGTTTTCAGTCTGACAAGGTGGAAATTAATGCGCTGAGATCCGATGCTAGAACTGGATGCCTACTGATTCCTGCCTTGGATTGTCTGATACAACAGATAGTCGGGTGTAAAGTATCATGAACAACTCTAAGCTCATTGATCAGGTCATCCCAGTATACACGAGGTCTGCTAACTATAGCCTATATTCACCTGGACCTAGTTATTATAGGTCCATTGGTTAAAAACCGCCGGAGAGGCCGCAAATGCTGGCCAACAGAGAGCTTCTCCTTCTGGTAGTAGCTCAGGAATTTAACTTACATTTTGTTCCTGTAGATTATACTAATACTTAATAGAGGTTTTGAATTCGCACATCCACACAATGCCGGTAACCAACCAGTTTGTGGGACGGAGTCTGGCCTAGCCCCTATAACCATAGGGAAATTCCTGTCCAAGTGTTAGACTCAGGATTATAATAAATATACTGGGGCGGGGGAATTCTTGGCCAACGCCACGGTATTTCACGCAAGGGCAGTCGACGTTCCTAGTTTCCGCGGATGACGGTGCATCGACCTCCGGCTCTACAAGTTGCTAGTCTGGTCACGTCATTGCGGCTCAGTTAGCCCGCCGCATAGTGGCGGGTGTGGGAAGCTGTGATCACCAACAGAGTATTGCAGAGAAAAAACCTGCTATCCAGGCGATCGTTTCGTCAGCTTGAATAGAGTCCTTACGTGCTAGGTACCACCTCATGATGTACAGTACGCCATAATTTGGGCTATCGACGTCGAGGTCCCCCGGGCTCATCACCGGCATTGAAGAGAAATCATACTAAGGATCCAAGCTGAGCGCAGCCGAGATGAGTCCCTTAGTGCCTAGAATTGTAGGGGACAACATGGCATGGTTGTCAAGCCCACGGACCAACTGCGCATCGTTCCGAAAGTCCTCCAGTTATAATAGGAATACATTAGATATCGATGGATTAAGTAATTCCGTGCTCGCGCCCGTCTCCGAACGAGGTCGTTCCGCATCGGTTGTGTTTCATCCCCAGATCAGTAAGGGATGTCCACTGTATCGCTCGGGTCGCCCTTGGTATCCATATCGCAAATTGGTGTATAAGCTTAGAACGCTTTCCTTTGAAGTTTTATCTGATATAAAACAGGTACCATCAGTAGCATCAATGTTCATGCGACTGTGGCCTCGCACCCACGTGTGCGTATCCTTTTCATCGTCAGGGCTCCTCCGATTGGGGAGCAACTGTCCTTTTAGGCCGAGCTCTTCAGCTTCTTCCATCTCCATATGTTGCCGTCCAATCAATCAAGGCCGCTATTCACTGGTCCACCTGCCCTCCACAGTCAGGGTGGCGGTTCAACCTACAAAGCTTGACGGTTTGGTGGCAGAACGGGAATTGCGCTGAATTGCTAATTTTGATATATCTGCGGGGTGTGTGGAGTGTCCTGTAAACCTACCGGTAGAATCCACGAGTAAAGACTGGTGCACAATTCTCGTTGAGGAGCCCTTCTAGTTCGCCAACCAACCGTCGTTATATGGACTAAGATGTTACCGGCCGAGATGAACTGGTCCTTGCAAAGTTATAGGTATCGAAAACTCGATTTTAAGGGACCCAGCTGTTAGCGTTCTTTTGTTGGCGCATCTGTGGGTCCTATGAAGTCATTCCACGCGTATTGTAGCAATCTGCCGTTTCAAGAAATCCATAAGGCAGCAGCCGACTCGCGACAACTATGGCTAACTCGTTCCAAGCAAGCTTAGTACCTATTGAGCTACCGGTCCACACAAGTTCAATGATAAACGCGGGACACATTTTCTAGGTGGGCGTTGCATCTTCCGGATTTGCGGACCGAAGGGCCGGGCGAGAGAACTTCATGGGAGAGATGAATGACCCCCAGCAACGTCGAACGCTGCGGGACCTCCGTATAATACTCTCTTTAAGCACGTACGCTAAGCACTATTGAGGCGGCAGGAAAACAACCTTCGGTAAACGGTCTCCAACTCTTTTGAAATTAGCGAGAGGTGGCTCCGATTTGAGCGAGTACCACCGTAAAGCTCGTTCCTGGAACGGATTGGCGTTACGGGCTGAAGTGTAGACAGGCTCCGCTAGGTCCCAGTGGCTGCTATAGAACAGGGTCCCCAGTTACAGTCGCTACCTGTAGTTGTGCGCCGGCCTATCCCGACTTTTTTGCCCTAAACTCTCTTGATGATAATCACGTCTCACCGAACTGGTTCGAGAGGTTGCTTGGGGGCAACTATCCCGCATCTGATTTTCGTCTATGGCAATAAGCAGACGGGTAGACTGAATTCGAACTGAACGTGCCATTCCGAACCTAGAAAGAAGTGGTAGTCAAATGTGAAGGTACCTGTTTGTATTGAGACGGAATTAACCTCCGTACAAAAGGGACCGGAGGAGGGGTAAGTCAATATCGGCGAGTTCCCTAGCCCCAGCTATGTAAATGGTGTCACAAATATGCAGAGTGATACCGCGGCAGGAAAAGACGCTCACTCTCGAGAAGTGTCTGTATTAAATAACACAAACTGAGTGGTAGAGATCTGTCGTAGTGCGGCAGAGGGACAAAAAGGGTACCGGCGCTTCGGGCAGTTTTTATTTATCGGGCTGGTGAAGACTCAACCATCAGCTGGCATCAGTTGCTTGCGGCAAAAGAGAATAAGCGCCGCAGAAAGCTGGGAACCTCAACTTTACTCTCATTTAAGCTAAGCATAGACAGTTCTGGCAATAAATCGGCGGCCTTTTGCCCTGGAACACTGCGTGAGTGGATGCACGTTTATCTTCCGGGTCGGCCGACTACCTTCCTGTTTGTTTTAATACGAACGACAGGCCTGAGAAGACGCTGGCGGCGGTATCTATAGGCCAGTAGCCACAGTGTGGGACGTAGAGCAGTAGCCCTCCCACTGTTCGTAAGCGTTATAACTTGAAATATATGACAACGCAAGAACGGCTAATGACTTCATAGTGGGTAACAGCTTCCCCGGGCATATCCGAAGATATACCGCAGCTGGTGTCTTCAACATACCGAGGCTCTGCAGGAGCGTTCGACGCCGTTTTCTGTCTTGTCTTGTTGTAGTCAGTCGGGGTCGTCCACCTTAGCTTAGACGGACTTCTCCATCAGTAGAGTCAGGTGCATTACCTAAGCAGGATGTTGTACTTGACCTGCTCCCCAATCGCACCGACTGCACAGCGAAGTCTTGGGTCCTTTGGTGTTGACCCAGTTTCATAGAATCACACTAGCGACAAGGAGAAGTTCAGCCACTCTAGTTTCCAAAGTGGCTCGGACTAGTCATTATTCCGTTGTGATGGGCAGCGACAATTATTTGGGTCTGTATAGCCGTTAAAAACGTTACACTTACATTAATTCGCAAGTGTGAGTCACCGGGTGAATGAAGAGGTGCAACGACCTGGCTCAGTATATATTGTAAGTATTGCCGGTTGGGAGTATAGGGATGTGAGGATTCTGCCTTGATGGGAGCGATGCCCCGGTACCCTGTCAACGCCCCTCAGCATGCCAACGTGCCCGCCAGAGTCTTGTCCCGTGTGCAACCGCCCTGTTTATTCGCGACTCACGGAACGTCGTCATAACCTGATTGTAGCTATCTTAGTGCCTTATACGTCGCTGGGCCAGTTGTTTGCGGGAACCTAGCGTTAGAGCATTGCGGATTAAGACGTGTAAAGCGCTAATTTAAGGGTAAATTGGATTTTTCGAACCCACAACCGGCATTTCAGGATTCACTTCGGGCTGCACTCCGAAGGGACTCAGGGCATGTTAGAGGTAATTAGAGTCGAATGAAGCACGAAGGGATTGTGGCCCCAGTTATCCTGGTAGTCCTGAACGGACTCGCCACGATGCCTCTCTGATCCCAG'
print (findComplement(gene))
