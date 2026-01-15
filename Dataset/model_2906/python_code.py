from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Type:

    pass
class Data_PrimitiveType(Type):

    pass
class Data_Entity(Type):

    pass
class Data_Attribute:

    def __init__(self, name: str, Data_Attribute: "Data_Type" = None, Data_Attribute4: "Data_Entity" = None):
        self.name = name
        self.Data_Attribute = Data_Attribute
        self.Data_Attribute4 = Data_Attribute4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Data_Attribute(self):
        return self.__Data_Attribute

    @Data_Attribute.setter
    def Data_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Attribute__Data_Attribute", None)
        self.__Data_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Type2"):
                opp_val = getattr(old_value, "Data_Type2", None)
                if opp_val == self:
                    setattr(old_value, "Data_Type2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Type2"):
                opp_val = getattr(value, "Data_Type2", None)
                setattr(value, "Data_Type2", self)

    @property
    def Data_Attribute4(self):
        return self.__Data_Attribute4

    @Data_Attribute4.setter
    def Data_Attribute4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Attribute__Data_Attribute4", None)
        self.__Data_Attribute4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Entity"):
                opp_val = getattr(old_value, "Data_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Entity"):
                opp_val = getattr(value, "Data_Entity", None)
                if opp_val is None:
                    setattr(value, "Data_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Data_Type(ABC):

    def __init__(self, name: str, Data_Type: "Data_Model" = None, Data_Type2: "Data_Attribute" = None):
        self.name = name
        self.Data_Type = Data_Type
        self.Data_Type2 = Data_Type2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Data_Type2(self):
        return self.__Data_Type2

    @Data_Type2.setter
    def Data_Type2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Type__Data_Type2", None)
        self.__Data_Type2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Attribute"):
                opp_val = getattr(old_value, "Data_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "Data_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Attribute"):
                opp_val = getattr(value, "Data_Attribute", None)
                setattr(value, "Data_Attribute", self)

    @property
    def Data_Type(self):
        return self.__Data_Type

    @Data_Type.setter
    def Data_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Type__Data_Type", None)
        self.__Data_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Model"):
                opp_val = getattr(old_value, "Data_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Model"):
                opp_val = getattr(value, "Data_Model", None)
                if opp_val is None:
                    setattr(value, "Data_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Data_Model:

    pass