from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Entity(Enum):
class EA(Enum):
    Institution = "Institution"
    Journal = "Journal"
    Author = "Author"
class Vocabulary(Enum):
    Normal = "Normal"
    Language = "Language"
    Eurovocs = "Eurovocs"
    Decs = "Decs"


############################################
# Definition of Classes
############################################

class PrimitiveDataType:

    pass
class Association:

    pass
class SimpleClass_Classifier:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SimpleClass_Attribute:

    def __init__(self, name: str, is_primary: str, SimpleClass_Attribute: "Classifier" = None):
        self.name = name
        self.is_primary = is_primary
        self.SimpleClass_Attribute = SimpleClass_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def is_primary(self) -> str:
        return self.__is_primary

    @is_primary.setter
    def is_primary(self, is_primary: str):
        self.__is_primary = is_primary

    @property
    def SimpleClass_Attribute(self):
        return self.__SimpleClass_Attribute

    @SimpleClass_Attribute.setter
    def SimpleClass_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Attribute__SimpleClass_Attribute", None)
        self.__SimpleClass_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier"):
                opp_val = getattr(old_value, "Classifier", None)
                if opp_val == self:
                    setattr(old_value, "Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier"):
                opp_val = getattr(value, "Classifier", None)
                setattr(value, "Classifier", self)

class SimpleClass_Association:

    def __init__(self, name: str, SimpleClass_Association: "Class" = None, SimpleClass_Association6: "Class" = None):
        self.name = name
        self.SimpleClass_Association = SimpleClass_Association
        self.SimpleClass_Association6 = SimpleClass_Association6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimpleClass_Association(self):
        return self.__SimpleClass_Association

    @SimpleClass_Association.setter
    def SimpleClass_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Association__SimpleClass_Association", None)
        self.__SimpleClass_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class4"):
                opp_val = getattr(old_value, "Class4", None)
                if opp_val == self:
                    setattr(old_value, "Class4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class4"):
                opp_val = getattr(value, "Class4", None)
                setattr(value, "Class4", self)

    @property
    def SimpleClass_Association6(self):
        return self.__SimpleClass_Association6

    @SimpleClass_Association6.setter
    def SimpleClass_Association6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Association__SimpleClass_Association6", None)
        self.__SimpleClass_Association6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class7"):
                opp_val = getattr(old_value, "Class7", None)
                if opp_val == self:
                    setattr(old_value, "Class7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class7"):
                opp_val = getattr(value, "Class7", None)
                setattr(value, "Class7", self)

class Attribute:

    pass
class Class:

    pass
class Classifier:

    pass
class SimpleClass_PrimitiveDataType(Classifier):

    pass
class SimpleClass_Schema(Classifier):

    pass
class SimpleClass_Class(Classifier):

    def __init__(self, is_persistent: str, SimpleClass_Class: "Class" = None, SimpleClass_Class2: set["Attribute"] = None, Classifier: "SimpleClass_Attribute"):
        self.is_persistent = is_persistent
        self.SimpleClass_Class = SimpleClass_Class
        self.SimpleClass_Class2 = SimpleClass_Class2 if SimpleClass_Class2 is not None else set()
        
    @property
    def is_persistent(self) -> str:
        return self.__is_persistent

    @is_persistent.setter
    def is_persistent(self, is_persistent: str):
        self.__is_persistent = is_persistent

    @property
    def SimpleClass_Class2(self):
        return self.__SimpleClass_Class2

    @SimpleClass_Class2.setter
    def SimpleClass_Class2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Class__SimpleClass_Class2", None)
        self.__SimpleClass_Class2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    @property
    def SimpleClass_Class(self):
        return self.__SimpleClass_Class

    @SimpleClass_Class.setter
    def SimpleClass_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Class__SimpleClass_Class", None)
        self.__SimpleClass_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)
