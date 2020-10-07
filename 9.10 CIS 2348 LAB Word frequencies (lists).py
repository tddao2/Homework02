#Tri Dao
#1954347
#9.10 CIS 2348 LAB: Word frequencies (lists)

import csv
# Type your code here. 
FileName = input() # User Input for the file
WordsFrequency = {} # Dictionary to store words with their frequencies
# Reading the file
with open(FileName, 'r') as csvfile:
    csvreader = csv.reader(csvfile) 
    for row in csvreader: # iterating throught each row
        for word in row: 
# checking if word exixt in the dictionary or not if not present then add the word in the dictionary with frequency 1
            if word not in WordsFrequency.keys():
                WordsFrequency[word] = 1
            else: # else increase the frequency by 1
                WordsFrequency[word] += 1
# printing the result
for key in WordsFrequency.keys():
    print(key + ' ' + str(WordsFrequency[key]))