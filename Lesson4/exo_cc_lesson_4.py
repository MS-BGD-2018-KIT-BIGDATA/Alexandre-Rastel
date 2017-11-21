from bs4 import BeautifulSoup
import requests
import re
import json
import pandas as pd


def medicament(code_med):
    med = requests.get("http://www.open-medicaments.fr/api/v1/medicaments/" + str(code_med))
    med = med.json()
    denomination = str(med["denomination"]).split(" ")
    nom = denomination[0]
    labo = denomination[1]
    actif = med["compositions"][0]["substancesActives"][0]["dosageSubstance"] # a diviser par refer
    prix = med["presentations"][0]["prix"]
    libelle = med["presentations"][0]["libelle"]
    nb_comprimes = re.search(r'(\d{1,4})(?: comprim)', libelle)
    if nb_comprimes != None:
        nb_comprimes = nb_comprimes.group(1)
    else:
        nb_comprimes = re.search(r'(\d{1,4})(?: m?l)', libelle)
        if nb_comprimes != None:
            nb_comprimes = nb_comprimes.group(1)
    ligne = pd.DataFrame([nom, labo, actif, libelle, nb_comprimes], index=["nom", "labo", "actif", "libelle", "comprimes"])
    return ligne



params={
    "query": "ibuprofene",
    "limit":10
}
res = requests.get("http://www.open-medicaments.fr/api/v1/medicaments", params=params)
res = res.json()


for e in res:
    if "codeCIS" in e:
        print(medicament(e["codeCIS"]))
