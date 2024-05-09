import string

code = [['A', 0.2], ["B", 0.1], ['C', 0.3], ['D', 0.4]]
freq = [['A', 0.1], ["B", 0.3], ['C', 0.4], ['D', 0.2]]

for i in range(len(code)):
    smallestSum = float('inf')
    SumDiff = sum(round(abs(code[i][1] - freq[j][1]), 6) for j in range(len(code)))
    print(SumDiff)    