from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

def inside_folder_checker(url):
    token=re.findall(re.compile(r'\w{33}|[^/]{33}'),url)[0]
    response=Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    res=urlopen(response)
    soup=BeautifulSoup(res,'lxml')
    match=re.compile(r'data:\[.*,"Folders"')
    match_two=re.compile(r'"\S{33}"')
    ndata=re.findall(match,str(soup))
    newdata=re.findall(match_two,str(ndata))
    folder_list=[]
    for i in newdata:
        if '.' in i or ',' in i or token.split('?')[0] in i :
            continue
        else:
            l=i.replace('"','')
            folder_list.append('https://drive.google.com/drive/folders/'+l)
    return folder_list