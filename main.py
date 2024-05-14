import re
import string
alphabet = list(string.ascii_uppercase)
running = True
def readCode(filepath):
    code_freq = []
    with open(str(filepath)) as f: ### read the cipher
        text = f.read()
    letters_only = re.sub(r'[^a-zA-Z]', '', text)
    letters_only = letters_only.upper()
    for i in alphabet:
        code_freq.append(letters_only.count(i))  ### find frequency of each letter
    total_code_freq = sum(int(item) for item in code_freq) ### find total frequency
    norm_code_freq = [(float(code_freq[i]) / total_code_freq) for i in range(len(code_freq))] ## find norm freq
    return norm_code_freq
def findShift(freqShifted):
    en_freq =[]
    with open("Assignment-3-Caesar-Cipher\\ch-freq-en.txt") as f:
        for line in f:    
            en_freq.append(line.split())
    total_en_freq = sum(float(item[1]) for item in en_freq) ### find total frequency
    norm_en_freq = [[item[0], round(float(item[1])/ total_en_freq, 6) ] for item in en_freq] ### find normalized frequncy
    norm_en_freq.sort() ### sort the list 
    alphabet, norm_en_freq = zip(*norm_en_freq) 
    shift = 0
    smallestDiff = float('inf')
    for j in range(len(freqShifted)):
        SumDiff = sum((abs(norm_en_freq[i] - freqShifted[i-j])) for i in range(len(freqShifted)))
        if SumDiff < smallestDiff:
            smallestDiff = SumDiff
            shift = j
    return shift
def cipher(shift, filepath):
    testl = []
    with open(filepath) as inputtext:
        text = inputtext.read()
    for i in text:
        if i.isalpha() and i.islower() and shift !=0: 
            text_shift = chr(((ord(i)+ shift - ord('a')) % 26) + ord('a'))
            testl.append(text_shift)
        elif i.isalpha() and i.isupper() and shift !=0: 
            text_shift = chr(((ord(i)+ shift - ord('A')) % 26) + ord('A'))
            testl.append(text_shift)
        else:
            testl.append(i)
    text_shifted = ''.join(testl)    
    output_name = input('What would you like to call your decoded secret?:')
    with open(output_name, 'w') as out:
        out.write(text_shifted)
while running:
    deCode = input("Do you want to (de)code a file (Y/N)")
    if deCode == 'N' or deCode == 'n':
        running = False
        break
    elif deCode == 'y' or deCode == 'Y':
        filepath = input('please provide a filepath:') 
        cipher(findShift(readCode(filepath)), filepath)
        done = input("Do you want to run this program again? (Y/N)")
        if done == 'n' or done == 'N':
            running = False
    else:
        print('\nplease enter Y to (de)code a file or N to (de)code a text input')
        continue