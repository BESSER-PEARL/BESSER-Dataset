from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class class_Class(Classifier):

    def __init__(self, isAbstract: bool, class_Class: "class_Class" = None, class_Class0: set["class_Class"] = None, owner: set["class_Attribute"] = None, Class: "class_Attribute" = None):
        self.isAbstract = isAbstract
        self.class_Class = class_Class
        self.class_Class0 = class_Class0 if class_Class0 is not None else set()
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
        old_value = getattr(self, f"_class_Class__owner", None)
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
    def class_Class(self):
        return self.__class_Class

    @class_Class.setter
    def class_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Class__class_Class", None)
        self.__class_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_Class0"):
                opp_val = getattr(old_value, "class_Class0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_Class0"):
                opp_val = getattr(value, "class_Class0", None)
                if opp_val is None:
                    setattr(value, "class_Class0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Class__Class", None)
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
    def class_Class0(self):
        return self.__class_Class0

    @class_Class0.setter
    def class_Class0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Class__class_Class0", None)
        self.__class_Class0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class_Class"):
                    opp_val = getattr(item, "class_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "class_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class_Class"):
                    opp_val = getattr(item, "class_Class", None)
                    
                    setattr(item, "class_Class", self)
                    

class class_DataType(Classifier):

    pass
class NamedElt:

    pass
class class_Classifier(NamedElt):

    pass
class class_ClassModel:

    pass
class class_Attribute(NamedElt):

    def __init__(self, multiValued: bool, Attribute: "class_Class" = None, attr: "class_Class" = None, class_Attribute: "class_Classifier" = None):
        self.multiValued = multiValued
        self.Attribute = Attribute
        self.attr = attr
        self.class_Attribute = class_Attribute
        
    @property
    def multiValued(self) -> bool:
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: bool):
        self.__multiValued = multiValued

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Attribute__Attribute", None)
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
    def class_Attribute(self):
        return self.__class_Attribute

    @class_Attribute.setter
    def class_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Attribute__class_Attribute", None)
        self.__class_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_Classifier"):
                opp_val = getattr(old_value, "class_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "class_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_Classifier"):
                opp_val = getattr(value, "class_Classifier", None)
                setattr(value, "class_Classifier", self)

    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Attribute__attr", None)
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

class class_NamedElt(ABC):

    def __init__(self, name: str, class_NamedElt: "class_ClassModel" = None):
        self.name = name
        self.class_NamedElt = class_NamedElt
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def class_NamedElt(self):
        return self.__class_NamedElt

    @class_NamedElt.setter
    def class_NamedElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_NamedElt__class_NamedElt", None)
        self.__class_NamedElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_ClassModel"):
                opp_val = getattr(old_value, "class_ClassModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_ClassModel"):
                opp_val = getattr(value, "class_ClassModel", None)
                if opp_val is None:
                    setattr(value, "class_ClassModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
