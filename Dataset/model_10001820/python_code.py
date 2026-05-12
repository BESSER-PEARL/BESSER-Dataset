from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Club_de_lecture_Faire_proposition_UseCase:

    pass


class Club_de_lecture_Emprunter_UseCase:

    pass


class Club_de_lecture_Emprunter_livre_num_rique_UseCase:

    pass


class Club_de_lecture_Emprunter_DVD_UseCase:

    pass


class Club_de_lecture_Emprunter_livres_UseCase:

    pass


class Club_de_lecture_Utilisateur_inscrit_Actor:

    pass


class Club_de_lecture_Consulter_p_riodiques___livres_UseCase:

    pass


class Club_de_lecture_S_inscrire_UseCase:

    pass


class Club_de_lecture_Habitant_Actor:

    pass





class Informations:

    pass


class Livre_num_rique:

    pass


class CD:

    pass


class Livre:

    pass


class Media_physique:

    pass


class Utilisateur_Inscrit1:

    def __init__(self, noCarte: str, empruntLivre8: set["Livre"] = None, cD10: "CD" = None, livre_num_rique12: set["Livre_num_rique"] = None):
        self.noCarte = noCarte
        self.empruntLivre8 = empruntLivre8 if empruntLivre8 is not None else set()
        self.cD10 = cD10
        self.livre_num_rique12 = livre_num_rique12 if livre_num_rique12 is not None else set()
        
        pass
    @property
    def noCarte(self):
        return self.__noCarte
    @noCarte.setter
    def noCarte(self, noCarte: str):
        self.__noCarte = noCarte

    @property
    def empruntLivre8(self):
        return self.__empruntLivre8
    @empruntLivre8.setter
    def empruntLivre8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur_Inscrit1__empruntLivre8", None)
        self.__empruntLivre8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emprunter_9"):
                    opp_val = getattr(item, "emprunter_9", None)
                    
                    if opp_val == self:
                        setattr(item, "emprunter_9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emprunter_9"):
                    opp_val = getattr(item, "emprunter_9", None)
                    
                    setattr(item, "emprunter_9", self)
                    

    @property
    def cD10(self):
        return self.__cD10
    @cD10.setter
    def cD10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur_Inscrit1__cD10", None)
        self.__cD10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "utilisateur_Inscrit11"):
                opp_val = getattr(old_value, "utilisateur_Inscrit11", None)
                if opp_val == self:
                    setattr(old_value, "utilisateur_Inscrit11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "utilisateur_Inscrit11"):
                opp_val = getattr(value, "utilisateur_Inscrit11", None)
                setattr(value, "utilisateur_Inscrit11", self)

    @property
    def livre_num_rique12(self):
        return self.__livre_num_rique12
    @livre_num_rique12.setter
    def livre_num_rique12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur_Inscrit1__livre_num_rique12", None)
        self.__livre_num_rique12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "utilisateur_Inscrit13"):
                    opp_val = getattr(item, "utilisateur_Inscrit13", None)
                    
                    if opp_val == self:
                        setattr(item, "utilisateur_Inscrit13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "utilisateur_Inscrit13"):
                    opp_val = getattr(item, "utilisateur_Inscrit13", None)
                    
                    setattr(item, "utilisateur_Inscrit13", self)
                    



class Utilisateur_Inscrit:

    pass


class Habitant:

    pass


class Animal:

    def __init__(self, Age: str):
        self.Age = Age
        
        pass
    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: str):
        self.__Age = Age



class Responsable_CL:

    pass


class Etudiant:

    pass
