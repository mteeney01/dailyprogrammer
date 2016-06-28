from math import log2

def entropy(s):
    return -1*(sum(i/len(s) * log2(i/len(s)) for i in [s.count(c) for c in list(set(s))]))

inputs = [
    '122333444455555666666777777788888888',
    '563881467447538846567288767728553786',
    'https://www.reddit.com/r/dailyprogrammer',
    'int main(int argc, char *argv[])'
]

for input in inputs:
    print(entropy(input))