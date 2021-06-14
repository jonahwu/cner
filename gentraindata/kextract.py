import os
import jieba.analyse
import jieba.posseg as pseg

def extractKeywords(allPhrase='', types='tfidf', userDict=[], topKnum=1000):
    jieba.initialize()
    #jieba.analyse.set_stop_words("./stop_words.txt")
    for dd in userDict:
        #print('adding dict:', dd)
        jieba.add_word(dd)
        #jieba.suggest_freq(dd, tune=True)
    keywords1=jieba.analyse.extract_tags(allPhrase,topK=topKnum, withWeight=True)
    return keywords1


def getIntersection(ia, ib):
    retB = list(set(ia).intersection(set(ib)))
    return retB

def showResult(it):
    print('the intersection words:',it)
    print('the intersection number:',len(it))

def appendKresult(ret):
    rret=[]
    for i in ret:
        #print(i[0])
        rret.append(i[0])
    return rret

def getInfoExtractMatch(userDict, allPhrase):
    ret = extractKeywords(allPhrase=allPhrase, userDict=userDict)
    rret = appendKresult(ret)
    #print(rret)
    #print(ret)
    it = getIntersection(rret, userDict)
    #showResult(it)
    return len(it), it

"""
userDict=['啥魯魯啥']

allPhrase='啥魯魯啥都不知道啦'
nI, nList = getInfoExtractMatch(userDict, allPhrase)
print(nI)
print(nList)
"""
"""
ret = extractKeywords(allPhrase=allPhrase, userDict=userDict)
rret = appendKresult(ret)
print(rret)
print(ret)
it = getIntersection(rret, userDict)
showResult(it)
"""

