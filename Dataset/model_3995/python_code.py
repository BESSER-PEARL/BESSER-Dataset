from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class Class_Class(Classifier):

    def __init__(self, isAbstract: bool, Class: "Class_Attribute" = None, Class_Class: "Class_Class" = None, Class_Class2: set["Class_Class"] = None, owner: set["Class_Attribute"] = None):
        self.isAbstract = isAbstract
        self.Class = Class
        self.Class_Class = Class_Class
        self.Class_Class2 = Class_Class2 if Class_Class2 is not None else set()
        self.owner = owner if owner is not None else set()
        
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
        self.__Class_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class_Class2"):
                opp_val = getattr(old_value, "Class_Class2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class_Class2"):
                opp_val = getattr(value, "Class_Class2", None)
                if opp_val is None:
                    setattr(value, "Class_Class2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def Class_Class2(self):
        return self.__Class_Class2

    @Class_Class2.setter
    def Class_Class2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Class__Class_Class2", None)
        self.__Class_Class2 = value if value is not None else set()
        
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
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "att"):
                opp_val = getattr(old_value, "att", None)
                if opp_val == self:
                    setattr(old_value, "att", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "att"):
                opp_val = getattr(value, "att", None)
                setattr(value, "att", self)

class Class_DataType(Classifier):

    pass
class NamedElt:

    pass
class Class_Classifier(NamedElt):

    pass
class Class_Attribute(NamedElt):

    def __init__(self, multiValued: bool, Class_Attribute: "Class_Classifier" = None, att: "Class_Class" = None, Attribute: "Class_Class" = None):
        self.multiValued = multiValued
        self.Class_Attribute = Class_Attribute
        self.att = att
        self.Attribute = Attribute
        
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
            if hasattr(old_value, "Class_Classifier"):
                opp_val = getattr(old_value, "Class_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "Class_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class_Classifier"):
                opp_val = getattr(value, "Class_Classifier", None)
                setattr(value, "Class_Classifier", self)

    @property
    def att(self):
        return self.__att

    @att.setter
    def att(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Attribute__att", None)
        self.__att = value
        
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

class Class_Package(NamedElt):

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
