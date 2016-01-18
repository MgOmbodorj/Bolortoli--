import requests
import bs4
import re


def asd():
    pass

t = open("test.txt","w")
word = raw_input("Enter Word :")

try:
    r = requests.get("http://www.bolor-toli.com/dictionary/word?authenticity_token=yatcpRETueKGdTR2u2TgduFui591b6Fvj18F2vNLFE8%3D&selected_lang=4-1&search="+word)
    soup = bs4.BeautifulSoup(r.content)
    result = soup.find_all('a',{'class':'link-string'})
    for j in result:
	print j.contents[0]
        #flag = j['onclick']
        #t = re.match(r"\'\W+\'",flag)
        #if t:
            #print (t.groups())

    
except requests.exceptions.RequestException as e:
    print e
    sys.exit(1)
