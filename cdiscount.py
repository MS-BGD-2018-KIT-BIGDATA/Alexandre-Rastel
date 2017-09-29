from bs4 import BeautifulSoup
import requests
import re

def getSoupFromURL(url):
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup
    else:
        return None

def getLaptops(url):
    soup = getSoupFromURL(url)
    result = soup.find(id='lpBloc')
    discount = [getDiscount(laptop) for laptop in result.find_all('li')]
    discount = [x for x in discount if x is not None]
    return discount

def getDiscount(laptop):
    discount = laptop.find('div', class_='ecoBlk')
    if discount != None :
        discount = discount.span.string[:-1]

        name = laptop.find('div', class_='prdtBTit')
        if name != None :
            name = name.string
            #print(name)
            if 'HP ' in name:
                return('HP ', int(discount))
            elif 'ASUS ' in name:
                return('ASUS ', int(discount))
    return None

#def getKarma(url):


url = 'https://www.cdiscount.com/informatique/ordinateurs-pc-portables/pc-portables/lf-228394_520-neuf.html'


#print(getDiscount(url))

print(getLaptops(url))
