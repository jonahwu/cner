import requests
from bs4 import BeautifulSoup

def getContentFromUrl(url):
    ret=""
    #vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
    #vgm_url = 'https://zh.wikipedia.org/zh-tw/%E8%8B%8F%E8%BD%BC'
    #vgm_url = 'https://twbsball.dils.tku.edu.tw/wiki/index.php/%E7%8E%8B%E5%BB%BA%E6%B0%91(1980)'
    try:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
    #print(soup.get_text())
        ret = soup.get_text()
    except:
        print(' can not read the web')
        ret=''
    """
    tag = soup.body
    # Print each string recursivey
    for string in tag.strings:
        print(string)
        ret = ret + string
    return ret
    """
    return ret

"""
url = 'https://twbsball.dils.tku.edu.tw/wiki/index.php/%E7%8E%8B%E5%BB%BA%E6%B0%91(1980)'
ret = getContentFromUrl(url)
print(ret)
"""
