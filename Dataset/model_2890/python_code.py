from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class entity_Feature:

    def __init__(self, name: str, entity_Feature: "entity_Entity" = None, entity_Feature3: "entity_Type" = None):
        self.name = name
        self.entity_Feature = entity_Feature
        self.entity_Feature3 = entity_Feature3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entity_Feature3(self):
        return self.__entity_Feature3

    @entity_Feature3.setter
    def entity_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_Feature__entity_Feature3", None)
        self.__entity_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_Type4"):
                opp_val = getattr(old_value, "entity_Type4", None)
                if opp_val == self:
                    setattr(old_value, "entity_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_Type4"):
                opp_val = getattr(value, "entity_Type4", None)
                setattr(value, "entity_Type4", self)

    @property
    def entity_Feature(self):
        return self.__entity_Feature

    @entity_Feature.setter
    def entity_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_Feature__entity_Feature", None)
        self.__entity_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_Entity"):
                opp_val = getattr(old_value, "entity_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_Entity"):
                opp_val = getattr(value, "entity_Entity", None)
                if opp_val is None:
                    setattr(value, "entity_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class entity_Entity(Type):

    pass
class entity_Datatype(Type):

    pass
class entity_Type(ABC):

    def __init__(self, name: str, entity_Type: "entity_Domain" = None, entity_Type4: "entity_Feature" = None):
        self.name = name
        self.entity_Type = entity_Type
        self.entity_Type4 = entity_Type4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entity_Type4(self):
        return self.__entity_Type4

    @entity_Type4.setter
    def entity_Type4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_Type__entity_Type4", None)
        self.__entity_Type4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_Feature3"):
                opp_val = getattr(old_value, "entity_Feature3", None)
                if opp_val == self:
                    setattr(old_value, "entity_Feature3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_Feature3"):
                opp_val = getattr(value, "entity_Feature3", None)
                setattr(value, "entity_Feature3", self)

    @property
    def entity_Type(self):
        return self.__entity_Type

    @entity_Type.setter
    def entity_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_Type__entity_Type", None)
        self.__entity_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_Domain"):
                opp_val = getattr(old_value, "entity_Domain", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_Domain"):
                opp_val = getattr(value, "entity_Domain", None)
                if opp_val is None:
                    setattr(value, "entity_Domain", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class entity_Domain:

    def __init__(self, name: str, entity_Domain: set["entity_Type"] = None):
        self.name = name
        self.entity_Domain = entity_Domain if entity_Domain is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entity_Domain(self):
        return self.__entity_Domain

    @entity_Domain.setter
    def entity_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_Domain__entity_Domain", None)
        self.__entity_Domain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entity_Type"):
                    opp_val = getattr(item, "entity_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "entity_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entity_Type"):
                    opp_val = getattr(item, "entity_Type", None)
                    
                    setattr(item, "entity_Type", self)
                    
