import os
import re
import random
import string

def textToSentence(text, fine=True):
    #sentences = re.split(r"[.!?。，;]", text)
    sentences = re.split(r"['.','!','?','。','，',';','...']", text)
    sentences = [sent.strip(" ") for sent in sentences]
    return sentences

def XtextToSentence(text, fine=False):
    if not fine:
        punctuation = re.compile(r"([^\d+])(\.|!|\?|;|\n|。|！|？|；|…|　|!|؟|؛)+")
    else:
        punctuation = re.compile(r"([^\d+])(\.|!|\?|;|\n|。|！|,|，|？|；|…|　|!|؟|؛)+")
        # 發生 and year but not same comma

    lines = []
    lines = punctuation.sub(r"\1\2<pad>", text)
    lines = [line.strip() for line in lines.split("<pad>") if line.strip()]
    #print('---------------  show senetence -------------------')
    """
    for line in lines:
        print('---line---',line)
    print('---------------  show senetence done -------------------')
    """
    return lines

def readFileAsList(filename):
    f = open(filename, "r")
    dictdata = f.read().splitlines()
    f.close()
    return dictdata

def readFileAsListWFirst(filename, sep=','):
    datalist=readFileAsList(filename)
    dlist = []
    for d in datalist:
        dlist.append(d.split(sep)[0].strip())
    return dlist

def dedupeList(alllist):
    delist = list(set(alllist))
    return delist

def storeFilebyList(mm, storefile='keywordlist.txt'):
    #storefile='keywordlist.txt'
    ff = open(storefile, "w")
    for sm in mm:
        ff.write(sm)
        ff.write('\n')
    ff.close()

def storeFilebyDict(mdocs):
    for m in mdocs:
        storefile=m.replace('data','datam')
        ff = open(storefile, "w")
        mm = mdocs[m]
        for sm in mm:
            ff.write(sm)
            ff.write('\n')
        ff.close()

def randomFile():
    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    #print(file_name)
    return file_name

def clenanSentence(s):
    sentence = ''.join(s.split())

    return sentence
