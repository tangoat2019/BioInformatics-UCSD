def findPatternMatching(gene, sub):
    len_sub = len(sub)
    matches = []
    for i in range(0, len(gene)- len_sub +1):
        current_char = gene[i: i+ len_sub]
        if current_char == sub:
            matches.append(i)
    return matches

sub = 'CTTGATCAT'
l = findPatternMatching(gene, sub)
for i in l:
    print(i, end =" ") 