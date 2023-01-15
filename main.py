#ReadyGB main file
"""
---TODO---
Create SimRGB function - averages RGB values
Finish ReturnColorSimRGB function 
    Get Google Search HTML using search term
    find links to other sites
    store image
    format image path
    get SimRGB values of every image on other sites
    return all SimRGB values for search term
"""
import numpy as np
from ss import pickRGB, cv2
import regex as re
import requests
from bs4 import BeautifulSoup
from os.path import basename
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpim
from PIL import Image
from io import BytesIO
#selectedRGB = pickRGB() #uses pickRGB to get a RGB (blue, green, red) value
phrase = 'red, or dark green& or $%^&*('# test case
specTerm = "+color" # helps get only color results, in cases of color names with another meaning, like bone (white). can be disabled.
siteCount = 15 # has to be from 1 - 30 
def splitTitles(phrase): #VERY IMPORTANT: must be seperated by or 
    
    all = []
    colorRX = re.compile('(?<colorTerm>\w+)') # xxxx or xxxx or xxxx xxxx
    a = colorRX.findall(phrase)
    b = []
    c = 0
    for i in a:
        if i == 'or':
            c+=1
        else:
            try: 
                b[c]
                b[c] += " " + i
            except:   
                b.append(i)
    all.append(b)
    return all[0]

def specChar(string):
    """
    @     #     $   %   ^   &   +
    %40   %23   %24 %25 %5E %26 %2B
    `   =   {   }   |   [   ]   \   :   ;   '   ?   ,   /
    %60 %3D %7B %7D %7C %5B %5D %5C %3A %3B %27 %3F %2C %2F
    """
    string = string.replace("%", "%25")
    string = string.replace("@", "%40")
    string = string.replace("#", "%23")
    string = string.replace("$", "%24")
    string = string.replace("^", "%5E")
    string = string.replace("&", "%26")
    string = string.replace("+", "%2B")
    string = string.replace("`", "%60")
    string = string.replace("=", "%3D")
    string = string.replace("{", "%7B")
    string = string.replace("}", "%7D")
    string = string.replace("\\", "%5C")
    string = string.replace(":", "%3A")
    string = string.replace(";", "%3B")
    string = string.replace("'", "%27")
    string = string.replace("?", "%3F")
    string = string.replace(",", "%2C")
    string = string.replace("/", "%2F")
    
    return string

def googlePrep(titleList, specTerm):
    prefix = "https://www.google.com/search?q="
    readyList = []
    for i in titleList:
        i = specChar(i)
        i = i.replace(" ", "+")
        i = prefix + i + specTerm + "&"
        readyList.append(i)
    
    return readyList

def SimRGB(filepath):
    rValues = 0 #sum of red values
    gValues = 0 #sum of green values
    bValues = 0 #sum of blue values
    mainImage = cv2.imread(filepath)
    for i in mainImage:
        for j in i:
            rValues += j[0]
            gValues += j[1]
            bValues += j[2]
    averageValue = len(mainImage) * len(mainImage[0])
    return(rValues/averageValue,gValues/averageValue,bValues/averageValue)


def returnColorSimRGB(link, siteCount): #finding all div, a, and body tags gets results | class BVG0Nb in tag a seems significant
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    allTagsTesting = set([tag.name for tag in soup.find_all()])
    for i in allTagsTesting:
        print(i)
        print(soup.findAll(i))
        print("\n\n\n\n\n")
    return
    sites = soup.findAll('a')
    print(soup)
    print("\nxXxXxXxXx\n")
    for i in sites:
        print(i)
        print("x")
    #print(sites)
    
a = googlePrep(splitTitles(phrase), specTerm)
b = a[0]
returnColorSimRGB(b, siteCount)