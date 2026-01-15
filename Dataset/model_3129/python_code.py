from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class Class_Class(Classifier):

    def __init__(self, isAbstract: bool, Class_Class: "Class_Class" = None, Class_Class0: set["Class_Class"] = None, owner: set["Class_Attribute"] = None, Class: "Class_Attribute" = None):
        self.isAbstract = isAbstract
        self.Class_Class = Class_Class
        self.Class_Class0 = Class_Class0 if Class_Class0 is not None else set()
        self.owner = owner if owner is not None else set()
        self.Class = Class
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

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
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attr"):
                opp_val = getattr(old_value, "attr", None)
                if opp_val == self:
                    setattr(old_value, "attr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attr"):
                opp_val = getattr(value, "attr", None)
                setattr(value, "attr", self)

    @property
    def Class_Class0(self):
        return self.__Class_Class0

    @Class_Class0.setter
    def Class_Class0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Class__Class_Class0", None)
        self.__Class_Class0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class_Class"):
                    opp_val = getattr(item, "Class_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "Class_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class_Class"):
                    opp_val = getattr(item, "Class_Class", None)
                    
                    setattr(item, "Class_Class", self)
                    

    @property
    def Class_Class(self):
        return self.__Class_Class

    @Class_Class.setter
    def Class_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Class__Class_Class", None)
        self.__Class_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class_Class0"):
                opp_val = getattr(old_value, "Class_Class0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class_Class0"):
                opp_val = getattr(value, "Class_Class0", None)
                if opp_val is None:
                    setattr(value, "Class_Class0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Class_DataType(Classifier):

    pass
class NamedElt:

    pass
class Class_Attribute(NamedElt):

    def __init__(self, multiValued: bool, Attribute: "Class_Class" = None, Class_Attribute: "Class_Classifier" = None, attr: "Class_Class" = None):
        self.multiValued = multiValued
        self.Attribute = Attribute
        self.Class_Attribute = Class_Attribute
        self.attr = attr
        
    @property
    def multiValued(self) -> bool:
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: bool):
        self.__multiValued = multiValued

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
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Class_Classifier"):
                opp_val = getattr(old_value, "Class_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "Class_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class_Classifier"):
                opp_val = getattr(value, "Class_Classifier", None)
                setattr(value, "Class_Classifier", self)

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
