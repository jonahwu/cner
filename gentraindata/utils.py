import os

def getTrainInfoFromFile(file='./trainwords.txt'):
    lines=[]
    with open(file) as f:
        lines = f.read().splitlines()
    key=[]
    label=[]
    for l in lines:
        if l:
            print(l)
            s=l.split()
            print(s[0],s[1])
            key.append(s[0])
            label.append(s[1])
    return key, label

def getUserDictFromFile(file='./trainwords.txt'):
    lines=[]
    with open(file) as f:
        lines = f.read().splitlines()
    return lines

"""
data = getUserDictFromFile()
print(data)
"""
