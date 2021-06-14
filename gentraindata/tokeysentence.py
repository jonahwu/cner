import glob2
from lib import common
import time

from utils import getTrainInfoFromFile
key,label = getTrainInfoFromFile()
keyword=key[0]

pdfbooks=glob2.glob('./data/*.txt', recursive=True)
print(pdfbooks)
keyList=[]
for pb in pdfbooks:
    l=common.readFileAsList(pb)
    for ll in l:
        print('-----------------------------')
        #print(ll)
        ss = common.textToSentence(ll)
        for s in ss:
            #print(s)
            if keyword in s:
                print('========')
                print(s)
                keyList.append(common.clenanSentence(s))

k=common.dedupeList(keyList)
common.storeFilebyList(k)



    #print(l)

