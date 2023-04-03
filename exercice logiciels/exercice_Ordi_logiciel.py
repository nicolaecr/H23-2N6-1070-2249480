class Ordinateur:
    
    def __init__(self,ID, adresseIP, processeur=None, memoire_vive=None) -> None:
        self.ID = ID
        self.adresseIP = adresseIP
        self.processeur = processeur
        self.memoire_vive =memoire_vive
    
    def __str__(self) -> str:
        return
    
    @classmethod
    def upgrader_processeur(cls, nouveau_processeur) -> None:
        return cls(processeur = nouveau_processeur)
    @classmethod
    def upgrader_memoire(cls, nouvelle_norme) -> None:
        return cls(memoire_vive = nouvelle_norme)
    
   
class Poste_de_travail(Ordinateur):
    
    def __init__(self,ID, adresseIP, utilisation,processeur=None, memoire_vive=None) -> None:
        super().__init__(self,ID,adresseIP,processeur,memoire_vive)
        self.utilisation =utilisation
    
    def installer_logiciel(self,logiciel,version) -> None:
        self.logiciel = logiciel
        self.version = version
        
        pass
    def desinstaller_logiciel(self,logiciel,version) -> None:
        pass 
    
    def imprimer_liste_logiciels(self) -> None:
        pass
    

