from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Type:

    pass
class classes_DataType(Type):

    pass
class classes_Type(ABC):

    def __init__(self, name: str, classes_Type: "classes_Attribute" = None):
        self.name = name
        self.classes_Type = classes_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classes_Type(self):
        return self.__classes_Type

    @classes_Type.setter
    def classes_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Type__classes_Type", None)
        self.__classes_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Attribute4"):
                opp_val = getattr(old_value, "classes_Attribute4", None)
                if opp_val == self:
                    setattr(old_value, "classes_Attribute4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Attribute4"):
                opp_val = getattr(value, "classes_Attribute4", None)
                setattr(value, "classes_Attribute4", self)

class classes_Class(Type):

    pass
class classes_Attribute:

    def __init__(self, name: str, value: str, classes_Attribute: "classes_Class" = None, classes_Attribute4: "classes_Type" = None):
        self.name = name
        self.value = value
        self.classes_Attribute = classes_Attribute
        self.classes_Attribute4 = classes_Attribute4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def classes_Attribute(self):
        return self.__classes_Attribute

    @classes_Attribute.setter
    def classes_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Attribute__classes_Attribute", None)
        self.__classes_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Class2"):
                opp_val = getattr(old_value, "classes_Class2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Class2"):
                opp_val = getattr(value, "classes_Class2", None)
                if opp_val is None:
                    setattr(value, "classes_Class2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Attribute4(self):
        return self.__classes_Attribute4

    @classes_Attribute4.setter
    def classes_Attribute4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Attribute__classes_Attribute4", None)
        self.__classes_Attribute4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Type"):
                opp_val = getattr(old_value, "classes_Type", None)
                if opp_val == self:
                    setattr(old_value, "classes_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Type"):
                opp_val = getattr(value, "classes_Type", None)
                setattr(value, "classes_Type", self)

class classes_Model:

    pass