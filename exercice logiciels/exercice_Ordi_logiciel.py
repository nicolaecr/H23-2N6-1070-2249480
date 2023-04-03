class Ordinateur:
    
    def __init__(self,ID, adresseIP, processeur=None, memoire_vive=None) -> None:
        pass
    
    def __str__(self) -> str:
        pass
    
    @classmethod
    def upgrader_processeur(cls, nouveau_processeur) -> None:
        pass
    
    @classmethod
    def upgrader_memoire(cls, nouvelle_norme) -> None:
        pass
    
   
class Poste_de_travail(Ordinateur):
    
    def __init__(self,ID, adresseIP, utilisation,processeur=None, memoire_vive=None) -> None:
        pass
    
    def installer_logiciel(self,logiciel,version) -> None:
        pass 
    
    def desinstaller_logiciel(self,logiciel,version) -> None:
        pass 
    
    def imprimer_liste_logiciels(self) -> None:
        pass
    

