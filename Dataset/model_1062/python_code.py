from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet_IdentifiableElement(ABC):

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

class Arc:

    pass
class PetriNet_TransToPlaceArc(Arc):

    pass
class PetriNet_PlaceToTransArc(Arc):

    pass
class PetriNet_Token:

    def __init__(self, values: str, PetriNet_Token: "PetriNet_Place" = None):
        self.values = values
        self.PetriNet_Token = PetriNet_Token
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

    @property
    def PetriNet_Token(self):
        return self.__PetriNet_Token

    @PetriNet_Token.setter
    def PetriNet_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Token__PetriNet_Token", None)
        self.__PetriNet_Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Place10"):
                opp_val = getattr(old_value, "PetriNet_Place10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Place10"):
                opp_val = getattr(value, "PetriNet_Place10", None)
                if opp_val is None:
                    setattr(value, "PetriNet_Place10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNet_PrimitiveAttribute:

    def __init__(self, name: str, primType: str, PetriNet_PrimitiveAttribute: "PetriNet_Type" = None):
        self.name = name
        self.primType = primType
        self.PetriNet_PrimitiveAttribute = PetriNet_PrimitiveAttribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def primType(self) -> str:
        return self.__primType

    @primType.setter
    def primType(self, primType: str):
        self.__primType = primType

    @property
    def PetriNet_PrimitiveAttribute(self):
        return self.__PetriNet_PrimitiveAttribute

    @PetriNet_PrimitiveAttribute.setter
    def PetriNet_PrimitiveAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PrimitiveAttribute__PetriNet_PrimitiveAttribute", None)
        self.__PetriNet_PrimitiveAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Type8"):
                opp_val = getattr(old_value, "PetriNet_Type8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Type8"):
                opp_val = getattr(value, "PetriNet_Type8", None)
                if opp_val is None:
                    setattr(value, "PetriNet_Type8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNet_Type:

    def __init__(self, name: str, PetriNet_Type: "PetriNet_PetriNet" = None, PetriNet_Type8: set["PetriNet_PrimitiveAttribute"] = None, PetriNet_Type13: "PetriNet_Place" = None):
        self.name = name
        self.PetriNet_Type = PetriNet_Type
        self.PetriNet_Type8 = PetriNet_Type8 if PetriNet_Type8 is not None else set()
        self.PetriNet_Type13 = PetriNet_Type13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_Type13(self):
        return self.__PetriNet_Type13

    @PetriNet_Type13.setter
    def PetriNet_Type13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Type__PetriNet_Type13", None)
        self.__PetriNet_Type13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Place12"):
                opp_val = getattr(old_value, "PetriNet_Place12", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_Place12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Place12"):
                opp_val = getattr(value, "PetriNet_Place12", None)
                setattr(value, "PetriNet_Place12", self)

    @property
    def PetriNet_Type(self):
        return self.__PetriNet_Type

    @PetriNet_Type.setter
    def PetriNet_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Type__PetriNet_Type", None)
        self.__PetriNet_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNet6"):
                opp_val = getattr(old_value, "PetriNet_PetriNet6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNet6"):
                opp_val = getattr(value, "PetriNet_PetriNet6", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNet6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNet_Type8(self):
        return self.__PetriNet_Type8

    @PetriNet_Type8.setter
    def PetriNet_Type8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Type__PetriNet_Type8", None)
        self.__PetriNet_Type8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_PrimitiveAttribute"):
                    opp_val = getattr(item, "PetriNet_PrimitiveAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_PrimitiveAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_PrimitiveAttribute"):
                    opp_val = getattr(item, "PetriNet_PrimitiveAttribute", None)
                    
                    setattr(item, "PetriNet_PrimitiveAttribute", self)
                    

class PetriNet_Arc(ABC):

    def __init__(self, weight: int, PetriNet_Arc: "PetriNet_PetriNet" = None):
        self.weight = weight
        self.PetriNet_Arc = PetriNet_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def PetriNet_Arc(self):
        return self.__PetriNet_Arc

    @PetriNet_Arc.setter
    def PetriNet_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__PetriNet_Arc", None)
        self.__PetriNet_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNet4"):
                opp_val = getattr(old_value, "PetriNet_PetriNet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNet4"):
                opp_val = getattr(value, "PetriNet_PetriNet4", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IdentifiableElement:

    pass
class PetriNet_Place(IdentifiableElement):

    pass
class PetriNet_Transition(IdentifiableElement):

    pass
class PetriNet_PetriNet(IdentifiableElement):

    pass