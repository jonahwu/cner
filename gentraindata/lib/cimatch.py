
from fuzzywuzzy import fuzz
from lib import common
import re
import time
from parse import *


def matchFuzz(k, t):
    score = fuzz.partial_ratio(k,t) #抽取匹配
    #print(k, t, score)
    if score==100:
        return True
    else:
        return False
def matchPy(k, t):
    #re.match(t, k)
    return t in k


def getDocTime(k):
    docTime=0
    try:
        ddd = search('{:d}/{:d}/{:d}{:s}{:d}:{:d}', k)
        #print(ddd[0])
        docTime=ddd[0]
        #print('---- we go doc time----',docTime)
    except:
        docTime=0
        #print(' can not get Doc time')
    return docTime

def checkListExisted(data, mlist):
    #a_string = "A string is more than its parts!"
    #matches = ["more", "string"]

    if all(x in data for x in mlist):
        return True
    else:
        return False

def getBirthDirect(k, target):
    kk = common.textToSentence(k, fine=True)
    birthdata=''
    for kkk in kk:
        #if ('生' and target) in kkk:
        checkList=['生', target]
        if checkListExisted(kkk, checkList):
            try:
                ddd = re.search(r'(\d{4}年)',kkk)
                #print('----------ddd:',ddd.group(), kkk)
                birthdata = ddd.group()
                birthdata = birthdata.replace('年','')
                #print('get directly',birthdata)
                return birthdata
            except:
                birthdata=''
    return None

def getAgeDirect(k, target):
    kk = common.textToSentence(k, fine=True)
    age=''
    for kkk in kk:
        if target in kkk:
            try:
                s = re.search(r'(\d+歲)',kkk)
                age=s.group()
                return age
            except:
                age=''

def searchAgeFromDoc(k, target):
    #print('into search birthday')
    age=''
    docTime=None
    birthday=None
    #s = re.search('[0-9]+歲', '100歲')
    docTime = getDocTime(k)
    #try:
        #s = re.search('[0-9]+歲', k)
    birthday = getBirthDirect(k, target)
    #print('--- show birthday----',birthday)
    if not birthday:
        #print('--- find age ------')
        age = getAgeDirect(k, target)
        #s = re.search(r'(\d+歲)',k)
        #age=s.group()
        if age:
            rage = age.replace('歲','')
            #rage=age
            if docTime and rage:
                #print(docTime, rage,'birthday:', int(docTime)-int(rage))
                #print(docTime, rage, int(docTime)-int(rage))
                #print(docTime, rage)
                birthday=str(int(docTime)-int(rage))
    #except:
    #    rage=age
    #    print('----- can not get birthday might be some error------')
    return birthday


def XsearchAgeFromDoc(k, target):
    age=''
    docTime=None
    birthday=None
    #s = re.search('[0-9]+歲', '100歲')
    docTime = getDocTime(k)
    try:
        #s = re.search('[0-9]+歲', k)
        birthday = getBirthDirect(k)
        if not birthday:
            s = re.search(r'(\d+歲)',k)
            age=s.group()
            if age:
                rage = age.replace('歲','')
                #rage=age
                if docTime and rage:
                    #print(docTime, rage, int(docTime)-int(rage))
                    birthday=str(int(docTime)-int(rage))
    except:
        rage=age
    return birthday


def matchTarget(docs, target, cdict):
#cPRatio = fuzz.partial_ratio("治略位於台北市中正區忠孝東路二段27號3樓","忠孝東路") #抽取匹配
    mtargets=common.readFileAsListWFirst(cdict)
    #print(mtargets)
    mdocs={}
    #print(cdict)
    for k in docs:
        common.textToSentence(docs[k])
        mres=[]
        #print(k)
        # match target
        for t in mtargets:
            t=t.strip()
            #cPRatio = fuzz.partial_ratio("治略位於台北市中正區忠孝東路二段27號3樓","忠孝東路") #抽取匹配
            #mflag = matchPy(docs[k], t)
            mflag = matchFuzz(docs[k], t)
            if mflag:
                mres.append(t)
        # match age need to reasoning to get the result but now it's a simple test
        birthday = searchAgeFromDoc(docs[k], target)
        if birthday:
            mres.append(birthday)
            #print('age', age)
        mdocs[k]=common.dedupeList(mres)

    #print(mdocs)
    return mdocs


def storeMatch(mdocs):
    common.storeFilebyDict(mdocs)
