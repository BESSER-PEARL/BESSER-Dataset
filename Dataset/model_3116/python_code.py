from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class CD_Class(Classifier):

    def __init__(self, isAbstract: str, CD_Class: "CD_Class" = None, CD_Class0: set["CD_Class"] = None, owner: set["CD_Attribute"] = None, Class: "CD_Attribute" = None):
        self.isAbstract = isAbstract
        self.CD_Class = CD_Class
        self.CD_Class0 = CD_Class0 if CD_Class0 is not None else set()
        self.owner = owner if owner is not None else set()
        self.Class = Class
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def CD_Class(self):
        return self.__CD_Class

    @CD_Class.setter
    def CD_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CD_Class__CD_Class", None)
        self.__CD_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CD_Class0"):
                opp_val = getattr(old_value, "CD_Class0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CD_Class0"):
                opp_val = getattr(value, "CD_Class0", None)
                if opp_val is None:
                    setattr(value, "CD_Class0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CD_Class__Class", None)
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
    def CD_Class0(self):
        return self.__CD_Class0

    @CD_Class0.setter
    def CD_Class0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CD_Class__CD_Class0", None)
        self.__CD_Class0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CD_Class"):
                    opp_val = getattr(item, "CD_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "CD_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CD_Class"):
                    opp_val = getattr(item, "CD_Class", None)
                    
                    setattr(item, "CD_Class", self)
                    

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CD_Class__owner", None)
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
                    

class CD_Package(Classifier):

    pass
class CD_DataType(Classifier):

    pass
class NamedElt:

    pass
class CD_Attribute(NamedElt):

    def __init__(self, multiValued: str, Attribute: "CD_Class" = None, CD_Attribute: "CD_Classifier" = None, attr: "CD_Class" = None):
        self.multiValued = multiValued
        self.Attribute = Attribute
        self.CD_Attribute = CD_Attribute
        self.attr = attr
        
    @property
    def multiValued(self) -> str:
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: str):
        self.__multiValued = multiValued

    @property
    def CD_Attribute(self):
        return self.__CD_Attribute

    @CD_Attribute.setter
    def CD_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CD_Attribute__CD_Attribute", None)
        self.__CD_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CD_Classifier"):
                opp_val = getattr(old_value, "CD_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "CD_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CD_Classifier"):
                opp_val = getattr(value, "CD_Classifier", None)
                setattr(value, "CD_Classifier", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CD_Attribute__Attribute", None)
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
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CD_Attribute__attr", None)
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

class CD_Classifier(NamedElt):

    pass
class CD_NamedElt(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
