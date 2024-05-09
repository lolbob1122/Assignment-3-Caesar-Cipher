import re
import string

alphabet = list(string.ascii_uppercase)

def readCode(filepath):
    code_freq = []
    with open(str(filepath)) as f: ### read the cipher
        text = f.read()
    letters_only = re.sub(r'[^a-zA-Z]', '', text)
    letters_only = letters_only.upper()
    ##print(list(letters_only)) ##DEBUG
    for i in alphabet:
        ## print(letters_only.count(i)) ## DEBUG
        code_freq.append(letters_only.count(i))  ### find frequency of each letter
    ##print(code_freq) ##DEBUG
    total_code_freq = sum(int(item) for item in code_freq) ### find total frequency
    ##print(total_code_freq) ##DEBUG
    norm_code_freq = [round(float(code_freq[i]) / total_code_freq, 6) for i in range(len(code_freq))] ## find norm freq
    # norm_code_freq = [[letter, freq] for letter, freq in zip(alphabet, norm_code_freq)]#
    ##print(norm_code_freq) ##DEBUG
    return norm_code_freq


def findShift(freqShifted):
    ## print(alphabet) ##DEBUG
    en_freq =[]
    with open("Assignment-3-Caesar-Cipher\\ch-freq-en.txt") as f:
        for line in f:    
            en_freq.append(line.split())
    total_en_freq = sum(float(item[1]) for item in en_freq) ### find total frequency
    norm_en_freq = [[item[0], round(float(item[1])/ total_en_freq, 6) ] for item in en_freq] ### find normalized frequncy
    norm_en_freq.sort() ### sort the list 
    alphabet, norm_en_freq = zip(*norm_en_freq) 
    ##print(freq)       ##DEBUG
  #  print(norm_en_freq)  ##DEBUG

    

    shift = 0
    smallestDiff = float('inf')
    matched_letter = []


    for j in range(len(freqShifted)):
        SumDiff = sum(round(abs(norm_en_freq[i-j] - freqShifted[i]), 6) for i in range(len(freqShifted)))
        if SumDiff < smallestDiff:
            smallestDiff = SumDiff
            shift = j
            ##print(SumDiff) ##DEBUG
            ##print(shift)
    ##print(shift) ##DEBUG
    return shift

norm_code_freq = readCode('Assignment-3-Caesar-Cipher\\codes\\secret0.txt')
shift = findShift(norm_code_freq)



##TO-DO##
# read code and determine frequencies
# match english freqs to code freqs 
# determine shift
# apply shift