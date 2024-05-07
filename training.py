table = []
with open("Assignment-3-Caesar-Cipher\\ch-freq-en.txt") as f:
    for line in f:    

        table.append(line.split())

total_freq = sum(float(item[1]) for item in table)
norm_table = [[item[0], round(float(item[1])/ total_freq, 6) ] for item in table]
table.sort()
print(table)
print(norm_table)

