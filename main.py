en_freq =[]
with open("Assignment-3-Caesar-Cipher\\ch-freq-en.txt") as f:
    for line in f:    
        en_freq.append(line.split())
total_en_freq = sum(float(item[1]) for item in en_freq)
norm_en_freq = [[item[0], round(float(item[1])/ total_en_freq, 6) ] for item in en_freq]
en_freq.sort()
##print(freq)       ##DEBUG
##print(norm_freq)  ##DEBUG

def readCode(filepath):
    with open(str(filepath)) as f:
        for line in f:
            lines = line.strip('')
            print(list(lines))

readCode('Assignment-3-Caesar-Cipher\\codes\\secret0.txt')


##TO-DO##
# read code and determine frequencies
# match english freqs to code freqs 
# determine shift
# apply shift