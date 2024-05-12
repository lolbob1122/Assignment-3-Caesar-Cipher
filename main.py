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
    ##print(list(letters_only)) ##DEBUG
    for i in alphabet:
        ## print(letters_only.count(i)) ## DEBUG
        code_freq.append(letters_only.count(i))  ### find frequency of each letter
    #print(code_freq) ##DEBUG
    total_code_freq = sum(int(item) for item in code_freq) ### find total frequency
    #print(total_code_freq) ##DEBUG
    norm_code_freq = [round(float(code_freq[i]) / total_code_freq, 6) for i in range(len(code_freq))] ## find norm freq
    #print(norm_code_freq) ##DEBUG
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
    ##print(norm_en_freq)  ##DEBUG
    shift = 0
    smallestDiff = float('inf')
    for j in range(len(freqShifted)):
        SumDiff = sum(round(abs(norm_en_freq[i] - freqShifted[i-j]), 6) for i in range(len(freqShifted)))
        if SumDiff < smallestDiff:
            smallestDiff = SumDiff
            shift = j
            ##print(SumDiff) ##DEBUG
            ##print(shift) ##DEBUG
    #print(shift) ##DEBUG
    return shift
def cipher(shift, filepath):
    testl = []
    with open(filepath) as inputtext:
        text = inputtext.read()

    for i in text:
        #print(i)
        if i.isalpha() and i.islower() and shift !=0: 
            text_shift = chr(((ord(i)+ shift - ord('a')) % 26) + ord('a'))
            testl.append(text_shift)
        elif i.isalpha() and i.isupper() and shift !=0: 
            text_shift = chr(((ord(i)+ shift - ord('A')) % 26) + ord('A'))
            testl.append(text_shift)
        else:
            testl.append(i)
    text_shifted = ''.join(testl)    
    #print(text_shifted) ##DEBUG
    output_name = input('What would you like to call your decoded secret?:')
    with open(output_name, 'w') as out:
        out.write(text_shifted)
     

while running:
    deCode = input("Do you want to (de)code a file (Y/N)")
    if deCode == 'N' or deCode == 'n':
        # code = input('Please type the text you wish to be ciphered:')
        # shift = int(input('Please enter the shift:'))
        # filename = str(input('Please give your output file a name:'))
        ## write a file with path filename that is used by cipher for both the read and then the write
        # cipher(shift, filename)
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

    ##TO-DO##
    # read code and determine frequencies
    # match english freqs to code freqs 
    # determine shift
    # apply shift
    #  Loop over all input ‘secret’ files, and
    #  Read the entire file contents into a string ‘secret’
    #  Determine the correct deciphering key using the findshift() function
    #  Decipher the encrypted text using the found key
    #  Store the deciphered text in a new file
    #  Print the deciphering key, the original filename, and the new filename