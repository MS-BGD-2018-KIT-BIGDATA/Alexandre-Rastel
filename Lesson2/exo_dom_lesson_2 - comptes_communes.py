import requests
import re
from bs4 import BeautifulSoup

def getComptesCommunes(url, year):

	results = dict()

	payload = {
		'icom':'056',
		'dep':'075',
		'type':'BPS',
		'param':'5',
		'exercice': str(year)
	}

	htmlText = requests.get(url, params=payload).text

	soup = BeautifulSoup(htmlText, 'html.parser')

	for line in soup.find_all('tr'):
		libelle = line.find("td", class_="libellepetit G")
		if( (libelle != None) ):
			libelle = re.search(r'= ([A-D])$', libelle.string)
			if( libelle != None):
				results[str(libelle.group(1))] = {}
				results[str(libelle.group(1))]['habitant'] = int(re.sub('[^1-9]','',line.contents[3].text))
				results[str(libelle.group(1))]['strate'] = int(re.sub('[^1-9]','',line.contents[5].text))

	return results
# 
# def test(year):
# 	yeah = {}
# 	yeah[year] = 'yeah'
# 	return yeah

def main():

	res = {}
	for year in range(2010,2016):
		stage = {}
		stage[year] = getComptesCommunes("http://alize2.finances.gouv.fr/communes/eneuro/detail.php", year)
	 	res = dict(res, **stage)
	print(res)

main()
