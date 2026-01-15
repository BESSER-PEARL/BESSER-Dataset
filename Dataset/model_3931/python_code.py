from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class entity_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Member:

    pass
class entity_Method(Member):

    def __init__(self, isAbstract: bool, entity_Method: "entity_Service" = None):
        self.isAbstract = isAbstract
        self.entity_Method = entity_Method
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def entity_Method(self):
        return self.__entity_Method

    @entity_Method.setter
    def entity_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_Method__entity_Method", None)
        self.__entity_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_Service"):
                opp_val = getattr(old_value, "entity_Service", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_Service"):
                opp_val = getattr(value, "entity_Service", None)
                if opp_val is None:
                    setattr(value, "entity_Service", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class entity_Field(Member):

    pass
class Type:

    pass
class entity_Service(Type):

    pass
class entity_Entity(Type):

    pass
class NamedElement:

    pass
class entity_Type(NamedElement):

    pass
class entity_Member(NamedElement):

    pass
class entity_Package(NamedElement):

    pass