import re
import string

alphabet = list(string.ascii_letters)
en_freq =[]
with open("Assignment-3-Caesar-Cipher\\ch-freq-en.txt") as f:
    for line in f:    
        en_freq.append(line.split())
total_en_freq = sum(float(item[1]) for item in en_freq)
norm_en_freq = [[item[0], round(float(item[1])/ total_en_freq, 6) ] for item in en_freq]
norm_en_freq.sort()
##print(freq)       ##DEBUG
##print(norm_en_freq)  ##DEBUG

def readCode(filepath):
    code_freq = []
    with open(str(filepath)) as f:
        text = f.read()
    letters_only = re.sub(r'[^a-zA-Z]', '', text)
    ## print(list(letters_only)) ##DEBUG
    for i in alphabet:
        print(letters_only.count(i))
        code_freq.append(letters_only.count(i))
    print(code_freq) ## Debug
    total_code_freq = sum()
    print(total_code_freq)
    norm_code_freq = [round((item)/total_code_freq, 6) for item in en_freq]
    print(norm_code_freq)


readCode('Assignment-3-Caesar-Cipher\\codes\\secret0.txt')


##TO-DO##
# read code and determine frequencies
# match english freqs to code freqs 
# determine shift
# apply shift