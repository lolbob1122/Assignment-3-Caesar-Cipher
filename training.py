import re
import string

filepath = 'Assignment-3-Caesar-Cipher\\codes\\secret0.txt'
shift = int(input('shift:'))
testl = []
with open(filepath) as inputtext:
    text = inputtext.read()

for i in text:
    print(i)
    if i.isalpha() and i.islower() and shift !=0: 
        text_shift = chr(((ord(i)+ shift - ord('a')) % 26) + ord('a'))
        testl.append(text_shift)
    elif i.isalpha() and i.isupper() and shift !=0: 
        text_shift = chr(((ord(i)+ shift - ord('A')) % 26) + ord('A'))
        testl.append(text_shift)
    else:
        testl.append(i)
text_shifted = ''.join(testl)    
print(text_shifted)

