from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeArc(Enum):
    ArcSimple = "ArcSimple"
    ReadArc = "ReadArc"


############################################
# Definition of Classes
############################################

class petriNet_PetriNetElt(ABC):

    pass
class petriNet_PetriNet:

    def __init__(self, name: str, petriNet_PetriNet: "petriNet_PetriNetElt" = None, petriNet_PetriNet8: set["petriNet_PetriNetElt"] = None):
        self.name = name
        self.petriNet_PetriNet = petriNet_PetriNet
        self.petriNet_PetriNet8 = petriNet_PetriNet8 if petriNet_PetriNet8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petriNet_PetriNet(self):
        return self.__petriNet_PetriNet

    @petriNet_PetriNet.setter
    def petriNet_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_PetriNet__petriNet_PetriNet", None)
        self.__petriNet_PetriNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_PetriNetElt"):
                opp_val = getattr(old_value, "petriNet_PetriNetElt", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_PetriNetElt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_PetriNetElt"):
                opp_val = getattr(value, "petriNet_PetriNetElt", None)
                setattr(value, "petriNet_PetriNetElt", self)

    @property
    def petriNet_PetriNet8(self):
        return self.__petriNet_PetriNet8

    @petriNet_PetriNet8.setter
    def petriNet_PetriNet8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_PetriNet__petriNet_PetriNet8", None)
        self.__petriNet_PetriNet8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNet_PetriNetElt9"):
                    opp_val = getattr(item, "petriNet_PetriNetElt9", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNet_PetriNetElt9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNet_PetriNetElt9"):
                    opp_val = getattr(item, "petriNet_PetriNetElt9", None)
                    
                    setattr(item, "petriNet_PetriNetElt9", self)
                    

class Noeud:

    pass
class petriNet_Place(Noeud):

    def __init__(self, jeton: int):
        self.jeton = jeton
        
    @property
    def jeton(self) -> int:
        return self.__jeton

    @jeton.setter
    def jeton(self, jeton: int):
        self.__jeton = jeton

class PetriNetElt:

    pass
class petriNet_Arc(PetriNetElt):

    def __init__(self, poids: int, typeArc: str, Arc: "petriNet_Noeud" = None, Arc2: "petriNet_Noeud" = None, noeudsSuccesseurs: "petriNet_Noeud" = None, noeudsPredecesseurs: "petriNet_Noeud" = None):
        self.poids = poids
        self.typeArc = typeArc
        self.Arc = Arc
        self.Arc2 = Arc2
        self.noeudsSuccesseurs = noeudsSuccesseurs
        self.noeudsPredecesseurs = noeudsPredecesseurs
        
    @property
    def typeArc(self) -> str:
        return self.__typeArc

    @typeArc.setter
    def typeArc(self, typeArc: str):
        self.__typeArc = typeArc

    @property
    def poids(self) -> int:
        return self.__poids

    @poids.setter
    def poids(self, poids: int):
        self.__poids = poids

    @property
    def Arc2(self):
        return self.__Arc2

    @Arc2.setter
    def Arc2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Arc__Arc2", None)
        self.__Arc2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successeur"):
                opp_val = getattr(old_value, "successeur", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successeur"):
                opp_val = getattr(value, "successeur", None)
                if opp_val is None:
                    setattr(value, "successeur", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecesseur"):
                opp_val = getattr(old_value, "predecesseur", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecesseur"):
                opp_val = getattr(value, "predecesseur", None)
                if opp_val is None:
                    setattr(value, "predecesseur", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def noeudsPredecesseurs(self):
        return self.__noeudsPredecesseurs

    @noeudsPredecesseurs.setter
    def noeudsPredecesseurs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Arc__noeudsPredecesseurs", None)
        self.__noeudsPredecesseurs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Noeud5"):
                opp_val = getattr(old_value, "Noeud5", None)
                if opp_val == self:
                    setattr(old_value, "Noeud5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Noeud5"):
                opp_val = getattr(value, "Noeud5", None)
                setattr(value, "Noeud5", self)

    @property
    def noeudsSuccesseurs(self):
        return self.__noeudsSuccesseurs

    @noeudsSuccesseurs.setter
    def noeudsSuccesseurs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Arc__noeudsSuccesseurs", None)
        self.__noeudsSuccesseurs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Noeud"):
                opp_val = getattr(old_value, "Noeud", None)
                if opp_val == self:
                    setattr(old_value, "Noeud", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Noeud"):
                opp_val = getattr(value, "Noeud", None)
                setattr(value, "Noeud", self)

class petriNet_Noeud(PetriNetElt):

    def __init__(self, name: str, predecesseur: set["petriNet_Arc"] = None, successeur: set["petriNet_Arc"] = None, Noeud: "petriNet_Arc" = None, Noeud5: "petriNet_Arc" = None):
        self.name = name
        self.predecesseur = predecesseur if predecesseur is not None else set()
        self.successeur = successeur if successeur is not None else set()
        self.Noeud = Noeud
        self.Noeud5 = Noeud5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Noeud(self):
        return self.__Noeud

    @Noeud.setter
    def Noeud(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Noeud__Noeud", None)
        self.__Noeud = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noeudsSuccesseurs"):
                opp_val = getattr(old_value, "noeudsSuccesseurs", None)
                if opp_val == self:
                    setattr(old_value, "noeudsSuccesseurs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noeudsSuccesseurs"):
                opp_val = getattr(value, "noeudsSuccesseurs", None)
                setattr(value, "noeudsSuccesseurs", self)

    @property
    def successeur(self):
        return self.__successeur

    @successeur.setter
    def successeur(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Noeud__successeur", None)
        self.__successeur = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc2"):
                    opp_val = getattr(item, "Arc2", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc2"):
                    opp_val = getattr(item, "Arc2", None)
                    
                    setattr(item, "Arc2", self)
                    

    @property
    def predecesseur(self):
        return self.__predecesseur

    @predecesseur.setter
    def predecesseur(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Noeud__predecesseur", None)
        self.__predecesseur = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    setattr(item, "Arc", self)
                    

    @property
    def Noeud5(self):
        return self.__Noeud5

    @Noeud5.setter
    def Noeud5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Noeud__Noeud5", None)
        self.__Noeud5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noeudsPredecesseurs"):
                opp_val = getattr(old_value, "noeudsPredecesseurs", None)
                if opp_val == self:
                    setattr(old_value, "noeudsPredecesseurs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noeudsPredecesseurs"):
                opp_val = getattr(value, "noeudsPredecesseurs", None)
                setattr(value, "noeudsPredecesseurs", self)

class petriNet_Transition(Noeud):

    pass