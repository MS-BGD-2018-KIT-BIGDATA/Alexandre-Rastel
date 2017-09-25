import requests
import re

def getNbVuesYoutube(url):

	htmlText = requests.get(url).text

	regex = r"(<div class=\"watch-view-count\">)(.*?)(?=vues)"

	matches = re.search(regex, htmlText)

	return matches[2]

def main():

	print(getNbVuesYoutube("https://www.youtube.com/watch?v=2bjk26RwjyU"))


main()
