import json
import re
from lib import common
from utils import getUserDictFromFile
from utils import getTrainInfoFromFile
#userDict=['王建民','中信','棒球員']
#userDict=['藍海地產','李進倫','劉威廷']
#userDict=['吳旭昇','展霖生化','陳武宗','陳柏良']
key,label = getTrainInfoFromFile()
query= key[0]
label= label[0]

#userDict=getUserDictFromFile()
#query= userDict[0]

def matchLoc(text, key):
    """
    s = 'shak#spea#e'
    c = '#'
    print([pos for pos, char in enumerate(s) if char == c])
    """
    #s = '我是什麼啦'
    #c = '什麼'
    s = text
    c = key
    #inn=s.index(c)
    try:
        inn=re.search(c, s).start()
        return (inn, inn+len(c))
    except:
        inn=None
        return (0,0)
    #print(inn)
    return (0,0)
    #print([pos for pos, char in enumerate(s) if char == c])

def getTermElementWCJson(text, key, label):
    s, e = matchLoc(text, key)
    print(f'show start end: {s},{e}')
    a={}
    #a['entities']=[[3,5,'emotion']]
    a['entities']=[[s,e,label]]
    return [text,a]



data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

#dataList=['我是什麼啦','什麼東西啦']
dataList=common.readFileAsList('keywordlist.txt')


ret=[]
ret2=[]
"""
info='我就是恋爱了'
key='aa'
ret = getTermElementWCJson(info, key)
"""
dataList2=[]
dataList3=[]

sizeofk=len(dataList)
sizetoDev=int(sizeofk*0.5)
print('size move to dev:',sizetoDev, sizeofk)
for i in range(0,int(sizetoDev)):
    res = dataList2.append(dataList.pop(0))
print(dataList2)
sizeofk=len(dataList)
sizetoInf=int(sizeofk*0.2)
for i in range(0,int(sizetoInf)):
    resInf = dataList3.append(dataList.pop(0))
print('show inf data:',dataList3)
common.storeFilebyList(dataList3, storefile='./assets/inf.txt')


for d in dataList:
    info=d
    key=query
    label='emotion'
    dd = getTermElementWCJson(info, key, label)
    ret.append(dd)

for d in dataList2:
    info=d
    key=query
    label='emotion'
    dd = getTermElementWCJson(info, key, label)
    ret2.append(dd)

data1=ret
data2=ret2


outfile='./assets/train.json'
#with open("data_file.json", "w",encoding='utf8' ) as write_file:
with open(outfile, "w",encoding='utf8' ) as write_file:
    json.dump(data1, write_file, indent=4, ensure_ascii=False)

outfile='./assets/dev.json'
#with open("data_file.json", "w",encoding='utf8' ) as write_file:
with open(outfile, "w",encoding='utf8' ) as write_file:
    json.dump(data2, write_file, indent=4, ensure_ascii=False)
