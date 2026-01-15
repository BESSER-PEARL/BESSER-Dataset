from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Ignore(Enum):
    lit1 = "lit1"
    anotherlit = "anotherlit"


############################################
# Definition of Classes
############################################

class ModelElement:

    pass
class simpleuml_Classifier(ModelElement):

    pass
class simpleuml_Association(ModelElement):

    pass
class simpleuml_ModelElement(ABC):

    def __init__(self, name: str, simpleuml_ModelElement: "simpleuml_UMLPackage" = None):
        self.name = name
        self.simpleuml_ModelElement = simpleuml_ModelElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleuml_ModelElement(self):
        return self.__simpleuml_ModelElement

    @simpleuml_ModelElement.setter
    def simpleuml_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_ModelElement__simpleuml_ModelElement", None)
        self.__simpleuml_ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_UMLPackage"):
                opp_val = getattr(old_value, "simpleuml_UMLPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_UMLPackage"):
                opp_val = getattr(value, "simpleuml_UMLPackage", None)
                if opp_val is None:
                    setattr(value, "simpleuml_UMLPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleuml_Attribute(ModelElement):

    pass
class simpleuml_UMLPackage:

    pass
class Classifier:

    pass
class simpleuml_PrimitiveDataType(Classifier):

    pass
class simpleuml_UMLClass(Classifier):

    def __init__(self, kind: str, UMLClass: "simpleuml_Attribute" = None, simpleuml_UMLClass: "simpleuml_UMLClass" = None, simpleuml_UMLClass0: set["simpleuml_UMLClass"] = None, owner: set["simpleuml_Attribute"] = None, simpleuml_UMLClass4: "simpleuml_Association" = None, simpleuml_UMLClass7: "simpleuml_Association" = None):
        self.kind = kind
        self.UMLClass = UMLClass
        self.simpleuml_UMLClass = simpleuml_UMLClass
        self.simpleuml_UMLClass0 = simpleuml_UMLClass0 if simpleuml_UMLClass0 is not None else set()
        self.owner = owner if owner is not None else set()
        self.simpleuml_UMLClass4 = simpleuml_UMLClass4
        self.simpleuml_UMLClass7 = simpleuml_UMLClass7
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def UMLClass(self):
        return self.__UMLClass

    @UMLClass.setter
    def UMLClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_UMLClass__UMLClass", None)
        self.__UMLClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attribute"):
                opp_val = getattr(old_value, "attribute", None)
                if opp_val == self:
                    setattr(old_value, "attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attribute"):
                opp_val = getattr(value, "attribute", None)
                setattr(value, "attribute", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_UMLClass__owner", None)
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
    def simpleuml_UMLClass4(self):
        return self.__simpleuml_UMLClass4

    @simpleuml_UMLClass4.setter
    def simpleuml_UMLClass4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_UMLClass__simpleuml_UMLClass4", None)
        self.__simpleuml_UMLClass4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_Association"):
                opp_val = getattr(old_value, "simpleuml_Association", None)
                if opp_val == self:
                    setattr(old_value, "simpleuml_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_Association"):
                opp_val = getattr(value, "simpleuml_Association", None)
                setattr(value, "simpleuml_Association", self)

    @property
    def simpleuml_UMLClass(self):
        return self.__simpleuml_UMLClass

    @simpleuml_UMLClass.setter
    def simpleuml_UMLClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_UMLClass__simpleuml_UMLClass", None)
        self.__simpleuml_UMLClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_UMLClass0"):
                opp_val = getattr(old_value, "simpleuml_UMLClass0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_UMLClass0"):
                opp_val = getattr(value, "simpleuml_UMLClass0", None)
                if opp_val is None:
                    setattr(value, "simpleuml_UMLClass0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleuml_UMLClass0(self):
        return self.__simpleuml_UMLClass0

    @simpleuml_UMLClass0.setter
    def simpleuml_UMLClass0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_UMLClass__simpleuml_UMLClass0", None)
        self.__simpleuml_UMLClass0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleuml_UMLClass"):
                    opp_val = getattr(item, "simpleuml_UMLClass", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleuml_UMLClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleuml_UMLClass"):
                    opp_val = getattr(item, "simpleuml_UMLClass", None)
                    
                    setattr(item, "simpleuml_UMLClass", self)
                    

    @property
    def simpleuml_UMLClass7(self):
        return self.__simpleuml_UMLClass7

    @simpleuml_UMLClass7.setter
    def simpleuml_UMLClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_UMLClass__simpleuml_UMLClass7", None)
        self.__simpleuml_UMLClass7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_Association6"):
                opp_val = getattr(old_value, "simpleuml_Association6", None)
                if opp_val == self:
                    setattr(old_value, "simpleuml_Association6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_Association6"):
                opp_val = getattr(value, "simpleuml_Association6", None)
                setattr(value, "simpleuml_Association6", self)
