import urlparse,urllib2
import os,sys,re

from bs4 import BeautifulSoup

if __name__=="__main__":

    url=("https://www.who.int/diabetes/country-profiles/en/")
    download_path = os.getcwd()

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}


    request = urllib2.Request(url,None,headers)
    html = urllib2.urlopen(request)
    soup = BeautifulSoup(html.read())
    for tag in soup.findAll('a',href=True):
        tag['href'] = urlparse.urljoin(url,tag['href'])
        s =  os.path.basename(tag['href'])
        if re.search('_en.pdf',s):
        #if os.path.splitext(os.path.basename(tag['href']))[1]=="pdf":
            current=urllib2.urlopen(tag['href'])
            print "\n[*] Downloading: %s" %(os.path.basename(tag['href']))
            f = open(download_path+"/"+os.path.basename(tag['href']),"wb")
            f.write(current.read())
            f.close()
            i+=1
    print "\n[*] Downloaded %d files"%(i+1) 
