from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class Class_Class(Classifier):

    def __init__(self, isAbstract: bool, Class_Class: set["Class"] = None, owner: set["Attribute"] = None, Classifier: "Class_Attribute" = None):
        self.isAbstract = isAbstract
        self.Class_Class = Class_Class if Class_Class is not None else set()
        self.owner = owner if owner is not None else set()
        
        pass
    @property
    def isAbstract(self):
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
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Class__owner", None)
        self.__owner = value if value is not None else set()
        
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
                    

class Class_DataType(Classifier):

    pass
class NamedElt:

    pass
class Class_Classifier(NamedElt):

    pass
class Class_Attribute(NamedElt):

    def __init__(self, multiValued: bool, Class_Attribute: "Classifier" = None, attr: "Class" = None):
        self.multiValued = multiValued
        self.Class_Attribute = Class_Attribute
        self.attr = attr
        
        pass
    @property
    def multiValued(self):
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
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Attribute__attr", None)
        self.__attr = value
        
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

class Attribute:

    pass
class Class:

    pass
class Class_NamedElt(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

