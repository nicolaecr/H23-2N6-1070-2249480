# On peut faire une invitation générale comme cela, mais c'est un peu froid
# Nous avons ici une simple invitation, sans nom précis #
# Si on envoie cette invitation à nos amis, ils pourraient être fachés car c'est un peu impersonnel.#
from multiprocessing.dummy import JoinableQueue


print("Bonjour \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")





# Nous avons ici la même invitation lancée à plusieurs de nos amis, avec leurs noms.                       #
print("Bonjour Marc,\n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Pierre,\n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Lucie, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Achraf, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Claude, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Ilyan, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Maria, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Thomas, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
# Cest mieux mais c'est de la répétition.  Et si je voulais inviter 30 personnes....

# Q1 A:  Faites une fonction pour inviter tout le monde, sans duplication du code.
#        Cette fonction prendra une liste d'amis en paramètres                                      #
def invitation(liste_ami):
    for amis in liste_ami:
        print(f"Bonjour {amis},\n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
  
  
  
  

# Q1 B:   Appel de la fonction avec la liste d'amis qu'on veut inviter. 
#         Il faudra créer une liste qui comprendra les noms de nos amis, "Marc","Pierre", etc
#         Puis faites l'appel de la fonction en lui passant en paramètre votre liste d'amis
liste_ami = ["Marc","Pierre","Lucie","Achraf","Claude"]
invitation(liste_ami)




# Q2 A:   Fonction pour inviter tout le monde, dans un lieu, un jour et une heure qui varient, sans duplication du code
#         Appelez cette fonction invitation2
def inviatition2(ami,lieux,jour,heure):
        print(f"Bonjour {ami} \n Je veux t'inviter à venir {lieux} {jour} vers {heure}. Cela t'intéresse?")

# Q2 B:  Appel de la fonction invitation2 pour inviter Sylvain et Nathalie au café étudiant, vendredi, vers 13h00
inviatition2("Nathalie","café étudiant","vendredi","13h00")
inviatition2("Sylvain","café étudiant","vendredi","13h00")

# Q2 C:  Appel de la fonction invitation2 pour inviter Sylvain, Nathalie et Paul chez moi pour souper, samedi vers 17h00
inviatition2("Nathalie","chez moi","samedi","17h00")
inviatition2("Sylvain","chez moi","samedi","17h00")
inviatition2("Paul","chez moi","samedi","17h00")

