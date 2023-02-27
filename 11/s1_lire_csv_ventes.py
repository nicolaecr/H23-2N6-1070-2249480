
import csv
from dis import disco
import json
import os
from statistics import quantiles

from traitlets import parse_notifier_name
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# Vous devez lire et extraire les informations du csv "data_ventes.csv"
# Le format de ce csv ne permet pas d'extraire les données très facilement.
# Regardez-le avant de commencer.

# Pour chaque client, il y la quantité de chacun des produits qu'ils ont achetés. 
# Les ids des produits sont dans l'en-tête et en ordre. 
# Donc les valeurs dans la colonne prodID1 correspondent à la quantité du produit dont l'ID est 1.
# Il en est ainsi pour chacun des 20 produits disponibles.

# Le but ultime de ce script est d'arriver à une liste, contenant pour chaque client
with open("data_ventes.csv","r",encoding='utf-8') as fichier :
    csv_reader = csv.reader(fichier)
    next(csv_reader)
    next(csv_reader)
    next(csv_reader)
    next(csv_reader)
    next(csv_reader)
    liste_client = []
    dic = {}
    int = 1
    quantity = 3
    for line in csv_reader:
        dic = {"ID":line[0],"nom":line[1],"prenom":line[2]}
        #for 
        int+= 1
        quantity+= 1
        liste_client.append(dic)
        print(json.dumps(liste_client,indent=4))
        
#"commande":[int],"quantity":line[quantity]

