from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SWMLTypes(Enum):
    Boolean = "Boolean"
    String = "String"
    Integer = "Integer"
    Float = "Float"
    Email = "Email"


############################################
# Definition of Classes
############################################

class sWML_Attribute:

    def __init__(self, name: str, type: str, sWML_Attribute: "sWML_Class" = None):
        self.name = name
        self.type = type
        self.sWML_Attribute = sWML_Attribute
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sWML_Attribute(self):
        return self.__sWML_Attribute

    @sWML_Attribute.setter
    def sWML_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sWML_Attribute__sWML_Attribute", None)
        self.__sWML_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sWML_Class11"):
                opp_val = getattr(old_value, "sWML_Class11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sWML_Class11"):
                opp_val = getattr(value, "sWML_Class11", None)
                if opp_val is None:
                    setattr(value, "sWML_Class11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sWML_Class:

    def __init__(self, name: str, sWML_Class: "sWML_IndexPage" = None, sWML_Class9: "sWML_ContentLayer" = None, sWML_Class11: set["sWML_Attribute"] = None):
        self.name = name
        self.sWML_Class = sWML_Class
        self.sWML_Class9 = sWML_Class9
        self.sWML_Class11 = sWML_Class11 if sWML_Class11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sWML_Class9(self):
        return self.__sWML_Class9

    @sWML_Class9.setter
    def sWML_Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sWML_Class__sWML_Class9", None)
        self.__sWML_Class9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sWML_ContentLayer8"):
                opp_val = getattr(old_value, "sWML_ContentLayer8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sWML_ContentLayer8"):
                opp_val = getattr(value, "sWML_ContentLayer8", None)
                if opp_val is None:
                    setattr(value, "sWML_ContentLayer8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sWML_Class11(self):
        return self.__sWML_Class11

    @sWML_Class11.setter
    def sWML_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sWML_Class__sWML_Class11", None)
        self.__sWML_Class11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sWML_Attribute"):
                    opp_val = getattr(item, "sWML_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "sWML_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sWML_Attribute"):
                    opp_val = getattr(item, "sWML_Attribute", None)
                    
                    setattr(item, "sWML_Attribute", self)
                    

    @property
    def sWML_Class(self):
        return self.__sWML_Class

    @sWML_Class.setter
    def sWML_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sWML_Class__sWML_Class", None)
        self.__sWML_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sWML_IndexPage6"):
                opp_val = getattr(old_value, "sWML_IndexPage6", None)
                if opp_val == self:
                    setattr(old_value, "sWML_IndexPage6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sWML_IndexPage6"):
                opp_val = getattr(value, "sWML_IndexPage6", None)
                setattr(value, "sWML_IndexPage6", self)

class sWML_IndexPage:

    def __init__(self, name: str, size: int, sWML_IndexPage: "sWML_HypertextLayer" = None, sWML_IndexPage6: "sWML_Class" = None):
        self.name = name
        self.size = size
        self.sWML_IndexPage = sWML_IndexPage
        self.sWML_IndexPage6 = sWML_IndexPage6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def sWML_IndexPage(self):
        return self.__sWML_IndexPage

    @sWML_IndexPage.setter
    def sWML_IndexPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sWML_IndexPage__sWML_IndexPage", None)
        self.__sWML_IndexPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sWML_HypertextLayer4"):
                opp_val = getattr(old_value, "sWML_HypertextLayer4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sWML_HypertextLayer4"):
                opp_val = getattr(value, "sWML_HypertextLayer4", None)
                if opp_val is None:
                    setattr(value, "sWML_HypertextLayer4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sWML_IndexPage6(self):
        return self.__sWML_IndexPage6

    @sWML_IndexPage6.setter
    def sWML_IndexPage6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sWML_IndexPage__sWML_IndexPage6", None)
        self.__sWML_IndexPage6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sWML_Class"):
                opp_val = getattr(old_value, "sWML_Class", None)
                if opp_val == self:
                    setattr(old_value, "sWML_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sWML_Class"):
                opp_val = getattr(value, "sWML_Class", None)
                setattr(value, "sWML_Class", self)

class sWML_ContentLayer:

    pass
class sWML_HypertextLayer:

    pass
class sWML_WebModel:

    def __init__(self, name: str, sWML_WebModel: "sWML_HypertextLayer" = None, sWML_WebModel2: "sWML_ContentLayer" = None):
        self.name = name
        self.sWML_WebModel = sWML_WebModel
        self.sWML_WebModel2 = sWML_WebModel2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sWML_WebModel(self):
        return self.__sWML_WebModel

    @sWML_WebModel.setter
    def sWML_WebModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sWML_WebModel__sWML_WebModel", None)
        self.__sWML_WebModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sWML_HypertextLayer"):
                opp_val = getattr(old_value, "sWML_HypertextLayer", None)
                if opp_val == self:
                    setattr(old_value, "sWML_HypertextLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sWML_HypertextLayer"):
                opp_val = getattr(value, "sWML_HypertextLayer", None)
                setattr(value, "sWML_HypertextLayer", self)

    @property
    def sWML_WebModel2(self):
        return self.__sWML_WebModel2

    @sWML_WebModel2.setter
    def sWML_WebModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sWML_WebModel__sWML_WebModel2", None)
        self.__sWML_WebModel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sWML_ContentLayer"):
                opp_val = getattr(old_value, "sWML_ContentLayer", None)
                if opp_val == self:
                    setattr(old_value, "sWML_ContentLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sWML_ContentLayer"):
                opp_val = getattr(value, "sWML_ContentLayer", None)
                setattr(value, "sWML_ContentLayer", self)
