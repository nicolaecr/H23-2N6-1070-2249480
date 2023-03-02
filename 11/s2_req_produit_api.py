import os
import requests
import json
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# Maintenant que nous avons un script capable de lire et décoder le fichier csv.
# Nous voulons ajouter des informations à liste de produits de chaque client
#       le prix de chaque produit et sa catégorie

# Les informations sur les produits proviennent du site du magasin.
# Vous devez aller chercher les informations à l'aide du module requests.
url = "https://fakestoreapi.com/"
import echantillon_data
liste = echantillon_data.liste_clients_s1

import s1_lire_csv_ventes
liste_price =[]
res = requests.get(f"{url}products")
resu = json.dumps(res.json(),indent=4)
resultat = json.loads(resu)
print(json.dumps(resultat,indent=4))

