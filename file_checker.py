from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

def inside_file_checker(url):
    token=re.findall(re.compile(r'\w{33}|[^/]{33}'),url)[0]
    response=Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    res=urlopen(response)
    soup=BeautifulSoup(res,'lxml')
    match=re.compile(r'data:\[.*,"Files"')
    match_two=re.compile(r'"\S{33}"')
    ndata=re.findall(match,str(soup))
    newdata=re.findall(match_two,str(ndata))
    filelist=[]
    for i in newdata:
        if '.' in i or ',' in i or token.split('?')[0] in i :
            continue
        else:
            l=i.replace('"','')
            filelist.append(l)
    return filelist
