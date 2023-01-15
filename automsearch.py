import requests
from os.path import basename
from bs4 import BeautifulSoup

#turn 

links = ["https://www.google.com/search?q=seven+seven+seven+fghjkl&"]
r = requests.get(links[0])
soup = BeautifulSoup(r.content)

for link in links:
    if "http" in link.get('src'):
        lnk = link.get('src')
        with open(basename(lnk), "wb") as f:
            f.write(requests.get(lnk).content)