import os
import jieba.analyse
import jieba.posseg as pseg
from kextract import getInfoExtractMatch
from gp import GSearch
from urlcontent import getContentFromUrl
import time
from utils import getUserDictFromFile
from utils import getTrainInfoFromFile
from lib import hlp

#userDict=['王建民','中信','棒球員']
#userDict=['藍海地產','李進倫','劉威廷']
#userDict=['吳旭昇','展霖生化','陳武宗','陳柏良']


#userDict=getUserDictFromFile()
key,label = getTrainInfoFromFile()
#userDict=key
query= key[0]
#query= '吸毒偷竊'
#query= '吸毒'
label= label[0]
#query="簡嘉宏 治略"
#query="簡嘉宏"
#query="馬英九 國家機密"

#allPhrase='啥魯魯啥都不知道啦'
#query='王建民'
#query='李進倫'
#query='吳旭昇'
links=[]
titles = []
targetLinks=[]
targetTitles=[]
totalSearchNumber=0
no=0
for ipage in range(13):
    links, titles = GSearch(query=query, page=ipage)
    totalSearchNumber = totalSearchNumber + len(links)
    #links='https://www.google.com/url?q=https://sports.ettoday.net/news/1750490&sa=U&ved=2ahUKEwiisI6jovrsAhV9yYsBHUANBCk4FBAWMAl6BAgEEAE&usg=AOvVaw0pzygjylVFP_uy9PGe07ZL'
    #titles=['test']
    for ilink in range(len(links)):
        allPhrase= getContentFromUrl(links[ilink])
        if len(allPhrase) > 0:
            if query in allPhrase:
                #print(allPhrase)
                #nI,nL = getInfoExtractMatch(userDict, allPhrase)
                nI,nL = getInfoExtractMatch(key, allPhrase)
                output=titles[ilink].replace('|','')
                output=output.replace('/','')
                output=str(no)+'-'+output
                try:
                    with open('./data/'+output+'.txt','w') as f:
                           f.write(allPhrase)
                           f.close()
                           print('store file:',titles[ilink])
                except Exception as e:
                    print(e)
            else:
                print('ignore .... some data that without query name',links[ilink])
        else:
            print('ignore .... get data with zero data',links[ilink])

        #print(nI, nL)
        #print(nI,nL, titles[ilink])
        #if nI >1:
            #print(titles[ilink], links[ilink])
        #    print('-----------------------------------------------')
        #    print('here: ', nL, titles[ilink], links[ilink])
        #    targetLinks.append(links[ilink])
        #    targetTitles.append(titles[ilink])
        time.sleep(1)
        no=no+1
    #time.sleep(2)

#print('hit/search result:%d / %d'%(len(targetTitles),totalSearchNumber))
#print('total search:', totalSearchNumber)

"""
ret = extractKeywords(allPhrase=allPhrase, userDict=userDict)
rret = appendKresult(ret)
print(rret)
print(ret)
it = getIntersection(rret, userDict)
showResult(it)
"""


