from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class classes_TypedElement(ABC):

    pass
class TypedElement:

    pass
class Classifier:

    pass
class classes_Datatype(Classifier):

    pass
class classes_CClass(Classifier):

    def __init__(self, abstract: bool, classes_CClass: "classes_CClass" = None, classes_CClass1: "classes_CClass" = None, classes_CClass4: set["classes_Attribute"] = None, classes_CClass7: "classes_CClass" = None, classes_CClass5: set["classes_CClass"] = None):
        self.abstract = abstract
        self.classes_CClass = classes_CClass
        self.classes_CClass1 = classes_CClass1
        self.classes_CClass4 = classes_CClass4 if classes_CClass4 is not None else set()
        self.classes_CClass7 = classes_CClass7
        self.classes_CClass5 = classes_CClass5 if classes_CClass5 is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def classes_CClass7(self):
        return self.__classes_CClass7

    @classes_CClass7.setter
    def classes_CClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_CClass__classes_CClass7", None)
        self.__classes_CClass7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_CClass5"):
                opp_val = getattr(old_value, "classes_CClass5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_CClass5"):
                opp_val = getattr(value, "classes_CClass5", None)
                if opp_val is None:
                    setattr(value, "classes_CClass5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_CClass5(self):
        return self.__classes_CClass5

    @classes_CClass5.setter
    def classes_CClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_CClass__classes_CClass5", None)
        self.__classes_CClass5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_CClass7"):
                    opp_val = getattr(item, "classes_CClass7", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_CClass7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_CClass7"):
                    opp_val = getattr(item, "classes_CClass7", None)
                    
                    setattr(item, "classes_CClass7", self)
                    

    @property
    def classes_CClass1(self):
        return self.__classes_CClass1

    @classes_CClass1.setter
    def classes_CClass1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_CClass__classes_CClass1", None)
        self.__classes_CClass1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_CClass"):
                opp_val = getattr(old_value, "classes_CClass", None)
                if opp_val == self:
                    setattr(old_value, "classes_CClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_CClass"):
                opp_val = getattr(value, "classes_CClass", None)
                setattr(value, "classes_CClass", self)

    @property
    def classes_CClass(self):
        return self.__classes_CClass

    @classes_CClass.setter
    def classes_CClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_CClass__classes_CClass", None)
        self.__classes_CClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_CClass1"):
                opp_val = getattr(old_value, "classes_CClass1", None)
                if opp_val == self:
                    setattr(old_value, "classes_CClass1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_CClass1"):
                opp_val = getattr(value, "classes_CClass1", None)
                setattr(value, "classes_CClass1", self)

    @property
    def classes_CClass4(self):
        return self.__classes_CClass4

    @classes_CClass4.setter
    def classes_CClass4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_CClass__classes_CClass4", None)
        self.__classes_CClass4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Attribute"):
                    opp_val = getattr(item, "classes_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Attribute"):
                    opp_val = getattr(item, "classes_Attribute", None)
                    
                    setattr(item, "classes_Attribute", self)
                    

class NamedElement:

    pass
class classes_Attribute(NamedElement, TypedElement):

    def __init__(self, isMany: bool, classes_Attribute: "classes_CClass" = None):
        self.isMany = isMany
        self.classes_Attribute = classes_Attribute
        
    @property
    def isMany(self) -> bool:
        return self.__isMany

    @isMany.setter
    def isMany(self, isMany: bool):
        self.__isMany = isMany

    @property
    def classes_Attribute(self):
        return self.__classes_Attribute

    @classes_Attribute.setter
    def classes_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Attribute__classes_Attribute", None)
        self.__classes_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_CClass4"):
                opp_val = getattr(old_value, "classes_CClass4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_CClass4"):
                opp_val = getattr(value, "classes_CClass4", None)
                if opp_val is None:
                    setattr(value, "classes_CClass4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classes_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class classes_Classifier(NamedElement):

    pass
class classes_CModel:

    pass