import urllib
from bs4 import BeautifulSoup


def func(u,filename):
    data=u.read()
    soup=BeautifulSoup(data)
    comm=soup.findAll('p',attrs={'class':'commsText'})
    f=open(filename,'a')
    i=0
    for l in comm:
        s=BeautifulSoup(str(l))
        txt=s.get_text()
        txt = txt.encode('utf-8')
    #    if txt in range(128):
#        print txt
        f.write(str(txt))
        f.write("\n")
#        print i
        i += 1
    f.close()
    f = open(filename,'r+')
    lines = f.readlines()
    f.close()
    f=open(filename,"w")
    #print lines
    for line in lines:
        if line!="\n":
            f.write(line)
    f.close()


u11=urllib.urlopen("http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667641.html?innings=1;view=commentary")
u12=urllib.urlopen("http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667641.html?innings=2;page=1;view=commentary")
u21 = urllib.urlopen("http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667643.html?innings=1;view=commentary")
u22=urllib.urlopen("http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667643.html?innings=2;page=1;view=commentary")
u31=urllib.urlopen("http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667645.html?innings=1;view=commentary")
u32=urllib.urlopen("http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667645.html?innings=2;page=1;view=commentary")
u51 = urllib.urlopen("http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667649.html?innings=1;view=commentary")
u52 = urllib.urlopen("http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667649.html?innings=2;page=1;view=commentary")
u41 = urllib.urlopen("http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667647.html?innings=1;view=commentary")
u42 = urllib.urlopen("http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667647.html?innings=2;page=1;view=commentary")

func(u11,"match1_innings1")
func(u12,"match1_innings2")
func(u21,"match2_innings1")
func(u22,"match2_innings2")
func(u31,"match3_innings1")
func(u32,"match3_innings2")
func(u41,"match4_innings1")
func(u42,"match4_innings2")
func(u51,"match5_innings1")
func(u52,"match5_innings2")





