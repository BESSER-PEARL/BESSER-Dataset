from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Attribute:

    pass
class Class:

    pass
class Classifier:

    pass
class ClassDiagram_DataType(Classifier):

    pass
class ClassDiagram_Class(Classifier):

    def __init__(self, isAbstract: str, ClassDiagram_Class: set["Class"] = None, 06: set["Attribute"] = None, #: "ClassDiagram_Package", Classifier: "ClassDiagram_Attribute"):
        self.isAbstract = isAbstract
        self.ClassDiagram_Class = ClassDiagram_Class if ClassDiagram_Class is not None else set()
        self.06 = 06 if 06 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def 06(self):
        return self.__06

    @06.setter
    def 06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Class__06", None)
        self.__06 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#7"):
                    opp_val = getattr(item, "#7", None)
                    
                    if opp_val == self:
                        setattr(item, "#7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#7"):
                    opp_val = getattr(item, "#7", None)
                    
                    setattr(item, "#7", self)
                    

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
                    

class NamedElement:

    pass
class ClassDiagram_System(NamedElement):

    pass
class ClassDiagram_Attribute(NamedElement):

    def __init__(self, multiValued: str, ClassDiagram_Attribute: "Classifier" = None, 010: "Class" = None):
        self.multiValued = multiValued
        self.ClassDiagram_Attribute = ClassDiagram_Attribute
        self.010 = 010
        
    @property
    def multiValued(self) -> str:
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
    def 010(self):
        return self.__010

    @010.setter
    def 010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Attribute__010", None)
        self.__010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#11"):
                opp_val = getattr(old_value, "#11", None)
                if opp_val == self:
                    setattr(old_value, "#11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#11"):
                opp_val = getattr(value, "#11", None)
                setattr(value, "#11", self)

class ClassDiagram_Package(NamedElement):

    pass
class ClassDiagram_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Package:

    pass
class ClassDiagram_Classifier(NamedElement):

    pass