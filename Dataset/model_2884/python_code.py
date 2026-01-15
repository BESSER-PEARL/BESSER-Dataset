from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class metamodel_Feature:

    def __init__(self, name: str, metamodel_Feature3: "metamodel_Type" = None, metamodel_Feature: "metamodel_Entity" = None):
        self.name = name
        self.metamodel_Feature3 = metamodel_Feature3
        self.metamodel_Feature = metamodel_Feature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Feature3(self):
        return self.__metamodel_Feature3

    @metamodel_Feature3.setter
    def metamodel_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Feature__metamodel_Feature3", None)
        self.__metamodel_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Type4"):
                opp_val = getattr(old_value, "metamodel_Type4", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Type4"):
                opp_val = getattr(value, "metamodel_Type4", None)
                setattr(value, "metamodel_Type4", self)

    @property
    def metamodel_Feature(self):
        return self.__metamodel_Feature

    @metamodel_Feature.setter
    def metamodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Feature__metamodel_Feature", None)
        self.__metamodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity"):
                opp_val = getattr(old_value, "metamodel_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity"):
                opp_val = getattr(value, "metamodel_Entity", None)
                if opp_val is None:
                    setattr(value, "metamodel_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class metamodel_Entity(Type):

    pass
class metamodel_Datatype(Type):

    pass
class metamodel_Type(ABC):

    def __init__(self, name: str, metamodel_Type4: "metamodel_Feature" = None, metamodel_Type: "metamodel_Model" = None):
        self.name = name
        self.metamodel_Type4 = metamodel_Type4
        self.metamodel_Type = metamodel_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Type4(self):
        return self.__metamodel_Type4

    @metamodel_Type4.setter
    def metamodel_Type4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Type__metamodel_Type4", None)
        self.__metamodel_Type4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Feature3"):
                opp_val = getattr(old_value, "metamodel_Feature3", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Feature3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Feature3"):
                opp_val = getattr(value, "metamodel_Feature3", None)
                setattr(value, "metamodel_Feature3", self)

    @property
    def metamodel_Type(self):
        return self.__metamodel_Type

    @metamodel_Type.setter
    def metamodel_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Type__metamodel_Type", None)
        self.__metamodel_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Model"):
                opp_val = getattr(old_value, "metamodel_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Model"):
                opp_val = getattr(value, "metamodel_Model", None)
                if opp_val is None:
                    setattr(value, "metamodel_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Model:

    pass