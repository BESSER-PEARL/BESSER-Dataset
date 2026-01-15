from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Metamodel:

    pass
class TypedElement:

    pass
class km3_StructuralFeature(TypedElement):

    pass
class Operation:

    pass
class StructuralFeature:

    pass
class km3_Reference(StructuralFeature):

    def __init__(self, isContainer: str, km3_Reference: "Reference" = None, #22: "km3_StructuralFeature", #25: "km3_StructuralFeature", #12: "km3_Class"):
        self.isContainer = isContainer
        self.km3_Reference = km3_Reference
        
    @property
    def isContainer(self) -> str:
        return self.__isContainer

    @isContainer.setter
    def isContainer(self, isContainer: str):
        self.__isContainer = isContainer

    @property
    def km3_Reference(self):
        return self.__km3_Reference

    @km3_Reference.setter
    def km3_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_Reference__km3_Reference", None)
        self.__km3_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Reference"):
                opp_val = getattr(old_value, "Reference", None)
                if opp_val == self:
                    setattr(old_value, "Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Reference"):
                opp_val = getattr(value, "Reference", None)
                setattr(value, "Reference", self)

class km3_Attribute(StructuralFeature):

    pass
class km3_Parameter(TypedElement):

    pass
class Parameter:

    pass
class km3_Operation(TypedElement):

    pass
class Reference:

    pass
class Classifier:

    pass
class km3_DataType(Classifier):

    pass
class ModelElement:

    pass
class km3_TypedElement(ModelElement):

    def __init__(self, lower: str, upper: str, isOrdered: str, isUnique: str, km3_TypedElement: "Classifier" = None, #38: "km3_Package"):
        self.lower = lower
        self.upper = upper
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.km3_TypedElement = km3_TypedElement
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def km3_TypedElement(self):
        return self.__km3_TypedElement

    @km3_TypedElement.setter
    def km3_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_TypedElement__km3_TypedElement", None)
        self.__km3_TypedElement = value
        
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

class km3_Package(ModelElement):

    pass
class km3_Classifier(ModelElement):

    pass
class Package:

    pass
class LocatedElement:

    pass
class km3_Metamodel(LocatedElement):

    pass
class km3_ModelElement(LocatedElement):

    def __init__(self, name: str, 0: "Package" = None):
        self.name = name
        self.0 = 0
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_ModelElement__0", None)
        self.__0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#"):
                opp_val = getattr(old_value, "#", None)
                if opp_val == self:
                    setattr(old_value, "#", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#"):
                opp_val = getattr(value, "#", None)
                setattr(value, "#", self)

class km3_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class Class:

    pass
class TemplateParameter:

    pass
class km3_Class(Classifier):

    def __init__(self, isAbstract: str, km3_Class: set["TemplateParameter"] = None, km3_Class9: set["Class"] = None, 011: set["StructuralFeature"] = None, 014: set["Operation"] = None, Classifier: "km3_TypedElement"):
        self.isAbstract = isAbstract
        self.km3_Class = km3_Class if km3_Class is not None else set()
        self.km3_Class9 = km3_Class9 if km3_Class9 is not None else set()
        self.011 = 011 if 011 is not None else set()
        self.014 = 014 if 014 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def 014(self):
        return self.__014

    @014.setter
    def 014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_Class__014", None)
        self.__014 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#15"):
                    opp_val = getattr(item, "#15", None)
                    
                    if opp_val == self:
                        setattr(item, "#15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#15"):
                    opp_val = getattr(item, "#15", None)
                    
                    setattr(item, "#15", self)
                    

    @property
    def 011(self):
        return self.__011

    @011.setter
    def 011(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_Class__011", None)
        self.__011 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#12"):
                    opp_val = getattr(item, "#12", None)
                    
                    if opp_val == self:
                        setattr(item, "#12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#12"):
                    opp_val = getattr(item, "#12", None)
                    
                    setattr(item, "#12", self)
                    

    @property
    def km3_Class9(self):
        return self.__km3_Class9

    @km3_Class9.setter
    def km3_Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_Class__km3_Class9", None)
        self.__km3_Class9 = value if value is not None else set()
        
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
    def km3_Class(self):
        return self.__km3_Class

    @km3_Class.setter
    def km3_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_Class__km3_Class", None)
        self.__km3_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TemplateParameter"):
                    opp_val = getattr(item, "TemplateParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "TemplateParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TemplateParameter"):
                    opp_val = getattr(item, "TemplateParameter", None)
                    
                    setattr(item, "TemplateParameter", self)
                    

class km3_TemplateParameter(Classifier):

    pass
class Enumeration:

    pass
class km3_EnumLiteral(ModelElement):

    pass
class EnumLiteral:

    pass
class km3_Enumeration(Classifier):

    pass