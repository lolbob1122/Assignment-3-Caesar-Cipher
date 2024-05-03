def findFreq(filepath):
    codeFreq = []
    with open(f'{filepath}') as f:
        for line in f:
