from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"


############################################
# Definition of Classes
############################################

class Class:

    pass
class Package:

    pass
class uml_Model(Package):

    pass
class uml_Element(ABC):

    pass
class Type:

    pass
class PackageableElement:

    pass
class uml_Type(PackageableElement):

    pass
class Classifier:

    pass
class uml_Class(Classifier):

    def __init__(self, isLeaf: str, isAbstract: str, uml_Class: set["uml_Classifier"] = None, uml_Class5: set["uml_Operation"] = None, uml_Class8: set["uml_Property"] = None, uml_Class10: set["uml_Classifier"] = None):
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.uml_Class = uml_Class if uml_Class is not None else set()
        self.uml_Class5 = uml_Class5 if uml_Class5 is not None else set()
        self.uml_Class8 = uml_Class8 if uml_Class8 is not None else set()
        self.uml_Class10 = uml_Class10 if uml_Class10 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

    @property
    def uml_Class5(self):
        return self.__uml_Class5

    @uml_Class5.setter
    def uml_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class5", None)
        self.__uml_Class5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Operation6"):
                    opp_val = getattr(item, "uml_Operation6", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Operation6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Operation6"):
                    opp_val = getattr(item, "uml_Operation6", None)
                    
                    setattr(item, "uml_Operation6", self)
                    

    @property
    def uml_Class(self):
        return self.__uml_Class

    @uml_Class.setter
    def uml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class", None)
        self.__uml_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier"):
                    opp_val = getattr(item, "uml_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier"):
                    opp_val = getattr(item, "uml_Classifier", None)
                    
                    setattr(item, "uml_Classifier", self)
                    

    @property
    def uml_Class8(self):
        return self.__uml_Class8

    @uml_Class8.setter
    def uml_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class8", None)
        self.__uml_Class8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property"):
                    opp_val = getattr(item, "uml_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property"):
                    opp_val = getattr(item, "uml_Property", None)
                    
                    setattr(item, "uml_Property", self)
                    

    @property
    def uml_Class10(self):
        return self.__uml_Class10

    @uml_Class10.setter
    def uml_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class10", None)
        self.__uml_Class10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier11"):
                    opp_val = getattr(item, "uml_Classifier11", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier11"):
                    opp_val = getattr(item, "uml_Classifier11", None)
                    
                    setattr(item, "uml_Classifier11", self)
                    

class TypedElement:

    pass
class uml_Behavior(Class):

    pass
class NamedElement:

    pass
class uml_Feature(NamedElement):

    pass
class uml_TypedElement(NamedElement):

    pass
class Feature:

    pass
class Element:

    pass
class uml_PackageableElement(Element, NamedElement):

    pass
class uml_Dependency(Element, PackageableElement):

    pass
class uml_Classifier(Type, NamedElement, Element):

    pass
class uml_Property(TypedElement, Feature, Element, NamedElement):

    pass
class uml_Parameter(TypedElement, Element):

    pass
class uml_Package(NamedElement, Element, PackageableElement):

    pass
class uml_NamedElement(Element):

    def __init__(self, name: str, visibility: str, uml_NamedElement: "uml_Dependency" = None, uml_NamedElement16: "uml_Dependency" = None):
        self.name = name
        self.visibility = visibility
        self.uml_NamedElement = uml_NamedElement
        self.uml_NamedElement16 = uml_NamedElement16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def uml_NamedElement(self):
        return self.__uml_NamedElement

    @uml_NamedElement.setter
    def uml_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement", None)
        self.__uml_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Dependency"):
                opp_val = getattr(old_value, "uml_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Dependency"):
                opp_val = getattr(value, "uml_Dependency", None)
                if opp_val is None:
                    setattr(value, "uml_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_NamedElement16(self):
        return self.__uml_NamedElement16

    @uml_NamedElement16.setter
    def uml_NamedElement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement16", None)
        self.__uml_NamedElement16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Dependency15"):
                opp_val = getattr(old_value, "uml_Dependency15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Dependency15"):
                opp_val = getattr(value, "uml_Dependency15", None)
                if opp_val is None:
                    setattr(value, "uml_Dependency15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_Operation(Feature, Element, NamedElement):

    pass