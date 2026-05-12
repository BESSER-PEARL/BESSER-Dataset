from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class ActionEvent2_Interface:

    pass


class Class:

    pass


class Graphics_Interface:

    pass


class JPanel:

    pass


class Controleur_Controleur:

    def __init__(self, modele: Modele_CModele, Controleur11: "Modele_CModele" = None):
        self.modele = modele
        self.Controleur11 = Controleur11
        
        pass
    @property
    def modele(self):
        return self.__modele
    @modele.setter
    def modele(self, modele: Modele_CModele):
        self.__modele = modele

    @property
    def Controleur11(self):
        return self.__Controleur11
    @Controleur11.setter
    def Controleur11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controleur_Controleur__Controleur11", None)
        self.__Controleur11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CModele_Controleur_010"):
                opp_val = getattr(old_value, "CModele_Controleur_010", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CModele_Controleur_010"):
                opp_val = getattr(value, "CModele_Controleur_010", None)
                if opp_val is None:
                    setattr(value, "CModele_Controleur_010", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Observable(ABC):

    pass


class Observer_Interface:

    pass


class Modele_Participants:

    def __init__(self, NOMBRE: int, attribute: str, Joueur12: set["Modele_Joueur"] = None):
        self.NOMBRE = NOMBRE
        self.attribute = attribute
        self.Joueur12 = Joueur12 if Joueur12 is not None else set()
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def NOMBRE(self):
        return self.__NOMBRE
    @NOMBRE.setter
    def NOMBRE(self, NOMBRE: int):
        self.__NOMBRE = NOMBRE

    @property
    def Joueur12(self):
        return self.__Joueur12
    @Joueur12.setter
    def Joueur12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Modele_Participants__Joueur12", None)
        self.__Joueur12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Participants13"):
                    opp_val = getattr(item, "Participants13", None)
                    
                    if opp_val == self:
                        setattr(item, "Participants13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Participants13"):
                    opp_val = getattr(item, "Participants13", None)
                    
                    setattr(item, "Participants13", self)
                    



class Modele_Joueur:

    def __init__(self, cles: int, x: int, y: int, artefacts: str, vivant: bool, Participants13: "Modele_Participants" = None):
        self.cles = cles
        self.x = x
        self.y = y
        self.artefacts = artefacts
        self.vivant = vivant
        self.Participants13 = Participants13
        
        pass
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def vivant(self):
        return self.__vivant
    @vivant.setter
    def vivant(self, vivant: bool):
        self.__vivant = vivant

    @property
    def cles(self):
        return self.__cles
    @cles.setter
    def cles(self, cles: int):
        self.__cles = cles

    @property
    def artefacts(self):
        return self.__artefacts
    @artefacts.setter
    def artefacts(self, artefacts: str):
        self.__artefacts = artefacts

    @property
    def Participants13(self):
        return self.__Participants13
    @Participants13.setter
    def Participants13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Modele_Joueur__Participants13", None)
        self.__Participants13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Joueur12"):
                opp_val = getattr(old_value, "Joueur12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Joueur12"):
                opp_val = getattr(value, "Joueur12", None)
                if opp_val is None:
                    setattr(value, "Joueur12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Modele_Cellule:

    def __init__(self, modele: Modele_CModele, etat: bool, x: int, prochaineEtat: bool, y: int, CModele9: "Modele_CModele" = None):
        self.modele = modele
        self.etat = etat
        self.x = x
        self.prochaineEtat = prochaineEtat
        self.y = y
        self.CModele9 = CModele9
        
        pass
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def modele(self):
        return self.__modele
    @modele.setter
    def modele(self, modele: Modele_CModele):
        self.__modele = modele

    @property
    def etat(self):
        return self.__etat
    @etat.setter
    def etat(self, etat: bool):
        self.__etat = etat

    @property
    def prochaineEtat(self):
        return self.__prochaineEtat
    @prochaineEtat.setter
    def prochaineEtat(self, prochaineEtat: bool):
        self.__prochaineEtat = prochaineEtat

    @property
    def CModele9(self):
        return self.__CModele9
    @CModele9.setter
    def CModele9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Modele_Cellule__CModele9", None)
        self.__CModele9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cellule8"):
                opp_val = getattr(old_value, "Cellule8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cellule8"):
                opp_val = getattr(value, "Cellule8", None)
                if opp_val is None:
                    setattr(value, "Cellule8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Modele_CModele:

    def __init__(self, hauteur: int, largeur: int, attribute: Modele_Cellule, VueGrille_CModele_13: set["Vue_VueGrille"] = None, VueCommande_CModele_17: set["Vue_VueCommande"] = None, Cellule8: set["Modele_Cellule"] = None, CModele_Controleur_010: set["Controleur_Controleur"] = None):
        self.hauteur = hauteur
        self.largeur = largeur
        self.attribute = attribute
        self.VueGrille_CModele_13 = VueGrille_CModele_13 if VueGrille_CModele_13 is not None else set()
        self.VueCommande_CModele_17 = VueCommande_CModele_17 if VueCommande_CModele_17 is not None else set()
        self.Cellule8 = Cellule8 if Cellule8 is not None else set()
        self.CModele_Controleur_010 = CModele_Controleur_010 if CModele_Controleur_010 is not None else set()
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: Modele_Cellule):
        self.__attribute = attribute

    @property
    def hauteur(self):
        return self.__hauteur
    @hauteur.setter
    def hauteur(self, hauteur: int):
        self.__hauteur = hauteur

    @property
    def largeur(self):
        return self.__largeur
    @largeur.setter
    def largeur(self, largeur: int):
        self.__largeur = largeur

    @property
    def Cellule8(self):
        return self.__Cellule8
    @Cellule8.setter
    def Cellule8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Modele_CModele__Cellule8", None)
        self.__Cellule8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CModele9"):
                    opp_val = getattr(item, "CModele9", None)
                    
                    if opp_val == self:
                        setattr(item, "CModele9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CModele9"):
                    opp_val = getattr(item, "CModele9", None)
                    
                    setattr(item, "CModele9", self)
                    

    @property
    def VueGrille_CModele_13(self):
        return self.__VueGrille_CModele_13
    @VueGrille_CModele_13.setter
    def VueGrille_CModele_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Modele_CModele__VueGrille_CModele_13", None)
        self.__VueGrille_CModele_13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VueGrille_CModele_02"):
                    opp_val = getattr(item, "VueGrille_CModele_02", None)
                    
                    if opp_val == self:
                        setattr(item, "VueGrille_CModele_02", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VueGrille_CModele_02"):
                    opp_val = getattr(item, "VueGrille_CModele_02", None)
                    
                    setattr(item, "VueGrille_CModele_02", self)
                    

    @property
    def VueCommande_CModele_17(self):
        return self.__VueCommande_CModele_17
    @VueCommande_CModele_17.setter
    def VueCommande_CModele_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Modele_CModele__VueCommande_CModele_17", None)
        self.__VueCommande_CModele_17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VueCommande_CModele_06"):
                    opp_val = getattr(item, "VueCommande_CModele_06", None)
                    
                    if opp_val == self:
                        setattr(item, "VueCommande_CModele_06", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VueCommande_CModele_06"):
                    opp_val = getattr(item, "VueCommande_CModele_06", None)
                    
                    setattr(item, "VueCommande_CModele_06", self)
                    

    @property
    def CModele_Controleur_010(self):
        return self.__CModele_Controleur_010
    @CModele_Controleur_010.setter
    def CModele_Controleur_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Modele_CModele__CModele_Controleur_010", None)
        self.__CModele_Controleur_010 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Controleur11"):
                    opp_val = getattr(item, "Controleur11", None)
                    
                    if opp_val == self:
                        setattr(item, "Controleur11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Controleur11"):
                    opp_val = getattr(item, "Controleur11", None)
                    
                    setattr(item, "Controleur11", self)
                    



class Vue_CVue:

    def __init__(self, frame: str, grille: Vue_VueGrille, commande: Vue_VueCommande, VueGrille_CVue_11: "Vue_VueGrille" = None, CVue_VueCommande_04: "Vue_VueCommande" = None):
        self.frame = frame
        self.grille = grille
        self.commande = commande
        self.VueGrille_CVue_11 = VueGrille_CVue_11
        self.CVue_VueCommande_04 = CVue_VueCommande_04
        
        pass
    @property
    def frame(self):
        return self.__frame
    @frame.setter
    def frame(self, frame: str):
        self.__frame = frame

    @property
    def commande(self):
        return self.__commande
    @commande.setter
    def commande(self, commande: Vue_VueCommande):
        self.__commande = commande

    @property
    def grille(self):
        return self.__grille
    @grille.setter
    def grille(self, grille: Vue_VueGrille):
        self.__grille = grille

    @property
    def VueGrille_CVue_11(self):
        return self.__VueGrille_CVue_11
    @VueGrille_CVue_11.setter
    def VueGrille_CVue_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vue_CVue__VueGrille_CVue_11", None)
        self.__VueGrille_CVue_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VueGrille_CVue_00"):
                opp_val = getattr(old_value, "VueGrille_CVue_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VueGrille_CVue_00"):
                opp_val = getattr(value, "VueGrille_CVue_00", None)
                if opp_val is None:
                    setattr(value, "VueGrille_CVue_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CVue_VueCommande_04(self):
        return self.__CVue_VueCommande_04
    @CVue_VueCommande_04.setter
    def CVue_VueCommande_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vue_CVue__CVue_VueCommande_04", None)
        self.__CVue_VueCommande_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CVue_VueCommande_15"):
                opp_val = getattr(old_value, "CVue_VueCommande_15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CVue_VueCommande_15"):
                opp_val = getattr(value, "CVue_VueCommande_15", None)
                if opp_val is None:
                    setattr(value, "CVue_VueCommande_15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Vue_VueGrille:

    def __init__(self, modele: Modele_CModele, TAILLE: int, update: str, VueGrille_CVue_00: set["Vue_CVue"] = None, VueGrille_CModele_02: "Modele_CModele" = None):
        self.modele = modele
        self.TAILLE = TAILLE
        self.update = update
        self.VueGrille_CVue_00 = VueGrille_CVue_00 if VueGrille_CVue_00 is not None else set()
        self.VueGrille_CModele_02 = VueGrille_CModele_02
        
        pass
    @property
    def modele(self):
        return self.__modele
    @modele.setter
    def modele(self, modele: Modele_CModele):
        self.__modele = modele

    @property
    def update(self):
        return self.__update
    @update.setter
    def update(self, update: str):
        self.__update = update

    @property
    def TAILLE(self):
        return self.__TAILLE
    @TAILLE.setter
    def TAILLE(self, TAILLE: int):
        self.__TAILLE = TAILLE

    @property
    def VueGrille_CModele_02(self):
        return self.__VueGrille_CModele_02
    @VueGrille_CModele_02.setter
    def VueGrille_CModele_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vue_VueGrille__VueGrille_CModele_02", None)
        self.__VueGrille_CModele_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VueGrille_CModele_13"):
                opp_val = getattr(old_value, "VueGrille_CModele_13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VueGrille_CModele_13"):
                opp_val = getattr(value, "VueGrille_CModele_13", None)
                if opp_val is None:
                    setattr(value, "VueGrille_CModele_13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def VueGrille_CVue_00(self):
        return self.__VueGrille_CVue_00
    @VueGrille_CVue_00.setter
    def VueGrille_CVue_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vue_VueGrille__VueGrille_CVue_00", None)
        self.__VueGrille_CVue_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VueGrille_CVue_11"):
                    opp_val = getattr(item, "VueGrille_CVue_11", None)
                    
                    if opp_val == self:
                        setattr(item, "VueGrille_CVue_11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VueGrille_CVue_11"):
                    opp_val = getattr(item, "VueGrille_CVue_11", None)
                    
                    setattr(item, "VueGrille_CVue_11", self)
                    



class Vue_VueCommande:

    def __init__(self, modele: Modele_CModele, CVue_VueCommande_15: set["Vue_CVue"] = None, VueCommande_CModele_06: "Modele_CModele" = None):
        self.modele = modele
        self.CVue_VueCommande_15 = CVue_VueCommande_15 if CVue_VueCommande_15 is not None else set()
        self.VueCommande_CModele_06 = VueCommande_CModele_06
        
        pass
    @property
    def modele(self):
        return self.__modele
    @modele.setter
    def modele(self, modele: Modele_CModele):
        self.__modele = modele

    @property
    def VueCommande_CModele_06(self):
        return self.__VueCommande_CModele_06
    @VueCommande_CModele_06.setter
    def VueCommande_CModele_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vue_VueCommande__VueCommande_CModele_06", None)
        self.__VueCommande_CModele_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VueCommande_CModele_17"):
                opp_val = getattr(old_value, "VueCommande_CModele_17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VueCommande_CModele_17"):
                opp_val = getattr(value, "VueCommande_CModele_17", None)
                if opp_val is None:
                    setattr(value, "VueCommande_CModele_17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CVue_VueCommande_15(self):
        return self.__CVue_VueCommande_15
    @CVue_VueCommande_15.setter
    def CVue_VueCommande_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vue_VueCommande__CVue_VueCommande_15", None)
        self.__CVue_VueCommande_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CVue_VueCommande_04"):
                    opp_val = getattr(item, "CVue_VueCommande_04", None)
                    
                    if opp_val == self:
                        setattr(item, "CVue_VueCommande_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CVue_VueCommande_04"):
                    opp_val = getattr(item, "CVue_VueCommande_04", None)
                    
                    setattr(item, "CVue_VueCommande_04", self)
                    



class ActionListener_Interface:

    pass
