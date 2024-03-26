# -*- coding: utf-8 -*-
import csv, glob, os, re, requests, sys, time
from random import random
from bs4 import BeautifulSoup as bs

# Get the current folder
folder = os.path.abspath(os.path.dirname(sys.argv[0]))
url = "https://www.wikidata.org/w/index.php?go=Lire&search={{query}}&title=Special%3ASearch&ns0=1&ns120=1"
queries = [
"André Mage sieur du Fiefmelin",
"Anthoine de Montchrestien",
"Antoine de La Pujade",
"Antoine Gaillard",
"Arnaud",
"Aymard de Veins",
"Bénésin",
"Bénigne Griguette",
"Benoet du Lac (anagramme de Claude Bonet)",
"Benoît Voron",
"Bernard Bardon de Brun",
"Bourzac",
"Bridard",
"Brion de La Tour",
"Brosse",
"Brosse le jeune",
"C. A. de C.",
"C.-S. de La Croix",
"Catherin Le Doux",
"Chabrol",
"Charles Bauter",
"Charles Bauter (pseudonyme Meliglosse)",
"Charles Chaulmer",
"Charles de Marguetel de Saint-Denis sieur de Saint-Evremond",
"Charles Hulpeau",
"Claude Billard",
"Claude Guérin",
"Cormeil",
"Desmares",
"Dominique Gaspard",
"E. Poytevin",
"Étienne Bellone",
"François Auffray",
"François Berthrand d’Orléans",
"François Chapoton",
"François le Duchat",
"Gabriel Chappuis",
"Gabriel Le Breton",
"Georges Thilloys",
"Grandchamp",
"Guillaume de Coste",
"Guillaume Le Riche",
"Guyllaume Regnault",
"Henry de Barran",
"Hugues de Picou",
"I.D.B.I.",
"I.M.S.",
"Jacques Auger",
"Jacques Champ-Repus",
"Jean Boissin",
"Jean de Beaubreuil",
"Jean de Gombaud",
"Jean de Magnon",
"Jean de Virey",
"Jean Du Teil",
"Jean François Grossombre de Chantelouve",
"Jean Galaut",
"Jean Gaulché",
"Jean George",
"Jean Hays",
"Jean Heudon",
"Jean Le Saulx d'Espannay",
"Jean Leger",
"Jean Prévost",
"Jean Robelin",
"Jean Thomas",
"Jean Gilbert Durval",
"Julien Guersens",
"La Barre",
"La Caze",
"La Morelle",
"La Pinelière",
"La Selve",
"Laurent Du Plastre Vieuget",
"Le Vert",
"Léon Quenel",
"Les Cinq Auteurs",
"Louys Des Masures",
"Louys Le Jars",
"Luc Percheron",
"Margarit Pageau",
"Monsieur de Monléon",
"Nicolas Chrestien des Croix",
"Nicolas Du Peschier",
"Nicolas L’Héritier de Nouvelon",
"Nicolas Romain",
"Octave-César Genetay",
"Oudineau",
"Passart",
"Pierard Poullet",
"Pierre Cotignon de La Charnays",
"Pierre de Bousy",
"Pierre de Brinon de Beaumartin",
"Pierre de Mainfray",
"Pierre de Nancel",
"Pierre et Baptiste Marye",
"Pierre Mouffle",
"Pierre Troterel",
"Rayssiguier",
"Du Rocher",
"sieur de Chazan",
"Simon-Thomas Bazin",
"Thomas Le Coq",
"Thullin",
"Timothée de Chillac",
"Veronneau",
"Ville-Toustain",
"Vincent Borée"
]

outputFile = open("results.csv", "w", encoding="utf-8")
for query in queries:
   time.sleep(0.5+random())
   response = requests.get(url.replace("{{query}}",query.replace(" ","+")))
   html = response.content
   soup = bs(html, 'features="html.parser"')
   id = ""
   description = ""
   try:
      id = soup.select(".wb-itemlink-id")[0].text
      description = soup.select(".wb-itemlink-description")[0].text
   except:
      print("erreur")
   print(id)
   outputFile.writelines(query + "\t" + id + "\t" + description + "\n")
outputFile.close()