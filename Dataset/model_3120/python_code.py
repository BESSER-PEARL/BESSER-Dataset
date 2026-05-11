from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Attribute:

    pass
class Class:

    pass
class Package:

    pass
class Classifier:

    pass
class ClassDiagram_Class(Classifier):

    def __init__(self, isAbstract: str, ClassDiagram_Class: set["Class"] = None, owner4: set["Attribute"] = None, Classifier: "ClassDiagram_Package" = None, Classifier6: "ClassDiagram_Attribute" = None):
        self.isAbstract = isAbstract
        self.ClassDiagram_Class = ClassDiagram_Class if ClassDiagram_Class is not None else set()
        self.owner4 = owner4 if owner4 is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def ClassDiagram_Class(self):
        return self.__ClassDiagram_Class

    @ClassDiagram_Class.setter
    def ClassDiagram_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Class__ClassDiagram_Class", None)
        self.__ClassDiagram_Class = value if value is not None else set()
        
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
    def owner4(self):
        return self.__owner4

    @owner4.setter
    def owner4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Class__owner4", None)
        self.__owner4 = value if value is not None else set()
        
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
                    

class ClassDiagram_DataType(Classifier):

    pass
class NamedElement:

    pass
class ClassDiagram_System(NamedElement):

    pass
class ClassDiagram_Attribute(NamedElement):

    def __init__(self, multiValued: str, ClassDiagram_Attribute: "Classifier" = None, attr: "Class" = None):
        self.multiValued = multiValued
        self.ClassDiagram_Attribute = ClassDiagram_Attribute
        self.attr = attr
        
        pass
    @property
    def multiValued(self):
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: str):
        self.__multiValued = multiValued


    @property
    def ClassDiagram_Attribute(self):
        return self.__ClassDiagram_Attribute

    @ClassDiagram_Attribute.setter
    def ClassDiagram_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Attribute__ClassDiagram_Attribute", None)
        self.__ClassDiagram_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier6"):
                opp_val = getattr(old_value, "Classifier6", None)
                if opp_val == self:
                    setattr(old_value, "Classifier6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier6"):
                opp_val = getattr(value, "Classifier6", None)
                setattr(value, "Classifier6", self)

    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Attribute__attr", None)
        self.__attr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class8"):
                opp_val = getattr(old_value, "Class8", None)
                if opp_val == self:
                    setattr(old_value, "Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class8"):
                opp_val = getattr(value, "Class8", None)
                setattr(value, "Class8", self)

class ClassDiagram_Classifier(NamedElement):

    pass
class ClassDiagram_Package(NamedElement):

    pass
class ClassDiagram_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

