from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    string = "string"
    int = "int"


############################################
# Definition of Classes
############################################

class Ref:

    pass
class myDot_EntityRef(Ref):

    pass
class myDot_DotExpression(Ref):

    pass
class myDot_Ref:

    pass
class Feature:

    pass
class myDot_Reference(Feature):

    pass
class myDot_Attribute(Feature):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class myDot_Feature:

    def __init__(self, name: str, myDot_Feature13: "myDot_DotExpression" = None, myDot_Feature: "myDot_Entity" = None):
        self.name = name
        self.myDot_Feature13 = myDot_Feature13
        self.myDot_Feature = myDot_Feature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDot_Feature13(self):
        return self.__myDot_Feature13

    @myDot_Feature13.setter
    def myDot_Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDot_Feature__myDot_Feature13", None)
        self.__myDot_Feature13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDot_DotExpression12"):
                opp_val = getattr(old_value, "myDot_DotExpression12", None)
                if opp_val == self:
                    setattr(old_value, "myDot_DotExpression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDot_DotExpression12"):
                opp_val = getattr(value, "myDot_DotExpression12", None)
                setattr(value, "myDot_DotExpression12", self)

    @property
    def myDot_Feature(self):
        return self.__myDot_Feature

    @myDot_Feature.setter
    def myDot_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDot_Feature__myDot_Feature", None)
        self.__myDot_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDot_Entity4"):
                opp_val = getattr(old_value, "myDot_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDot_Entity4"):
                opp_val = getattr(value, "myDot_Entity4", None)
                if opp_val is None:
                    setattr(value, "myDot_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDot_Usage:

    pass
class myDot_Entity:

    def __init__(self, name: str, myDot_Entity: "myDot_Model" = None, myDot_Entity4: set["myDot_Feature"] = None, myDot_Entity6: "myDot_Reference" = None, myDot_Entity15: "myDot_EntityRef" = None):
        self.name = name
        self.myDot_Entity = myDot_Entity
        self.myDot_Entity4 = myDot_Entity4 if myDot_Entity4 is not None else set()
        self.myDot_Entity6 = myDot_Entity6
        self.myDot_Entity15 = myDot_Entity15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDot_Entity6(self):
        return self.__myDot_Entity6

    @myDot_Entity6.setter
    def myDot_Entity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDot_Entity__myDot_Entity6", None)
        self.__myDot_Entity6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDot_Reference"):
                opp_val = getattr(old_value, "myDot_Reference", None)
                if opp_val == self:
                    setattr(old_value, "myDot_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDot_Reference"):
                opp_val = getattr(value, "myDot_Reference", None)
                setattr(value, "myDot_Reference", self)

    @property
    def myDot_Entity(self):
        return self.__myDot_Entity

    @myDot_Entity.setter
    def myDot_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDot_Entity__myDot_Entity", None)
        self.__myDot_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDot_Model"):
                opp_val = getattr(old_value, "myDot_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDot_Model"):
                opp_val = getattr(value, "myDot_Model", None)
                if opp_val is None:
                    setattr(value, "myDot_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDot_Entity4(self):
        return self.__myDot_Entity4

    @myDot_Entity4.setter
    def myDot_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDot_Entity__myDot_Entity4", None)
        self.__myDot_Entity4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDot_Feature"):
                    opp_val = getattr(item, "myDot_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "myDot_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDot_Feature"):
                    opp_val = getattr(item, "myDot_Feature", None)
                    
                    setattr(item, "myDot_Feature", self)
                    

    @property
    def myDot_Entity15(self):
        return self.__myDot_Entity15

    @myDot_Entity15.setter
    def myDot_Entity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDot_Entity__myDot_Entity15", None)
        self.__myDot_Entity15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDot_EntityRef"):
                opp_val = getattr(old_value, "myDot_EntityRef", None)
                if opp_val == self:
                    setattr(old_value, "myDot_EntityRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDot_EntityRef"):
                opp_val = getattr(value, "myDot_EntityRef", None)
                setattr(value, "myDot_EntityRef", self)

class myDot_Model:

    pass