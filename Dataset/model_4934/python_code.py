from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CardinalityKind(Enum):
    ONE = "ONE"
    MANY = "MANY"


############################################
# Definition of Classes
############################################

class backbone_RouterMapping:

    def __init__(self, path: str, backbone_RouterMapping: "backbone_Router" = None, backbone_RouterMapping26: "backbone_View" = None):
        self.path = path
        self.backbone_RouterMapping = backbone_RouterMapping
        self.backbone_RouterMapping26 = backbone_RouterMapping26
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def backbone_RouterMapping(self):
        return self.__backbone_RouterMapping

    @backbone_RouterMapping.setter
    def backbone_RouterMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backbone_RouterMapping__backbone_RouterMapping", None)
        self.__backbone_RouterMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backbone_Router"):
                opp_val = getattr(old_value, "backbone_Router", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backbone_Router"):
                opp_val = getattr(value, "backbone_Router", None)
                if opp_val is None:
                    setattr(value, "backbone_Router", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def backbone_RouterMapping26(self):
        return self.__backbone_RouterMapping26

    @backbone_RouterMapping26.setter
    def backbone_RouterMapping26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backbone_RouterMapping__backbone_RouterMapping26", None)
        self.__backbone_RouterMapping26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backbone_View"):
                opp_val = getattr(old_value, "backbone_View", None)
                if opp_val == self:
                    setattr(old_value, "backbone_View", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backbone_View"):
                opp_val = getattr(value, "backbone_View", None)
                setattr(value, "backbone_View", self)

class NamedElement:

    pass
class backbone_Parameter(NamedElement):

    pass
class backbone_Collection(NamedElement):

    pass
class backbone_Model(NamedElement):

    pass
class backbone_Router(NamedElement):

    pass
class backbone_View(NamedElement):

    pass
class backbone_Application(NamedElement):

    pass
class backbone_Operation(NamedElement):

    pass
class backbone_Reference(NamedElement):

    def __init__(self, cardinality: str, backbone_Reference: "backbone_Model" = None, backbone_Reference14: "backbone_Model" = None):
        self.cardinality = cardinality
        self.backbone_Reference = backbone_Reference
        self.backbone_Reference14 = backbone_Reference14
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def backbone_Reference14(self):
        return self.__backbone_Reference14

    @backbone_Reference14.setter
    def backbone_Reference14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backbone_Reference__backbone_Reference14", None)
        self.__backbone_Reference14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backbone_Model15"):
                opp_val = getattr(old_value, "backbone_Model15", None)
                if opp_val == self:
                    setattr(old_value, "backbone_Model15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backbone_Model15"):
                opp_val = getattr(value, "backbone_Model15", None)
                setattr(value, "backbone_Model15", self)

    @property
    def backbone_Reference(self):
        return self.__backbone_Reference

    @backbone_Reference.setter
    def backbone_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backbone_Reference__backbone_Reference", None)
        self.__backbone_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backbone_Model9"):
                opp_val = getattr(old_value, "backbone_Model9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backbone_Model9"):
                opp_val = getattr(value, "backbone_Model9", None)
                if opp_val is None:
                    setattr(value, "backbone_Model9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class backbone_Attribute(NamedElement):

    def __init__(self, defaultValue: str, cardinality: str, backbone_Attribute: "backbone_Model" = None):
        self.defaultValue = defaultValue
        self.cardinality = cardinality
        self.backbone_Attribute = backbone_Attribute
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def backbone_Attribute(self):
        return self.__backbone_Attribute

    @backbone_Attribute.setter
    def backbone_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backbone_Attribute__backbone_Attribute", None)
        self.__backbone_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backbone_Model"):
                opp_val = getattr(old_value, "backbone_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backbone_Model"):
                opp_val = getattr(value, "backbone_Model", None)
                if opp_val is None:
                    setattr(value, "backbone_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class backbone_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
