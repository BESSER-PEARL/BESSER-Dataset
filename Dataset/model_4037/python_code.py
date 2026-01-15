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
class Type:

    pass
class uml_Behavior(Class):

    pass
class Classifier:

    pass
class uml_Class(Classifier):

    def __init__(self, isAbstract: str, uml_Class: set["uml_Classifier"] = None, uml_Class4: set["uml_Operation"] = None, uml_Class6: set["uml_Classifier"] = None, uml_Class9: set["uml_Property"] = None):
        self.isAbstract = isAbstract
        self.uml_Class = uml_Class if uml_Class is not None else set()
        self.uml_Class4 = uml_Class4 if uml_Class4 is not None else set()
        self.uml_Class6 = uml_Class6 if uml_Class6 is not None else set()
        self.uml_Class9 = uml_Class9 if uml_Class9 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def uml_Class6(self):
        return self.__uml_Class6

    @uml_Class6.setter
    def uml_Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class6", None)
        self.__uml_Class6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier7"):
                    opp_val = getattr(item, "uml_Classifier7", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier7"):
                    opp_val = getattr(item, "uml_Classifier7", None)
                    
                    setattr(item, "uml_Classifier7", self)
                    

    @property
    def uml_Class4(self):
        return self.__uml_Class4

    @uml_Class4.setter
    def uml_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class4", None)
        self.__uml_Class4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Operation"):
                    opp_val = getattr(item, "uml_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Operation"):
                    opp_val = getattr(item, "uml_Operation", None)
                    
                    setattr(item, "uml_Operation", self)
                    

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
    def uml_Class9(self):
        return self.__uml_Class9

    @uml_Class9.setter
    def uml_Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class9", None)
        self.__uml_Class9 = value if value is not None else set()
        
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
                    

class NamedElement:

    pass
class uml_TypedElement(NamedElement):

    pass
class uml_Classifier(NamedElement, Type):

    pass
class uml_Feature(NamedElement):

    pass
class Package:

    pass
class uml_Model(Package):

    pass
class TypedElement:

    pass
class uml_Parameter(TypedElement):

    pass
class uml_NamedElement(ABC):

    def __init__(self, name: str, visibility: str, uml_NamedElement: "uml_Dependency" = None):
        self.name = name
        self.visibility = visibility
        self.uml_NamedElement = uml_NamedElement
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class Feature:

    pass
class uml_Operation(NamedElement, Feature):

    pass
class uml_Property(NamedElement, Feature, TypedElement):

    pass
class uml_PackageableElement(NamedElement):

    pass
class PackageableElement:

    pass
class uml_Dependency(PackageableElement):

    pass
class uml_Type(PackageableElement):

    pass
class uml_Package(NamedElement, PackageableElement):

    pass