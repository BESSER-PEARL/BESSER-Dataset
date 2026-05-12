from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Toit:

    def __init__(self, IntNumereoWagon: int):
        self.IntNumereoWagon = IntNumereoWagon
        
        pass
    @property
    def IntNumereoWagon(self):
        return self.__IntNumereoWagon
    @IntNumereoWagon.setter
    def IntNumereoWagon(self, IntNumereoWagon: int):
        self.__IntNumereoWagon = IntNumereoWagon



class Interieur:

    def __init__(self, InnumeroWagon: int):
        self.InnumeroWagon = InnumeroWagon
        
        pass
    @property
    def InnumeroWagon(self):
        return self.__InnumeroWagon
    @InnumeroWagon.setter
    def InnumeroWagon(self, InnumeroWagon: int):
        self.__InnumeroWagon = InnumeroWagon



class Position:

    def __init__(self, numeroWagon: int):
        self.numeroWagon = numeroWagon
        
        pass
    @property
    def numeroWagon(self):
        return self.__numeroWagon
    @numeroWagon.setter
    def numeroWagon(self, numeroWagon: int):
        self.__numeroWagon = numeroWagon



class Controleur:

    def __init__(self, modeletrain: ModelTraint, vue: Vue, vue6: "Vue" = None):
        self.modeletrain = modeletrain
        self.vue = vue
        self.vue6 = vue6
        
        pass
    @property
    def modeletrain(self):
        return self.__modeletrain
    @modeletrain.setter
    def modeletrain(self, modeletrain: ModelTraint):
        self.__modeletrain = modeletrain

    @property
    def vue(self):
        return self.__vue
    @vue.setter
    def vue(self, vue: Vue):
        self.__vue = vue

    @property
    def vue6(self):
        return self.__vue6
    @vue6.setter
    def vue6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controleur__vue6", None)
        self.__vue6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controleur7"):
                opp_val = getattr(old_value, "controleur7", None)
                if opp_val == self:
                    setattr(old_value, "controleur7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controleur7"):
                opp_val = getattr(value, "controleur7", None)
                setattr(value, "controleur7", self)



class Vue:

    def __init__(self, modeltrain: ModelTraint, controleur7: "Controleur" = None):
        self.modeltrain = modeltrain
        self.controleur7 = controleur7
        
        pass
    @property
    def modeltrain(self):
        return self.__modeltrain
    @modeltrain.setter
    def modeltrain(self, modeltrain: ModelTraint):
        self.__modeltrain = modeltrain

    @property
    def controleur7(self):
        return self.__controleur7
    @controleur7.setter
    def controleur7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vue__controleur7", None)
        self.__controleur7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vue6"):
                opp_val = getattr(old_value, "vue6", None)
                if opp_val == self:
                    setattr(old_value, "vue6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vue6"):
                opp_val = getattr(value, "vue6", None)
                setattr(value, "vue6", self)



class Obsever_Interface:

    pass


class Cellule:

    def __init__(self, model: ModelTraint, modelTraint0: "ModelTraint" = None):
        self.model = model
        self.modelTraint0 = modelTraint0
        
        pass
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model: ModelTraint):
        self.__model = model

    @property
    def modelTraint0(self):
        return self.__modelTraint0
    @modelTraint0.setter
    def modelTraint0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cellule__modelTraint0", None)
        self.__modelTraint0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cellule1"):
                opp_val = getattr(old_value, "cellule1", None)
                if opp_val == self:
                    setattr(old_value, "cellule1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cellule1"):
                opp_val = getattr(value, "cellule1", None)
                setattr(value, "cellule1", self)



class Joueur:

    def __init__(self, model: ModelTraint, nomJoueur: str, x_y: int, a_b: int, positionBandit: Position, attribute: str, modelTrant3: "ModelTraint" = None):
        self.model = model
        self.nomJoueur = nomJoueur
        self.x_y = x_y
        self.a_b = a_b
        self.positionBandit = positionBandit
        self.attribute = attribute
        self.modelTrant3 = modelTrant3
        
        pass
    @property
    def a_b(self):
        return self.__a_b
    @a_b.setter
    def a_b(self, a_b: int):
        self.__a_b = a_b

    @property
    def x_y(self):
        return self.__x_y
    @x_y.setter
    def x_y(self, x_y: int):
        self.__x_y = x_y

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model: ModelTraint):
        self.__model = model

    @property
    def nomJoueur(self):
        return self.__nomJoueur
    @nomJoueur.setter
    def nomJoueur(self, nomJoueur: str):
        self.__nomJoueur = nomJoueur

    @property
    def positionBandit(self):
        return self.__positionBandit
    @positionBandit.setter
    def positionBandit(self, positionBandit: Position):
        self.__positionBandit = positionBandit

    @property
    def modelTrant3(self):
        return self.__modelTrant3
    @modelTrant3.setter
    def modelTrant3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Joueur__modelTrant3", None)
        self.__modelTrant3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "joueurs2"):
                opp_val = getattr(old_value, "joueurs2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "joueurs2"):
                opp_val = getattr(value, "joueurs2", None)
                if opp_val is None:
                    setattr(value, "joueurs2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Wagon:

    def __init__(self, modele: ModelTraint, numeroWagon: int, ListedesButin__: str, listeDesBandit: Joueur, modelTrant5: set["ModelTraint"] = None):
        self.modele = modele
        self.numeroWagon = numeroWagon
        self.ListedesButin__ = ListedesButin__
        self.listeDesBandit = listeDesBandit
        self.modelTrant5 = modelTrant5 if modelTrant5 is not None else set()
        
        pass
    @property
    def ListedesButin__(self):
        return self.__ListedesButin__
    @ListedesButin__.setter
    def ListedesButin__(self, ListedesButin__: str):
        self.__ListedesButin__ = ListedesButin__

    @property
    def numeroWagon(self):
        return self.__numeroWagon
    @numeroWagon.setter
    def numeroWagon(self, numeroWagon: int):
        self.__numeroWagon = numeroWagon

    @property
    def listeDesBandit(self):
        return self.__listeDesBandit
    @listeDesBandit.setter
    def listeDesBandit(self, listeDesBandit: Joueur):
        self.__listeDesBandit = listeDesBandit

    @property
    def modele(self):
        return self.__modele
    @modele.setter
    def modele(self, modele: ModelTraint):
        self.__modele = modele

    @property
    def modelTrant5(self):
        return self.__modelTrant5
    @modelTrant5.setter
    def modelTrant5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wagon__modelTrant5", None)
        self.__modelTrant5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wagons4"):
                    opp_val = getattr(item, "wagons4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wagons4"):
                    opp_val = getattr(item, "wagons4", None)
                    
                    if opp_val is None:
                        setattr(item, "wagons4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Observable(ABC):

    def __init__(self, listObservers__: str):
        self.listObservers__ = listObservers__
        
        pass
    @property
    def listObservers__(self):
        return self.__listObservers__
    @listObservers__.setter
    def listObservers__(self, listObservers__: str):
        self.__listObservers__ = listObservers__



class ModelTraint:

    def __init__(self, listeWagon__: Wagon, cellule____: Cellule, joueurs__: Joueur, indiceWagonCourant: int, indiceJoueurCourant: int, nombreWagon: int, nombreJoueur: int, cellule1: "Cellule" = None, joueurs2: set["Joueur"] = None, wagons4: set["Wagon"] = None):
        self.listeWagon__ = listeWagon__
        self.cellule____ = cellule____
        self.joueurs__ = joueurs__
        self.indiceWagonCourant = indiceWagonCourant
        self.indiceJoueurCourant = indiceJoueurCourant
        self.nombreWagon = nombreWagon
        self.nombreJoueur = nombreJoueur
        self.cellule1 = cellule1
        self.joueurs2 = joueurs2 if joueurs2 is not None else set()
        self.wagons4 = wagons4 if wagons4 is not None else set()
        
        pass
    @property
    def indiceWagonCourant(self):
        return self.__indiceWagonCourant
    @indiceWagonCourant.setter
    def indiceWagonCourant(self, indiceWagonCourant: int):
        self.__indiceWagonCourant = indiceWagonCourant

    @property
    def indiceJoueurCourant(self):
        return self.__indiceJoueurCourant
    @indiceJoueurCourant.setter
    def indiceJoueurCourant(self, indiceJoueurCourant: int):
        self.__indiceJoueurCourant = indiceJoueurCourant

    @property
    def listeWagon__(self):
        return self.__listeWagon__
    @listeWagon__.setter
    def listeWagon__(self, listeWagon__: Wagon):
        self.__listeWagon__ = listeWagon__

    @property
    def nombreJoueur(self):
        return self.__nombreJoueur
    @nombreJoueur.setter
    def nombreJoueur(self, nombreJoueur: int):
        self.__nombreJoueur = nombreJoueur

    @property
    def cellule____(self):
        return self.__cellule____
    @cellule____.setter
    def cellule____(self, cellule____: Cellule):
        self.__cellule____ = cellule____

    @property
    def nombreWagon(self):
        return self.__nombreWagon
    @nombreWagon.setter
    def nombreWagon(self, nombreWagon: int):
        self.__nombreWagon = nombreWagon

    @property
    def joueurs__(self):
        return self.__joueurs__
    @joueurs__.setter
    def joueurs__(self, joueurs__: Joueur):
        self.__joueurs__ = joueurs__

    @property
    def cellule1(self):
        return self.__cellule1
    @cellule1.setter
    def cellule1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ModelTraint__cellule1", None)
        self.__cellule1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelTraint0"):
                opp_val = getattr(old_value, "modelTraint0", None)
                if opp_val == self:
                    setattr(old_value, "modelTraint0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelTraint0"):
                opp_val = getattr(value, "modelTraint0", None)
                setattr(value, "modelTraint0", self)

    @property
    def joueurs2(self):
        return self.__joueurs2
    @joueurs2.setter
    def joueurs2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ModelTraint__joueurs2", None)
        self.__joueurs2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modelTrant3"):
                    opp_val = getattr(item, "modelTrant3", None)
                    
                    if opp_val == self:
                        setattr(item, "modelTrant3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modelTrant3"):
                    opp_val = getattr(item, "modelTrant3", None)
                    
                    setattr(item, "modelTrant3", self)
                    

    @property
    def wagons4(self):
        return self.__wagons4
    @wagons4.setter
    def wagons4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ModelTraint__wagons4", None)
        self.__wagons4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modelTrant5"):
                    opp_val = getattr(item, "modelTrant5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modelTrant5"):
                    opp_val = getattr(item, "modelTrant5", None)
                    
                    if opp_val is None:
                        setattr(item, "modelTrant5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

