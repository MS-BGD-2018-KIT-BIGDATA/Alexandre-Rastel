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


def getDiscount(url):
    soup = getSoupFromURL(url)
    result = soup.find_all('dic', class_='ecoBlk')
    discount = [discount.string for discount in result]
    return discount


url = 'https://news.ycombinator.com/'
page = 'news?p='
user_page = 'user?id='

users = []
for i in range(1, 4):
    print(i)
    users += getUsers(url + page + str(i))
print(users)

dico = {}
for j in users:
    dico[j] =
