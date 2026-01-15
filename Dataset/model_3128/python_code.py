from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Class:

    pass
class Classifier:

    pass
class Class_Class(Classifier):

    def __init__(self, isAbstract: bool, 1: set["Attribute"] = None, Class_Class: set["Class"] = None, Classifier: "Class_Attribute"):
        self.isAbstract = isAbstract
        self.1 = 1 if 1 is not None else set()
        self.Class_Class = Class_Class if Class_Class is not None else set()
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def Class_Class(self):
        return self.__Class_Class

    @Class_Class.setter
    def Class_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Class__Class_Class", None)
        self.__Class_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    if opp_val == self:
                        setattr(item, "Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    setattr(item, "Class", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Class__1", None)
        self.__1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    if opp_val == self:
                        setattr(item, "#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    setattr(item, "#", self)
                    

class Class_DataType(Classifier):

    pass
class NamedElt:

    pass
class Class_Classifier(NamedElt):

    pass
class Class_NamedElt(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Class_Attribute(NamedElt):

    def __init__(self, multiValued: bool, Class_Attribute: "Classifier" = None, 14: "Class" = None):
        self.multiValued = multiValued
        self.Class_Attribute = Class_Attribute
        self.14 = 14
        
    @property
    def multiValued(self) -> bool:
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: bool):
        self.__multiValued = multiValued

    @property
    def Class_Attribute(self):
        return self.__Class_Attribute

    @Class_Attribute.setter
    def Class_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Attribute__Class_Attribute", None)
        self.__Class_Attribute = value
        
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

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Attribute__14", None)
        self.__14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#5"):
                opp_val = getattr(old_value, "#5", None)
                if opp_val == self:
                    setattr(old_value, "#5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#5"):
                opp_val = getattr(value, "#5", None)
                setattr(value, "#5", self)

class Attribute:

    pass