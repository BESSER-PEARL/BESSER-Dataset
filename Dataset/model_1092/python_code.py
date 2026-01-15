from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_Arc(ABC):

    def __init__(self, nbJetons: int, petrinet_Arc: "petrinet_Reseau" = None):
        self.nbJetons = nbJetons
        self.petrinet_Arc = petrinet_Arc
        
    @property
    def nbJetons(self) -> int:
        return self.__nbJetons

    @nbJetons.setter
    def nbJetons(self, nbJetons: int):
        self.__nbJetons = nbJetons

    @property
    def petrinet_Arc(self):
        return self.__petrinet_Arc

    @petrinet_Arc.setter
    def petrinet_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc", None)
        self.__petrinet_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Reseau10"):
                opp_val = getattr(old_value, "petrinet_Reseau10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Reseau10"):
                opp_val = getattr(value, "petrinet_Reseau10", None)
                if opp_val is None:
                    setattr(value, "petrinet_Reseau10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_Reseau:

    def __init__(self, nom: str, petrinet_Reseau: set["petrinet_Element"] = None, petrinet_Reseau10: set["petrinet_Arc"] = None):
        self.nom = nom
        self.petrinet_Reseau = petrinet_Reseau if petrinet_Reseau is not None else set()
        self.petrinet_Reseau10 = petrinet_Reseau10 if petrinet_Reseau10 is not None else set()
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def petrinet_Reseau(self):
        return self.__petrinet_Reseau

    @petrinet_Reseau.setter
    def petrinet_Reseau(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Reseau__petrinet_Reseau", None)
        self.__petrinet_Reseau = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Element"):
                    opp_val = getattr(item, "petrinet_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Element"):
                    opp_val = getattr(item, "petrinet_Element", None)
                    
                    setattr(item, "petrinet_Element", self)
                    

    @property
    def petrinet_Reseau10(self):
        return self.__petrinet_Reseau10

    @petrinet_Reseau10.setter
    def petrinet_Reseau10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Reseau__petrinet_Reseau10", None)
        self.__petrinet_Reseau10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Arc"):
                    opp_val = getattr(item, "petrinet_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Arc"):
                    opp_val = getattr(item, "petrinet_Arc", None)
                    
                    setattr(item, "petrinet_Arc", self)
                    

class petrinet_Element(ABC):

    def __init__(self, nom: str, petrinet_Element: "petrinet_Reseau" = None):
        self.nom = nom
        self.petrinet_Element = petrinet_Element
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def petrinet_Element(self):
        return self.__petrinet_Element

    @petrinet_Element.setter
    def petrinet_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Element__petrinet_Element", None)
        self.__petrinet_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Reseau"):
                opp_val = getattr(old_value, "petrinet_Reseau", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Reseau"):
                opp_val = getattr(value, "petrinet_Reseau", None)
                if opp_val is None:
                    setattr(value, "petrinet_Reseau", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ArcSortant:

    pass
class petrinet_ReadArc(ArcSortant):

    pass
class Arc:

    pass
class petrinet_ArcEntrant(Arc):

    pass
class petrinet_ArcSortant(Arc):

    pass
class Element:

    pass
class petrinet_Transition(Element):

    pass
class petrinet_Place(Element):

    def __init__(self, jetons: int, petrinet_Place: "petrinet_ArcSortant" = None, petrinet_Place5: "petrinet_ArcEntrant" = None):
        self.jetons = jetons
        self.petrinet_Place = petrinet_Place
        self.petrinet_Place5 = petrinet_Place5
        
    @property
    def jetons(self) -> int:
        return self.__jetons

    @jetons.setter
    def jetons(self, jetons: int):
        self.__jetons = jetons

    @property
    def petrinet_Place5(self):
        return self.__petrinet_Place5

    @petrinet_Place5.setter
    def petrinet_Place5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place5", None)
        self.__petrinet_Place5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_ArcEntrant"):
                opp_val = getattr(old_value, "petrinet_ArcEntrant", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_ArcEntrant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_ArcEntrant"):
                opp_val = getattr(value, "petrinet_ArcEntrant", None)
                setattr(value, "petrinet_ArcEntrant", self)

    @property
    def petrinet_Place(self):
        return self.__petrinet_Place

    @petrinet_Place.setter
    def petrinet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place", None)
        self.__petrinet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_ArcSortant"):
                opp_val = getattr(old_value, "petrinet_ArcSortant", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_ArcSortant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_ArcSortant"):
                opp_val = getattr(value, "petrinet_ArcSortant", None)
                setattr(value, "petrinet_ArcSortant", self)
