
from pyhanlp import *
import glob2
import pdftotext


def toCommaString(slists, target=''):
    ret =""
    print('where to comma target:',target, toSC(target))
    for slist in slists:
    #    if slist!=toSC(target) or slist!=target:
        #ret = ret+slist+','
        ret = ret+slist+'  '

    return ret


def comparePer(iinput ):
    data100t=['陳', '林', '黃', '張', '李', '王', '吳', '劉', '蔡', '楊', '許', '鄭', '謝', '郭', '洪', '曾', '邱', '廖', '賴', '周', '徐', '蘇', '葉', '莊', '呂', '江', '何', '蕭', '羅', '高', '簡', '朱', '鍾', '施', '游', '詹', '沈', '彭', '胡', '余', '盧', '潘', '顏', '梁', '趙', '柯', '翁', '魏', '方', '孫', '張簡', '戴', '范', '歐陽', '宋', '鄧', '杜', '侯', '曹', '薛', '傅', '丁', '溫', '紀', '范姜', '蔣',   '歐', '藍', '>連', '唐', '馬', '董', '石', '卓', '程', '姚', '康', '馮', '古', '姜', '湯', '汪', '白', '田', '涂', '鄒', '巫',   '尤', '鐘', '龔', '嚴', '韓', '黎', '阮', '袁', '童', '陸', '金', '錢', '邵', '于', '崔', '任', '夏', '譚', '韋', '賈', '熊', '>  孟', '秦', '閻', '雷', '龍', '段', '郝', '孔', '史', '毛', '常', '萬', '顧', '賀', '尹', '牛']
    #data100 = read100PerFile()
    data100=toSC(data100t)
    print(len(data100))
    if len(iinput)<2:
        return False
    if iinput[0] in data100:
        return True
    else:
        return False

def dedupeList(alllist):
    delist = list(set(alllist))
    return delist

def getdirpdfname(dirr=''):
    if dirr:
        filename='%s/**/*.*'%(dirr)
    else:
        filename='./**/*.*'
    #print(filename)
    pdfbooks=glob2.glob(filename, recursive=True)
    #pdfbooks=glob2.glob('./**/*.pdf', recursive=True)
    return pdfbooks

def getTextFromTXT(pdfbooks, pageNum=0):
    print(pdfbooks)
    f = open(pdfbooks, "r")
    d = f.read()
    return d, 1

def getFileFormat(file):
    return file.rsplit('.', -1)[-1]

def getTextFromPDF(pdfbook, pageNum=0):
    #file='pdfdata/TestingDoc.pdf'
    file=pdfbook
    with open(file, "rb") as f:
        pdf = pdftotext.PDF(f)
    npage=1
    totPages=len(pdf)
    for page in pdf:
        #print('-----individual page---------', npage)
        #print(npage)
        #print(page)
        npage=npage+1
    #print(pageNum)
    if pageNum==0:
        #print('------ all pages data ------')
        #print("\n\n".join(pdf))
        alltext="\n\n".join(pdf)
    else:
        alltext=pdf[pageNum]
    print('----- show 1level text -----')
    #print(alltext)
    return alltext, totPages

def AllPdfToTextList(files):
    #this_loc=1
    #df=pd.DataFrame(columns=("name", "content"))
    allpdfs=[]
    for file in files:
        this_doc=""
        if getFileFormat(file) == 'pdf':
            this_text, n_pages=getTextFromPDF(file)
        else:
            this_text, npages = getTextFromTXT(file)
        allpdfs.append(this_text)
        #df.loc[this_loc] = file, this_doc
        #this_loc=this_loc+1
    return allpdfs

def AllPdfToText(files):
    #this_loc=1
    #df=pd.DataFrame(columns=("name", "content"))
    datalist= AllPdfToTextList(files)
    datastr = "".join(datalist)
    return datastr

def getNewWords(text):
    HanLP = JClass('com.hankcs.hanlp.HanLP')
    newW=HanLP.extractWords(toSC(text), 100)
    return newW


def toSC(text):
    HanLP = JClass('com.hankcs.hanlp.HanLP')
    if isinstance(text, str):
        #return HanLP.tw2s(text)
        return HanLP.convertToSimplifiedChinese(text)
    elif isinstance(text, list):
        #print('---- running list -----')
        text1=[]
        for i in text:
            #textt=HanLP.tw2s(i)
            textt=HanLP.convertToSimplifiedChinese(i)
            text1.append(textt)
        return text1
    else:
        text=list(text)
        text1=[]
        for i in text:
            #textt=HanLP.s2tw(i)
            textt=HanLP.convertToSimplifiedChinese(i)
            #print(textt)
            text1.append(textt)
        return text1

def toTC(text):
    HanLP = JClass('com.hankcs.hanlp.HanLP')
    if isinstance(text, str):
        #return HanLP.s2tw(text)
        return HanLP.convertToTraditionalChinese(text)
    elif isinstance(text, list):
        #print('---- running list -----')
        text1=[]
        for i in text:
            #textt=HanLP.s2tw(i)
            textt=HanLP.convertToTraditionalChinese(i)
            #print(textt)
            text1.append(textt)
        return text1
    else:
        text=list(text)
        text1=[]
        for i in text:
            #textt=HanLP.s2tw(i)
            textt=HanLP.convertToTraditionalChinese(i)
            #print(textt)
            text1.append(textt)
        return text1

def addCustomerDict(CustomDictionary, cdict):
    try:
        f = open(cdict, "r")
        dictdata = f.read().splitlines()
        f.close()
    except:
        return CustomDictionary

    #CustomDictionary.add(toSC("治略"),"nt 1024 n 1")  #  increase
    #CustomDictionary.add("治略", "nt 1024 n 1")  #  increase
    for d in dictdata:
        #CustomDictionary.add("治略", "nt 1024 n 1")  #  increase
        key=d.split(',')
        print('--- add dictionary -----',key[0],'and', key[1].strip())
        # need strip alot
        CustomDictionary.add(key[0].strip(), key[1].strip())  #  increase
        CustomDictionary.add(toSC(key[0]).strip(),key[1].strip())  #  increase
    return CustomDictionary

def addNewWords(newwords_list):
    CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    for n in newwords_list:
        CustomDictionary.add(toSC(str(n).strip()))
        CustomDictionary.add(str(n).strip())
    return CustomDictionary


def chinese_name_recognition(sentences, nrecog='nr', cdict='', newwords_list=[]):
    #人nr 地名ns 机构名 nt
    HanLP = JClass('com.hankcs.hanlp.HanLP')
    CustomDictionary = addNewWords(newwords_list)
    CustomDictionary=addCustomerDict(CustomDictionary, cdict)

    """
    if cdict:
        f = open(cdict, "r")
        dictdata = f.read().splitlines()
        addCustomerDict(dictdata)
    else:
        print('no dictionary input')
    """
    """
    CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    CustomDictionary.add(toSC("治略"),"nt 1024 n 1")  #  increase
    CustomDictionary.add("治略", "nt 1024 n 1")  #  increase
    """

    name=[]
    segment = HanLP.newSegment().enableNameRecognize(True);
    for sentence in sentences:
        term_list = segment.seg(toSC(sentence))
        #print(term_list)

        for nn in term_list:
            na = str(nn.nature)
            if na.strip()==nrecog:
                if nrecog=='nr':
                    #if len(nn.word)>1:
                    if comparePer(nn.word):
                        name.append(nn.word)
                else:
                    name.append(nn.word)
                #print(nn.word,nn.nature)
    return name

def checkRequestJson(request):
    if request.headers['Content-type'] == 'application/json':
        print('------- send text only not file ------')
        return True
    return False
def listToTC(scl):
    ret = []
    for s in scl:
        ret.append(toTC(s))
    return ret

