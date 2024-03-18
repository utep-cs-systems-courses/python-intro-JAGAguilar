#! /usr/bin/env python3

import sys
import re
import os
import string

if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

inputF = sys.argv[1]
outputF = sys.argv[2]

if not os.path.exists(inputF):
    print("text file input %s doesn't exist! Exiting" % inputF)
    exit()


if not os.path.exists(outputF):
    print("output file %s doesn't exist! Exiting" % outputF)
    exit()

word_Count = {}

with open(inputF, 'r') as file:
    for line in file:
        line = line.lower()
        line = line.strip()
        words = re.split(r'[-\' \t]', line)
        for word in words:
            word = word.strip(string.punctuation)
            if word.strip():
                if word in word_Count:
                    word_Count[word] += 1
                else:
                    word_Count[word] = 1

    file.close()
    
word_Count = {key: word_Count[key] for key in sorted(word_Count)}

with open(outputF, 'w') as oFile:
    for word, count in word_Count.items():
        oFile.write(f"{word} {count}\n")
    oFile.close()
    

