def ReverseComplement(s):
    xlat = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    ss = ''.join(map(lambda x: xlat[x], s))
    return ss[::-1]
