from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from functools import reduce
import logging

logger = logging.getLogger(__name__)

session = requests.Session()
session.trust_env = False

def getSoupFromURL(url):
    res = session.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup
    else:
        return None


def getTop256(url):
    df_top = pd.DataFrame(columns=["name","count"])
    soup = getSoupFromURL(url)
    table = soup.find('tbody')
    for user in table.find_all('tr'):
        new_user = pd.DataFrame(
                [[user.td.a.string,user.td.next_sibling.next_sibling.string]],
                columns=["name","count"])
        df_top = df_top.append(new_user, ignore_index=True)
        #print(user.td.a.string)
        #print(user.td.next_sibling.next_sibling.string)

    #discount = [getDiscount(laptop) for laptop in result.find_all('li')]
    return df_top

def get_repos(username):
     res = session.get("https://api.github.com/users/"+username)
     if res.status_code == 200:
         nb_pages = int(round(res.json()['public_repos']/100))
         print(nb_pages)
         return mean_stars(username, nb_pages)
     else:
         return None

def mean_stars(username, nb_pages):

    repos = []
    for page in range(1,nb_pages+1):
        payload = {
           'oauth_token': "f620cb7ad0a6d79e0dee541810626121d1ab5c81",
           'oauth_version': 1.0,
           'per_page': 100,
           'page': page
        }
        res = session.get("https://api.github.com/users/"+username+"/repos", params=payload)
        if res.status_code == 200:
            repos += res.json()

    stars = list(map(lambda x: x['stargazers_count'], repos))
    mean_stars = round(reduce(lambda x, y: x + y, stars) / len(stars),2)
    return pd.DataFrame([[username,mean_stars]],
                        columns=["name","stars"])


def main():
   #ts = time()
   df_stars = pd.DataFrame(columns=["name","stars"])
   url = 'https://gist.github.com/paulmillr/2657075'
   df_top = getTop256(url)
   #results = get_repos()
   # with Pool(8) as p:
    #   r = p.map(df_top['name'], results)
   # print('Took {}s'.format(time() - ts))
   for username in df_top['name']:
       print(username)
       df_stars = df_stars.append(get_repos(username), ignore_index=True)
   print(df_stars)


# url = 'https://gist.github.com/paulmillr/2657075'
# print(getTop256(url))


   #getTop256(url)
#print(get_repos("AdamBien"))

main()
