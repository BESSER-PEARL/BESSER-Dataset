from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class smalluml_ElementNomme(ABC):

    def __init__(self, nom: str):
        self.nom = nom
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

class Type:

    pass
class smalluml_Type(ABC):

    pass
class smalluml_ElementDiagramme(ABC):

    pass
class smalluml_Booleen(Type):

    pass
class smalluml_Entier(Type):

    pass
class smalluml_Chaine(Type):

    pass
class ElementNomme:

    pass
class smalluml_Cardinalite(ElementNomme):

    def __init__(self, multipliciteInf: str, multipliciteSup: str, smalluml_Cardinalite: "smalluml_Association" = None, smalluml_Cardinalite21: "smalluml_Classe" = None):
        self.multipliciteInf = multipliciteInf
        self.multipliciteSup = multipliciteSup
        self.smalluml_Cardinalite = smalluml_Cardinalite
        self.smalluml_Cardinalite21 = smalluml_Cardinalite21
        
    @property
    def multipliciteSup(self) -> str:
        return self.__multipliciteSup

    @multipliciteSup.setter
    def multipliciteSup(self, multipliciteSup: str):
        self.__multipliciteSup = multipliciteSup

    @property
    def multipliciteInf(self) -> str:
        return self.__multipliciteInf

    @multipliciteInf.setter
    def multipliciteInf(self, multipliciteInf: str):
        self.__multipliciteInf = multipliciteInf

    @property
    def smalluml_Cardinalite(self):
        return self.__smalluml_Cardinalite

    @smalluml_Cardinalite.setter
    def smalluml_Cardinalite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Cardinalite__smalluml_Cardinalite", None)
        self.__smalluml_Cardinalite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association"):
                opp_val = getattr(old_value, "smalluml_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association"):
                opp_val = getattr(value, "smalluml_Association", None)
                if opp_val is None:
                    setattr(value, "smalluml_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Cardinalite21(self):
        return self.__smalluml_Cardinalite21

    @smalluml_Cardinalite21.setter
    def smalluml_Cardinalite21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Cardinalite__smalluml_Cardinalite21", None)
        self.__smalluml_Cardinalite21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Classe22"):
                opp_val = getattr(old_value, "smalluml_Classe22", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Classe22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Classe22"):
                opp_val = getattr(value, "smalluml_Classe22", None)
                setattr(value, "smalluml_Classe22", self)

class smalluml_Methode(ElementNomme):

    def __init__(self, methodeAbstraite: bool, smalluml_Methode: "smalluml_Classe" = None, smalluml_Methode12: "smalluml_Type" = None, smalluml_Methode15: set["smalluml_Attribut"] = None):
        self.methodeAbstraite = methodeAbstraite
        self.smalluml_Methode = smalluml_Methode
        self.smalluml_Methode12 = smalluml_Methode12
        self.smalluml_Methode15 = smalluml_Methode15 if smalluml_Methode15 is not None else set()
        
    @property
    def methodeAbstraite(self) -> bool:
        return self.__methodeAbstraite

    @methodeAbstraite.setter
    def methodeAbstraite(self, methodeAbstraite: bool):
        self.__methodeAbstraite = methodeAbstraite

    @property
    def smalluml_Methode12(self):
        return self.__smalluml_Methode12

    @smalluml_Methode12.setter
    def smalluml_Methode12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Methode__smalluml_Methode12", None)
        self.__smalluml_Methode12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Type13"):
                opp_val = getattr(old_value, "smalluml_Type13", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Type13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Type13"):
                opp_val = getattr(value, "smalluml_Type13", None)
                setattr(value, "smalluml_Type13", self)

    @property
    def smalluml_Methode(self):
        return self.__smalluml_Methode

    @smalluml_Methode.setter
    def smalluml_Methode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Methode__smalluml_Methode", None)
        self.__smalluml_Methode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Classe2"):
                opp_val = getattr(old_value, "smalluml_Classe2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Classe2"):
                opp_val = getattr(value, "smalluml_Classe2", None)
                if opp_val is None:
                    setattr(value, "smalluml_Classe2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Methode15(self):
        return self.__smalluml_Methode15

    @smalluml_Methode15.setter
    def smalluml_Methode15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Methode__smalluml_Methode15", None)
        self.__smalluml_Methode15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Attribut16"):
                    opp_val = getattr(item, "smalluml_Attribut16", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Attribut16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Attribut16"):
                    opp_val = getattr(item, "smalluml_Attribut16", None)
                    
                    setattr(item, "smalluml_Attribut16", self)
                    

class smalluml_Attribut(ElementNomme):

    pass
class ElementDiagramme:

    pass
class smalluml_TypeDonnee(ElementNomme, Type, ElementDiagramme):

    pass
class smalluml_Association(ElementNomme, ElementDiagramme):

    pass
class smalluml_Enumeration(ElementNomme, Type, ElementDiagramme):

    def __init__(self, elements: str, smalluml_Enumeration: "smalluml_ElementDiagramme" = None):
        self.elements = elements
        self.smalluml_Enumeration = smalluml_Enumeration
        
    @property
    def elements(self) -> str:
        return self.__elements

    @elements.setter
    def elements(self, elements: str):
        self.__elements = elements

    @property
    def smalluml_Enumeration(self):
        return self.__smalluml_Enumeration

    @smalluml_Enumeration.setter
    def smalluml_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Enumeration__smalluml_Enumeration", None)
        self.__smalluml_Enumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_ElementDiagramme31"):
                opp_val = getattr(old_value, "smalluml_ElementDiagramme31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_ElementDiagramme31"):
                opp_val = getattr(value, "smalluml_ElementDiagramme31", None)
                if opp_val is None:
                    setattr(value, "smalluml_ElementDiagramme31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smalluml_Diagramme(ElementNomme, ElementDiagramme):

    pass
class smalluml_Classe(ElementNomme, ElementDiagramme):

    def __init__(self, abstrait: bool, classeAbstraite: bool, smalluml_Classe: set["smalluml_Attribut"] = None, smalluml_Classe2: set["smalluml_Methode"] = None, smalluml_Classe5: "smalluml_Classe" = None, smalluml_Classe3: set["smalluml_Classe"] = None, smalluml_Classe8: "smalluml_Classe" = None, smalluml_Classe6: "smalluml_Classe" = None, smalluml_Classe22: "smalluml_Cardinalite" = None, smalluml_Classe26: "smalluml_ElementDiagramme" = None):
        self.abstrait = abstrait
        self.classeAbstraite = classeAbstraite
        self.smalluml_Classe = smalluml_Classe if smalluml_Classe is not None else set()
        self.smalluml_Classe2 = smalluml_Classe2 if smalluml_Classe2 is not None else set()
        self.smalluml_Classe5 = smalluml_Classe5
        self.smalluml_Classe3 = smalluml_Classe3 if smalluml_Classe3 is not None else set()
        self.smalluml_Classe8 = smalluml_Classe8
        self.smalluml_Classe6 = smalluml_Classe6
        self.smalluml_Classe22 = smalluml_Classe22
        self.smalluml_Classe26 = smalluml_Classe26
        
    @property
    def classeAbstraite(self) -> bool:
        return self.__classeAbstraite

    @classeAbstraite.setter
    def classeAbstraite(self, classeAbstraite: bool):
        self.__classeAbstraite = classeAbstraite

    @property
    def abstrait(self) -> bool:
        return self.__abstrait

    @abstrait.setter
    def abstrait(self, abstrait: bool):
        self.__abstrait = abstrait

    @property
    def smalluml_Classe2(self):
        return self.__smalluml_Classe2

    @smalluml_Classe2.setter
    def smalluml_Classe2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Classe__smalluml_Classe2", None)
        self.__smalluml_Classe2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Methode"):
                    opp_val = getattr(item, "smalluml_Methode", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Methode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Methode"):
                    opp_val = getattr(item, "smalluml_Methode", None)
                    
                    setattr(item, "smalluml_Methode", self)
                    

    @property
    def smalluml_Classe3(self):
        return self.__smalluml_Classe3

    @smalluml_Classe3.setter
    def smalluml_Classe3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Classe__smalluml_Classe3", None)
        self.__smalluml_Classe3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Classe5"):
                    opp_val = getattr(item, "smalluml_Classe5", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Classe5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Classe5"):
                    opp_val = getattr(item, "smalluml_Classe5", None)
                    
                    setattr(item, "smalluml_Classe5", self)
                    

    @property
    def smalluml_Classe6(self):
        return self.__smalluml_Classe6

    @smalluml_Classe6.setter
    def smalluml_Classe6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Classe__smalluml_Classe6", None)
        self.__smalluml_Classe6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Classe8"):
                opp_val = getattr(old_value, "smalluml_Classe8", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Classe8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Classe8"):
                opp_val = getattr(value, "smalluml_Classe8", None)
                setattr(value, "smalluml_Classe8", self)

    @property
    def smalluml_Classe(self):
        return self.__smalluml_Classe

    @smalluml_Classe.setter
    def smalluml_Classe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Classe__smalluml_Classe", None)
        self.__smalluml_Classe = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Attribut"):
                    opp_val = getattr(item, "smalluml_Attribut", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Attribut", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Attribut"):
                    opp_val = getattr(item, "smalluml_Attribut", None)
                    
                    setattr(item, "smalluml_Attribut", self)
                    

    @property
    def smalluml_Classe5(self):
        return self.__smalluml_Classe5

    @smalluml_Classe5.setter
    def smalluml_Classe5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Classe__smalluml_Classe5", None)
        self.__smalluml_Classe5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Classe3"):
                opp_val = getattr(old_value, "smalluml_Classe3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Classe3"):
                opp_val = getattr(value, "smalluml_Classe3", None)
                if opp_val is None:
                    setattr(value, "smalluml_Classe3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Classe22(self):
        return self.__smalluml_Classe22

    @smalluml_Classe22.setter
    def smalluml_Classe22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Classe__smalluml_Classe22", None)
        self.__smalluml_Classe22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Cardinalite21"):
                opp_val = getattr(old_value, "smalluml_Cardinalite21", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Cardinalite21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Cardinalite21"):
                opp_val = getattr(value, "smalluml_Cardinalite21", None)
                setattr(value, "smalluml_Cardinalite21", self)

    @property
    def smalluml_Classe8(self):
        return self.__smalluml_Classe8

    @smalluml_Classe8.setter
    def smalluml_Classe8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Classe__smalluml_Classe8", None)
        self.__smalluml_Classe8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Classe6"):
                opp_val = getattr(old_value, "smalluml_Classe6", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Classe6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Classe6"):
                opp_val = getattr(value, "smalluml_Classe6", None)
                setattr(value, "smalluml_Classe6", self)

    @property
    def smalluml_Classe26(self):
        return self.__smalluml_Classe26

    @smalluml_Classe26.setter
    def smalluml_Classe26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Classe__smalluml_Classe26", None)
        self.__smalluml_Classe26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_ElementDiagramme25"):
                opp_val = getattr(old_value, "smalluml_ElementDiagramme25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_ElementDiagramme25"):
                opp_val = getattr(value, "smalluml_ElementDiagramme25", None)
                if opp_val is None:
                    setattr(value, "smalluml_ElementDiagramme25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
