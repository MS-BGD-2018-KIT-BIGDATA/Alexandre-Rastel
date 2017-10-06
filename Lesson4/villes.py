from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from functools import reduce
import logging
import time
import csv

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

def getTop100(url):
    top100 = []
    soup = getSoupFromURL(url)
    table = soup.find('table')
    # print(table)
    for user in table.find_all('tr'):
        if user is not None:
        # new_user = pd.DataFrame(
            if user.td is not None:
                top100.append(user.td.next_sibling.next_sibling.a.text)#,user.td.next_sibling.next_sibling.string]],
    #             columns=["name","count"])
    #     df_top = df_top.append(new_user, ignore_index=True)
        #print(user.td.a.string)
        #print(user.td.next_sibling.next_sibling.string)

    #discount = [getDiscount(laptop) for laptop in result.find_all('li')]
    top100[:100]
    return top100

def get_matrix(cities):
    params = {
        'origins':cities,
        'destinations': cities,
        'departure_time':'1507400230',
        'traffic_model':'best_guess',
        'key':'AIzaSyDvdlISuEqFVm4s_0bP5vHpmJlPnocCHE0'
    }
    res = session.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=params)
    if res.status_code == 200:
         dist = res.json()
         return dist
    else:
         return None

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


# print(get_matrix('sdbf'))
top100 = getTop100('https://fr.wikipedia.org/wiki/Liste_des_communes_de_France_les_plus_peupl%C3%A9es')
n = 10
splited = [top100[i:i + n] for i in range(0, len(top100), n)]

res = get_matrix('|'.join(splited[0]))
double_list = [res['origin_addresses']]
for row in res['rows']:
    list_row = []
    for element in row['elements']:
        list_row.append(element['distance']['text'])
    double_list.append(list_row)
print(double_list)

with open("matrix.csv", 'w+') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for row in double_list:
        wr.writerow(row)
