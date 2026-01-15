from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    string = "string"
    int = "int"


############################################
# Definition of Classes
############################################

class Feature:

    pass
class myDsl_Reference(Feature):

    pass
class myDsl_Attribute(Feature):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class myDsl_Feature:

    def __init__(self, name: str, myDsl_Feature: "myDsl_Entity" = None):
        self.name = name
        self.myDsl_Feature = myDsl_Feature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Feature(self):
        return self.__myDsl_Feature

    @myDsl_Feature.setter
    def myDsl_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature", None)
        self.__myDsl_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Entity2"):
                opp_val = getattr(old_value, "myDsl_Entity2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Entity2"):
                opp_val = getattr(value, "myDsl_Entity2", None)
                if opp_val is None:
                    setattr(value, "myDsl_Entity2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Entity:

    def __init__(self, name: str, myDsl_Entity: "myDsl_Model" = None, myDsl_Entity2: set["myDsl_Feature"] = None, myDsl_Entity4: "myDsl_Reference" = None):
        self.name = name
        self.myDsl_Entity = myDsl_Entity
        self.myDsl_Entity2 = myDsl_Entity2 if myDsl_Entity2 is not None else set()
        self.myDsl_Entity4 = myDsl_Entity4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Entity(self):
        return self.__myDsl_Entity

    @myDsl_Entity.setter
    def myDsl_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Entity__myDsl_Entity", None)
        self.__myDsl_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Model"):
                opp_val = getattr(old_value, "myDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model"):
                opp_val = getattr(value, "myDsl_Model", None)
                if opp_val is None:
                    setattr(value, "myDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Entity2(self):
        return self.__myDsl_Entity2

    @myDsl_Entity2.setter
    def myDsl_Entity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Entity__myDsl_Entity2", None)
        self.__myDsl_Entity2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Feature"):
                    opp_val = getattr(item, "myDsl_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Feature"):
                    opp_val = getattr(item, "myDsl_Feature", None)
                    
                    setattr(item, "myDsl_Feature", self)
                    

    @property
    def myDsl_Entity4(self):
        return self.__myDsl_Entity4

    @myDsl_Entity4.setter
    def myDsl_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Entity__myDsl_Entity4", None)
        self.__myDsl_Entity4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Reference"):
                opp_val = getattr(old_value, "myDsl_Reference", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Reference"):
                opp_val = getattr(value, "myDsl_Reference", None)
                setattr(value, "myDsl_Reference", self)

class myDsl_Model:

    pass