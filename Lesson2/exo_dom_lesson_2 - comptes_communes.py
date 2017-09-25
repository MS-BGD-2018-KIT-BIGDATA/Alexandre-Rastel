import requests
import re

def getComptesCommunes(url):

	payload = {
		'icom':'056',
		'dep':'075',
		'type':'BPS',
		'param':'5',
		'exercice':'2010'
	}

	htmlText = requests.get(url, data=payload).text

	regex = r"(<tr class=\"bleu\">).{5}"

	#regex = r"(<tr class=\"bleu\">)(.*?)(?=<td class=\"libellepetit G\">TOTAL DES PRODUITS DE FONCTIONNEMENT = A</td>)"

	#regex = r"(<div class=\"watch-view-count\">)(.*?)(?=vues)"

	matches = re.search(regex, htmlText)
	print(matches)

	return matches[2]

	#return htmlText

def main():

	print(getComptesCommunes("http://alize2.finances.gouv.fr/communes/eneuro/detail.php"))


main()
