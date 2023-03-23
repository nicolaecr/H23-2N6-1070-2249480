from operator import eq


class personne :
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

class joueur(personne) :
    def __init__(self, nom, prenom, date_naissance,no_chandail,position):
        super().__init__(nom, prenom, date_naissance)
        self.no_chandail = no_chandail
        self.position = position
        
class attaquant(joueur):
    def __init__(self, nom, prenom, date_naissance,no_chandail,position,nb_tirs_but,nb_assist):
        super().__init__(nom, prenom, date_naissance,no_chandail,position)
        self.nb_tirs_but = nb_tirs_but
        self.nb_assist = nb_assist
    def compter_but(self):
        self.nb_tirs_but += 1
class defenceur(joueur):
    def __init__(self, nom, prenom, date_naissance,no_chandail,position,nb_interceptions,nb_passes):
        super().__init__(nom, prenom, date_naissance,no_chandail,position)
        self.nb_interceptions = nb_interceptions
        self.nb_passes = nb_passes
class guardien(joueur):
    def __init__(self, nom, prenom, date_naissance,no_chandail,position,nb_arret,nb_tirs_essuyes):
        super().__init__(nom, prenom, date_naissance,no_chandail,position)
        self.nb_arret = nb_arret
        self.nb_tirs_essuyes = nb_tirs_essuyes
    def arreter_tirs(self):
        self.nb_arret += 1
gardien_Logan_Ketterer = guardien("Ketterer","Logan","9 novembre 1993",1,"Guardien",128,208)
defenseur_Zachary_Brault_Guillard = defenceur("Zachary","Brault Guillard","5 mars 1991",15,"defenceur",32,44)
attaquant_Sunusi_Ibrahim = attaquant("Sunusi","Ibrahim","1 octobre 2002",14,"attaque",23,44)
for player in [gardien_Logan_Ketterer,defenseur_Zachary_Brault_Guillard,attaquant_Sunusi_Ibrahim]:
    print(player.__dict__)
    
    #__str__(self)
    #return(f"{self.nom}")
class equipe:
    nb_joueur = 0
    liste_joueur = []
    def __init__(self,nom,liste_joueur) -> None:
        self.nom = nom
        self.liste_joueur = liste_joueur
        equipe.nb_joueur = len(liste_joueur)
    def engager_player(self):
        equipe.nb_joueur += 1
        pass
    def ejecter_joueur(self):
        equipe.nb_joueur -= 1
        pass