from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import webbrowser
def downloader(url_token):
    output_url="https://drive.google.com/uc?export=download&id="+ url_token
    try:
        ress=Request(url=output_url,)
        res=urlopen(ress)
        soup=BeautifulSoup(res, 'lxml')
        print((soup.find('a').contents)[0]+' is Downloading')
        for link in soup.find_all("form"):
            finalurl=link.get('action')
            webbrowser.open(url=finalurl,new=1)
    except:
        webbrowser.open(url=output_url,new=1)