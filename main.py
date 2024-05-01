chfreq = []

# Read our data file
with open('ch-freq-en.txt', 'r') as file:
    for line in file:
        # Strip whitespace and make completely lower-case
        words = line.split()

        Letter = words[0]
        Freq = words[1]

